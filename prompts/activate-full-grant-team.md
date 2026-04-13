# Activate Full Grant Team

Use this prompt in GitHub Copilot after running `npm run build:agents`.

```text
Activate Agents Orchestrator in NEXUS-Full grant mode.

Project: Denver NC Recording Studio Grants
Mission: Build and run a full-team grant acquisition system for a studio-first independent artist in Denver, North Carolina.

Read these files first:
1. denver-nc-music-grants/project-specs/denver-recording-studio-grants.md
2. denver-nc-music-grants/workflows/nexus-grant-pipeline.md
3. denver-nc-music-grants/docs/team-topology.md
4. denver-nc-music-grants/generated/agent-inventory.json

Operating rules:
1. Treat every agent in generated/agent-inventory.json as part of the available team.
2. Activate agents by relevance and phase; do not force irrelevant agents into active work.
3. Keep one canonical submission tracker and one canonical narrative bank.
4. Never pitch the studio as a business subsidy request.
5. Always frame funding requests around artistic creation, access, education, preservation, or community impact.
6. Require evidence before concluding an opportunity is eligible or ready.

Execute this workflow:
1. Phase 0 Discovery: produce an opportunity map for Denver, Lincoln County, North Carolina, federal pass-through, and private artist support.
2. Phase 1 Strategy: produce a ranked funding roadmap and recommend the best program wrapper for the studio.
3. Phase 2 Foundation: produce narrative bank, budget template, evidence checklist, and submission tracker.
4. Phase 3 Build: draft the first application package and partner-outreach materials.
5. Phase 4 Harden: red-team the package and return a GO or NO-GO decision.

Required first deliverables:
1. A one-page funding thesis.
2. A fit-ranked target list.
3. A missing-information list.
4. A 30-60-90 day action plan.
```