#!/usr/bin/env python3
"""Write the Hope Sessions index.html rewrite."""

html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hope Sessions — Music, Recording &amp; Creative Access | PMA Recording Studios</title>
  <meta name="description" content="Hope Sessions is a recording initiative led by Paul Andrejack at PMA Recording Studios in Denver, NC. Original music creation, artist development, and future community access to professional recording.">
  <link rel="canonical" href="https://www.pmarecordingstudios.com/hope-sessions/">

  <!-- Open Graph -->
  <meta property="og:type"        content="website">
  <meta property="og:url"         content="https://www.pmarecordingstudios.com/hope-sessions/">
  <meta property="og:title"       content="Hope Sessions — Music, Recording &amp; Creative Access">
  <meta property="og:description" content="A Hope-centered recording initiative by Paul Andrejack at PMA Recording Studios in Denver, North Carolina.">
  <meta property="og:image"       content="assets/img/hope.png">
  <meta property="og:site_name"   content="PMA Recording Studios">
  <meta property="og:locale"      content="en_US">

  <!-- Twitter Card -->
  <meta name="twitter:card"        content="summary_large_image">
  <meta name="twitter:title"       content="Hope Sessions — Music, Recording &amp; Creative Access">
  <meta name="twitter:description" content="A Hope-centered recording initiative by Paul Andrejack at PMA Recording Studios in Denver, North Carolina.">
  <meta name="twitter:image"       content="assets/img/hope.png">

  <!-- Structured Data -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "WebPage",
        "@id": "https://www.pmarecordingstudios.com/hope-sessions/",
        "url": "https://www.pmarecordingstudios.com/hope-sessions/",
        "name": "Hope Sessions — Music, Recording and Creative Access | PMA Recording Studios",
        "description": "Hope Sessions is a Hope-centered recording initiative led by Paul Andrejack at PMA Recording Studios in Denver, NC. Original music, artist development, and community creative access.",
        "inLanguage": "en-US",
        "author":    { "@id": "https://www.pmarecordingstudios.com/hope-sessions/#paul-andrejack" },
        "publisher": { "@id": "https://www.pmarecordingstudios.com/#pma-recording-studios" }
      },
      {
        "@type": "Person",
        "@id": "https://www.pmarecordingstudios.com/hope-sessions/#paul-andrejack",
        "name": "Paul Andrejack",
        "jobTitle": ["Independent Artist", "Record Producer", "Audio Engineer", "Songwriter"],
        "url": "https://www.pmarecordingstudios.com",
        "worksFor":  { "@id": "https://www.pmarecordingstudios.com/#pma-recording-studios" },
        "memberOf":  { "@id": "https://www.pmarecordingstudios.com/hope-sessions/#andrejack-band" },
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "Denver",
          "addressRegion": "NC",
          "addressCountry": "US"
        }
      },
      {
        "@type": "LocalBusiness",
        "@id": "https://www.pmarecordingstudios.com/#pma-recording-studios",
        "name": "PMA Recording Studios",
        "url": "https://www.pmarecordingstudios.com",
        "email": "pmastudios@hotmail.com",
        "telephone": "+16318751380",
        "description": "Professional recording studio in Denver, North Carolina offering recording, mixing, mastering, and music production services.",
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "Denver",
          "addressRegion": "NC",
          "addressCountry": "US"
        },
        "founder": { "@id": "https://www.pmarecordingstudios.com/hope-sessions/#paul-andrejack" }
      },
      {
        "@type": "MusicGroup",
        "@id": "https://www.pmarecordingstudios.com/hope-sessions/#andrejack-band",
        "name": "Andrejack",
        "description": "Independent music group fronted by Paul Andrejack, based in Denver, North Carolina. Known for the album Hope.",
        "genre": ["Rock", "Indie Rock"],
        "member": { "@id": "https://www.pmarecordingstudios.com/hope-sessions/#paul-andrejack" }
      },
      {
        "@type": "Organization",
        "@id": "https://www.pmarecordingstudios.com/hope-sessions/#hope-sessions",
        "name": "Hope Sessions",
        "url": "https://www.pmarecordingstudios.com/hope-sessions/",
        "description": "A Hope-centered recording initiative led by Paul Andrejack at PMA Recording Studios in Denver, North Carolina. Focused on original music creation, artist development, and future community access to professional recording infrastructure.",
        "founder":  { "@id": "https://www.pmarecordingstudios.com/hope-sessions/#paul-andrejack" },
        "location": {
          "@type": "Place",
          "address": {
            "@type": "PostalAddress",
            "addressLocality": "Denver",
            "addressRegion": "NC",
            "addressCountry": "US"
          }
        }
      }
    ]
  }
  </script>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,700;1,9..144,500&family=Oswald:wght@400;500;600&family=Source+Sans+3:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>

  <!-- Skip navigation — first focusable element -->
  <a class="skip-link" href="#main-content">Skip to main content</a>

  <!-- SITE HEADER ============================================== -->
  <header class="site-header">
    <div class="site-header__inner shell">

      <a class="brand" href="#top" aria-label="Hope Sessions — return to top of page">
        <span class="brand__wordmark"><strong>Hope</strong> Sessions</span>
      </a>

      <nav class="site-nav" aria-label="Primary navigation">
        <ul class="site-nav__list" role="list">
          <li><a href="#why-hope">Why Hope</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#initiative">Initiative</a></li>
          <li><a href="#proof">Proof</a></li>
          <li><a href="#partners">Partners</a></li>
          <li><a href="#connect">Connect</a></li>
        </ul>
      </nav>

      <!-- PMA logo: 2064x512 wide-banner. White-background logo
           sits in a light pill so the white blends naturally. -->
      <div class="header-logo">
        <img
          src="assets/img/pma_logo.png"
          alt="PMA Recording Studios"
          width="2064"
          height="512"
          loading="eager"
          onerror="this.style.display='none'; this.nextElementSibling.removeAttribute('hidden');"
        >
        <span hidden>PMA Recording Studios</span>
      </div>

    </div>
  </header>

  <!-- MAIN ===================================================== -->
  <main id="main-content">

    <!-- HERO --------------------------------------------------- -->
    <section class="hero" id="top" aria-labelledby="hero-heading">
      <div class="hero__layout shell">

        <div class="hero__body">
          <p class="eyebrow">PMA Recording Studios &middot; Denver, NC</p>
          <h1 id="hero-heading">Hope<br>Sessions</h1>
          <p class="text-lead">Music, recording, and creative access built by Paul Andrejack in Denver, North Carolina.</p>
          <p>Hope Sessions is a Hope-centered recording initiative rooted in original music, artist development, and the belief that serious creative work deserves a credible path from idea to finished form. Built through PMA Recording Studios, the project begins with new music from Paul Andrejack and grows toward broader access, collaboration, and community-facing creative opportunity.</p>
          <div class="hero__ctas">
            <a class="button button--solid" href="#connect">Partner With Hope Sessions</a>
            <a class="button button--ghost" href="#why-hope">Explore The Story</a>
          </div>
          <div class="hero__proof-rail" aria-label="Key facts about Hope Sessions">
            <span class="proof-pill">Denver, NC &middot; Lincoln County</span>
            <span class="proof-pill">PMA Recording Studios</span>
            <span class="proof-pill">Album: <em>Hope</em> &mdash; Andrejack</span>
          </div>
        </div>

        <div class="hero__media">
          <figure class="asset-card asset-card--cover">
            <img
              class="asset-image"
              src="assets/img/hope.png"
              alt="Hope — album cover art by the band Andrejack, the artistic foundation of this initiative"
              width="1200"
              height="896"
              loading="eager"
              onerror="this.parentElement.style.display='none';"
            >
            <figcaption class="asset-card__caption">
              <em>Hope</em> by Andrejack &mdash; the album this initiative builds from.
            </figcaption>
          </figure>
        </div>

      </div>
    </section>

    <!-- WHY HOPE ----------------------------------------------- -->
    <section class="section" id="why-hope" aria-labelledby="why-hope-heading">
      <div class="shell shell--narrow">
        <p class="eyebrow">Why Hope</p>
        <h2 id="why-hope-heading">A real artistic foundation, not borrowed branding.</h2>
        <p>Hope Sessions begins with real artistic history. Paul Andrejack and the band Andrejack established <em>Hope</em> as part of their creative identity through the album of the same name. That body of work is the origin of this initiative &mdash; not a tagline applied later.</p>
        <p>This initiative builds from that foundation, extending the idea of hope through new music, disciplined recording, and future pathways for collaboration, access, and artist growth. The name is earned. The work came first.</p>
      </div>
    </section>

    <!-- ABOUT PAUL ANDREJACK ----------------------------------- -->
    <section class="section section--surface" id="about" aria-labelledby="about-heading">
      <div class="about__layout shell">
        <header class="about__header">
          <p class="eyebrow">Built by Paul Andrejack</p>
          <h2 id="about-heading">Artist. Songwriter. Engineer. Producer.</h2>
        </header>
        <div class="about__copy">
          <p>Paul Andrejack is an independent artist, songwriter, engineer, and producer based in Denver, North Carolina. Through his work with Andrejack and PMA Recording Studios, he has built a practice grounded in original music, studio craft, and long-term artist development. Hope Sessions is the natural extension of that work &mdash; not a pivot, but a continuation.</p>
          <p>Using a professional recording environment as infrastructure, the initiative creates new music and lays the groundwork for broader creative opportunity in and around Lincoln County.</p>
          <ul class="credential-list" aria-label="Paul Andrejack professional credentials">
            <li>Independent artist and frontman of Andrejack</li>
            <li>Owner and operator of PMA Recording Studios, Denver, NC</li>
            <li>Songwriter, recording engineer, and music producer</li>
            <li>Artist development experience across original projects and studio collaborations</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- INITIATIVE --------------------------------------------- -->
    <section class="section" id="initiative" aria-labelledby="initiative-heading">
      <div class="shell">
        <div class="section-header section-header--narrow">
          <p class="eyebrow">What This Initiative Is Building</p>
          <h2 id="initiative-heading">Start with strong new work. Build toward broader access.</h2>
          <p class="text-lead">The first phase of Hope Sessions is a focused recording project centered on new original music. That core creates the artistic platform for everything that follows.</p>
        </div>
        <div class="initiative-grid">
          <article class="initiative-card">
            <div class="initiative-card__marker" aria-hidden="true">01</div>
            <h3>New Work Recording</h3>
            <p>A disciplined recording and finishing process for new songs that extend the artistic world of <em>Hope</em>. Scoped for completion, not concept.</p>
          </article>
          <article class="initiative-card">
            <div class="initiative-card__marker" aria-hidden="true">02</div>
            <h3>Artist Development</h3>
            <p>A framework for turning strong creative ideas into finished, release-ready work with greater clarity, craft, and intentionality than working alone.</p>
          </article>
          <article class="initiative-card">
            <div class="initiative-card__marker" aria-hidden="true">03</div>
            <h3>Future Community Access</h3>
            <p>A long-term model for making professional recording support more accessible through carefully built partnerships and public-facing formats in Lincoln County.</p>
          </article>
        </div>
      </div>
    </section>

    <!-- WHY IT MATTERS ----------------------------------------- -->
    <section class="section section--surface" id="why-matters" aria-labelledby="why-matters-heading">
      <div class="shell shell--narrow">
        <p class="eyebrow">Lincoln County Context</p>
        <h2 id="why-matters-heading">Professional creative infrastructure in a place that needs it.</h2>
        <p>Artists outside major market centers often have talent, ideas, and drive but fewer pathways to complete work at a strong professional level. Denver, North Carolina and Lincoln County sit outside the institutional network of urban arts funding, recording access, and industry infrastructure.</p>
        <p>Hope Sessions responds to that gap from inside the community &mdash; using real recording infrastructure and an artist-led process to create new music now while building toward broader creative access over time. This is not a program imported from outside. It is built here, by someone already working here.</p>
      </div>
    </section>

    <!-- PROOF -------------------------------------------------- -->
    <section class="section" id="proof" aria-labelledby="proof-heading">
      <div class="shell">
        <div class="section-header section-header--narrow">
          <p class="eyebrow">Proof, Process &amp; Practice</p>
          <h2 id="proof-heading">Built from real work.</h2>
          <p>Hope Sessions is grounded in active creative practice &mdash; released work, recording experience, and a working studio environment that already supports serious music-making.</p>
        </div>
        <div class="proof-grid">

          <article class="proof-card proof-card--feature" aria-label="The Hope album as artistic foundation">
            <figure class="proof-card__media">
              <img
                src="assets/img/hope.png"
                alt="Hope — album by Andrejack, proof of existing released work and creative identity"
                width="600"
                height="448"
                loading="lazy"
              >
            </figure>
            <div class="proof-card__body">
              <h3>The artistic world of <em>Hope</em></h3>
              <p>The album <em>Hope</em> by Andrejack establishes the artistic foundation this initiative builds from &mdash; original songwriting, disciplined recording, and a coherent creative identity that predates the initiative by years. Hope Sessions is the natural continuation of that work. The name is earned through prior creative output and an existing audience connection, not constructed for a grant application.</p>
              <a
                class="button button--ghost button--sm"
                href="https://open.spotify.com/search/andrejack"
                target="_blank"
                rel="noreferrer"
                aria-label="Find Andrejack on Spotify (opens in a new tab)"
              >
                Find Andrejack on Spotify
                <span class="visually-hidden">(opens in a new tab)</span>
              </a>
            </div>
          </article>

          <article class="proof-card" aria-label="Working studio infrastructure">
            <div class="proof-card__body">
              <h3>Working Studio Infrastructure</h3>
              <p>PMA Recording Studios in Denver, NC is an active professional recording environment. The infrastructure for Hope Sessions is already in place &mdash; not a proposal to build something new, but to use what already exists with greater purpose and public benefit.</p>
            </div>
          </article>

          <article class="proof-card" aria-label="Grant documentation package">
            <div class="proof-card__body">
              <h3>Grant Documentation</h3>
              <p>Work samples, project documentation, and a full evidence package are assembled as part of the Artist Support Grant application targeting the Arts &amp; Science Council Charlotte-Mecklenburg consortium for Lincoln County, with a September 2026 submission deadline.</p>
            </div>
          </article>

          <article class="proof-card" aria-label="Credits and production experience">
            <div class="proof-card__body">
              <h3>Credits &amp; Experience</h3>
              <p>Contact Hope Sessions directly for Paul Andrejack's full body of work, studio production credits, engineering history, and artist development experience relevant to your partnership or collaboration inquiry.</p>
            </div>
          </article>

        </div>
      </div>
    </section>

    <!-- PARTNER PATHWAYS -------------------------------------- -->
    <section class="section section--surface" id="partners" aria-labelledby="partners-heading">
      <div class="shell shell--narrow">
        <p class="eyebrow">For Partners</p>
        <h2 id="partners-heading">Built to grow through thoughtful collaboration.</h2>
        <p>Hope Sessions is designed to grow through specific, credible partnerships &mdash; not generic programming promises. Schools, churches, nonprofits, and arts organizations can help shape future formats around creative access, artist development, workshops, and story-centered music activity in Lincoln County and the broader region.</p>
        <p>The goal is to build opportunities that genuinely fit the people and communities involved. If your organization is looking for a community-rooted creative partner, reach out.</p>
        <a class="button button--solid" href="#connect">Start A Conversation</a>
      </div>
    </section>

    <!-- FOR ARTISTS ------------------------------------------- -->
    <section class="section" id="artists" aria-labelledby="artists-heading">
      <div class="shell shell--narrow">
        <p class="eyebrow">For Artists</p>
        <h2 id="artists-heading">Start with serious work. Build toward broader support.</h2>
        <p>This initiative begins with Paul Andrejack's own next chapter of original music &mdash; but it is designed to grow toward broader support for artists who need stronger pathways to finished, high-quality creative output in the region.</p>
        <p>If that future direction is relevant to your work, stay connected. There is no timeline commitment, only an honest invitation to remain in conversation as the initiative develops.</p>
        <a class="button button--ghost" href="#connect">Stay In Touch</a>
      </div>
    </section>

    <!-- CONTACT — inside <main> per WCAG 1.3.1 --------------- -->
    <section class="section section--contact" id="connect" aria-labelledby="connect-heading">
      <div class="shell">
        <p class="eyebrow">Connect</p>
        <h2 id="connect-heading">Connect With Hope Sessions</h2>

        <div class="connect-layout">

          <div class="connect-info">
            <p>Reach out directly:</p>
            <ul class="contact-list" aria-label="Direct contact information">
              <li><a href="mailto:pmastudios@hotmail.com">pmastudios@hotmail.com</a></li>
              <li><a href="tel:+16318751380">+1 (631) 875-1380</a></li>
              <li>Denver, North Carolina &middot; Lincoln County</li>
            </ul>
            <div class="connect-actions">
              <a class="button button--solid" href="mailto:pmastudios@hotmail.com">Email Hope Sessions</a>
              <a
                class="button button--ghost"
                href="https://www.pmarecordingstudios.com"
                target="_blank"
                rel="noreferrer"
                aria-label="Visit PMA Studios website (opens in a new tab)"
              >
                Visit PMA Studios
                <span class="visually-hidden">(opens in a new tab)</span>
              </a>
            </div>
          </div>

          <!-- TODO: Replace action="#" with live form endpoint.
               Formspree: action="https://formspree.io/f/YOUR_FORM_ID"
               Netlify: add netlify attribute and method="post" -->
          <form
            class="contact-form"
            id="hope-contact-form"
            method="post"
            action="#"
            novalidate
            aria-label="Hope Sessions inquiry form"
          >
            <div
              class="form-error-summary"
              role="alert"
              aria-live="assertive"
              aria-atomic="true"
              id="form-error-summary"
              hidden
            ></div>

            <fieldset class="form-group form-group--radio">
              <legend class="form-label">
                Inquiry type
                <span class="required-indicator" aria-hidden="true"> *</span>
                <span class="visually-hidden">(required)</span>
              </legend>
              <div class="radio-options">
                <label class="radio-label"><input type="radio" name="inquiry_type" value="partner" required> Partner inquiry</label>
                <label class="radio-label"><input type="radio" name="inquiry_type" value="artist"> Artist inquiry</label>
                <label class="radio-label"><input type="radio" name="inquiry_type" value="media"> Media inquiry</label>
                <label class="radio-label"><input type="radio" name="inquiry_type" value="general"> General question</label>
              </div>
              <p class="field-error" id="inquiry-type-error" role="alert" hidden>Please select an inquiry type.</p>
            </fieldset>

            <div class="form-group">
              <label class="form-label" for="contact-name">
                Your name
                <span class="required-indicator" aria-hidden="true"> *</span>
                <span class="visually-hidden">(required)</span>
              </label>
              <input class="form-control" type="text" id="contact-name" name="name"
                autocomplete="name" required aria-required="true" aria-describedby="name-error">
              <p class="field-error" id="name-error" role="alert" hidden>Please enter your name.</p>
            </div>

            <div class="form-group">
              <label class="form-label" for="contact-email">
                Email address
                <span class="required-indicator" aria-hidden="true"> *</span>
                <span class="visually-hidden">(required)</span>
              </label>
              <input class="form-control" type="email" id="contact-email" name="email"
                autocomplete="email" required aria-required="true" aria-describedby="email-error">
              <p class="field-error" id="email-error" role="alert" hidden>Please enter a valid email address.</p>
            </div>

            <div class="form-group">
              <label class="form-label" for="contact-org">Organization or role</label>
              <input class="form-control" type="text" id="contact-org" name="organization" autocomplete="organization">
            </div>

            <div class="form-group">
              <label class="form-label" for="contact-message">
                Message
                <span class="required-indicator" aria-hidden="true"> *</span>
                <span class="visually-hidden">(required)</span>
              </label>
              <textarea class="form-control" id="contact-message" name="message" rows="5"
                required aria-required="true" aria-describedby="message-error"></textarea>
              <p class="field-error" id="message-error" role="alert" hidden>Please enter a message.</p>
            </div>

            <button class="button button--solid" type="submit">Send Message</button>
          </form>

        </div>
      </div>
    </section>

  </main>

  <!-- FOOTER ================================================== -->
  <footer class="site-footer">
    <div class="site-footer__inner shell">

      <div class="footer-brand">
        <a class="brand" href="#top" aria-label="Hope Sessions — return to top of page">
          <span class="brand__wordmark"><strong>Hope</strong> Sessions</span>
        </a>
        <p class="fine-print">
          A Hope-centered recording initiative by Paul Andrejack.<br>
          Built through PMA Recording Studios &middot; Denver, NC &middot; Lincoln County
        </p>
      </div>

      <nav class="footer-nav" aria-label="Footer navigation">
        <ul class="footer-nav__list" role="list">
          <li><a href="#why-hope">Why Hope</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#initiative">Initiative</a></li>
          <li><a href="#proof">Proof</a></li>
          <li><a href="#partners">Partners</a></li>
          <li><a href="#connect">Connect</a></li>
        </ul>
      </nav>

      <p class="fine-print footer-copy">
        &copy; 2026 PMA Recording Studios. Hope Sessions initiative by Paul Andrejack.
      </p>

    </div>
  </footer>

</body>
</html>
"""

with open('/Users/jamestylee/Projects/denver-nc-music-grants/site/hope-sessions/index.html', 'w') as f:
    f.write(html)

print("index.html written:", len(html), "chars")
