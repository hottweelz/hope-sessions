# Hope Sessions

**Music, recording, and creative access. Built by Paul Andrejack in Denver, North Carolina.**

Hope Sessions is a recording initiative led by Paul Andrejack at PMA Recording Studios in Denver, NC. It starts with new original music extending the artistic world of the album *Hope* by Andrejack, and builds toward broader access — professional studio time, artist development, mentorship, and musical education for artists and youth in Lincoln County who currently have no path to it.

The initiative is tied to an Artist Support Grant application targeting the **Arts & Science Council Charlotte-Mecklenburg consortium for Lincoln County**, with a September 2026 submission deadline.

---

## The Site

The public-facing site lives at `site/hope-sessions/` and is deployed on **Cloudflare Pages**.

- **Stack:** Plain HTML5, CSS, vanilla JS — no build step, no framework
- **Typography:** Fraunces (display), Oswald (labels), Source Sans 3 (body) via Google Fonts
- **Form:** Web3Forms (free, AJAX, no server required) — delivers submissions directly to `pmastudios@hotmail.com`
- **Compliance:** WCAG 2.2 AA, ADA Title III, GDPR/CCPA. Legal pages included.
- **Security:** `_headers` file sets CSP, X-Frame-Options, and security headers natively via CF Pages

```
site/
  hope-sessions/
    index.html          ← main page
    privacy.html
    terms.html
    accessibility.html
    _headers            ← Cloudflare Pages security headers
    assets/
      css/styles.css
      img/
        pma_logo.png
        hope.png
        favicon.svg
        pma_seo_og.png
```

### Deploy

Cloudflare Pages is connected to this repo. Every push to `main` auto-deploys.

To deploy manually from the CLI:
```bash
npx wrangler pages deploy
```

The `wrangler.toml` at the repo root handles all config — project name and output directory are already set.

---

## The Initiative

**Paul Andrejack** is an Internet Records recording artist, producer, and engineer based in Denver, NC. He built his career on Long Island — original studio, multiple bands, released albums, European tours — before relocating south and founding PMA Recording Studios.

His credits include co-writes with Grammy Award winners Mark Mangold and Mark Gatz, collaboration with The Alessi Brothers (McCartney / Lennon collaborators), music placement on the Food Network's Bobby Flay show, and consulting work for Bakithi Kumalo (Paul Simon's bassist) and Kent Marcum (Harpo Productions).

Hope Sessions uses that infrastructure and experience to serve artists in a region where professional studio access, gear, and experienced guidance aren't available without traveling to Charlotte, Raleigh, or Nashville — and paying for it.

**What the initiative is building:**
1. New original music — finished recordings extending the world of *Hope*
2. All-level artist development — first-time visitors through experienced performers
3. Barrier removal — grant funding covers what most independent artists can't
4. Community creative infrastructure — schools, nonprofits, and orgs in Lincoln County
5. Grant sustainability model — covering session, equipment, mixing, and mastering costs
6. Youth programming — professional studio access and mentorship for Lincoln County youth

---

## Repo Layout

```
site/               ← public site (deployed to CF Pages)
docs/               ← grant docs, narrative bank, submission materials
project-specs/      ← canonical project specification
workflows/          ← grant pipeline workflow
prompts/            ← AI agent activation prompts
scripts/            ← utility scripts
generated/          ← agent inventory (auto-generated)
wrangler.toml       ← Cloudflare Pages / Wrangler config
```

---

## Links

- **Live site:** https://hope-sessions.pages.dev *(or custom domain once connected)*
- **PMA Recording Studios:** https://pmastudios.com
- **Andrejack on Spotify:** https://open.spotify.com/artist/7F3dLxEyOL3kTXMootzocB
- **Album — Hope:** https://open.spotify.com/album/1ndzVS6hVxs6kjkd0uFCEn
- **Contact:** pmastudios@hotmail.com