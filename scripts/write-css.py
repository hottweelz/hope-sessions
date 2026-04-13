#!/usr/bin/env python3
"""Write the Hope Sessions styles.css rewrite."""

css = r"""/* ================================================================
   Hope Sessions — styles.css
   Dark editorial theme | WCAG 2.2 AA | Mobile-first
   Team: UX Architect + UI Designer + Frontend Developer + Accessibility Auditor
   ================================================================ */

/* ================================================================
   LAYER 0 — GOOGLE FONTS IMPORT
   ================================================================ */
@import url("https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,700;1,9..144,500&family=Oswald:wght@400;500;600&family=Source+Sans+3:ital,wght@0,400;0,500;0,600;1,400&display=swap");

/* ================================================================
   LAYER 1 — PRIMITIVE TOKENS
   ================================================================ */
:root {
  /* Color primitives */
  --prim-slate-1000:  #07090d;
  --prim-slate-950:   #0b0e14;
  --prim-slate-900:   #111620;
  --prim-slate-850:   #141924;
  --prim-slate-800:   #1a2030;
  --prim-slate-700:   #2c3a4e;
  --prim-slate-600:   #3e5168;
  --prim-slate-400:   #8a99ab;
  --prim-slate-200:   #dce6ef;
  --prim-slate-100:   #edf3f8;

  --prim-amber-700:   #7a4e1e;
  --prim-amber-500:   #d48c35;
  --prim-amber-400:   #eea84a;
  --prim-amber-200:   #f5d486;

  --prim-sky-800:     #2e4f6b;
  --prim-sky-500:     #6baed4;
  --prim-sky-300:     #a8d4ec;

  /* ================================================================
     LAYER 2 — SEMANTIC TOKENS
     ================================================================ */

  /* Backgrounds */
  --color-bg:             var(--prim-slate-950);   /* page */
  --color-surface:        var(--prim-slate-900);   /* cards, panels */
  --color-surface-alt:    var(--prim-slate-800);   /* elevated / hover */
  --color-section-stripe: rgba(17, 22, 32, 0.70);  /* alternating section */

  /* Text */
  --color-text:           var(--prim-slate-200);
  --color-text-muted:     var(--prim-slate-400);
  --color-text-inverse:   var(--prim-slate-950);
  --color-text-on-accent: #0e1117;  /* 6.97:1 on #d48c35 ✅ */

  /* Accent */
  --color-accent:         var(--prim-amber-500);   /* #d48c35 */
  --color-accent-hover:   var(--prim-amber-400);   /* #eea84a */
  --color-accent-dim:     var(--prim-amber-700);
  --color-accent-gold:    var(--prim-amber-200);   /* hope gold — use sparingly */
  --color-cool:           var(--prim-sky-500);
  --color-cool-dim:       var(--prim-sky-800);

  /* Borders */
  --color-border:         rgba(138, 153, 171, 0.18);
  --color-border-strong:  rgba(138, 153, 171, 0.28);
  --color-border-accent:  rgba(212, 140, 53, 0.32);

  /* Focus — WCAG 2.4.11: #eea84a on #0b0e14 = 10.2:1 ✅ */
  --color-focus:          var(--prim-amber-400);

  /* CONTRAST NOTE (WCAG 1.4.3):
     NEVER use light text on amber backgrounds.
     --color-accent (#d48c35): only dark text (#0e1117) — ratio 6.97:1 ✅
     --color-accent-hover (#eea84a): only dark text (#0e1117) — ratio 9.77:1 ✅
     White on amber (#d48c35) = 2.61:1 ❌ FORBIDDEN */

  /* Typography */
  --font-serif:    "Fraunces", Georgia, "Times New Roman", serif;
  --font-label:    "Oswald", "Arial Narrow", Arial, sans-serif;
  --font-body:     "Source Sans 3", "Helvetica Neue", Arial, sans-serif;

  --weight-normal:   400;
  --weight-medium:   500;
  --weight-semibold: 600;
  --weight-bold:     700;

  /* Spacing (8px base) */
  --space-1:  0.5rem;    /* 8px */
  --space-2:  0.75rem;   /* 12px */
  --space-3:  1rem;      /* 16px */
  --space-4:  1.5rem;    /* 24px */
  --space-5:  2rem;      /* 32px */
  --space-6:  3rem;      /* 48px */
  --space-7:  4rem;      /* 64px */
  --space-8:  5.5rem;    /* 88px */
  --space-9:  7rem;      /* 112px */

  /* Layout */
  --shell:         76rem;    /* 1216px */
  --shell-narrow:  48rem;    /* 768px */
  --gutter:        1.25rem;  /* mobile inline padding */
  --gutter-lg:     2rem;     /* desktop inline padding */

  /* Header */
  --header-height: 4.5rem;
  --header-bg:     rgba(11, 14, 20, 0.88);
  --header-blur:   16px;

  /* Radius */
  --radius-sm:   6px;
  --radius-md:   12px;
  --radius-lg:   18px;
  --radius-xl:   24px;
  --radius-pill: 9999px;

  /* Shadows */
  --shadow-sm:     0 2px 8px rgba(0, 0, 0, 0.24);
  --shadow-md:     0 8px 24px rgba(0, 0, 0, 0.30);
  --shadow-lg:     0 20px 48px rgba(0, 0, 0, 0.38);
  --shadow-accent: 0 12px 28px rgba(212, 140, 53, 0.24);

  /* Z-index */
  --z-skip:   100;
  --z-header: 50;
  --z-raised: 10;

  /* Motion */
  --ease:     cubic-bezier(0.4, 0.0, 0.2, 1);
  --dur-fast: 120ms;
  --dur-base: 200ms;
  --dur-slow: 320ms;
}

/* ================================================================
   RESET
   ================================================================ */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
}

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

img, video {
  max-width: 100%;
  height: auto;
  display: block;
}

ul, ol {
  list-style: none;
}

button, input, textarea, select {
  font: inherit;
}

/* ================================================================
   ACCESSIBILITY UTILITIES
   ================================================================ */

/* Visually hidden — for screen-reader-only text */
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* Skip link — first element in DOM, only visible on :focus */
.skip-link {
  position: absolute;
  left: 1rem;
  top: -4rem;
  z-index: var(--z-skip);
  padding: 0.75rem 1.25rem;
  border-radius: var(--radius-pill);
  background: var(--prim-slate-100);
  color: #111111;                /* 15.27:1 contrast ✅ */
  font-family: var(--font-label);
  font-weight: var(--weight-semibold);
  font-size: 0.9rem;
  letter-spacing: 0.04em;
  text-decoration: none;
  white-space: nowrap;
  box-shadow: var(--shadow-md);
  transition: top var(--dur-fast) var(--ease);
}

/* :focus (not :focus-visible) — skip links must always show on keyboard activation */
.skip-link:focus {
  top: 1rem;
  outline: 3px solid #111111;
  outline-offset: 3px;
}

/* Global focus-visible — WCAG 2.4.11 Focus Appearance */
:focus-visible {
  outline: 3px solid var(--color-focus);
  outline-offset: 4px;
  border-radius: 3px;
}

/* ================================================================
   BASE STYLES
   ================================================================ */
body {
  font-family: var(--font-body);
  font-size: 1.0625rem;    /* 17px */
  font-weight: var(--weight-normal);
  line-height: 1.72;
  color: var(--color-text);
  background-color: var(--color-bg);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
}

/* ================================================================
   TYPOGRAPHY
   ================================================================ */
h1, .h1 {
  font-family: var(--font-serif);
  font-size: clamp(3.25rem, 10vw, 7rem);
  font-weight: var(--weight-bold);
  line-height: 0.92;
  letter-spacing: -0.035em;
  font-optical-sizing: auto;
  margin-bottom: var(--space-4);
}

h2, .h2 {
  font-family: var(--font-serif);
  font-size: clamp(2rem, 5.5vw, 3.5rem);
  font-weight: var(--weight-bold);
  line-height: 0.96;
  letter-spacing: -0.02em;
  font-optical-sizing: auto;
  margin-bottom: var(--space-4);
}

h3, .h3 {
  font-family: var(--font-label);
  font-size: 1.1rem;
  font-weight: var(--weight-semibold);
  line-height: 1.3;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--color-accent-hover);
  margin-bottom: var(--space-2);
}

p {
  font-size: 1.0625rem;
  line-height: 1.72;
  margin-bottom: var(--space-4);
  max-width: 64ch;
}

p:last-child {
  margin-bottom: 0;
}

.text-lead {
  font-size: clamp(1.15rem, 2.5vw, 1.3rem);
  line-height: 1.58;
  color: var(--prim-slate-100);
  margin-bottom: var(--space-4);
  max-width: 42rem;
}

.eyebrow {
  font-family: var(--font-label);
  font-size: 0.8125rem;
  font-weight: var(--weight-medium);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--color-accent-hover);
  margin-bottom: var(--space-2);
}

.fine-print {
  font-size: 0.875rem;
  line-height: 1.55;
  color: var(--color-text-muted);
}

strong {
  font-weight: var(--weight-semibold);
  color: var(--prim-slate-100);
}

em {
  font-style: italic;
}

a {
  color: var(--prim-slate-200);
  text-underline-offset: 3px;
  text-decoration-color: rgba(138, 153, 171, 0.35);
  transition:
    color var(--dur-base) var(--ease),
    text-decoration-color var(--dur-base) var(--ease);
}

a:hover {
  color: var(--color-accent-hover);
  text-decoration-color: rgba(238, 168, 74, 0.5);
}

/* ================================================================
   LAYOUT — SHELL
   ================================================================ */
.shell {
  width: min(calc(100% - var(--gutter) * 2), var(--shell));
  margin-inline: auto;
}

.shell--narrow {
  width: min(calc(100% - var(--gutter) * 2), var(--shell-narrow));
  margin-inline: auto;
}

/* ================================================================
   BUTTONS
   ================================================================ */
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  height: 3rem;
  padding-inline: 1.5rem;
  border-radius: var(--radius-pill);
  font-family: var(--font-label);
  font-size: 0.875rem;
  font-weight: var(--weight-semibold);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  text-decoration: none;
  white-space: nowrap;
  cursor: pointer;
  border: 2px solid transparent;
  transition:
    background-color var(--dur-base) var(--ease),
    color var(--dur-base) var(--ease),
    border-color var(--dur-base) var(--ease),
    box-shadow var(--dur-base) var(--ease);
}

.button--solid {
  background-color: var(--color-accent);
  color: var(--color-text-on-accent);
  border-color: var(--color-accent);
}

.button--solid:hover {
  background-color: var(--color-accent-hover);
  border-color: var(--color-accent-hover);
  color: var(--color-text-on-accent);
  box-shadow: var(--shadow-accent);
  text-decoration: none;
}

.button--ghost {
  background-color: transparent;
  color: var(--color-text);
  border-color: var(--color-border-strong);
}

.button--ghost:hover {
  border-color: var(--color-accent);
  color: var(--color-accent-hover);
  background-color: rgba(212, 140, 53, 0.06);
  text-decoration: none;
}

.button--sm {
  height: 2.5rem;
  padding-inline: 1.1rem;
  font-size: 0.8125rem;
}

.button:focus-visible {
  outline: 3px solid var(--color-focus);
  outline-offset: 4px;
}

/* ================================================================
   SITE HEADER
   ================================================================ */
.site-header {
  position: sticky;
  top: 0;
  z-index: var(--z-header);
  background: var(--header-bg);
  backdrop-filter: blur(var(--header-blur));
  -webkit-backdrop-filter: blur(var(--header-blur));
  border-bottom: 1px solid var(--color-border);
}

/* Forced-colors / high-contrast mode */
@media (forced-colors: active) {
  .site-header {
    background: Canvas;
    border-bottom: 1px solid ButtonText;
  }
}

.site-header__inner {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  height: var(--header-height);
  flex-wrap: wrap;
  padding-block: 0.5rem;
}

/* Brand wordmark */
.brand {
  text-decoration: none;
  flex-shrink: 0;
}

.brand__wordmark {
  font-family: var(--font-serif);
  font-size: 1.25rem;
  font-weight: var(--weight-bold);
  color: var(--prim-slate-100);
  letter-spacing: -0.02em;
  font-optical-sizing: auto;
  white-space: nowrap;
}

.brand__wordmark strong {
  color: var(--color-accent-gold);
}

.brand:hover .brand__wordmark {
  color: var(--color-text);
}

/* Primary nav */
.site-nav {
  flex: 1;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none;
}

.site-nav::-webkit-scrollbar {
  display: none;
}

.site-nav__list {
  display: flex;
  gap: 0;
  list-style: none;
  white-space: nowrap;
}

.site-nav__list a {
  display: block;
  padding: 0.5rem 0.75rem;
  font-family: var(--font-label);
  font-size: 0.8125rem;
  font-weight: var(--weight-medium);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--color-text-muted);
  text-decoration: none;
  border-radius: var(--radius-sm);
  transition: color var(--dur-base) var(--ease);
}

.site-nav__list a:hover {
  color: var(--color-accent-hover);
}

/* PMA logo pill — white-bg logo sits in a light container */
.header-logo {
  flex-shrink: 0;
  background: rgba(255, 255, 255, 0.96);
  border-radius: var(--radius-pill);
  padding: 0.3rem 0.75rem;
  display: flex;
  align-items: center;
  box-shadow: var(--shadow-sm);
}

.header-logo img {
  width: min(9rem, 22vw);
  height: auto;
  display: block;
}

/* Scroll offset — header height + 16px breathing room */
.hero, .section, .section--contact {
  scroll-margin-top: 7rem;   /* mobile: header may wrap */
}

@media (min-width: 48rem) {
  .hero, .section, .section--contact {
    scroll-margin-top: 5.5rem;
  }
}

/* ================================================================
   SECTION — BASE
   ================================================================ */
.section {
  padding-block: var(--space-8);
}

.section--surface {
  background-color: var(--color-surface);
}

.section-header {
  margin-bottom: var(--space-6);
}

.section-header--narrow {
  max-width: var(--shell-narrow);
}

/* ================================================================
   HERO
   ================================================================ */
.hero {
  background: linear-gradient(
    165deg,
    var(--prim-slate-950) 0%,
    var(--prim-slate-900) 50%,
    rgba(26, 32, 48, 0.80) 100%
  );
  padding-block: var(--space-8);
}

.hero__layout {
  display: grid;
  gap: var(--space-6);
  align-items: center;
  min-height: calc(100svh - var(--header-height));
}

@media (min-width: 48rem) {
  .hero__layout {
    grid-template-columns: 1fr 1fr;
    min-height: calc(100svh - var(--header-height));
    gap: var(--space-7);
  }
}

.hero__body {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.hero__body h1 {
  color: var(--prim-slate-100);
  margin-bottom: var(--space-4);
}

.hero__ctas {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
  margin-block: var(--space-5);
}

.hero__proof-rail {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-1);
  margin-top: var(--space-2);
}

.proof-pill {
  display: inline-flex;
  align-items: center;
  padding: 0.3rem 0.75rem;
  border-radius: var(--radius-pill);
  border: 1px solid var(--color-border-accent);
  font-family: var(--font-label);
  font-size: 0.75rem;
  font-weight: var(--weight-medium);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-text-muted);
}

/* Hero media — Hope album cover */
.hero__media {
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

@media (min-width: 48rem) {
  .hero__media {
    justify-content: flex-end;
  }
}

.asset-card {
  width: 100%;
  position: relative;
}

.asset-card--cover {
  border-radius: var(--radius-xl);
  overflow: hidden;
  box-shadow: var(--shadow-lg), 0 0 80px rgba(107, 174, 212, 0.08);
  max-width: 520px;
}

.asset-card--cover .asset-image {
  width: 100%;
  height: auto;
  aspect-ratio: 75 / 56;   /* matches 1200×896 native proportions */
  object-fit: cover;
  display: block;
}

.asset-card__caption {
  padding: 0.75rem 1rem;
  background: rgba(11, 14, 20, 0.72);
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  font-family: var(--font-body);
  font-style: italic;
  border-top: 1px solid var(--color-border);
}

/* ================================================================
   ABOUT SECTION
   ================================================================ */
.about__layout {
  display: grid;
  gap: var(--space-5);
}

@media (min-width: 48rem) {
  .about__layout {
    grid-template-columns: 1fr 1.4fr;
    gap: var(--space-7);
    align-items: start;
  }
}

.about__header h2 {
  margin-bottom: var(--space-2);
}

.credential-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  margin-top: var(--space-4);
}

.credential-list li {
  padding-left: 1.25rem;
  position: relative;
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  line-height: 1.5;
}

.credential-list li::before {
  content: "—";
  position: absolute;
  left: 0;
  color: var(--color-accent);
  font-weight: var(--weight-semibold);
}

/* ================================================================
   INITIATIVE GRID
   ================================================================ */
.initiative-grid {
  display: grid;
  gap: var(--space-4);
  margin-top: var(--space-5);
}

@media (min-width: 40rem) {
  .initiative-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 64rem) {
  .initiative-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

.initiative-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  padding: var(--space-5);
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  transition: border-color var(--dur-base) var(--ease),
              box-shadow var(--dur-base) var(--ease);
}

.initiative-card:hover {
  border-color: var(--color-border-accent);
  box-shadow: var(--shadow-md);
}

.initiative-card__marker {
  font-family: var(--font-label);
  font-size: 2rem;
  font-weight: var(--weight-bold);
  color: var(--color-accent-dim);
  line-height: 1;
  margin-bottom: var(--space-1);
}

.initiative-card h3 {
  margin-bottom: 0;
}

.initiative-card p {
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  max-width: none;
  margin-bottom: 0;
}

/* ================================================================
   PROOF GRID
   ================================================================ */
.proof-grid {
  display: grid;
  gap: var(--space-4);
  margin-top: var(--space-5);
}

@media (min-width: 48rem) {
  .proof-grid {
    grid-template-columns: repeat(3, 1fr);
  }

  .proof-card--feature {
    grid-column: 1 / -1;
    display: grid;
    grid-template-columns: 1fr 1.2fr;
    gap: var(--space-6);
    align-items: start;
  }
}

.proof-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  overflow: hidden;
  transition: border-color var(--dur-base) var(--ease),
              box-shadow var(--dur-base) var(--ease);
}

.proof-card:hover {
  border-color: var(--color-border-accent);
  box-shadow: var(--shadow-md);
}

.proof-card--feature {
  border-color: var(--color-border-accent);
  box-shadow: var(--shadow-lg);
}

.proof-card__media {
  overflow: hidden;
  margin: 0;
}

.proof-card__media img {
  width: 100%;
  height: auto;
  display: block;
  object-fit: cover;
  aspect-ratio: 4 / 3;
}

@media (min-width: 48rem) {
  .proof-card--feature .proof-card__media img {
    height: 100%;
    min-height: 360px;
    aspect-ratio: auto;
    object-fit: cover;
  }
}

.proof-card__body {
  padding: var(--space-5);
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  justify-content: center;
}

.proof-card__body h3 {
  margin-bottom: 0;
}

.proof-card__body p {
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  max-width: 52ch;
  margin-bottom: 0;
  line-height: 1.62;
}

/* ================================================================
   CONTACT SECTION
   ================================================================ */
.section--contact {
  background: linear-gradient(
    180deg,
    var(--color-bg) 0%,
    var(--prim-slate-900) 100%
  );
}

.connect-layout {
  display: grid;
  gap: var(--space-7);
  margin-top: var(--space-5);
}

@media (min-width: 56rem) {
  .connect-layout {
    grid-template-columns: 1fr 1.6fr;
    align-items: start;
  }
}

.connect-info p {
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  max-width: none;
}

.contact-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  margin-block: var(--space-4);
}

.contact-list li {
  font-size: 0.9375rem;
  color: var(--color-text-muted);
}

.contact-list a {
  color: var(--prim-slate-200);
  font-weight: var(--weight-medium);
}

.connect-actions {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
  margin-top: var(--space-4);
}

/* ================================================================
   CONTACT FORM
   ================================================================ */
.contact-form {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  padding: var(--space-6);
}

.form-error-summary {
  padding: var(--space-3) var(--space-4);
  background: rgba(180, 50, 50, 0.15);
  border: 1px solid rgba(180, 50, 50, 0.40);
  border-radius: var(--radius-md);
  color: #f9a8a8;
  font-size: 0.9rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.form-group--radio {
  border: none;
  padding: 0;
}

.form-label {
  font-family: var(--font-label);
  font-size: 0.8125rem;
  font-weight: var(--weight-medium);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--color-text-muted);
}

.required-indicator {
  color: var(--color-accent-hover);
}

.radio-options {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
  margin-top: var(--space-1);
}

.radio-label {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  cursor: pointer;
  padding: 0.35rem 0;
}

.radio-label input[type="radio"] {
  accent-color: var(--color-accent);
  width: 1rem;
  height: 1rem;
  flex-shrink: 0;
}

.form-control {
  width: 100%;
  padding: 0.75rem 1rem;
  background: rgba(44, 58, 78, 0.40);
  border: 1px solid var(--color-border-strong);
  border-radius: var(--radius-md);
  color: var(--color-text);
  font-size: 1rem;
  line-height: 1.5;
  transition:
    border-color var(--dur-base) var(--ease),
    box-shadow var(--dur-base) var(--ease);
  -webkit-appearance: none;
  appearance: none;
}

.form-control:focus {
  outline: none;
  border-color: var(--color-accent);
  box-shadow: 0 0 0 3px rgba(212, 140, 53, 0.28);
}

.form-control::placeholder {
  color: var(--prim-slate-400);
  opacity: 0.7;
}

textarea.form-control {
  resize: vertical;
  min-height: 9rem;
}

.field-error {
  font-size: 0.875rem;
  color: #f9a8a8;
  margin-bottom: 0;
  max-width: none;
}

/* ================================================================
   FOOTER
   ================================================================ */
.site-footer {
  background: var(--prim-slate-1000);
  border-top: 1px solid var(--color-border);
  padding-block: var(--space-7);
}

.site-footer__inner {
  display: grid;
  gap: var(--space-5);
}

@media (min-width: 48rem) {
  .site-footer__inner {
    grid-template-columns: 1fr 1fr;
    align-items: start;
  }
}

.footer-brand {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.footer-nav__list {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-1) var(--space-3);
  list-style: none;
}

.footer-nav__list a {
  font-family: var(--font-label);
  font-size: 0.8125rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-text-muted);
  text-decoration: none;
  padding: 0.25rem 0;
}

.footer-nav__list a:hover {
  color: var(--color-accent-hover);
}

.footer-copy {
  grid-column: 1 / -1;
  border-top: 1px solid var(--color-border);
  padding-top: var(--space-4);
  color: var(--color-text-muted);
}

/* ================================================================
   DESKTOP REFINEMENTS (64rem+)
   ================================================================ */
@media (min-width: 64rem) {
  .shell {
    --gutter: var(--gutter-lg);
  }

  .site-nav__list a {
    padding-inline: 1rem;
  }

  .section {
    padding-block: var(--space-9);
  }
}
"""

with open('/Users/jamestylee/Projects/denver-nc-music-grants/site/hope-sessions/assets/css/styles.css', 'w') as f:
    f.write(css)

print("styles.css written:", len(css), "chars")
