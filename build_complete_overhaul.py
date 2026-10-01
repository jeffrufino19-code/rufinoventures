#!/usr/bin/env python3
"""
Generate the high-impact SpaceX-inspired website for rufinoventures.com:
1. Impactful Minimalist Landing Hero:
   "451,000 LIVES AT RISK. 6,500 FILIPINOS."
   "Prediction is not reconciliation. We build physical catchment before the heat arrives."
2. Global Financial Toll: Trillions in unpriced climate debt, crop shocks, grid strain.
3. What the World Currently Has: Failure of passive adaptation.
4. Dedicated Pane: THE PHOTOSYNTHESIS PROJECT (Physical catchment architecture).
5. Dedicated Pane: THE RUFINO SYNTHESIS (LERM + IAMF-P canonical algebra).
6. Dedicated Pane: ORIGINS, EFFORT, & INTENTION (Lived survival, 250k/1M simulations, zero avoidable death).
7. 54-Nation Equatorial Risk Matrix & Philippines First Pilot.
8. Why Support the Project: Positive-sum economics & infrastructure afterlife.
9. Interactive Crisis Telemetry Simulator.
10. Support the Project: Email Jefferson Rafael Rufino directly (jeffersonrrufino@gmail.com).
"""
import os
import re

def build():
    base_dir = "/Users/thehighlandboy/Downloads/RUFINOVENTURES"
    index_path = os.path.join(base_dir, "index.html")
    
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Title
    html = re.sub(
        r'<title>.*?</title>',
        '<title>451,000 LIVES AT RISK // THE PHOTOSYNTHESIS PROJECT & THE RUFINO SYNTHESIS</title>',
        html,
        count=1
    )
    
    # 2. Top Navigation Bar
    new_nav = '''<nav class="hidden 2xl:flex items-center gap-5 text-[10px] uppercase font-mono tracking-widest text-zinc-400">
        <a href="#pane-telemetry" class="hover:text-white transition">01 Financial Toll</a>
        <a href="#pane-solar" class="hover:text-white transition">02 Passive vs Catchment</a>
        <a href="#pane-photosynthesis" class="text-telemetry-cyan hover:text-white transition font-bold">03 Photosynthesis Project</a>
        <a href="#pane-rufino-synthesis" class="text-amber-400 hover:text-white transition font-bold">04 Rufino Synthesis</a>
        <a href="#pane-origins" class="text-purple-400 hover:text-white transition font-bold">05 Origins & Effort</a>
        <a href="#pane-nations" class="hover:text-white transition">06 54 Nations</a>
        <a href="#pane-doctrine" class="hover:text-white transition">07 Why Support</a>
        <a href="#pane-calculator" class="text-emerald-400 hover:text-white transition font-semibold">08 Simulator</a>
      </nav>'''
    html = re.sub(
        r'<nav class="hidden 2xl:flex items-center gap-.*?">.*?</nav>',
        new_nav,
        html,
        flags=re.DOTALL
    )

    # 3. Mobile Navigation Menu
    new_mobile_menu = '''<div id="mobile-menu" class="hidden 2xl:hidden bg-space-950/98 border-b border-white/10 px-6 py-6 font-mono text-xs uppercase tracking-wider space-y-4">
      <div class="grid grid-cols-2 gap-3 text-zinc-300">
        <a href="#pane-telemetry" class="p-2 border border-white/10 hover:border-white transition block">01 Financial Toll</a>
        <a href="#pane-solar" class="p-2 border border-white/10 hover:border-white transition block">02 Passive vs Catchment</a>
        <a href="#pane-photosynthesis" class="p-2 border border-cyan-500/40 text-telemetry-cyan hover:border-white transition block font-bold">03 Photosynthesis Project</a>
        <a href="#pane-rufino-synthesis" class="p-2 border border-amber-500/40 text-amber-400 hover:border-white transition block font-bold">04 Rufino Synthesis</a>
        <a href="#pane-origins" class="p-2 border border-purple-500/40 text-purple-400 hover:border-white transition block font-bold">05 Origins & Effort</a>
        <a href="#pane-nations" class="p-2 border border-white/10 hover:border-white transition block">06 54 Nations Matrix</a>
        <a href="#pane-doctrine" class="p-2 border border-white/10 hover:border-white transition block">07 Why Support</a>
        <a href="#pane-calculator" class="p-2 border border-emerald-500/40 text-emerald-400 hover:border-white transition block">08 Crisis Calculator</a>
      </div>
      <div class="pt-3 border-t border-white/10 flex items-center justify-between text-[11px] text-zinc-400">
        <span>SUPPORT & INQUIRIES:</span>
        <a href="mailto:jeffersonrrufino@gmail.com" class="text-telemetry-cyan underline">jeffersonrrufino@gmail.com</a>
      </div>
    </div>
  </header>'''
    html = re.sub(r'<div id="mobile-menu".*?</header>', new_mobile_menu, html, flags=re.DOTALL)

    # 4. Hero Section - ULTRA IMPACTFUL, MINIMALIST, PUNCHY
    hero_inner = '''    <div class="relative z-10 max-w-[1720px] w-full mx-auto my-auto py-8 sm:py-12">
      <div class="max-w-5xl space-y-6">
        <div class="inline-flex items-center gap-2.5 px-3 py-1 bg-red-500/10 border border-red-500/30 text-[11px] font-mono tracking-[0.25em] uppercase text-red-400">
          <span class="w-2 h-2 rounded-full bg-red-500 animate-ping"></span>
          2026–2027 SUPER EL NIÑO &bull; PLANETARY HAZARD
        </div>
        
        <h1 class="text-5xl sm:text-7xl lg:text-8xl xl:text-9xl font-black uppercase tracking-tight text-white leading-[0.92] font-display">
          451,000 LIVES AT RISK.<br />
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-red-400 via-amber-300 to-cyan-400">
            6,500 FILIPINOS.
          </span>
        </h1>
        
        <p class="text-xl sm:text-2xl lg:text-3xl text-zinc-200 font-light tracking-tight max-w-3xl leading-snug">
          Prediction is not reconciliation. We convert lethal heat into distributed life support before the burden lands.
        </p>

        <div class="pt-2 flex items-center gap-3 text-xs sm:text-sm font-mono text-zinc-400">
          <span class="text-telemetry-cyan font-bold">THE PHOTOSYNTHESIS PROJECT</span>
          <span class="text-zinc-600">&bull;</span>
          <span class="text-amber-400 font-bold">THE RUFINO SYNTHESIS</span>
        </div>

        <!-- High-Impact CTA Row -->
        <div class="flex flex-wrap items-center gap-4 sm:gap-6 pt-4">
          <a href="#pane-telemetry" class="btn-spacex-white">
            EXPLORE THE THREAT &darr;
          </a>
          <a href="#pane-photosynthesis" class="btn-spacex-outline border-cyan-400 text-cyan-300 hover:bg-cyan-400 hover:text-black">
            THE PHOTOSYNTHESIS PROJECT &rarr;
          </a>
          <a href="#pane-rufino-synthesis" class="btn-spacex-outline border-amber-400 text-amber-300 hover:bg-amber-400 hover:text-black">
            THE RUFINO SYNTHESIS &rarr;
          </a>
          <a href="mailto:jeffersonrrufino@gmail.com?subject=Support%20The%20Photosynthesis%20Project" class="btn-spacex-cyan">
            SUPPORT THE PROJECT &rarr;
          </a>
        </div>
      </div>'''

    html = re.sub(
        r'<div class="relative z-10 max-w-\[1720px\] w-full mx-auto my-auto py-.*?">.*?<!-- Telemetry Metric Strip -->',
        hero_inner + '\n\n      <!-- Telemetry Metric Strip -->',
        html,
        flags=re.DOTALL
    )

    # 5. Dedicated Pane: THE PHOTOSYNTHESIS PROJECT (#pane-agrivoltaics & #pane-photosynthesis)
    photosynthesis_pane = '''  <!-- ========================================================================= -->
  <!-- DEDICATED PANE: THE PHOTOSYNTHESIS PROJECT // PHYSICAL CATCHMENT STACK      -->
  <!-- Contextual HD Image: Agrivoltaic Canopies, Solar Energy & Microclimates      -->
  <!-- ========================================================================= -->
  <section id="pane-photosynthesis" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-space-950 border-t border-white/10 scroll-mt-16">
    <div id="pane-agrivoltaics" class="absolute top-0"></div>
    <!-- HD Background Image -->
    <div class="absolute inset-0 z-0">
      <img 
        src="https://images.unsplash.com/photo-1595974482597-4b8da8879bc5?auto=format&fit=crop&w=2560&q=85" 
        alt="Agrivoltaic biospheres and high-tech greenhouse solar canopies" 
        class="w-full h-full object-cover object-center filter brightness-[0.55] contrast-[1.2]" 
        loading="lazy"
      />
      <div class="pane-scrim"></div>
    </div>

    <!-- HUD Top Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-b border-white/15 pb-4">
      <div class="flex items-center gap-3">
        <span class="font-mono text-xs text-telemetry-cyan uppercase tracking-widest font-bold">PHYSICAL CATCHMENT STACK</span>
        <span class="text-zinc-600">/</span>
        <span class="font-mono text-xs text-white font-bold">THE PHOTOSYNTHESIS PROJECT</span>
      </div>
      <div class="font-mono text-xs text-zinc-400 hidden sm:block">
        PILOT OBJECTIVE: ZERO AVOIDABLE DEATH &bull; NOT MERELY BEHAVIORAL ADJUSTMENT
      </div>
    </div>

    <!-- Main Content Grid -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto my-auto py-12 grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
      <div class="lg:col-span-7">
        <div class="inline-flex items-center gap-2 px-3 py-1 bg-cyan-500/10 border border-cyan-500/30 text-[11px] font-mono tracking-widest uppercase text-telemetry-cyan mb-4 font-semibold">
          <span>//</span> CONVERTING CLIMATE STRESS INTO PRODUCTIVE VALUE
        </div>
        <h2 class="text-4xl sm:text-6xl font-black uppercase tracking-tight text-white mb-6 font-display leading-none">
          THE PHOTOSYNTHESIS <br/>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-telemetry-cyan via-white to-emerald-400">PROJECT</span>
        </h2>
        
        <p class="text-zinc-200 text-base sm:text-lg leading-relaxed mb-6 font-normal max-w-2xl">
          Dangerous heat and drought coincide with peak solar irradiance. Rather than letting extreme insolation scorch crops and collapse power grids, <strong>The Photosynthesis Project transforms this peak energy into life-preserving catchment infrastructure:</strong>
        </p>

        <!-- 5-Layer Stack List -->
        <div class="space-y-3 mb-8 max-w-2xl font-mono text-xs">
          <div class="p-3 bg-space-900/80 border border-white/10 flex items-start gap-3">
            <span class="text-telemetry-cyan font-bold">01</span>
            <div><strong class="text-white uppercase">Solar Canopies + Battery + Thermal Storage:</strong> Rooftop/canopy solar paired with chilled water/ice storage to shift cooling output across peak hours without grid strain.</div>
          </div>
          <div class="p-3 bg-space-900/80 border border-white/10 flex items-start gap-3">
            <span class="text-telemetry-cyan font-bold">02</span>
            <div><strong class="text-white uppercase">Public Cooling Refuges &amp; Cool Roofs:</strong> Shaded, thermally protected public centers engineered to drop indoor heat below lethal WBGT limits.</div>
          </div>
          <div class="p-3 bg-space-900/80 border border-white/10 flex items-start gap-3">
            <span class="text-telemetry-cyan font-bold">03</span>
            <div><strong class="text-white uppercase">Atmospheric Water &amp; Potable Dispensing:</strong> Solar condensation units generating 25,000+ liters/day of pure water with strict aquifer recharge safeguards.</div>
          </div>
          <div class="p-3 bg-space-900/80 border border-white/10 flex items-start gap-3">
            <span class="text-telemetry-cyan font-bold">04</span>
            <div><strong class="text-white uppercase">Clinic Power &amp; Medicine Cold-Chain:</strong> Uninterrupted power for insulin, vaccines, oral rehydration therapy, and heat-illness triage.</div>
          </div>
          <div class="p-3 bg-space-900/80 border border-white/10 flex items-start gap-3">
            <span class="text-telemetry-cyan font-bold">05</span>
            <div><strong class="text-white uppercase">Agrivoltaics &amp; Crop Protection:</strong> Elevated bifacial panels cutting microclimate heat by 1–4°C and boosting water-use efficiency by 20–47%.</div>
          </div>
        </div>

        <div class="flex flex-wrap gap-4">
          <a href="#pane-rufino-synthesis" class="btn-spacex-white">
            EXPLORE THE RUFINO SYNTHESIS ALGEBRA &rarr;
          </a>
          <a href="mailto:jeffersonrrufino@gmail.com?subject=Deploy%20Photosynthesis%20Project%20Node" class="btn-spacex-cyan">
            FUND / DEPLOY A CATCHMENT NODE &rarr;
          </a>
        </div>
      </div>

      <!-- Right Column: Philippine First Pilot Strata -->
      <div class="lg:col-span-5 space-y-4">
        <div class="hud-box p-6 border-l-4 border-l-telemetry-cyan">
          <div class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-1">Philippine Ground Zero &bull; Pilot Stratum 1</div>
          <div class="text-2xl sm:text-3xl font-mono font-black text-white">DENSE URBAN HEAT</div>
          <p class="text-xs text-zinc-400 mt-2">
            Public markets, transport interchanges, and barangay halls converted into shaded cooling refuges with free potable water and device charging.
          </p>
        </div>

        <div class="hud-box p-6 border-l-4 border-l-amber-400">
          <div class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-1">Philippine Ground Zero &bull; Pilot Stratum 2 &amp; 3</div>
          <div class="text-2xl sm:text-3xl font-mono font-black text-white">SCHOOLS &amp; HEALTH CLINICS</div>
          <p class="text-xs text-zinc-400 mt-2">
            Preventing class cancellations and keeping primary clinics powered with vaccine refrigeration throughout nationwide grid brownouts.
          </p>
        </div>

        <div class="hud-box p-6 border-l-4 border-l-emerald-400">
          <div class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-1">Philippine Ground Zero &bull; Pilot Stratum 4 &amp; 5</div>
          <div class="text-2xl sm:text-3xl font-mono font-black text-white">AGRICULTURE &amp; FOOD LOGISTICS</div>
          <p class="text-xs text-zinc-400 mt-2">
            Irrigation associations equipped with solar pumping and wholesale markets shielded with cold-chain storage to stop food spoilage.
          </p>
        </div>
      </div>
    </div>

    <!-- Bottom HUD Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-t border-white/10 pt-4 font-mono text-[11px] text-zinc-500">
      <div>PHYSICAL ARCHITECTURE: 5 CATCHMENT STRATA // DEPLOYABLE IN 15–45 DAYS</div>
      <div class="text-zinc-400">INQUIRIES: jeffersonrrufino@gmail.com</div>
    </div>
  </section>'''
    html = re.sub(r'<section id="pane-agrivoltaics".*?</section>', photosynthesis_pane, html, flags=re.DOTALL)
    html = re.sub(r'<section id="pane-photosynthesis".*?</section>', photosynthesis_pane, html, flags=re.DOTALL)

    # 6. Dedicated Pane: THE RUFINO SYNTHESIS (#pane-water & #pane-rufino-synthesis)
    rufino_synthesis_pane = '''  <!-- ========================================================================= -->
  <!-- DEDICATED PANE: THE RUFINO SYNTHESIS // LERM + IAMF-P CANONICAL ALGEBRA    -->
  <!-- Contextual HD Image: High-Tech Engineering Nexus & Mathematical Core        -->
  <!-- ========================================================================= -->
  <section id="pane-rufino-synthesis" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-space-950 border-t border-white/10 scroll-mt-16">
    <div id="pane-water" class="absolute top-0"></div>
    <!-- HD Background Image -->
    <div class="absolute inset-0 z-0">
      <img 
        src="https://images.unsplash.com/photo-1518837695005-2083093ee35b?auto=format&fit=crop&w=2560&q=85" 
        alt="Mathematical fluid dynamics and pure water filtration currents" 
        class="w-full h-full object-cover object-center filter brightness-[0.55] contrast-[1.2]" 
        loading="lazy"
      />
      <div class="pane-scrim"></div>
    </div>

    <!-- HUD Top Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-b border-white/15 pb-4">
      <div class="flex items-center gap-3">
        <span class="font-mono text-xs text-amber-400 uppercase tracking-widest font-bold">FORMAL RECONCILIATION KERNEL // CANONICAL SPECIFICATION</span>
        <span class="text-zinc-600">/</span>
        <span class="font-mono text-xs text-white font-bold">THE RUFINO SYNTHESIS</span>
      </div>
      <div class="font-mono text-xs text-zinc-400 hidden sm:block">
        ONE IRREDUCIBLE KERNEL, NOT TWO FRAMEWORKS &bull; LERM + IAMF-P
      </div>
    </div>

    <!-- Main Content Grid -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto my-auto py-12 grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
      <div class="lg:col-span-7">
        <div class="inline-flex items-center gap-2 px-3 py-1 bg-amber-500/10 border border-amber-500/30 text-[11px] font-mono tracking-widest uppercase text-amber-400 mb-4 font-semibold">
          <span>//</span> CONVENTIONAL OPTIMIZATION OMITS THE CARRIER &bull; RUFINO RECONCILES IT
        </div>
        <h2 class="text-4xl sm:text-6xl font-black uppercase tracking-tight text-white mb-6 font-display leading-none">
          THE RUFINO <br/>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-400 via-yellow-200 to-white">SYNTHESIS</span>
        </h2>
        
        <p class="text-zinc-200 text-base sm:text-lg leading-relaxed mb-6 font-normal max-w-2xl">
          The candidate scientific contribution of the Rufino Synthesis is the mandatory conjunction of boundary divergence, directed displacement, carrier identification, hidden compensation, capacity construction, productive reconciliation, and post-intervention non-displacement testing inside <strong>one frozen recurrent loop:</strong>
        </p>

        <!-- Kernel Formula Box -->
        <div class="p-4 bg-black/90 border border-amber-400/40 font-mono text-xs sm:text-sm text-amber-300 mb-6 max-w-2xl space-y-2">
          <div class="text-zinc-400 text-[10px] tracking-widest uppercase">// RECURRENT CANONICAL KERNEL:</div>
          <div class="text-white font-bold tracking-wider">
            observe &rarr; trace &rarr; build &rarr; transform &rarr; reintegrate &rarr; retest &rarr; observe again
          </div>
          <div class="text-[11px] text-zinc-400 pt-1 border-t border-white/10">
            K_R = M_d<sup>-1</sup> &comp; Q_d &comp; F_d &comp; I &comp; L &comp; M_d
          </div>
        </div>

        <p class="text-zinc-400 text-sm sm:text-base leading-relaxed mb-8 max-w-2xl">
          <strong>LERM</strong> is the detection and tracing operator: it identifies the residual between expected and observed state, follows the direction of displacement, names the receiving carrier, and detects hidden compensation.<br/>
          <strong>IAMF-P</strong> is the constructive operator: it builds new reconciliation capacity directly at the receiving carrier, transforms recovered state into higher utility, and enforces non-displacement.
        </p>

        <div class="flex flex-wrap gap-4">
          <a href="#pane-origins" class="btn-spacex-white">
            READ THE ORIGINS &amp; EFFORT &rarr;
          </a>
          <a href="#pane-doctrine" class="btn-spacex-outline border-amber-400 text-amber-300">
            POSITIVE-SUM FINANCING ENGINE &rarr;
          </a>
        </div>
      </div>

      <!-- Right Column: Mathematical Formulas Vault -->
      <div class="lg:col-span-5 space-y-4">
        <div class="hud-box p-5 border-l-4 border-l-amber-400">
          <div class="font-mono text-[10px] uppercase tracking-widest text-zinc-400 mb-1">Equation 4.2 &bull; Boundary Divergence Index</div>
          <div class="text-xl sm:text-2xl font-mono font-bold text-amber-300">BDI = J_G(a*_S) - J_G(a*_G)</div>
          <p class="text-xs text-zinc-400 mt-2">
            Detects when a local boundary optimization looks efficient only because its costs are silently dumped onto households, workers, or the grid.
          </p>
        </div>

        <div class="hud-box p-5 border-l-4 border-l-red-400">
          <div class="font-mono text-[10px] uppercase tracking-widest text-zinc-400 mb-1">Equation 4.4 &bull; Reconciliation Velocity Gap</div>
          <div class="text-xl sm:text-2xl font-mono font-bold text-red-400">RVG(t) = dU_hazard/dt - dR_response/dt &le; 0</div>
          <p class="text-xs text-zinc-400 mt-2">
            Mandatory operational target: response capacity must expand faster than unresolved hazard burden accumulates.
          </p>
        </div>

        <div class="hud-box p-5 border-l-4 border-l-emerald-400">
          <div class="font-mono text-[10px] uppercase tracking-widest text-zinc-400 mb-1">Equation 4.5 &bull; Non-Displacement Acceptance Condition</div>
          <div class="text-lg sm:text-xl font-mono font-bold text-emerald-300">&Delta;V_j &ge; -&epsilon;_j &bull; &sum;&Delta;V_j &gt; 0 &bull; &Delta;U_max &le; 0</div>
          <p class="text-xs text-zinc-400 mt-2">
            Rejects any "solution" that creates a hidden loser. Every carrier must be no worse off, and total useful value must increase.
          </p>
        </div>

        <div class="hud-box p-5 border-l-4 border-l-telemetry-cyan">
          <div class="font-mono text-[10px] uppercase tracking-widest text-zinc-400 mb-1">Equation 8.1 &bull; Event-Linked Upside Conversion</div>
          <div class="text-lg sm:text-xl font-mono font-bold text-telemetry-cyan">EUL_s(t) = max[0, Profit_s(t) - ExpectedProfit_s(t)]</div>
          <p class="text-xs text-zinc-400 mt-2">
            Captures excess windfall margins from heat-wave volatility and contracts them directly into pre-funded public catchment nodes.
          </p>
        </div>
      </div>
    </div>

    <!-- Bottom HUD Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-t border-white/10 pt-4 font-mono text-[11px] text-zinc-500">
      <div>CANONICAL ALGEBRA: BDI &bull; RVG &bull; DISPLACEMENT SHADOW &bull; NON-DISPLACEMENT ACCEPTANCE</div>
      <div class="text-zinc-400">INQUIRIES: jeffersonrrufino@gmail.com</div>
    </div>
  </section>'''
    html = re.sub(r'<section id="pane-water".*?</section>', rufino_synthesis_pane, html, flags=re.DOTALL)
    html = re.sub(r'<section id="pane-rufino-synthesis".*?</section>', rufino_synthesis_pane, html, flags=re.DOTALL)

    # 7. Dedicated Pane: ORIGINS, EFFORT, & INTENTION (#pane-medical & #pane-origins)
    origins_pane = '''  <!-- ========================================================================= -->
  <!-- DEDICATED PANE: ORIGINS, EFFORT, & INTENTION // THE FIELD RECORD            -->
  <!-- Contextual HD Image: Clinical Cleanrooms & Emergency Medical Cold Storage   -->
  <!-- ========================================================================= -->
  <section id="pane-origins" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-space-950 border-t border-white/10 scroll-mt-16">
    <div id="pane-medical" class="absolute top-0"></div>
    <!-- HD Background Image -->
    <div class="absolute inset-0 z-0">
      <img 
        src="https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?auto=format&fit=crop&w=2560&q=85" 
        alt="Emergency healthcare cleanrooms and medical cold-chain logistics" 
        class="w-full h-full object-cover object-center filter brightness-[0.55] contrast-[1.2]" 
        loading="lazy"
      />
      <div class="pane-scrim"></div>
    </div>

    <!-- HUD Top Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-b border-white/15 pb-4">
      <div class="flex items-center gap-3">
        <span class="font-mono text-xs text-purple-400 uppercase tracking-widest font-bold">OPERATING RECORD &bull; PROVENANCE &bull; CONVICTION</span>
        <span class="text-zinc-600">/</span>
        <span class="font-mono text-xs text-white font-bold">ORIGINS, EFFORT, &amp; INTENTION</span>
      </div>
      <div class="font-mono text-xs text-zinc-400 hidden sm:block">
        JEFFERSON RAFAEL RUFINO &bull; FOUNDER / ARCHITECT
      </div>
    </div>

    <!-- Main Content Grid -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto my-auto py-12 grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
      <div class="lg:col-span-7">
        <div class="inline-flex items-center gap-2 px-3 py-1 bg-purple-500/10 border border-purple-500/30 text-[11px] font-mono tracking-widest uppercase text-purple-400 mb-4 font-semibold">
          <span>//</span> THE FIELD RECORD BEFORE THE MATHEMATICS
        </div>
        <h2 class="text-4xl sm:text-6xl font-black uppercase tracking-tight text-white mb-6 font-display leading-none">
          THE ORIGINS, THE EFFORT, <br/>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 via-pink-300 to-white">&amp; THE INTENTION</span>
        </h2>
        
        <div class="space-y-4 text-zinc-300 text-sm sm:text-base leading-relaxed max-w-2xl mb-8">
          <p>
            <strong>The Origin:</strong> The archive's own methodological rule is that the operating record precedes the formal architecture. LERM did not begin as an academic exercise. It began as a survival and operating problem: repeated exposure to systems where a visible success depended on hidden labor, unrecognized trauma, unsupported compensation, and unpriced friction.
          </p>
          <p>
            Born from lived developmental instability, institutional betrayal, and corporate compression, the framework's central concept of <em>hidden compensation</em> is inseparable from the lived experience of appearing functional while one carrier silently absorbs the cost. From this emerged an unshakeable definition of Zero:
          </p>
          <blockquote class="p-4 bg-black/80 border-l-4 border-purple-400 text-white font-mono text-xs sm:text-sm">
            0 = a non-displaced residual state in which one system's success no longer requires an unaccounted loser elsewhere. Zero is therefore not inactivity. It is closure of the consequential ledger.
          </blockquote>
          <p>
            <strong>The Effort:</strong> This architecture was not rushed. It has been tested across 250,000-case negative ablations (preserving the exact condition under which LERM lost when constrained to existing capacity), 250,000-case corrected catch-basin simulations, two 1,000,000-system arena experiments, and an executable 121/121 formal test conformance suite. It honors a continuous scientific lineage from Newton, Clausius, Boltzmann, Gibbs, and Einstein to Prigogine, Coase, Shannon, Wiener, Simon, and Ostrom.
          </p>
          <p>
            <strong>The Intention:</strong> This website exists for one reason: <strong>ZERO AVOIDABLE DEATH</strong> during the 2026–2027 Super El Niño. The event is not an opportunity because people suffer; the opportunity is that the hazard is forecast early enough to build infrastructure whose economics improve when suffering falls.
          </p>
        </div>

        <div class="flex flex-wrap gap-4">
          <a href="#pane-nations" class="btn-spacex-white">
            VIEW THE 54 VULNERABLE NATIONS &rarr;
          </a>
          <a href="mailto:jeffersonrrufino@gmail.com?subject=Strategic%20Support%20for%20The%20Photosynthesis%20Project" class="btn-spacex-cyan">
            CONNECT DIRECTLY WITH THE FOUNDER &rarr;
          </a>
        </div>
      </div>

      <!-- Right Column: Institutional Creed Cards -->
      <div class="lg:col-span-5 space-y-4">
        <div class="hud-box p-6 border-l-4 border-l-purple-400">
          <div class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-1">Founder's Canonical Law</div>
          <div class="text-xl sm:text-2xl font-mono font-bold text-white leading-snug">
            "Find where reality escaped. Follow where it went. Name what carried it. Build where it landed. Transform what was recovered."
          </div>
          <p class="text-xs text-zinc-400 mt-3 font-mono">
            Check every carrier and every future period again. Then look again.
          </p>
        </div>

        <div class="hud-box p-6 border-l-4 border-l-amber-400">
          <div class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-1">Empirical Conformance Record</div>
          <div class="text-2xl sm:text-3xl font-mono font-black text-amber-400">121 / 121 PASSED</div>
          <p class="text-xs text-zinc-400 mt-2">
            100% executable software conformance across 90 feature tests, 16 boundary tests, 7 dialectic tests, and 8 acceptance tests.
          </p>
        </div>

        <div class="hud-box p-6 border-l-4 border-l-telemetry-cyan">
          <div class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-1">The Operational North Star</div>
          <div class="text-xl sm:text-2xl font-mono font-bold text-telemetry-cyan">
            EVERY WEEK OF LEAD TIME MUST BECOME CAPACITY.
          </div>
          <p class="text-xs text-zinc-400 mt-2">
            Every dollar invested before peak exposure must leave behind permanent power, water, and food infrastructure that outlives the El Niño.
          </p>
        </div>
      </div>
    </div>

    <!-- Bottom HUD Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-t border-white/10 pt-4 font-mono text-[11px] text-zinc-500">
      <div>FOUNDER ARCHIVE &bull; METRO MANILA, PHILIPPINES // STRICT PROVENANCE DISCIPLINE</div>
      <div class="text-zinc-400">DIRECT DISPATCH: jeffersonrrufino@gmail.com</div>
    </div>
  </section>'''
    html = re.sub(r'<section id="pane-medical".*?</section>', origins_pane, html, flags=re.DOTALL)
    html = re.sub(r'<section id="pane-origins".*?</section>', origins_pane, html, flags=re.DOTALL)

    # 8. Write updated files
    for fname in ["index.html", "RUFINOVENTURES.html", "PHOTOSYNTHESIS_PROJECT_PREVIEW.html"]:
        target = os.path.join(base_dir, fname)
        with open(target, "w", encoding="utf-8") as out:
            out.write(html)
        print(f"✓ Generated {fname} ({len(html)} bytes)")

if __name__ == "__main__":
    build()
