#!/usr/bin/env python3
"""
Comprehensive Master Generator for RUFINOVENTURES.html, index.html, and PHOTOSYNTHESIS_PROJECT_PREVIEW.html
Implements:
1. Operational Boundary & Division of Labor (The Architect's Charter):
   - Nations and LGUs are strictly in charge of hardware procurement, civil construction, and asset ownership.
   - The Architect (Jefferson Rafael Rufino) provides the system architecture, integration advisory, diagnostic stress-testing of existing national/municipal plans, and global coalition building.
   - Clear invitation for governments and agencies to submit their current El Niño plans for stress-testing and architecture commissioning.
2. Global Steps & Zero-Redundancy Analysis:
   - Deep evaluation of active global and national initiatives (UN WMO Early Warnings for All, FAO/WFP Anticipatory Action $202M appeal, Philippines Task Force El Niño EO 53, World Bank Cat-DDO).
   - Demonstrates exact compatibility and explains how The Photosynthesis Project eliminates fatal gaps without duplicating existing state programs.
3. Dedicated Per-Country Coalition Panel (#pane-coalition) with Philippines as flagship default landing,
   profiling 8 key governing bodies and inter-agency strategic pairings ("who works with whom towards what").
4. Dedicated Media & Attention Architecture Panel (#pane-media):
   - The Attention War: Where Filipino Attention Is (Distraction/Doomscrolling) vs. Where It Must Be (Survival/Accountability).
   - The Broadcasting Matrix: Who Broadcasts What to Whom across 5 broadcast channels.
   - Free Media Toolkit (Open Telemetry API and Plug-and-Play Creator Social Kits).
5. All CTAs updated to "Work with me." (pointing to jeffersonrrufino@gmail.com).
6. Idempotent baseline reset to commit 588c9a8 before applying transformations.
"""

import os
import re
import subprocess

def build():
    base_dir = "/Users/thehighlandboy/Downloads/RUFINOVENTURES"
    index_path = os.path.join(base_dir, "index.html")

    # Step 0: Reset to clean baseline commit 588c9a8 for 100% idempotence
    print("[*] Resetting working files to baseline commit 588c9a8...")
    subprocess.run(
        ["git", "checkout", "588c9a8", "--", "index.html", "RUFINOVENTURES.html", "PHOTOSYNTHESIS_PROJECT_PREVIEW.html"],
        cwd=base_dir,
        check=True
    )

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update all button texts and CTAs to "Work with me."
    html = re.sub(
        r'SUPPORT THE PROJECT \(EMAIL JEFFERSON\) &rarr;',
        'WORK WITH ME &rarr;',
        html
    )
    html = re.sub(
        r'SUPPORT THE PROJECT &rarr;',
        'WORK WITH ME &rarr;',
        html
    )
    html = re.sub(
        r'CONNECT DIRECTLY WITH THE FOUNDER &rarr;',
        'WORK WITH ME &rarr;',
        html
    )
    html = re.sub(
        r'SUPPORT THIS VISION \(EMAIL ME\) &rarr;',
        'WORK WITH ME &rarr;',
        html
    )
    html = re.sub(
        r'Engage Direct &rarr;',
        'Work With Me &rarr;',
        html
    )
    html = re.sub(
        r'ENGAGE MISSION CONTROL',
        'WORK WITH ME',
        html
    )
    html = re.sub(
        r'TO SUPPORT THE PHOTOSYNTHESIS PROJECT:<br />.*?EMAIL JEFFERSON RAFAEL RUFINO DIRECTLY.*?</h2',
        'WORK WITH ME.<br /><span class="text-transparent bg-clip-text bg-gradient-to-r from-telemetry-cyan via-white to-amber-400">LET\'S PROTECT OUR PEOPLE BEFORE THE HEAT PEAKS.</span></h2',
        html,
        flags=re.DOTALL
    )

    # 1b. Update Contact Pane text: Zero Gatekeeping / No Hardware Procurement / Let Nations Do Their Jobs
    old_contact_intro_pattern = r'<div class="lg:col-span-6">\s*<p class="font-mono text-xs tracking-\[0\.3em\] text-telemetry-cyan uppercase mb-3 font-semibold">\s*ACTIVATE SOVEREIGN CONTINGENCY // 2026–2027 WINDOW\s*</p>\s*<h2 class="text-4xl sm:text-6xl lg:text-7xl font-black uppercase tracking-tight text-white mb-6 font-display leading-\[0\.95\]">\s*COMMISSION <br/>\s*<span class="text-transparent bg-clip-text bg-gradient-to-r from-white via-zinc-200 to-zinc-400">THE SYNTHESIS</span>\s*</h2>\s*<p class="text-zinc-300 text-base sm:text-lg leading-relaxed mb-6 font-normal">\s*The 2026–2027 Super El Niño is an unavoidable planetary thermodynamic reality\. The catastrophe, however, is completely preventable\.\s*</p>\s*<p class="text-zinc-400 text-sm sm:text-base leading-relaxed mb-8">\s*We invite heads of state, ministers of water, energy, and agriculture, disaster risk management agencies, sovereign wealth funds, and multilateral defense organizations to commission <strong class="text-white">The Photosynthesis Project</strong>\. Our team provides end-to-end hardware procurement, telemetry calibration, and rapid modular deployment across all 54 target nations\.\s*</p>'

    new_contact_intro = '''<div class="lg:col-span-6">
        <p class="font-mono text-xs tracking-[0.3em] text-telemetry-cyan uppercase mb-3 font-semibold">
          SOVEREIGN EMPOWERMENT // SYSTEM ARCHITECTURE &amp; CONSULTATION
        </p>
        <h2 class="text-4xl sm:text-6xl lg:text-7xl font-black uppercase tracking-tight text-white mb-6 font-display leading-[0.95]">
          WORK WITH ME. <br/>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 via-white to-amber-300">LET NATIONS DO THEIR JOBS.</span>
        </h2>

        <div class="p-4 bg-amber-500/10 border-l-4 border-l-amber-400 mb-6 text-xs font-mono text-amber-200 uppercase tracking-wider">
          // ARCHITECTURAL BOUNDARY: NO HARDWARE PROCUREMENT &bull; ZERO GATEKEEPING
        </div>

        <p class="text-zinc-300 text-base sm:text-lg leading-relaxed mb-4 font-normal">
          The 2026–2027 Super El Niño is an unavoidable planetary thermodynamic reality. The catastrophe, however, is completely preventable.
        </p>

        <div class="space-y-4 text-zinc-300 text-xs sm:text-sm leading-relaxed mb-8">
          <p>
            <strong class="text-white">Our team is NOT in charge of hardware procurement.</strong> Hardware procurement, civil works execution, and physical asset ownership belong 100% to sovereign nations, local government units (LGUs), and certified engineering contractors.
          </p>
          <p>
            <strong class="text-white">I am simply the architect of the system.</strong> Protecting citizens from extreme heat catastrophe is the sovereign duty of each country's leaders, engineers, and public servants. This blueprint is open so that nations can implement the steps themselves. I am not an essential bottleneck—this is me letting you do your jobs.
          </p>
          <p class="text-zinc-400">
            <strong class="text-white">Where I enter:</strong> If you want to consult with me—to ask my opinion on your integration, to share what you're currently doing and what your current plans are, and to let us stress-test your plan against thermodynamic collapse models to see if it will hold up when applied. If you want to commission this advisory or support the project, reach out and let's build the coalition.
          </p>
        </div>'''

    html = re.sub(old_contact_intro_pattern, new_contact_intro, html, flags=re.DOTALL)

    # 1c. Update form header and labels
    html = html.replace(
        '<span class="font-mono text-xs uppercase tracking-widest text-white font-bold">SOVEREIGN TRANSMISSION DISPATCH</span>\n            <p class="text-xs text-zinc-400 mt-1">Direct pipeline to Jefferson Rafael Rufino. Expect response within 12 hours.</p>',
        '<span class="font-mono text-xs uppercase tracking-widest text-white font-bold">CONSULTATION &amp; PLAN AUDIT TRANSMISSION</span>\n            <p class="text-xs text-zinc-400 mt-1">Direct pipeline to Jefferson Rafael Rufino. Share your current El Niño plans or request an architectural consultation.</p>'
    )
    html = html.replace(
        '<label class="block text-zinc-400 uppercase tracking-wider mb-2">Priority Operational Vectors Requested:</label>',
        '<label class="block text-zinc-400 uppercase tracking-wider mb-2">Consultation &amp; Architectural Focus Areas:</label>'
    )
    html = html.replace(
        '<span>Satellite Telemetry</span>',
        '<span>Plan Review &amp; Stress-Testing</span>'
    )
    html = html.replace(
        '<span>Solar Canopies & Storage</span>',
        '<span>Canopies &amp; Ice Storage Integration</span>'
    )
    html = html.replace(
        '<span>Agrivoltaic Biospheres</span>',
        '<span>Agrivoltaic Evaporation Defense</span>'
    )
    html = html.replace(
        '<span>AWG & Aquifer Recharge</span>',
        '<span>Atmospheric Water Generation</span>'
    )
    html = html.replace(
        '<span>Off-Grid Cold-Chain Triage Field Clinics</span>',
        '<span>Off-Grid Clinic Cold-Chain</span>'
    )
    html = html.replace(
        '<label class="block text-zinc-400 uppercase tracking-wider mb-1">Brief Statement of Emergency / Requirements *</label>',
        '<label class="block text-zinc-400 uppercase tracking-wider mb-1">What is your country/agency currently doing, current plans, or consultation request? *</label>'
    )
    html = html.replace(
        'placeholder="Detail current rainfall deficits, reservoir depletion status, or requested briefing timeline..."',
        'placeholder="Share what your country or agency is currently doing, your current plans, or what you would like to consult on..."'
    )
    html = html.replace(
        'TRANSMIT HIGH-PRIORITY DISPATCH TO JEFFERSONRRUFINO@GMAIL.COM &rarr;',
        'REQUEST CONSULTATION WITH JEFFERSON RAFAEL RUFINO &rarr;'
    )

    # 2. Update Navigation
    new_nav = '''<nav class="hidden 2xl:flex items-center gap-5 text-[10px] uppercase font-mono tracking-widest text-zinc-400">
        <a href="#pane-telemetry" class="hover:text-white transition">01 Financial Toll</a>
        <a href="#pane-solar" class="hover:text-white transition">02 Passive vs Catchment</a>
        <a href="#pane-photosynthesis" class="text-telemetry-cyan hover:text-white transition font-bold">03 Photosynthesis Project</a>
        <a href="#pane-rufino-synthesis" class="text-amber-400 hover:text-white transition font-bold">04 Rufino Synthesis</a>
        <a href="#pane-origins" class="text-purple-400 hover:text-white transition font-bold">05 Origins & Effort</a>
        <a href="#pane-coalition" class="text-emerald-400 hover:text-white transition font-bold">06 Country Coalition</a>
        <a href="#pane-media" class="text-rose-400 hover:text-white transition font-bold">07 Media & Attention</a>
        <a href="#pane-nations" class="hover:text-white transition">08 54 Nations</a>
        <a href="#pane-doctrine" class="hover:text-white transition">09 Why Support</a>
        <a href="#pane-calculator" class="hover:text-white transition">10 Simulator</a>
      </nav>'''
    html = re.sub(r'<nav class="hidden 2xl:flex items-center gap-.*?">.*?</nav>', new_nav, html, flags=re.DOTALL)

    # 3. Update Mobile Menu
    new_mobile = '''<div id="mobile-menu" class="hidden 2xl:hidden bg-space-950/98 border-b border-white/10 px-6 py-6 font-mono text-xs uppercase tracking-wider space-y-4">
      <div class="grid grid-cols-2 gap-3 text-zinc-300">
        <a href="#pane-telemetry" class="p-2 border border-white/10 hover:border-white transition block">01 Financial Toll</a>
        <a href="#pane-solar" class="p-2 border border-white/10 hover:border-white transition block">02 Passive vs Catchment</a>
        <a href="#pane-photosynthesis" class="p-2 border border-cyan-500/40 text-telemetry-cyan hover:border-white transition block font-bold">03 Photosynthesis Project</a>
        <a href="#pane-rufino-synthesis" class="p-2 border border-amber-500/40 text-amber-400 hover:border-white transition block font-bold">04 Rufino Synthesis</a>
        <a href="#pane-origins" class="p-2 border border-purple-500/40 text-purple-400 hover:border-white transition block font-bold">05 Origins & Effort</a>
        <a href="#pane-coalition" class="p-2 border border-emerald-500/40 text-emerald-400 hover:border-white transition block font-bold">06 Country Coalition</a>
        <a href="#pane-media" class="p-2 border border-rose-500/40 text-rose-400 hover:border-white transition block font-bold">07 Media & Attention</a>
        <a href="#pane-nations" class="p-2 border border-white/10 hover:border-white transition block">08 54 Nations Matrix</a>
        <a href="#pane-doctrine" class="p-2 border border-white/10 hover:border-white transition block">09 Why Support</a>
        <a href="#pane-calculator" class="p-2 border border-white/10 hover:border-white transition block">10 Simulator</a>
      </div>
      <div class="pt-3 border-t border-white/10 flex items-center justify-between text-[11px] text-zinc-400">
        <span>WORK WITH ME:</span>
        <a href="mailto:jeffersonrrufino@gmail.com?subject=Work%20With%20Me%20•%20The%20Photosynthesis%20Project" class="text-telemetry-cyan underline">jeffersonrrufino@gmail.com</a>
      </div>
    </div>
  </header>'''
    html = re.sub(r'<div id="mobile-menu".*?</header>', new_mobile, html, flags=re.DOTALL)

    # 4. Construct Coalition Pane
    coalition_pane = '''  <!-- ========================================================================= -->
  <!-- DEDICATED PANE 06: PER COUNTRY COALITION & GOVERNING BODIES                 -->
  <!-- Contextual HD Image: High-Tech Global Logistics, Architecture & Governance  -->
  <!-- ========================================================================= -->
  <section id="pane-coalition" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-space-950 border-t border-white/10 scroll-mt-16">
    <!-- HD Background Image -->
    <div class="absolute inset-0 z-0">
      <img 
        src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=2560&q=85" 
        alt="Modern civic institutions, glass and steel governance infrastructure" 
        class="w-full h-full object-cover object-center filter brightness-[0.45] contrast-[1.2]" 
        loading="lazy"
      />
      <div class="pane-scrim"></div>
    </div>

    <!-- HUD Top Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-b border-white/15 pb-4">
      <div class="flex items-center gap-3">
        <span class="font-mono text-xs text-emerald-400 uppercase tracking-widest font-bold">INTER-AGENCY CONVERGENCE</span>
        <span class="text-zinc-600">/</span>
        <span class="font-mono text-xs text-white font-bold">PER-COUNTRY GOVERNING BODIES MATRIX</span>
      </div>
      <div class="font-mono text-xs text-zinc-400 hidden sm:block">
        BREAKING DEPARTMENTAL SILOS &bull; BRIDGING THE RESPONSE GAP
      </div>
    </div>

    <!-- Main Content -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto my-auto py-12">
      <div class="max-w-4xl mb-8">
        <div class="inline-flex items-center gap-2 px-3 py-1 bg-emerald-500/10 border border-emerald-500/30 text-[11px] font-mono tracking-widest uppercase text-emerald-400 mb-3 font-semibold">
          <span>//</span> WHO DOES WHAT WITH WHOM &bull; HOW WE HELP
        </div>
        <h2 class="text-3xl sm:text-5xl lg:text-6xl font-black uppercase text-white tracking-tight font-display mb-4">
          THE INTER-AGENCY COALITION: <br />
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 via-teal-200 to-white">WHO SHOULD BE WORKING TOGETHER TOWARDS WHAT.</span>
        </h2>
        <p class="text-zinc-300 text-sm sm:text-base leading-relaxed">
          The state is not starting from zero. Many departments already possess emergency budgets, drought contingency plans, and disaster protocols. <strong>The fatal breakdown is that these bodies operate in rigid, isolated silos</strong>—leaving blind spots where thousands of vulnerable citizens fall through. Here is the operational convergence matrix: which agencies must collaborate, what their operational mandates are, and how <strong>The Photosynthesis Project</strong> supplies the physical catchment stack and real-time telemetry to bridge the gap.
        </p>
      </div>

      <!-- Country Selector Tabs -->
      <div class="flex flex-wrap items-center gap-2 sm:gap-3 mb-8 border-b border-white/10 pb-4">
        <button onclick="switchCoalitionCountry('PH')" id="tab-coalition-PH" class="px-4 py-2 text-xs font-mono font-bold uppercase tracking-wider bg-emerald-500 text-black border border-emerald-400 transition">
          🇵🇭 PHILIPPINES (PILOT GROUND ZERO)
        </button>
        <button onclick="switchCoalitionCountry('NG')" id="tab-coalition-NG" class="px-4 py-2 text-xs font-mono font-bold uppercase tracking-wider bg-space-900/90 text-zinc-400 border border-white/15 hover:border-white transition">
          🇳🇬 NIGERIA
        </button>
        <button onclick="switchCoalitionCountry('ID')" id="tab-coalition-ID" class="px-4 py-2 text-xs font-mono font-bold uppercase tracking-wider bg-space-900/90 text-zinc-400 border border-white/15 hover:border-white transition">
          🇮🇩 INDONESIA
        </button>
        <button onclick="switchCoalitionCountry('IN')" id="tab-coalition-IN" class="px-4 py-2 text-xs font-mono font-bold uppercase tracking-wider bg-space-900/90 text-zinc-400 border border-white/15 hover:border-white transition">
          🇮🇳 INDIA
        </button>
        <button onclick="switchCoalitionCountry('BR')" id="tab-coalition-BR" class="px-4 py-2 text-xs font-mono font-bold uppercase tracking-wider bg-space-900/90 text-zinc-400 border border-white/15 hover:border-white transition">
          🇧🇷 BRAZIL
        </button>
        <button onclick="switchCoalitionCountry('KE')" id="tab-coalition-KE" class="px-4 py-2 text-xs font-mono font-bold uppercase tracking-wider bg-space-900/90 text-zinc-400 border border-white/15 hover:border-white transition">
          🇰🇪 KENYA
        </button>
      </div>

      <!-- Dynamic Country Agency Matrix Container -->
      <div id="coalition-agency-matrix" class="space-y-4">
        <!-- Rendered by JavaScript dynamically -->
      </div>

      <!-- Inter-Agency Strategic Pairings Banner -->
      <div class="mt-8 p-6 bg-space-900/90 border border-white/15">
        <div class="text-xs font-mono uppercase tracking-widest text-emerald-400 font-bold mb-3">// PHILIPPINE INTER-AGENCY PARTNERSHIP BLUEPRINT ("WHO WORKS WITH WHOM TOWARDS WHAT")</div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
          <div class="p-3 bg-black/60 border border-white/10">
            <span class="text-emerald-400 font-bold block mb-1">DOST-PAGASA + DOH + MEDIA</span>
            <p class="text-zinc-300 text-[11px] leading-relaxed">
              <strong>Towards What:</strong> Converting meteorological heat index forecasts into clinical triage surge preparation, outdoor labor alerts, and mandatory broadcast sirens before heat casualties arrive at ERs.
            </p>
          </div>
          <div class="p-3 bg-black/60 border border-white/10">
            <span class="text-amber-400 font-bold block mb-1">DA & NIA + DOE & NGCP</span>
            <p class="text-zinc-300 text-[11px] leading-relaxed">
              <strong>Towards What:</strong> Deploying canal-top bifacial solar and agrivoltaics over main irrigation channels to slash canal water evaporation by 60%+ while feeding distributed clean power into rural grids.
            </p>
          </div>
          <div class="p-3 bg-black/60 border border-white/10">
            <span class="text-telemetry-cyan font-bold block mb-1">NWRB + DILG & LGUs</span>
            <p class="text-zinc-300 text-[11px] leading-relaxed">
              <strong>Towards What:</strong> Erecting atmospheric solar water condensation hubs in barangay halls and public markets, producing free drinking water without draining depleted municipal dams.
            </p>
          </div>
          <div class="p-3 bg-black/60 border border-white/10">
            <span class="text-purple-400 font-bold block mb-1">DepEd + DILG + DPWH</span>
            <p class="text-zinc-300 text-[11px] leading-relaxed">
              <strong>Towards What:</strong> Retrofitting public school roofs with high-albedo reflective coatings and solar microgrids, keeping classrooms under 32°C WBGT so school is never cancelled due to heat.
            </p>
          </div>
        </div>
      </div>

      <!-- Architectural Boundary & Division of Responsibilities -->
      <div class="mt-8 p-6 sm:p-8 bg-space-900/90 border border-amber-500/40 relative overflow-hidden">
        <div class="absolute top-0 right-0 px-3 py-1 bg-amber-500/20 text-amber-400 font-mono text-[10px] uppercase tracking-widest font-bold border-b border-l border-amber-500/30">
          ZERO GATEKEEPING &bull; SOVEREIGN EMPOWERMENT
        </div>
        <div class="flex items-center gap-3 mb-3">
          <span class="text-2xl text-amber-400">⚖️</span>
          <h3 class="text-xl sm:text-2xl font-bold font-display text-white uppercase tracking-tight">
            THE ARCHITECT'S POSTURE: LETTING NATIONS DO THEIR JOBS
          </h3>
        </div>
        <p class="text-zinc-300 text-xs sm:text-sm leading-relaxed mb-6 max-w-4xl">
          I am not an essential bottleneck, and I am not trying to gatekeep sovereign action. <strong>Protecting citizens from extreme climate shock is the sovereign duty of each nation and its public servants.</strong> This architecture is open so governments can do their jobs. Our team does not procure, warehouse, or mark up hardware. Nations procure their own equipment and implement the steps themselves.
        </p>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
          <div class="p-4 bg-black/60 border border-white/10 space-y-2">
            <div class="font-mono text-[10px] text-zinc-400 uppercase tracking-widest font-bold">// THE SOVEREIGN NATION'S ROLE (IMPLEMENT THE STEPS YOURSELVES):</div>
            <ul class="space-y-1.5 text-zinc-300 text-[11px]">
              <li class="flex items-start gap-2">
                <span class="text-emerald-400 font-bold shrink-0">&check;</span>
                <span><strong>Hardware Procurement:</strong> Procuring solar panels, inverters, batteries, chillers, and atmospheric water units through your own sovereign national bidding processes.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-emerald-400 font-bold shrink-0">&check;</span>
                <span><strong>Local Civil Execution:</strong> Mobilizing local labor, municipal permits, and domestic engineering contractors to erect physical catchment infrastructure.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-emerald-400 font-bold shrink-0">&check;</span>
                <span><strong>100% Asset Ownership:</strong> The facilities, water yields, and clean energy belong entirely to your municipalities and citizens—not to external vendors.</span>
              </li>
            </ul>
          </div>

          <div class="p-4 bg-black/60 border border-amber-500/30 space-y-2">
            <div class="font-mono text-[10px] text-amber-400 uppercase tracking-widest font-bold">// WHERE I ENTER (OPTIONAL CONSULTATION &amp; INTEGRATION):</div>
            <ul class="space-y-1.5 text-zinc-200 text-[11px]">
              <li class="flex items-start gap-2">
                <span class="text-amber-400 font-bold shrink-0">&rarr;</span>
                <span><strong>Consult With Me If You Want:</strong> If you want my opinion, or want to share what you're currently doing and what your current plans are, we will review them together.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-amber-400 font-bold shrink-0">&rarr;</span>
                <span><strong>Diagnostic Stress-Testing:</strong> We run your existing plan through our system to see if it will hold up during peak thermal load, uncovering blind spots before lives are lost.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-amber-400 font-bold shrink-0">&rarr;</span>
                <span><strong>Integration Advisory:</strong> Advising how to integrate your separate department initiatives into one coordinated life-saving coalition—then you take over and run it.</span>
              </li>
            </ul>
          </div>

          <!-- 100% Free Consultation Declaration Card -->
          <div class="p-4 bg-emerald-950/40 border border-emerald-500/50 space-y-2 md:col-span-2">
            <div class="flex items-center justify-between flex-wrap gap-2">
              <div class="font-mono text-[10px] text-emerald-400 uppercase tracking-widest font-bold">// ZERO-FEE HUMANITARIAN MANDATE: 100% FREE CONSULTATION</div>
              <span class="px-2 py-0.5 bg-emerald-500/20 text-emerald-300 text-[10px] font-mono font-bold uppercase border border-emerald-500/30">ZERO CHARGE TO SOVEREIGN STATES</span>
            </div>
            <p class="text-white text-xs sm:text-sm font-semibold">
              "Let it be known the consultation is free. I'm not charging to save people's lives." — Jefferson Rafael Rufino
            </p>
            <p class="text-zinc-300 text-[11px] leading-relaxed">
              I am putting up this website and open-sourcing the system architecture so that sovereign leaders, disaster councils, and municipal engineers know what is about to happen before the heat arrives. You can choose to work with me, consult with me for free, or consult with your own national advisors. I am not an essential bottleneck—it is each nation's sovereign duty to protect their citizens. But if you want my opinion, a plan review, or a stress-test against our thermodynamic model, you can consult with me at zero cost.
            </p>
          </div>
        </div>

        <div class="mt-4 p-3.5 bg-black/50 border border-emerald-500/30 font-mono text-[11px] text-zinc-300">
          <strong class="text-emerald-400">THE BOTTOM LINE:</strong> All consultations with Jefferson Rafael Rufino are <strong>100% free of charge</strong>. You don't need anyone's permission to save lives—implement the steps yourselves, consult your own advisors, or consult with me for free.
        </div>
      </div>

      <!-- Anti-Redundancy & Global Compatibility Matrix -->
      <div class="mt-8 p-6 sm:p-8 bg-space-900/90 border border-white/15">
        <div class="flex items-center justify-between flex-wrap gap-2 mb-4 border-b border-white/10 pb-3">
          <div>
            <div class="text-xs font-mono uppercase tracking-widest text-emerald-400 font-bold mb-1">// ZERO REDUNDANCY POLICY</div>
            <h3 class="text-xl sm:text-2xl font-bold font-display text-white uppercase tracking-tight">
              CURRENT GLOBAL STEPS VS. THE RUFINO SYNTHESIS
            </h3>
          </div>
          <div class="text-[11px] font-mono text-zinc-400">
            WE DO NOT DUPLICATE &bull; WE INTEGRATE &amp; COMPLETE
          </div>
        </div>
        <p class="text-zinc-300 text-xs sm:text-sm leading-relaxed mb-6 max-w-4xl">
          Billions of dollars are already allocated globally toward climate resilience. Yet populations still suffer fatal heat stroke, crops wither, and reservoirs run dry. <strong>We do not reinvent or compete with existing programs.</strong> We diagnose why they fail in isolation, and supply the thermodynamic integration architecture that makes their existing investments actually prevent death.
        </p>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
          <!-- Initiative 1: WMO & PAGASA Forecasting -->
          <div class="p-4 bg-black/60 border border-white/10 flex flex-col justify-between space-y-3">
            <div>
              <div class="flex items-center justify-between text-[10px] font-mono text-blue-400 uppercase tracking-wider mb-1">
                <span>GLOBAL PILLAR 01</span>
                <span class="px-1.5 py-0.5 border border-blue-500/30 bg-blue-500/10">WMO &amp; PAGASA</span>
              </div>
              <h4 class="text-sm font-bold text-white font-display">WMO "EARLY WARNINGS FOR ALL" &amp; PAGASA ADVISORIES</h4>
              <div class="mt-2 space-y-1.5 text-[11px] text-zinc-300">
                <p><strong>What They Do Well:</strong> High-precision satellite monitoring, equatorial sea surface temperature tracking (RONI), and 60-day rainfall deficit forecasts.</p>
                <p class="text-red-300"><strong>The Fatal Gap:</strong> A meteorological warning cannot cool a fever or hydrate an infant. Issuing an advisory without a physical cooling refuge simply announces disaster without providing defense.</p>
                <p class="text-emerald-300"><strong>How We Integrate (No Redundancy):</strong> We do NOT launch competing satellites or weather models. We use WMO and PAGASA forecast feeds as automated digital triggers that immediately ramp up physical cooling refuges and water condensation nodes before the heat crests.</p>
              </div>
            </div>
          </div>

          <!-- Initiative 2: FAO & WFP Anticipatory Action -->
          <div class="p-4 bg-black/60 border border-white/10 flex flex-col justify-between space-y-3">
            <div>
              <div class="flex items-center justify-between text-[10px] font-mono text-amber-400 uppercase tracking-wider mb-1">
                <span>GLOBAL PILLAR 02</span>
                <span class="px-1.5 py-0.5 border border-amber-500/30 bg-amber-500/10">FAO &amp; WFP</span>
              </div>
              <h4 class="text-sm font-bold text-white font-display">UN FAO &amp; WFP $202M ANTICIPATORY ACTION APPEAL</h4>
              <div class="mt-2 space-y-1.5 text-[11px] text-zinc-300">
                <p><strong>What They Do Well:</strong> Anticipatory cash-based transfers (CERF), distributing drought-tolerant seeds, livestock vaccinations, and temporary canal desilting.</p>
                <p class="text-red-300"><strong>The Fatal Gap:</strong> Cash payouts rapidly erode as local food prices quadruple during national drought. Drought seeds wither into dust when unshaded irrigation canals evaporate dry under 45°C sun.</p>
                <p class="text-emerald-300"><strong>How We Integrate (No Redundancy):</strong> We do NOT hand out emergency cash or food parcels. We design canal-top solar canopies that slash canal water evaporation by 60%+, ensuring the irrigation water actually reaches the FAO seeds while generating clean rural power.</p>
              </div>
            </div>
          </div>

          <!-- Initiative 3: Philippine Executive Order 53 (Task Force El Niño) -->
          <div class="p-4 bg-black/60 border border-white/10 flex flex-col justify-between space-y-3">
            <div>
              <div class="flex items-center justify-between text-[10px] font-mono text-yellow-400 uppercase tracking-wider mb-1">
                <span>NATIONAL PILLAR 03</span>
                <span class="px-1.5 py-0.5 border border-yellow-500/30 bg-yellow-500/10">EO 53 TASK FORCE</span>
              </div>
              <h4 class="text-sm font-bold text-white font-display">PHILIPPINES TASK FORCE EL NIÑO (EXECUTIVE ORDER 53)</h4>
              <div class="mt-2 space-y-1.5 text-[11px] text-zinc-300">
                <p><strong>What They Do Well:</strong> Multi-agency coordination led by DND &amp; DOST across 5 sectors: Water, Food, Energy, Health, and Public Safety; monitoring Angat Dam levels and cloud seeding.</p>
                <p class="text-red-300"><strong>The Fatal Gap:</strong> Departmental silos. DA addresses crops, DOE manages grid alerts, NWRB rations municipal water, and DOH records heat exhaustion in ERs. None of them deploy co-located solar thermal ice catchment at the community level.</p>
                <p class="text-emerald-300"><strong>How We Integrate (No Redundancy):</strong> We provide the physical cross-sectoral connective tissue. One solar canopy array simultaneously cuts DA irrigation evaporation, relieves DOE grid peaks via thermal ice storage, and supplies NWRB with decentralized atmospheric drinking water.</p>
              </div>
            </div>
          </div>

          <!-- Initiative 4: World Bank & Multilateral Cat-DDO Credit -->
          <div class="p-4 bg-black/60 border border-white/10 flex flex-col justify-between space-y-3">
            <div>
              <div class="flex items-center justify-between text-[10px] font-mono text-purple-400 uppercase tracking-wider mb-1">
                <span>FINANCE PILLAR 04</span>
                <span class="px-1.5 py-0.5 border border-purple-500/30 bg-purple-500/10">WORLD BANK &amp; ADB</span>
              </div>
              <h4 class="text-sm font-bold text-white font-display">MULTILATERAL CONTINGENCY FINANCING (CAT-DDO &amp; CERCs)</h4>
              <div class="mt-2 space-y-1.5 text-[11px] text-zinc-300">
                <p><strong>What They Do Well:</strong> Instant sovereign liquidity disbursals once national states of calamity are declared, preventing immediate sovereign debt default.</p>
                <p class="text-red-300"><strong>The Fatal Gap:</strong> Emergency debt is consumed on consumable relief (tarps, water trucking, canned food) that vanishes within weeks, leaving national debt higher with zero permanent physical protection.</p>
                <p class="text-emerald-300"><strong>How We Integrate (No Redundancy):</strong> We convert emergency capital into permanent physical infrastructure that outlives the El Niño, delivering up to $7 in avoided socioeconomic destruction for every $1 invested.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Commissioning Invitation Banner -->
      <div class="mt-8 p-6 sm:p-8 bg-gradient-to-r from-space-900 via-emerald-950/40 to-space-900 border border-emerald-500/40 flex flex-col lg:flex-row items-center justify-between gap-6">
        <div>
          <div class="flex items-center gap-2 mb-1">
            <span class="text-xs font-mono uppercase tracking-widest text-emerald-400 font-bold">// 100% FREE CONSULTATION &amp; ARCHITECTURAL REVIEW</span>
            <span class="px-1.5 py-0.5 text-[9px] font-mono uppercase bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-bold">ZERO CHARGE</span>
          </div>
          <h3 class="text-xl sm:text-2xl font-bold text-white font-display">Have an existing El Niño plan in your country, city, or agency?</h3>
          <p class="text-zinc-300 text-xs sm:text-sm mt-1 max-w-2xl leading-relaxed">
            Let me know what you're currently doing in your country and what your current plans are. We will stress-test your plan against thermodynamic collapse thresholds, reveal where your departmental silos fall short, and see if it works with the system applied. <strong>This consultation is 100% free of charge—I am not charging to save lives.</strong>
          </p>
        </div>
        <a href="mailto:jeffersonrrufino@gmail.com?subject=Free%20National%20Plan%20Review%20%26%20Architecture%20Consultation" class="btn-mission-cyan whitespace-nowrap">
          WORK WITH ME (FREE CONSULTATION) &rarr;
        </a>
      </div>

    </div>

    <!-- Bottom HUD Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-t border-white/10 pt-4 font-mono text-[11px] text-zinc-500">
      <div>GOVERNANCE CONVERGENCE LEDGER // SYNCHRONIZING STATE CAPABILITIES</div>
      <div class="text-zinc-400">CONTACT ARCHITECT: jeffersonrrufino@gmail.com</div>
    </div>
  </section>
'''

    # 5. Construct Dedicated Media & Attention Pane
    media_pane = '''  <!-- ========================================================================= -->
  <!-- DEDICATED PANE 07: THE ATTENTION ECONOMY & BROADCASTING MATRIX              -->
  <!-- Contextual HD Image: High-Tech Broadcast Control Desk & Telecommunications  -->
  <!-- ========================================================================= -->
  <section id="pane-media" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-space-950 border-t border-white/10 scroll-mt-16">
    <!-- HD Background Image -->
    <div class="absolute inset-0 z-0">
      <img 
        src="https://images.unsplash.com/photo-1585829365295-ab7cd400c167?auto=format&fit=crop&w=2560&q=85" 
        alt="Television broadcast studio, media control room, telecommunications screens" 
        class="w-full h-full object-cover object-center filter brightness-[0.4] contrast-[1.25]" 
        loading="lazy"
      />
      <div class="pane-scrim"></div>
    </div>

    <!-- HUD Top Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-b border-white/15 pb-4">
      <div class="flex items-center gap-3">
        <span class="font-mono text-xs text-rose-400 uppercase tracking-widest font-bold">ATTENTION INFRASTRUCTURE</span>
        <span class="text-zinc-600">/</span>
        <span class="font-mono text-xs text-white font-bold">BROADCASTING &amp; CONTENT CONSUMPTION MATRIX</span>
      </div>
      <div class="font-mono text-xs text-zinc-400 hidden sm:block">
        RECLAIMING PUBLIC CONSCIOUSNESS &bull; REDIRECTING ATTENTION TO SURVIVAL
      </div>
    </div>

    <!-- Main Content -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto my-auto py-12">
      <div class="max-w-4xl mb-8">
        <div class="inline-flex items-center gap-2 px-3 py-1 bg-rose-500/10 border border-rose-500/30 text-[11px] font-mono tracking-widest uppercase text-rose-400 mb-3 font-semibold">
          <span>//</span> BROADCASTING WHO &amp; TO WHOM &bull; THE ATTENTION WAR
        </div>
        <h2 class="text-3xl sm:text-5xl lg:text-6xl font-black uppercase text-white tracking-tight font-display mb-4">
          WHERE FILIPINO ATTENTION IS: <br />
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-rose-400 via-amber-300 to-white">VS. WHERE IT MUST BE TO SURVIVE.</span>
        </h2>
        <p class="text-zinc-300 text-sm sm:text-base leading-relaxed">
          The Philippines is the social media capital of the world. Over <strong>85 million Filipinos spend an average of nearly 4 hours daily</strong> consuming algorithms designed for distraction. While viral celebrity feuds, political rage-bait, and mindless video doomscrolling consume the public bandwidth, <strong>a silent, lethal thermodynamic catastrophe is arriving</strong>: 6,500 Filipino lives are at risk from extreme heat, dams are draining, and outdoor laborers are suffering organ damage in silence. Media is not an accessory—it is the frontline weapon of survival.
        </p>
      </div>

      <!-- Attention Realignment Terminal (Side-by-Side Comparison) -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-12">
        <!-- Where Attention Currently Is -->
        <div class="p-6 sm:p-8 bg-space-900/90 border border-red-500/40 relative overflow-hidden">
          <div class="absolute top-0 right-0 px-3 py-1 bg-red-500/20 text-red-400 font-mono text-[10px] uppercase tracking-widest font-bold border-b border-l border-red-500/30">
            THE DISTRACTION TRAP
          </div>
          <div class="flex items-center gap-2 mb-4">
            <span class="text-xl">⚠️</span>
            <h3 class="text-xl font-bold font-display text-red-400 uppercase tracking-wide">WHERE FILIPINO ATTENTION IS TODAY</h3>
          </div>
          <p class="text-xs text-zinc-400 font-mono mb-4">CURRENT CONTENT CONSUMPTION &amp; ALGORITHMIC HIJACKING:</p>
          
          <ul class="space-y-3 text-xs text-zinc-300">
            <li class="flex items-start gap-2.5">
              <span class="text-red-400 font-bold shrink-0">&times;</span>
              <div>
                <strong class="text-white">Celebrity Scandals &amp; Love-Team Gossip:</strong>
                Millions of viewing hours spent debating breakups and showbiz feuds while outdoor temperatures silently reach lethal 46°C–50°C heat indices.
              </div>
            </li>
            <li class="flex items-start gap-2.5">
              <span class="text-red-400 font-bold shrink-0">&times;</span>
              <div>
                <strong class="text-white">Partisan Political Rage-Bait:</strong>
                Endless cycles of manufactured controversies, troll-farm bickering, and factional noise designed to trigger outrage rather than solve crumbling utilities.
              </div>
            </li>
            <li class="flex items-start gap-2.5">
              <span class="text-red-400 font-bold shrink-0">&times;</span>
              <div>
                <strong class="text-white">Mindless 15-Second Doomscrolling:</strong>
                Passive consumption of short-form brain-rot clips that exhausts mental reserves and leaves citizens numb to environmental warning signs.
              </div>
            </li>
            <li class="flex items-start gap-2.5">
              <span class="text-red-400 font-bold shrink-0">&times;</span>
              <div>
                <strong class="text-white">Fatalistic Normalization ("Sanay naman tayo sa init"):</strong>
                The toxic cultural shrug of <em>"tiis-ganda"</em> and <em>"ganyan talaga,"</em> treating preventable heatstroke and dehydration casualties as an unavoidable fact of life.
              </div>
            </li>
          </ul>

          <div class="mt-6 p-4 bg-red-950/30 border border-red-500/30 font-mono text-[11px] text-red-300">
            <strong>THE FATAL TOLL:</strong> When public attention is captive to spectacle, heat casualties happen in total silence. Grandmothers suffer fatal strokes, delivery riders collapse, and dry water faucets go unaddressed until it is too late.
          </div>
        </div>

        <!-- Where Attention Must Be -->
        <div class="p-6 sm:p-8 bg-space-900/90 border border-emerald-500/40 relative overflow-hidden">
          <div class="absolute top-0 right-0 px-3 py-1 bg-emerald-500/20 text-emerald-400 font-mono text-[10px] uppercase tracking-widest font-bold border-b border-l border-emerald-500/30">
            THE SURVIVAL SHIFT
          </div>
          <div class="flex items-center gap-2 mb-4">
            <span class="text-xl">⚡</span>
            <h3 class="text-xl font-bold font-display text-emerald-400 uppercase tracking-wide">WHERE ATTENTION MUST BE DIRECTED</h3>
          </div>
          <p class="text-xs text-zinc-400 font-mono mb-4">SURVIVAL AWARENESS &amp; ACTIVE CIVIC MOBILIZATION:</p>

          <ul class="space-y-3 text-xs text-zinc-300">
            <li class="flex items-start gap-2.5">
              <span class="text-emerald-400 font-bold shrink-0">&check;</span>
              <div>
                <strong class="text-white">Daily Wet-Bulb &amp; Heat Index Telemetry (Before 9:00 AM):</strong>
                Treating thermal warnings with the same life-or-death discipline as a Signal #4 typhoon warning before stepping outdoors.
              </div>
            </li>
            <li class="flex items-start gap-2.5">
              <span class="text-emerald-400 font-bold shrink-0">&check;</span>
              <div>
                <strong class="text-white">Locating Shaded Cooling Refuges &amp; Clean Water Points:</strong>
                Knowing exactly where free municipal drinking water, shaded plazas, and solar-cooled barangay centers are situated in every town.
              </div>
            </li>
            <li class="flex items-start gap-2.5">
              <span class="text-emerald-400 font-bold shrink-0">&check;</span>
              <div>
                <strong class="text-white">The "Lolo, Lola, at Sanggol" Community Check:</strong>
                Active vigilance between 11 AM and 3 PM: checking elderly relatives, infants, and neighborhood tricycle drivers for early heat exhaustion symptoms.
              </div>
            </li>
            <li class="flex items-start gap-2.5">
              <span class="text-emerald-400 font-bold shrink-0">&check;</span>
              <div>
                <strong class="text-white">Holding Elected Officials Accountable:</strong>
                Demanding why local budgets are spent on reactive food packs instead of installing permanent solar cool roofs on public schools and open markets.
              </div>
            </li>
          </ul>

          <div class="mt-6 p-4 bg-emerald-950/30 border border-emerald-500/30 font-mono text-[11px] text-emerald-300">
            <strong>THE RESULT:</strong> Attention becomes a life-saving shield. When 85 million citizens know their numbers, know their safe zones, and look out for each other, preventable mortality plummets toward zero.
          </div>
        </div>
      </div>

      <!-- The Broadcasting Matrix: Who Broadcasts What to Whom -->
      <div class="mb-10">
        <div class="text-xs font-mono uppercase tracking-widest text-rose-400 font-bold mb-3">// THE CIVIC BROADCASTING MATRIX ("WHO BROADCASTS WHAT TO WHOM")</div>
        <h3 class="text-2xl font-bold font-display text-white mb-6 uppercase">Five Critical Media Channels &amp; Their Operational Directives</h3>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <!-- Channel 1: National TV & Radio -->
          <div class="p-5 bg-space-900/80 border border-white/10 hover:border-rose-500/50 transition space-y-3 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between text-[10px] font-mono text-rose-400 uppercase tracking-wider mb-1">
                <span>CHANNEL 01</span>
                <span class="px-1.5 py-0.5 border border-rose-500/30 bg-rose-500/10">BROADCAST NETWORKS</span>
              </div>
              <h4 class="text-base font-bold text-white font-display">NATIONAL TELEVISION &amp; RADIO</h4>
              <p class="text-[11px] font-mono text-zinc-400 mb-3">GMA, ABS-CBN News, TV5, Bombo Radyo, DZBB, DZMM, RMN</p>
              
              <div class="space-y-2 text-xs">
                <div class="p-2.5 bg-black/60 border border-white/5">
                  <span class="font-mono text-[10px] text-zinc-400 block mb-0.5">FROM &rarr; TO:</span>
                  <span class="text-white font-medium">DOST-PAGASA &amp; DOH &rarr; General Public, Commuters, Farmers, Drivers</span>
                </div>
                <div class="p-2.5 bg-black/60 border border-white/5">
                  <span class="font-mono text-[10px] text-amber-400 block mb-0.5">WHAT MUST BE BROADCAST:</span>
                  <p class="text-zinc-300 text-[11px] leading-relaxed">
                    Continuous on-screen Heat Index tickers; hourly hydration alerts ("Inom ng tubig tuwing 30 minuto"); 30-second primers explaining the difference between fatigue and lethal heat stroke (cessation of sweating, confusion).
                  </p>
                </div>
              </div>
            </div>
            <div class="pt-2 border-t border-white/5 font-mono text-[10px] text-zinc-500">
              TARGET: 60M+ DAILY TELEVISION &amp; RADIO LISTENERS
            </div>
          </div>

          <!-- Channel 2: Telco & Emergency Cell Broadcast -->
          <div class="p-5 bg-space-900/80 border border-white/10 hover:border-rose-500/50 transition space-y-3 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between text-[10px] font-mono text-rose-400 uppercase tracking-wider mb-1">
                <span>CHANNEL 02</span>
                <span class="px-1.5 py-0.5 border border-rose-500/30 bg-rose-500/10">EMERGENCY CELL SIRENS</span>
              </div>
              <h4 class="text-base font-bold text-white font-display">TELCO EMERGENCY CELL BROADCAST (ECBS)</h4>
              <p class="text-[11px] font-mono text-zinc-400 mb-3">Globe, Smart / PLDT, DITO, NTC, DICT, NDRRMC</p>
              
              <div class="space-y-2 text-xs">
                <div class="p-2.5 bg-black/60 border border-white/5">
                  <span class="font-mono text-[10px] text-zinc-400 block mb-0.5">FROM &rarr; TO:</span>
                  <span class="text-white font-medium">NDRRMC &amp; NTC &rarr; All 85+ Million Mobile Phone Users</span>
                </div>
                <div class="p-2.5 bg-black/60 border border-white/5">
                  <span class="font-mono text-[10px] text-amber-400 block mb-0.5">WHAT MUST BE BROADCAST:</span>
                  <p class="text-zinc-300 text-[11px] leading-relaxed">
                    Audible loud emergency siren phone alerts on days when Heat Index breaches 42°C (Danger) or 51°C (Extreme Danger); zero-rated (100% free data) access to real-time heat maps, cooling refuges, and hydration point locators.
                  </p>
                </div>
              </div>
            </div>
            <div class="pt-2 border-t border-white/5 font-mono text-[10px] text-zinc-500">
              TARGET: 85M+ ACTIVE SMARTPHONES ACROSS ALL ISLANDS
            </div>
          </div>

          <!-- Channel 3: Creators & Social Media -->
          <div class="p-5 bg-space-900/80 border border-white/10 hover:border-rose-500/50 transition space-y-3 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between text-[10px] font-mono text-rose-400 uppercase tracking-wider mb-1">
                <span>CHANNEL 03</span>
                <span class="px-1.5 py-0.5 border border-rose-500/30 bg-rose-500/10">VIRAL SOCIAL CREATORS</span>
              </div>
              <h4 class="text-base font-bold text-white font-display">CREATORS, INFLUENCERS &amp; SOCIAL APPS</h4>
              <p class="text-[11px] font-mono text-zinc-400 mb-3">TikTok, YouTube, Facebook, X, Instagram, Viber Communities</p>
              
              <div class="space-y-2 text-xs">
                <div class="p-2.5 bg-black/60 border border-white/5">
                  <span class="font-mono text-[10px] text-zinc-400 block mb-0.5">FROM &rarr; TO:</span>
                  <span class="text-white font-medium">Digital Creators &amp; Youth &rarr; Gen Z, Millennials, Family Group Chats</span>
                </div>
                <div class="p-2.5 bg-black/60 border border-white/5">
                  <span class="font-mono text-[10px] text-amber-400 block mb-0.5">WHAT MUST BE BROADCAST:</span>
                  <p class="text-zinc-300 text-[11px] leading-relaxed">
                    30-second vertical video survival guides: DIY home oral rehydration, cold-compress neck wraps, spotting confusion in elderly neighbors; viral "#CheckOnYourLola" campaigns; crowdsourcing open air-conditioned safe spaces.
                  </p>
                </div>
              </div>
            </div>
            <div class="pt-2 border-t border-white/5 font-mono text-[10px] text-zinc-500">
              TARGET: 3.8 HOURS/DAY OF FILIPINO CONTENT CONSUMPTION
            </div>
          </div>

          <!-- Channel 4: Grassroots Recorida & Megaphones -->
          <div class="p-5 bg-space-900/80 border border-white/10 hover:border-rose-500/50 transition space-y-3 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between text-[10px] font-mono text-rose-400 uppercase tracking-wider mb-1">
                <span>CHANNEL 04</span>
                <span class="px-1.5 py-0.5 border border-rose-500/30 bg-rose-500/10">GRASSROOTS RECORIDA</span>
              </div>
              <h4 class="text-base font-bold text-white font-display">BARANGAY RECORIDA &amp; MEGAPHONES</h4>
              <p class="text-[11px] font-mono text-zinc-400 mb-3">Mobile PAs on Tricycles/Patrols, Barangay Hall Speakers, BHWs</p>
              
              <div class="space-y-2 text-xs">
                <div class="p-2.5 bg-black/60 border border-white/5">
                  <span class="font-mono text-[10px] text-zinc-400 block mb-0.5">FROM &rarr; TO:</span>
                  <span class="text-white font-medium">Barangay Captains &amp; Health Workers &rarr; Slum Areas, Markets, TODA Terminals</span>
                </div>
                <div class="p-2.5 bg-black/60 border border-white/5">
                  <span class="font-mono text-[10px] text-amber-400 block mb-0.5">WHAT MUST BE BROADCAST:</span>
                  <p class="text-zinc-300 text-[11px] leading-relaxed">
                    Loudspeaker announcements in Tagalog, Bisaya, Ilocano, and local dialects announcing free potable water refills, shaded covered court openings, and enforcing mandatory 15-minute shaded pauses for outdoor laborers.
                  </p>
                </div>
              </div>
            </div>
            <div class="pt-2 border-t border-white/5 font-mono text-[10px] text-zinc-500">
              TARGET: 42,000+ BARANGAYS NATIONWIDE
            </div>
          </div>

          <!-- Channel 5: Campus Media & Schools -->
          <div class="p-5 bg-space-900/80 border border-white/10 hover:border-rose-500/50 transition space-y-3 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between text-[10px] font-mono text-rose-400 uppercase tracking-wider mb-1">
                <span>CHANNEL 05</span>
                <span class="px-1.5 py-0.5 border border-rose-500/30 bg-rose-500/10">CAMPUS CHANNELS</span>
              </div>
              <h4 class="text-base font-bold text-white font-display">CAMPUS MEDIA &amp; PARENT CHATS</h4>
              <p class="text-[11px] font-mono text-zinc-400 mb-3">DepEd Portals, School Facebook Pages, Parent-Teacher Viber Groups</p>
              
              <div class="space-y-2 text-xs">
                <div class="p-2.5 bg-black/60 border border-white/5">
                  <span class="font-mono text-[10px] text-zinc-400 block mb-0.5">FROM &rarr; TO:</span>
                  <span class="text-white font-medium">School Principals &amp; Student Governments &rarr; 28 Million Students &amp; Parents</span>
                </div>
                <div class="p-2.5 bg-black/60 border border-white/5">
                  <span class="font-mono text-[10px] text-amber-400 block mb-0.5">WHAT MUST BE BROADCAST:</span>
                  <p class="text-zinc-300 text-[11px] leading-relaxed">
                    Hourly classroom heat tracking; automatic shifts to early-morning (6 AM–10 AM) schedules before classrooms breach 35°C; mandatory student hydration breaks at every bell; immediate suspension of outdoor afternoon PE drills.
                  </p>
                </div>
              </div>
            </div>
            <div class="pt-2 border-t border-white/5 font-mono text-[10px] text-zinc-500">
              TARGET: 47,000+ PUBLIC SCHOOLS &amp; UNIVERSITIES
            </div>
          </div>

          <!-- Channel 6: Newsroom Open API & Graphics Kit -->
          <div class="p-5 bg-space-900/80 border border-rose-500/30 hover:border-rose-400 transition space-y-3 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between text-[10px] font-mono text-emerald-400 uppercase tracking-wider mb-1">
                <span>OUR CONTRIBUTION</span>
                <span class="px-1.5 py-0.5 border border-emerald-500/30 bg-emerald-500/10 text-emerald-300">FREE MEDIA ENABLER</span>
              </div>
              <h4 class="text-base font-bold text-white font-display">HOW WE EMPOWER THE MEDIA</h4>
              <p class="text-[11px] font-mono text-zinc-400 mb-3">The Photosynthesis Project Media Toolkit</p>
              
              <div class="space-y-2 text-xs">
                <div class="p-2.5 bg-emerald-950/20 border border-emerald-500/30">
                  <span class="font-mono text-[10px] text-emerald-400 block mb-0.5">// OPEN TELEMETRY API &amp; GRAPHICS KITS:</span>
                  <p class="text-zinc-200 text-[11px] leading-relaxed">
                    We supply broadcast newsrooms, independent creators, and community journalists with free real-time WBGT data feeds, pre-rendered vertical video templates, and localized dialect graphics—turning thermodynamics into viral survival knowledge.
                  </p>
                </div>
              </div>
            </div>
            <div class="pt-2 border-t border-white/5 flex items-center justify-between font-mono text-[10px]">
              <span class="text-zinc-500">MEDIA BRIEFING DECK</span>
              <a href="mailto:jeffersonrrufino@gmail.com?subject=Media%20Toolkit%20%26%20Broadcast%20Partnership%20Request" class="text-rose-400 hover:text-white transition font-bold uppercase">
                Work With Me (Media Kit) &rarr;
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- Media Call to Action Banner -->
      <div class="p-6 sm:p-8 bg-black/90 border border-rose-500/30 flex flex-col lg:flex-row items-center justify-between gap-6">
        <div>
          <div class="text-xs font-mono uppercase tracking-widest text-rose-400 font-bold mb-1">// JOURNALISTS, BROADCASTERS &amp; CONTENT CREATORS</div>
          <h3 class="text-xl sm:text-2xl font-bold text-white font-display">Help us redirect the national conversation from spectacle to survival.</h3>
          <p class="text-zinc-400 text-xs sm:text-sm mt-1 max-w-2xl">
            Whether you run a national news desk, a community radio program, or a TikTok channel with millions of views—we will equip you with verified data, graphics, and survival protocols.
          </p>
        </div>
        <a href="mailto:jeffersonrrufino@gmail.com?subject=Media%20%26%20Creator%20Broadcasting%20Partnership" class="btn-mission-cyan whitespace-nowrap">
          WORK WITH ME (BROADCAST MISSION) &rarr;
        </a>
      </div>

    </div>

    <!-- Bottom HUD Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-t border-white/10 pt-4 font-mono text-[11px] text-zinc-500">
      <div>CIVIC ATTENTION PROTOCOL // TURNING SOCIAL CONSUMPTION INTO HUMAN RESILIENCE</div>
      <div class="text-zinc-400">CONTACT ARCHITECT: jeffersonrrufino@gmail.com</div>
    </div>
  </section>
'''

    # Place coalition_pane and media_pane right above <section id="pane-nations"
    panes_combined = coalition_pane + '\n' + media_pane + '\n'
    html = html.replace('<section id="pane-nations"', panes_combined + '  <section id="pane-nations"')

    # 6. Add Coalition JavaScript Data and Logic
    coalition_js = '''
    // ==========================================
    // INTER-AGENCY COALITION MATRIX DATA & ENGINE
    // ==========================================
    const COALITION_DATA = {
      PH: {
        country: "Philippines",
        flag: "🇵🇭",
        title: "PHILIPPINES // INTER-AGENCY CONVERGENCE LEDGER",
        overview: "6,500 ± 410 Filipino lives projected at risk. PAGASA warned on Sept 23, 2026 that a historic Super El Niño is active and strengthening through 2027. Existing programs across DOST, DA, DOH, and DOE are fragmented in departmental silos. The Photosynthesis Project provides the unified physical and data backbone connecting them into one non-displacement defense.",
        agencies: [
          {
            body: "DOST-PAGASA",
            full: "Philippine Atmospheric, Geophysical and Astronomical Services Administration",
            badge: "CLIMATE TELEMETRY & ADVISORIES",
            badgeColor: "text-blue-400 border-blue-500/30 bg-blue-500/10",
            duty: "Issue 60–90 day lead-time advisories, monitor equatorial sea-surface temperatures (RONI), forecast regional rainfall deficits, and track dangerous Wet-Bulb Globe Temperatures (WBGT).",
            help: "We connect PAGASA's predictive forecast directly into automated physical dispatch triggers—turning meteorological warnings into active cooling shelter dispatch, water generation ramp-ups, and clinic surge staffing before the heat crests."
          },
          {
            body: "DOH (Department of Health)",
            full: "Department of Health & Rural Health Units (RHUs)",
            badge: "HEALTH SURGE & CLINICAL DEFENSE",
            badgeColor: "text-red-400 border-red-500/30 bg-red-500/10",
            duty: "Manage hospital emergency admissions, treat heat-stroke and dehydration casualties, deploy oral rehydration therapy, and monitor cardiovascular heat stress in vulnerable elderly populations.",
            help: "We install off-grid solar + battery + ice thermal storage at barangay clinics and Rural Health Units (RHUs), guaranteeing 100% cold-chain preservation for insulin, vaccines, and emergency fluids even during complete grid collapse."
          },
          {
            body: "DA & NIA",
            full: "Department of Agriculture & National Irrigation Administration",
            badge: "AGRICULTURE & IRRIGATION DEFENSE",
            badgeColor: "text-amber-400 border-amber-500/30 bg-amber-500/10",
            duty: "Operate irrigation canals, distribute drought-resistant seeds, maintain solar-powered irrigation pumps, and protect domestic food harvests against severe drought.",
            help: "We deploy elevated agrivoltaic bifacial solar canopies over crops and irrigation canals. This cuts canal water evaporation by 60%+, drops microclimate heat by 1–4°C, enhances water-use efficiency by 20–47%, and provides farmers with solar power sales to offset crop stress."
          },
          {
            body: "DOE & NGCP",
            full: "Department of Energy & National Grid Corporation of the Philippines",
            badge: "POWER GRID STABILITY & RELIEF",
            badgeColor: "text-yellow-400 border-yellow-500/30 bg-yellow-500/10",
            duty: "Maintain grid frequency and reserves, dispatch peaker generation, prevent cascading yellow/red alerts, and manage soaring residential cooling demand.",
            help: "Our thermal ice storage nodes and distributed solar canopies absorb massive daytime cooling loads and discharge cold stored water during 1 PM–6 PM peak hours, shaving hundreds of megawatts off grid strain and preventing transformer burnouts."
          },
          {
            body: "NWRB & Water Concessionaires",
            full: "National Water Resources Board, MWSS, Maynilad, Manila Water & Water Districts",
            badge: "WATER SECURITY & AQUIFER RECHARGE",
            badgeColor: "text-telemetry-cyan border-cyan-500/30 bg-cyan-500/10",
            duty: "Manage Angat Dam and regional reservoir allocations, enforce water rationing schedules, and organize emergency potable water trucking to drought-stricken communities.",
            help: "We deploy decentralized solar atmospheric water condensation hubs producing 25,000+ liters/day per cluster, dispensing free pure drinking water directly to vulnerable citizens without drawing down critically depleted reservoirs."
          },
          {
            body: "DILG & Local Government Units (LGUs)",
            full: "Department of the Interior and Local Government, Governors, Mayors & Barangays",
            badge: "LOCAL CITIZEN PROTECTION & REFUGES",
            badgeColor: "text-emerald-400 border-emerald-500/30 bg-emerald-500/10",
            duty: "Establish local evacuation and cooling centers, enforce heat-safety workplace protocols for outdoor laborers, and protect public markets and transport terminals.",
            help: "We retrofit public markets, bus interchanges, and barangay halls into shaded, cool-roof public cooling refuges with free clean drinking water and phone charging—allowing community commerce and normal life to survive without shut-downs."
          },
          {
            body: "DepEd (Department of Education)",
            full: "Department of Education & School Divisions",
            badge: "STUDENT & TEACHER WELFARE",
            badgeColor: "text-purple-400 border-purple-500/30 bg-purple-500/10",
            duty: "Safeguard schoolchildren and educators from dangerous classroom heat, determine school cancellation thresholds, and oversee transition to distance learning.",
            help: "We apply cool-roof reflective coatings, rooftop solar microgrids, and high-efficiency cross-ventilation so classrooms remain thermally safe below 32°C WBGT—ending the cycle of cancelled classes and learning loss."
          },
          {
            body: "NDRRMC & DSWD",
            full: "National Disaster Risk Reduction and Management Council & DSWD",
            badge: "ANTICIPATORY ACTION & BLENDED FINANCE",
            badgeColor: "text-pink-400 border-pink-500/30 bg-pink-500/10",
            duty: "Disburse Quick Response Funds, coordinate interagency disaster relief, and distribute anticipatory cash transfers to impoverished families before loss occurs.",
            help: "We provide an auditable non-displacement ledger and positive-sum financing structure, converting emergency relief spending into permanent physical infrastructure that outlives the El Niño, delivering up to $7 in avoided losses per $1 invested."
          }
        ]
      },
      NG: {
        country: "Nigeria",
        flag: "🇳🇬",
        title: "NIGERIA // 31,400 PROJECTED CASUALTIES",
        overview: "Ranked #1 globally in projected heat mortality. Extreme heat stress across northern agricultural belts and high-density urban centers requires urgent inter-ministerial deployment.",
        agencies: [
          {
            body: "NiMet (Nigerian Meteorological Agency)",
            full: "Nigerian Meteorological Agency & Hydrological Services Agency",
            badge: "HEAT-HEALTH WARNINGS",
            badgeColor: "text-blue-400 border-blue-500/30 bg-blue-500/10",
            duty: "Issue seasonal climate predictions, heatwave alerts, and agricultural drought advisories.",
            help: "We integrate NiMet's early alerts into localized solar microgrid dispatch and water condensation triggers in high-vulnerability Sahelian states."
          },
          {
            body: "Federal Ministry of Health & NPHCDA",
            full: "National Primary Health Care Development Agency",
            badge: "PRIMARY CLINIC RESILIENCE",
            badgeColor: "text-red-400 border-red-500/30 bg-red-500/10",
            duty: "Prevent heatstroke mortality, coordinate rural clinic surge capacity, and ensure vaccine preservation.",
            help: "We deploy solar-powered cold-chain hubs at primary health centers, eliminating vaccine spoilage and powering rehydration stations during national grid collapses."
          },
          {
            body: "Federal Ministry of Water Resources",
            full: "River Basin Development Authorities",
            badge: "DROUGHT & WATER RECHARGE",
            badgeColor: "text-telemetry-cyan border-cyan-500/30 bg-cyan-500/10",
            duty: "Manage basin water allocations and mitigate dry-season water table depletion.",
            help: "We install solar-powered atmospheric water generators and sustainable solar groundwater pumping with aquifer drawdown protection."
          },
          {
            body: "Federal Ministry of Agriculture & Food Security",
            full: "Agricultural Development Programmes (ADPs)",
            badge: "CROP & LIVESTOCK SHELTER",
            badgeColor: "text-amber-400 border-amber-500/30 bg-amber-500/10",
            duty: "Shield smallholder farmers, protect livestock from extreme thermal stress, and stabilize food staples.",
            help: "We build agrivoltaic shading systems that co-produce clean energy while reducing crop irrigation demand by over 30%."
          }
        ]
      },
      ID: {
        country: "Indonesia",
        flag: "🇮🇩",
        title: "INDONESIA // 19,300 PROJECTED CASUALTIES",
        overview: "Ranked #2 globally. Compounded by severe drought, peatland wildfire risks, and urban heat exposure across Java, Sumatra, and Kalimantan.",
        agencies: [
          {
            body: "BMKG (Meteorology, Climatology & Geophysics)",
            full: "Badan Meteorologi, Klimatologi, dan Geofisika",
            badge: "CLIMATE & EL NIÑO SENSING",
            badgeColor: "text-blue-400 border-blue-500/30 bg-blue-500/10",
            duty: "Monitor Indian Ocean Dipole and Pacific ENSO triggers, forecast drought zones, and track fire weather index.",
            help: "We link BMKG climate telemetry directly to automated cooling shelter dispatch and early fire-buffer water deployment."
          },
          {
            body: "Ministry of Health (Kemenkes)",
            full: "Kementerian Kesehatan Republik Indonesia",
            badge: "HEAT & SMOKE HEALTH INTERVENTION",
            badgeColor: "text-red-400 border-red-500/30 bg-red-500/10",
            duty: "Protect vulnerable urban populations from compound heat and haze respiratory illness, and reinforce Puskesmas clinics.",
            help: "We equip community Puskesmas with off-grid solar filtration and clean-air cooling refuges that protect citizens during peak heat."
          },
          {
            body: "BNPB (National Disaster Management)",
            full: "Badan Nasional Penanggulangan Bencana",
            badge: "DISASTER LOGISTICS & PEATLAND RECOVERY",
            badgeColor: "text-emerald-400 border-emerald-500/30 bg-emerald-500/10",
            duty: "Lead peatland water management, organize clean water distribution, and mobilize emergency disaster response.",
            help: "We deploy containerized water generation nodes and solar irrigation canopies that re-wet dry peatlands and protect farming communities."
          }
        ]
      },
      IN: {
        country: "India",
        flag: "🇮🇳",
        title: "INDIA // 15,800 PROJECTED CASUALTIES",
        overview: "Ranked #4 globally. Severe pre-monsoon and post-monsoon heat anomalies hitting peninsular and central states with intense agricultural and labor stress.",
        agencies: [
          {
            body: "NDMA & State Disaster Management Authorities",
            full: "National Disaster Management Authority",
            badge: "HEAT ACTION PLANS (HAPs)",
            badgeColor: "text-amber-400 border-amber-500/30 bg-amber-500/10",
            duty: "Activate city Heat Action Plans, set work-hour limits, and coordinate emergency water tankers.",
            help: "We transform paper Heat Action Plans into permanent physical infrastructure: cool roofs, public shade canopies, and solar thermal ice cooling."
          },
          {
            body: "Ministry of Power & State DISCOMs",
            full: "Central Electricity Authority & Distribution Companies",
            badge: "GRID PEAK SHAVING",
            badgeColor: "text-yellow-400 border-yellow-500/30 bg-yellow-500/10",
            duty: "Prevent grid collapses during 250+ GW peak demand days driven by continuous air conditioning load.",
            help: "Our ice-based thermal energy storage shifts building cooling off the grid during peak hours, reducing power purchase costs and avoiding blackouts."
          },
          {
            body: "Ministry of Jal Shakti",
            full: "Department of Water Resources & Jal Jeevan Mission",
            badge: "GROUNDWATER & POTABLE ACCESS",
            badgeColor: "text-telemetry-cyan border-cyan-500/30 bg-cyan-500/10",
            duty: "Maintain piped drinking water to rural households and manage reservoir levels.",
            help: "We deploy solar atmospheric water generation nodes and canal-top solar systems that save water from evaporating under intense sun."
          }
        ]
      },
      BR: {
        country: "Brazil",
        flag: "🇧🇷",
        title: "BRAZIL // 13,300 PROJECTED CASUALTIES",
        overview: "Ranked #5 globally. Extreme heat and severe drought across Amazon basin riverways, Cerrado grain belts, and densely populated southeastern urban centers.",
        agencies: [
          {
            body: "INMET & Cemaden",
            full: "National Institute of Meteorology & Disaster Early Warning",
            badge: "HYDRO-METEOROLOGICAL SENSING",
            badgeColor: "text-blue-400 border-blue-500/30 bg-blue-500/10",
            duty: "Track river basin depths, soil moisture depletion, and thermal anomalies.",
            help: "We convert early warnings into pre-built off-grid water pumping and local cooling microgrids in river-dependent communities."
          },
          {
            body: "ONS & Ministry of Mines and Energy",
            full: "Operador Nacional do Sistema Elétrico",
            badge: "HYDROELECTRIC CONTINGENCY",
            badgeColor: "text-yellow-400 border-yellow-500/30 bg-yellow-500/10",
            duty: "Manage hydroelectric reservoir storage and dispatch thermal peakers when river flows collapse.",
            help: "We deploy floating solar (floatovoltaics) over dam reservoirs, generating clean solar power while reducing water evaporation."
          },
          {
            body: "Ministry of Health (SUS)",
            full: "Sistema Único de Saúde",
            badge: "PUBLIC CLINICAL TRIAGE",
            badgeColor: "text-red-400 border-red-500/30 bg-red-500/10",
            duty: "Treat heat exhaustion in urban peripheries and preserve rural vaccine supplies.",
            help: "We install solar battery cooling systems at primary care clinics (UBS), guaranteeing uninterruptible cold chains and shaded triage zones."
          }
        ]
      },
      KE: {
        country: "Kenya",
        flag: "🇰🇪",
        title: "KENYA // EAST AFRICAN EQUATORIAL BELT",
        overview: "High risk of compound weather shocks—severe northern drought followed by extreme flash flooding. Requires dual-resilient catchment nodes.",
        agencies: [
          {
            body: "Kenya Meteorological Department (KMD)",
            full: "Ministry of Environment, Climate Change & Forestry",
            badge: "CLIMATE PREDICTIONS",
            badgeColor: "text-blue-400 border-blue-500/30 bg-blue-500/10",
            duty: "Provide early warnings for pastoralist counties and agricultural high-yield regions.",
            help: "We link seasonal advisories to anticipatory borehole solar pumping and livestock shade hubs."
          },
          {
            body: "NDMA Kenya",
            full: "National Drought Management Authority",
            badge: "DROUGHT MITIGATION",
            badgeColor: "text-amber-400 border-amber-500/30 bg-amber-500/10",
            duty: "Distribute emergency livestock feed, emergency water trucking, and drought response cash.",
            help: "We deploy permanent solar water condensation and agrivoltaic pasture shields, reducing costly emergency trucking."
          },
          {
            body: "Ministry of Health",
            full: "National and County Health Services",
            badge: "CLINIC ELECTRIFICATION & COLD CHAIN",
            badgeColor: "text-red-400 border-red-500/30 bg-red-500/10",
            duty: "Keep dispensaries and rural maternity centers powered and prevent waterborne disease outbreaks.",
            help: "We install 24/7 solar microgrids with battery storage and water filtration at off-grid county dispensaries."
          }
        ]
      }
    };

    function renderCoalitionCountry(code) {
      const data = COALITION_DATA[code];
      if (!data) return;

      const container = document.getElementById('coalition-agency-matrix');
      if (!container) return;

      // Update Tab Styles
      ['PH', 'NG', 'ID', 'IN', 'BR', 'KE'].forEach(c => {
        const btn = document.getElementById('tab-coalition-' + c);
        if (btn) {
          if (c === code) {
            btn.className = "px-4 py-2 text-xs font-mono font-bold uppercase tracking-wider bg-emerald-500 text-black border border-emerald-400 transition";
          } else {
            btn.className = "px-4 py-2 text-xs font-mono font-bold uppercase tracking-wider bg-space-900/90 text-zinc-400 border border-white/15 hover:border-white transition";
          }
        }
      });

      let htmlCards = `
        <div class="p-6 bg-space-900/90 border border-emerald-500/40 mb-6">
          <div class="flex items-center gap-3 mb-2">
            <span class="text-2xl">${data.flag}</span>
            <h4 class="text-xl sm:text-2xl font-bold font-display text-white">${data.title}</h4>
          </div>
          <p class="text-zinc-300 text-xs sm:text-sm leading-relaxed">${data.overview}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      `;

      data.agencies.forEach((a, i) => {
        htmlCards += `
          <div class="p-5 bg-space-900/80 border border-white/10 hover:border-emerald-500/50 transition flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between gap-2 mb-2">
                <span class="font-mono text-sm font-black text-white tracking-wider">${a.body}</span>
                <span class="px-2 py-0.5 border text-[9px] font-mono font-bold uppercase tracking-wider ${a.badgeColor}">${a.badge}</span>
              </div>
              <div class="text-[11px] font-mono text-zinc-400 mb-3">${a.full}</div>
              
              <div class="space-y-3 text-xs leading-relaxed">
                <div class="p-3 bg-black/60 border border-white/5">
                  <div class="font-mono text-[10px] text-amber-400 uppercase tracking-widest font-bold mb-1">// MANDATED OPERATIONAL DIRECTIVE:</div>
                  <p class="text-zinc-300">${a.duty}</p>
                </div>

                <div class="p-3 bg-emerald-950/20 border border-emerald-500/30">
                  <div class="font-mono text-[10px] text-emerald-400 uppercase tracking-widest font-bold mb-1">// HOW WE HELP THEM (OUR INTERVENTION):</div>
                  <p class="text-zinc-200">${a.help}</p>
                </div>
              </div>
            </div>

            <div class="pt-2 border-t border-white/5 flex items-center justify-between font-mono text-[10px] text-zinc-500">
              <span>INTER-AGENCY SYNERGY</span>
              <a href="mailto:jeffersonrrufino@gmail.com?subject=${encodeURIComponent('Work With Me • ' + data.country + ' Coalition (' + a.body + ')')}" class="text-emerald-400 hover:text-white transition font-bold uppercase">
                Work With Me on ${a.body} &rarr;
              </a>
            </div>
          </div>
        `;
      });

      htmlCards += `</div>`;
      container.innerHTML = htmlCards;
    }

    function switchCoalitionCountry(code) {
      renderCoalitionCountry(code);
    }
'''

    # Insert JavaScript right above document.addEventListener('DOMContentLoaded'
    html = re.sub(
        r"(document\.addEventListener\('DOMContentLoaded', function\(\) \{)",
        coalition_js + r"\n    \1\n      renderCoalitionCountry('PH');",
        html,
        count=1
    )

    # Save to all target files
    for fname in ["index.html", "RUFINOVENTURES.html", "PHOTOSYNTHESIS_PROJECT_PREVIEW.html"]:
        target = os.path.join(base_dir, fname)
        with open(target, "w", encoding="utf-8") as out:
            out.write(html)
        print(f"✓ Successfully generated {fname} with Architect's Charter, Anti-Redundancy, Coalition, Media Matrix, and 'Work with me' ({len(html)} bytes)")

if __name__ == "__main__":
    build()
