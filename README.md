# Denver NC Music Grants Workspace

This workspace turns the existing `agency-agents` repository into a grant-seeking team for a Denver, North Carolina recording studio.

The operating model is simple:

1. The `agency-agents` repo remains the source of truth for all available agents.
2. This project adds a grant-specific spec, workflow, prompts, and outputs.
3. The inventory builder scans the repo so the full team can stay current as agents are added or changed.

## Mission

Secure grant and grant-adjacent funding for a studio-first independent music business in Denver, North Carolina by positioning the studio as infrastructure for artistic output, artist access, education, and community value.

## Project Layout

- `project-specs/denver-recording-studio-grants.md` — canonical project specification
- `workflows/nexus-grant-pipeline.md` — NEXUS-style grant workflow adapted from the agency playbooks
- `docs/team-topology.md` — how the full agency roster participates in this mission
- `prompts/activate-full-grant-team.md` — ready-to-use activation prompt for Copilot
- `scripts/build-agent-inventory.mjs` — scans `agency-agents` and generates the live roster
- `generated/agent-inventory.json` — machine-readable full roster
- `generated/agent-inventory.md` — human-readable full roster

## Quick Start

1. Run `npm run build:agents` from this folder.
2. Read the project spec and team topology.
3. Copy the activation prompt into Copilot.
4. Use the generated inventory as the full-team source of truth.

## Working Rules

- Treat all agents in the generated inventory as members of the team.
- Activate agents by relevance and phase, not by forcing all of them to speak at once.
- Keep one canonical spec and one current opportunity tracker.
- Do not pitch the studio as a for-profit business needing subsidy.
- Always pitch outcomes the studio enables: creation, community access, training, preservation, and artist development.

## Primary Funding Thesis

1. Immediate path: North Carolina artist support and local pass-through grants.
2. Mid-term path: partnerships with nonprofits, schools, and local arts organizations.
3. Scale path: a light program wrapper around recording access, artist development, workshops, or cultural preservation.

## Source Repositories

- Agency roster: `../agency-agents`
- Workspace project: `.`