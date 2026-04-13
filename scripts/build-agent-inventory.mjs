import { promises as fs } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const projectRoot = path.resolve(__dirname, '..');
const workspaceRoot = path.resolve(projectRoot, '..');
const agencyRoot = process.env.AGENCY_AGENTS_ROOT
    ? path.resolve(process.env.AGENCY_AGENTS_ROOT)
    : path.join(workspaceRoot, 'agency-agents');
const generatedDir = path.join(projectRoot, 'generated');

const includedDivisions = [
    'academic',
    'cybersecurity',
    'data-analytics',
    'design',
    'developer-relations',
    'engineering',
    'finance',
    'game-development',
    'manufacturing',
    'marketing',
    'paid-media',
    'product',
    'project-management',
    'sales',
    'spatial-computing',
    'specialized',
    'support',
    'testing'
];

function parseFrontmatter(contents) {
    if (!contents.startsWith('---\n')) {
        return null;
    }

    const lines = contents.split('\n');
    const frontmatter = {};
    let index = 1;

    while (index < lines.length) {
        const line = lines[index];

        if (line.trim() === '---') {
            break;
        }

        const match = line.match(/^([A-Za-z0-9_\-]+):\s*(.*)$/);
        if (match) {
            const [, key, rawValue] = match;
            frontmatter[key] = rawValue.trim();
        }

        index += 1;
    }

    return frontmatter.name ? frontmatter : null;
}

async function walk(directory) {
    const entries = await fs.readdir(directory, { withFileTypes: true });
    const results = [];

    for (const entry of entries) {
        if (entry.name.startsWith('.')) {
            continue;
        }

        const fullPath = path.join(directory, entry.name);

        if (entry.isDirectory()) {
            results.push(...(await walk(fullPath)));
            continue;
        }

        if (!entry.isFile() || !entry.name.endsWith('.md') || entry.name === 'README.md') {
            continue;
        }

        results.push(fullPath);
    }

    return results;
}

async function collectAgents() {
    const records = [];

    for (const division of includedDivisions) {
        const divisionPath = path.join(agencyRoot, division);
        const files = await walk(divisionPath);

        for (const filePath of files) {
            const contents = await fs.readFile(filePath, 'utf8');
            const frontmatter = parseFrontmatter(contents);

            if (!frontmatter) {
                continue;
            }

            const relativePath = path.relative(agencyRoot, filePath).replaceAll(path.sep, '/');

            records.push({
                name: frontmatter.name,
                description: frontmatter.description || '',
                emoji: frontmatter.emoji || '',
                vibe: frontmatter.vibe || '',
                division,
                file: relativePath
            });
        }
    }

    records.sort((left, right) => {
        if (left.division !== right.division) {
            return left.division.localeCompare(right.division);
        }

        return left.name.localeCompare(right.name);
    });

    return records;
}

function buildMarkdown(records) {
    const counts = records.reduce((map, record) => {
        map.set(record.division, (map.get(record.division) || 0) + 1);
        return map;
    }, new Map());

    const lines = [
        '# Agent Inventory',
        '',
        `Source: ${agencyRoot}`,
        `Generated: ${new Date().toISOString()}`,
        '',
        `Total agents: ${records.length}`,
        `Total divisions: ${counts.size}`,
        '',
        '## Division Summary',
        '',
        '| Division | Count |',
        '| --- | ---: |'
    ];

    for (const [division, count] of [...counts.entries()].sort((a, b) => a[0].localeCompare(b[0]))) {
        lines.push(`| ${division} | ${count} |`);
    }

    lines.push('', '## Agent Roster', '', '| Agent | Division | File | Description |', '| --- | --- | --- | --- |');

    for (const record of records) {
        const safeDescription = record.description.replaceAll('|', '\\|');
        lines.push(`| ${record.name} | ${record.division} | ${record.file} | ${safeDescription} |`);
    }

    lines.push('');
    return lines.join('\n');
}

async function main() {
    const records = await collectAgents();
    await fs.mkdir(generatedDir, { recursive: true });

    const counts = records.reduce((map, record) => {
        map[record.division] = (map[record.division] || 0) + 1;
        return map;
    }, {});

    const jsonOutput = {
        source: agencyRoot,
        generatedAt: new Date().toISOString(),
        totalAgents: records.length,
        totalDivisions: Object.keys(counts).length,
        counts,
        agents: records
    };

    await fs.writeFile(
        path.join(generatedDir, 'agent-inventory.json'),
        `${JSON.stringify(jsonOutput, null, 2)}\n`,
        'utf8'
    );

    await fs.writeFile(
        path.join(generatedDir, 'agent-inventory.md'),
        `${buildMarkdown(records)}\n`,
        'utf8'
    );

    process.stdout.write(`Built inventory for ${records.length} agents across ${Object.keys(counts).length} divisions.\n`);
}

main().catch((error) => {
    process.stderr.write(`${error.stack || error.message}\n`);
    process.exitCode = 1;
});