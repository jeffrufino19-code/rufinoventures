import os, json

# Import generator framework
from build_all_pages import render_html_page, save_page, adapters, families, adapters_json, families_json

# =========================================================================
# 1. PAGE: INDEX (Main Landing Page - Interpretation of the Atlas)
# =========================================================================
index_body = """
<!-- HERO SECTION (SPACEX MINIMALIST) -->
<section class="relative pt-20 pb-28 border-b border-zinc-900 grid-bg">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="inline-flex items-center gap-2 px-3 py-1 bg-zinc-900 border border-zinc-800 text-[10px] font-mono text-zinc-400 mb-8 uppercase tracking-widest">
      <span class="w-1.5 h-1.5 rounded-full bg-white animate-ping mr-1"></span>
      CANONICAL EDITION 1.0 · 1,170 PAGES · OCTOBER 9, 2026 FREEZE
    </div>

    <div class="max-w-4xl space-y-6">
      <h1 class="font-display font-black text-4xl sm:text-6xl lg:text-7xl tracking-tight text-white uppercase leading-[1.05]">
        ONE GRAMMAR.<br />
        <span class="text-zinc-500">MANY SUBSTRATES.</span>
      </h1>
      
      <p class="text-xl sm:text-2xl font-light text-zinc-300 leading-relaxed font-sans max-w-3xl">
        The consequential systems encyclopedia proving that <span class="text-white font-medium underline underline-offset-4 decoration-zinc-700">consequence burden is conserved</span> across all reality perimeters.
      </p>

      <p class="text-sm sm:text-base text-zinc-400 font-sans leading-relaxed max-w-3xl">
        Optimization within a closed boundary does not eliminate loss; it displaces it across the perimeter onto unregistered carriers. Born from 1.8 years of sole vertical commercial execution, acute spatial displacement, and forensic accounting of institutional failures—the Universal Reality Atlas decodes the universal grammar governing cancer diagnostics, criminal courts, algorithmic credit, financial crises, and crustal plate tectonics.
      </p>

      <!-- Canonical Theorem Quote -->
      <div class="p-4 bg-zinc-950 border-l-2 border-white border-y border-r border-zinc-800 text-xs font-mono text-zinc-300">
        <span class="text-white font-bold">CANONICAL INVARIANT:</span> "The operating record precedes the formal architecture." (Atlas p. 1170)
      </div>

      <div class="flex flex-wrap items-center gap-4 pt-4 font-mono text-xs">
        <a href="/realities" class="px-6 py-3 bg-white text-black font-semibold hover:bg-zinc-200 uppercase tracking-wider transition">
          EXPLORE 120 ADAPTERS
        </a>
        <a href="/founder" class="px-6 py-3 bg-zinc-900 text-white border border-zinc-800 hover:border-zinc-500 uppercase tracking-wider transition">
          THE FOUNDER SCARS
        </a>
        <a href="/LERM" class="px-6 py-3 bg-zinc-950 text-zinc-400 border border-zinc-850 hover:text-white uppercase tracking-wider transition">
          PAX SILICA & 2027 CRASH
        </a>
      </div>
    </div>

    <!-- Telemetry Stats Grid -->
    <div class="mt-20 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4 font-mono text-center">
      <div class="p-4 bg-zinc-950 border border-zinc-900">
        <div class="text-3xl font-display font-bold text-white">1,170</div>
        <div class="text-[10px] text-zinc-500 uppercase tracking-widest mt-1">CANONICAL PAGES</div>
      </div>
      <div class="p-4 bg-zinc-950 border border-zinc-900">
        <div class="text-3xl font-display font-bold text-white">120</div>
        <div class="text-[10px] text-zinc-500 uppercase tracking-widest mt-1">REALITY ADAPTERS</div>
      </div>
      <div class="p-4 bg-zinc-950 border border-zinc-900">
        <div class="text-3xl font-display font-bold text-white">12</div>
        <div class="text-[10px] text-zinc-500 uppercase tracking-widest mt-1">REALITY BRANCHES</div>
      </div>
      <div class="p-4 bg-zinc-950 border border-zinc-900">
        <div class="text-3xl font-display font-bold text-white">₱2.85T</div>
        <div class="text-[10px] text-zinc-500 uppercase tracking-widest mt-1">DISPLACEMENT SUM</div>
      </div>
      <div class="p-4 bg-zinc-950 border border-zinc-900">
        <div class="text-3xl font-display font-bold text-white">0.00%</div>
        <div class="text-[10px] text-zinc-500 uppercase tracking-widest mt-1">ARITHMETIC VARIANCE</div>
      </div>
      <div class="p-4 bg-zinc-950 border border-zinc-900">
        <div class="text-3xl font-display font-bold text-white">121/121</div>
        <div class="text-[10px] text-zinc-500 uppercase tracking-widest mt-1">TEST CONFORMANCE</div>
      </div>
    </div>

  </div>
</section>

<!-- INTERPRETATION OF THE ATLAS -->
<section class="py-24 border-b border-zinc-900">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16">
    
    <div class="max-w-3xl">
      <div class="text-[10px] font-mono uppercase tracking-widest text-zinc-500 mb-2">SYSTEM THEORETIC ESSENCE</div>
      <h2 class="font-display font-black text-3xl sm:text-4xl text-white tracking-tight uppercase">
        THE CONGRUENCE OF ALL REALITIES
      </h2>
      <p class="text-zinc-400 mt-4 text-sm font-sans leading-relaxed">
        The Universal Reality Atlas establishes that what the world calls separate disciplines—medicine, law, banking, physics, psychology, and geology—are merely local dialects of a single conservation law. The split between quantum mechanics and classical physics, the collapse of credit markets, the misdiagnosis of mental illness, and the eruption of volcanic stress all obey the exact same boundary dynamics.
      </p>
    </div>

    <!-- The 10-Step Consequential Cycle -->
    <div class="p-8 bg-zinc-950 border border-zinc-900 space-y-6">
      <div class="flex items-center justify-between pb-4 border-b border-zinc-800 text-xs font-mono text-zinc-400">
        <span class="text-white font-bold uppercase">THE FROZEN CONSEQUENTIAL GRAMMAR</span>
        <span>FOUNDATION 03 // ATLAS p. 4</span>
      </div>

      <div class="text-center font-mono text-xs sm:text-sm text-zinc-200 overflow-x-auto py-2">
        $$\Omega_t \longrightarrow M_d \longrightarrow X^*_t \longrightarrow \Sigma_d \longrightarrow G_\Sigma \longrightarrow BDI \longrightarrow D_a \longrightarrow C, \Gamma, H \longrightarrow \Delta R^* \longrightarrow a \longrightarrow MU^+ \longrightarrow 	ext{retest}$$
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-xs font-mono text-zinc-400 pt-4 border-t border-zinc-900">
        <div>
          <span class="text-white block font-bold mb-1">1. STATE & SCHEMA GAP (\(G_\Sigma\))</span>
          The distance between evidence-grounded native reality \(X^*\) and what the reductionist administrative schema \(\Sigma\) is legally or technologically capable of seeing.
        </div>
        <div>
          <span class="text-white block font-bold mb-1">2. BOUNDARY DIVERGENCE (BDI)</span>
          Measures the divergence between the locally optimized action \(a^*_S\) and the globally consequential action \(a^*_G\). If BDI > 0, local efficiency creates systemic damage.
        </div>
        <div>
          <span class="text-white block font-bold mb-1">3. MUTUAL UPTICK GATE (\(MU^+\))</span>
          Strict rejection of scalar averages. Every protected carrier must clear its native threshold with uncertainty accounted for before an action is permitted.
        </div>
      </div>
    </div>

    <!-- The Master Macroeconomic Theorem -->
    <div class="p-8 bg-zinc-950 border border-zinc-800 space-y-4">
      <div class="flex items-center justify-between text-xs font-mono text-zinc-400">
        <span class="text-white font-bold uppercase">THE LERM MASTER THEOREM OF SYSTEM DISPLACEMENT</span>
        <span>SECTION 1.1 // LERM VAULT</span>
      </div>
      <div class="text-center font-mono text-sm sm:text-base text-zinc-100 overflow-x-auto py-4">
        $$\mathbf{\mathcal{D}}_{	ext{net}}(T) = \int_{0}^{T} \left[ \sum_{i=1}^{N} \left( \nabla \cdot \mathbf{J}_i^{	ext{ext}}(t) + \mathcal{L}_i^{	ext{tacit}}(t) + \mathcal{K}_i^{	ext{debt}}(t) 
ight) - \sum_{j=1}^{M} \mathcal{R}_j^{	ext{recov}}(t) 
ight] dt - \Delta \mathcal{V}_{	ext{real}}(T)$$
      </div>
      <p class="text-xs text-zinc-400 font-sans leading-relaxed">
        Gauss's Divergence Theorem applied to socioeconomic and computational boundaries. When a corporation, algorithm, or government minimizes costs inside \(\partial S_i\), the flux \(\nabla \cdot \mathbf{J}_i^{	ext{ext}}\) is uncompensated cost exported into the surrounding human and ecological carriers.
      </p>
    </div>

    <!-- Quick Portal Cards to All Companion Tabs -->
    <div>
      <h3 class="text-xs font-mono uppercase tracking-widest text-zinc-400 mb-6">THE ATLAS ARCHITECTURE SUITE</h3>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 font-mono text-xs">
        
        <a href="/founder" class="p-5 bg-zinc-950 border border-zinc-900 hover:border-white transition block group">
          <div class="text-zinc-500 text-[10px]">01 // DOSSIER</div>
          <div class="text-white font-bold text-sm mt-1 group-hover:underline">THE FOUNDER</div>
          <p class="text-zinc-500 text-[11px] font-sans mt-2">The unbroken chronological arc: university rupture, homelessness, Rockwell counterfeit pivot, family reconciliation, and grit.</p>
        </a>

        <a href="/realities" class="p-5 bg-zinc-950 border border-zinc-900 hover:border-white transition block group">
          <div class="text-zinc-500 text-[10px]">02 // CATALOG</div>
          <div class="text-white font-bold text-sm mt-1 group-hover:underline">120 REALITIES</div>
          <p class="text-zinc-500 text-[11px] font-sans mt-2">Interactive matrix of all 12 Reality Branches and 120 Adapters with complete 7-Plate consequential profiles.</p>
        </a>

        <a href="/LERM" class="p-5 bg-zinc-950 border border-zinc-900 hover:border-white transition block group">
          <div class="text-zinc-500 text-[10px]">03 // MACROECONOMIC</div>
          <div class="text-white font-bold text-sm mt-1 group-hover:underline">PAX SILICA RADAR</div>
          <p class="text-zinc-500 text-[11px] font-sans mt-2">The August 2027 Triple Cliff convergence and Philippine ₱2.85T macroeconomic cross-subsidy forensic audit.</p>
        </a>

        <a href="/photosynthesisproject" class="p-5 bg-zinc-950 border border-zinc-900 hover:border-white transition block group">
          <div class="text-zinc-500 text-[10px]">04 // CLIMATE</div>
          <div class="text-white font-bold text-sm mt-1 group-hover:underline">PHOTOSYNTHESIS</div>
          <p class="text-zinc-500 text-[11px] font-sans mt-2">451,000 lives at risk: agrivoltaics, atmospheric water harvesting, and off-grid cold chain for Super El Niño.</p>
        </a>

        <a href="/shopfamcollective" class="p-5 bg-zinc-950 border border-zinc-900 hover:border-white transition block group">
          <div class="text-zinc-500 text-[10px]">05 // ORIGIN TESTBED</div>
          <div class="text-white font-bold text-sm mt-1 group-hover:underline">SHOPFAM COLLECTIVE</div>
          <p class="text-zinc-500 text-[11px] font-sans mt-2">The ARCH file: ₱3.477M commercial execution proving the then-unnamed MU+ effect and 8-node vertical bricolage.</p>
        </a>

        <a href="/scientists" class="p-5 bg-zinc-950 border border-zinc-900 hover:border-white transition block group">
          <div class="text-zinc-500 text-[10px]">06 // GENEALOGY</div>
          <div class="text-white font-bold text-sm mt-1 group-hover:underline">SCIENTISTS & LINEAGE</div>
          <p class="text-zinc-500 text-[11px] font-sans mt-2">Arrow, Coase, Hayek, Friston, Shannon, Wiener, Williamson, Ostrom, Boltzmann, Bak, Einstein, and Rufino.</p>
        </a>

        <a href="/build" class="p-5 bg-zinc-950 border border-zinc-900 hover:border-white transition block group">
          <div class="text-zinc-500 text-[10px]">07 // COALITION</div>
          <div class="text-white font-bold text-sm mt-1 group-hover:underline">BUILD WITH US</div>
          <p class="text-zinc-500 text-[11px] font-sans mt-2">Technical builds, sandbox implementations, and sovereign capital partnership blueprints.</p>
        </a>

        <a href="/contactus" class="p-5 bg-zinc-950 border border-zinc-900 hover:border-white transition block group">
          <div class="text-zinc-500 text-[10px]">08 // ADVISORY</div>
          <div class="text-white font-bold text-sm mt-1 group-hover:underline">CONTACT & AUDIT</div>
          <p class="text-zinc-500 text-[11px] font-sans mt-2">Direct correspondence with Jefferson Rafael Rufino: email, LinkedIn, Instagram, and 9:00 AM protocol.</p>
        </a>

      </div>
    </div>

  </div>
</section>
"""

save_page("index", render_html_page("RUFINO VENTURES // THE UNIVERSAL REALITY ATLAS", "index", index_body))

# =========================================================================
# 2. PAGE: FOUNDER (The Unsanitized Chronology & Existential Truth)
# =========================================================================
founder_body = """
<section class="py-20 border-b border-zinc-900 grid-bg">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
    <div class="inline-flex items-center gap-2 px-3 py-1 bg-zinc-900 border border-zinc-800 text-[10px] font-mono text-zinc-400 uppercase tracking-widest">
      FOUNDER DOSSIER // THE UNSANITIZED RECORD
    </div>
    <h1 class="font-display font-black text-4xl sm:text-6xl text-white uppercase tracking-tight leading-[1.08]">
      THE ARCHITECT'S MIRROR.<br />
      <span class="text-zinc-500">WHAT WAS PAID TO SEE REALITY.</span>
    </h1>
    <p class="text-lg text-zinc-300 font-sans leading-relaxed">
      How a boy from the Philippines with no Ivy League pedigree, no venture capital buffer, and no institutional patronage survived spatial eviction, commercial humiliation, and severe somatic exhaustion to decode the conservation grammar of reality—and chose to build for coexistence rather than revenge.
    </p>
    <div class="p-4 bg-zinc-950 border-l-2 border-white text-xs font-mono text-zinc-300">
      "Because to be truly seen — you have to truly see as well." — Jefferson Rafael Rufino
    </div>
  </div>
</section>

<section class="py-20 border-b border-zinc-900">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16">

    <!-- 1. The Dialectical Truth -->
    <div class="p-8 bg-zinc-950 border border-zinc-800 space-y-4">
      <div class="text-xs font-mono text-white font-bold uppercase tracking-wider">
        THE DIALECTICAL NON-FRAGMENTATION MANDATE
      </div>
      <p class="text-xs text-zinc-300 font-sans leading-relaxed">
        Conventional corporate and academic evaluators repeatedly split individuals into false dichotomies: either romanticizing high-tail cognitive output as invulnerable genius (erasing the physical agony, insomnia, and terror), or pathologizing systemic trauma as intellectual deficiency.
      </p>
      <p class="text-xs text-zinc-300 font-sans leading-relaxed">
        <strong class="text-white">The canonical truth is non-fragmented:</strong> The subject operates as a verified P5 Generative Systems Architect with zero mathematical variance (\(\epsilon = 0.00\%\)), while simultaneously carrying severe somatic and autonomic wear on Carrier 3 (human physiology). Neither dimension cancels the other.
      </p>
    </div>

    <!-- 2. The Unbroken Chronological Arc -->
    <div class="space-y-8">
      <h2 class="font-display font-bold text-2xl text-white uppercase tracking-wider">
        THE UNBROKEN CHRONOLOGY: THE GOOD, THE BAD, AND THE SCARS
      </h2>

      <div class="relative border-l border-zinc-800 ml-4 space-y-10 pl-6 text-xs font-mono">
        
        <div>
          <span class="text-zinc-500">EPOCH I · PRE-2016</span>
          <h3 class="text-white font-bold text-sm mt-0.5">Childhood Volatility & Defensive Hyper-Vigilance</h3>
          <p class="text-zinc-400 mt-2 font-sans leading-relaxed">
            Severe domestic instability in the Philippines. Developing high-frequency environmental threat scanning and multi-variable pattern recognition as survival adaptations—the cognitive baseline for detecting invisible system friction.
          </p>
        </div>

        <div>
          <span class="text-zinc-500">EPOCH II · ~2016</span>
          <h3 class="text-white font-bold text-sm mt-0.5">University Institutional Abuse & Autodidactic Pivot</h3>
          <p class="text-zinc-400 mt-2 font-sans leading-relaxed">
            Severe abuse within the tertiary educational institution. Exiting credential cartels permanently; refusing victimhood; initiating an autodidactic curriculum in tensor mathematics, thermodynamics, software engineering, and non-equilibrium economics.
          </p>
        </div>

        <div>
          <span class="text-zinc-500">EPOCH III · 2017–2023</span>
          <h3 class="text-white font-bold text-sm mt-0.5">Corporate Compression in Philippine BPO/IT-BPM</h3>
          <p class="text-zinc-400 mt-2 font-sans leading-relaxed">
            Employment across TELUS International, Castlery, IHG, HRnFLEX. Observing firsthand how Western supply chains treat Filipino labor as uncompensated shock absorbers—absorbing emotional wear, graveyard shift sleep loss, and cognitive exhaustion for static wages.
          </p>
        </div>

        <div>
          <span class="text-zinc-500">EPOCH IV · EARLY 2024</span>
          <h3 class="text-white font-bold text-sm mt-0.5">Dual-Reality: Pageantry Visibility & Predatory Grooming</h3>
          <p class="text-zinc-400 mt-2 font-sans leading-relaxed">
            Public national pageantry while subjected to private coercive financial grooming and extractive domestic relationships. Navigating extreme divergence between public aesthetic glamour and acute private financial starvation.
          </p>
        </div>

        <div class="p-4 bg-zinc-950 border border-zinc-800">
          <span class="text-white font-bold">EPOCH V · LATE 2024 · THE ZERO-POINT CRUCIBLE</span>
          <h3 class="text-white font-bold text-sm mt-0.5">Metro Manila Spatial Eviction & Absolute Liquidity Depletion</h3>
          <p class="text-zinc-300 mt-2 font-sans leading-relaxed">
            Total cash exhaustion. Eviction onto the streets and transient spaces of Metro Manila. Carrying everything in bags. Severe caloric and sleep deprivation.
          </p>
          <div class="mt-2 text-white italic">
            "Zero is not nothing. It is the non-displaced residual state where one system's success no longer requires an unaccounted loser elsewhere." (Canonical LERM)
          </div>
        </div>

        <div>
          <span class="text-zinc-500">EPOCH VI · LATE 2024</span>
          <h3 class="text-white font-bold text-sm mt-0.5">The Rockwell Center Counterfeit Humiliation & Forensic Pivot</h3>
          <p class="text-zinc-400 mt-2 font-sans leading-relaxed">
            Attempted luxury resale at Rockwell Center Makati. Accused of counterfeit inventory by mall security; threatened with criminal charges. Instead of despairing, the subject executed an immediate forensic audit, discovering the systemic truth: <strong class="text-white">Bureau of Customs (BOC) border tariff clearance ≠ Brand IP distribution provenance.</strong> The LERM provenance architecture was born.
          </p>
        </div>

        <div>
          <span class="text-zinc-500">EPOCH VII · 2024–2026</span>
          <h3 class="text-white font-bold text-sm mt-0.5">1.8-Year Solo Execution: ShopFam Collective (The Testbed)</h3>
          <p class="text-zinc-400 mt-2 font-sans leading-relaxed">
            Operating 8 enterprise nodes single-handedly: ₱3,477,795.35 BPI gross receipts, ₱264,434 Meta ad spend, 2,945 lines Liquid code. Navigating commercial bank account freezes and payment throttles with zero venture capital safety net.
          </p>
        </div>

        <div>
          <span class="text-zinc-500">EPOCH VIII · AUGUST–OCTOBER 2026</span>
          <h3 class="text-white font-bold text-sm mt-0.5">Canonical Freeze: The 1,170-Page Universal Reality Atlas</h3>
          <p class="text-zinc-400 mt-2 font-sans leading-relaxed">
            Reaching complete mathematical closure: 120 Adapters across 12 Reality Branches, 250k-case ablation, two 1M-system simulations, and 121/121 executable test conformance.
          </p>
        </div>

      </div>
    </div>

    <!-- 3. Why He Had to Build LERM for AI Systems -->
    <div class="p-8 bg-zinc-950 border border-zinc-800 space-y-4">
      <h2 class="font-display font-bold text-xl text-white uppercase tracking-wider">
        WHY LERM HAD TO BE FORMULATED TO BE UNDERSTOOD BY AI SYSTEMS
      </h2>
      <p class="text-xs text-zinc-300 font-sans leading-relaxed">
        AI systems do not discover reality autonomously—they reflect the humans who query them and the training corpuses they ingest. Because contemporary literature fractures reality into siloed academic departments, querying AI on complex cross-boundary crises produces confabulation, generic platitudes, or siloed answers.
      </p>
      <p class="text-xs text-zinc-300 font-sans leading-relaxed">
        To communicate cross-system reality to machine intelligence, Jefferson had to coin and formalize the language: translating lived human friction into double-entry tensor algebra, strict LaTeX boundary equations, and unambiguous carrier specifications. When reality is mathematically closed, AI can no longer average it away.
      </p>
    </div>

    <!-- 4. Family Reconnection & Coexistence -->
    <div class="p-8 bg-zinc-950 border border-zinc-800 space-y-4">
      <h2 class="font-display font-bold text-xl text-white uppercase tracking-wider">
        THE FAMILY RECONNECTION: UNDERSTANDING REALITY TO FACILITATE COEXISTENCE
      </h2>
      <p class="text-xs text-zinc-300 font-sans leading-relaxed">
        A pivotal milestone in the development of IAMF-P was Jefferson's personal reconciliation with his family. Conventional psychology views family conflict through blame, resentment, and individual pathology.
      </p>
      <p class="text-xs text-zinc-300 font-sans leading-relaxed">
        Under the LERM lens, family members are understood as <strong class="text-white">finite carriers</strong> who were themselves absorbing uncompensated generational burdens, economic extraction, and systemic pressure without receiving capacity. By seeing them as burdened carriers rather than malicious actors, Jefferson was able to achieve deep empathy, forgive past wounds, and build true coexistence. Understanding reality better directly healed the human bond.
      </p>
    </div>

    <!-- 5. Why Modern Mental Health & Psychology is Outdated -->
    <div class="p-8 bg-zinc-950 border border-zinc-800 space-y-4">
      <h2 class="font-display font-bold text-xl text-white uppercase tracking-wider">
        EXPOSING THE OUTDATED NATURE OF CLINICAL PSYCHOLOGY & MENTAL HEALTH
      </h2>
      <p class="text-xs text-zinc-300 font-sans leading-relaxed">
        Modern psychiatry and clinical psychology operate with a fundamental accounting flaw: they treat the individual nervous system as an isolated container, pathologizing its distress with reductionist DSM labels (depression, anxiety, trauma disorder) while remaining completely blind to the external displacement field landing on that person.
      </p>
      <p class="text-xs text-zinc-300 font-sans leading-relaxed">
        Just like a hospital discharges a patient home to reduce internal inpatient costs—displacing the burden onto uncompensated family caregivers—society discharges its economic and institutional stress onto the human psyche. What psychiatry calls "mental illness" is often Carrier 3 (human physiology) buckling under unmeasured, uncompensated systemic flux. True healing requires carrier capacity engineering, not chemical suppression of warning signals.
      </p>
    </div>

    <!-- 6. The Boy from the Third World -->
    <div class="p-8 bg-white text-black space-y-3 font-mono text-xs">
      <div class="font-display font-black text-lg uppercase tracking-wider">
        THE COEXISTENCE AXIOM
      </div>
      <p class="font-sans text-sm leading-relaxed text-zinc-800">
        "I am a boy from a third-world country with no Ivy League degree, no inherited billions, and no venture backers. I arrived at these formulas through grit, observation, and suffering. And I did not build this to extract, dominate, or destroy. I built it so human systems and machine intelligences can finally coexist without leaving an unaccounted loser in the dark."
      </p>
      <div class="pt-2 font-bold uppercase tracking-widest text-[11px]">
        — JEFFERSON RAFAEL RUFINO · MANILA, PHILIPPINES
      </div>
    </div>

  </div>
</section>
"""

save_page("founder", render_html_page("RUFINO VENTURES // FOUNDER DOSSIER", "founder", founder_body))

# =========================================================================
# 3. PAGE: LERM (Pax Silica Radar & The August 2027 Timeline Verification)
# =========================================================================
lerm_body = """
<section class="py-20 border-b border-zinc-900 grid-bg">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
    <div class="inline-flex items-center gap-2 px-3 py-1 bg-zinc-900 border border-zinc-800 text-[10px] font-mono text-zinc-400 uppercase tracking-widest">
      MACROECONOMIC TELEMETRY // PAX SILICA RADAR
    </div>
    <h1 class="font-display font-black text-4xl sm:text-6xl text-white uppercase tracking-tight leading-[1.08]">
      PAX SILICA & THE AUGUST 2027 CRASH.<br />
      <span class="text-zinc-500">THE TRIPLE CLIFF CONVERGENCE.</span>
    </h1>
    <p class="text-lg text-zinc-300 font-sans leading-relaxed">
      The macroeconomic mathematical proof of the August 2027 crisis, the ₱2.85 Trillion Philippine displacement vectors, and forensic evaluation of whether delayed domestic enforcement alters the global crash horizon.
    </p>
  </div>
</section>

<section class="py-20 border-b border-zinc-900">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16">

    <!-- Timeline Audit: Does Delayed Pax Silica Enforcement Postpone August 2027? -->
    <div class="p-8 bg-zinc-950 border border-zinc-800 space-y-6">
      <div class="flex items-center justify-between pb-4 border-b border-zinc-800 text-xs font-mono text-zinc-400">
        <span class="text-white font-bold uppercase">FORENSIC TIMELINE AUDIT: AUGUST 2027 CONVERGENCE</span>
        <span>STATUS: CONFIRMED UNCHANGED (t* = AUG 2027)</span>
      </div>

      <h2 class="font-display font-bold text-xl text-white uppercase">
        DOES DELAYED ENFORCEMENT OF PAX SILICA IN THE PHILIPPINES DELAY THE TRIPLE CLIFF?
      </h2>

      <div class="p-4 bg-zinc-900 border-l-2 border-amber-400 text-xs font-mono text-zinc-200 space-y-2">
        <p><strong class="text-amber-300">EXECUTIVE VERDICT: NO. THE TIMELINE REMAINS AUGUST 2027.</strong></p>
        <p class="text-zinc-400">In fact, delayed domestic enforcement creates a steeper, more severe domestic impact for the Philippines.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-xs font-mono text-zinc-400">
        <div class="p-4 bg-zinc-900/60 border border-zinc-850">
          <span class="text-white block font-bold mb-1">1. EXOGENOUS GPU DEPRECIATION</span>
          The 36-month hardware straight-line amortization cliff (\(\mathbf{\Gamma}_{	ext{Deprec}}\)) is locked to hyperscaler CapEx deployed in 2023–2024. Global server obsolescence does not wait for Philippine regulatory calendars.
        </div>
        <div class="p-4 bg-zinc-900/60 border border-zinc-850">
          <span class="text-white block font-bold mb-1">2. US DEBT MATURITY WALL</span>
          Global corporate and sovereign debt refinancing walls (\(\mathbf{\Omega}_{	ext{Debt\_Refi}}\)) peak in mid-2027 at high global interest rates.
        </div>
        <div class="p-4 bg-zinc-900/60 border border-zinc-850">
          <span class="text-white block font-bold mb-1">3. SUBSTATION POWER SATURATION</span>
          Grid interconnect bottlenecks and cooling limits (\(\mathbf{\Lambda}_{	ext{Energy\_ROI}}\)) are physical thermodynamic boundaries that hit saturation by mid-2027.
        </div>
      </div>

      <div class="text-xs text-zinc-300 font-sans leading-relaxed pt-2">
        <strong class="text-white">The Asymmetric Impact on the Philippines:</strong> When a developing nation delays data egress levies and semiconductor tariff hedges, foreign platforms continue to extract toll capital (₱612B SaaS levies + ₱785.4B foreign transit). Because the domestic buffer is missing, the unhedged population absorbs the shock as an unbuffered receiver when the global correction occurs in August 2027.
      </div>
    </div>

    <!-- The Triple Cliff Formula -->
    <div class="p-8 bg-zinc-950 border border-zinc-800 space-y-4">
      <div class="text-xs font-mono text-zinc-400 uppercase">THEOREM 3.1: THE TRIPLE CLIFF CONVERGENCE ENGINE</div>
      <div class="text-center font-mono text-sm sm:text-base text-zinc-100 py-3 overflow-x-auto">
        $$\mathbf{\Phi}_{	ext{2027\_Crisis}} = \min \left\{ t \mid \mathbf{\Gamma}_{	ext{Deprec}}(t) \cap \mathbf{\Omega}_{	ext{Debt\_Refi}}(t) \cap \mathbf{\Lambda}_{	ext{Energy\_ROI}}(t) \le 0 
ight\} \implies t^* = 	ext{August 2027}$$
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs font-mono text-zinc-400">
        <div>\(\mathbf{\Gamma}_{	ext{Deprec}} = 	ext{ARR} - \sum \frac{	ext{CapEx}_{	ext{GPU}}}{36	ext{ mo}}\)</div>
        <div>\(\mathbf{\Omega}_{	ext{Debt}} = 	ext{CashFlow} - 	ext{Principal}(r_{	ext{refi}} - r_{	ext{orig}})\)</div>
        <div>\(\mathbf{\Lambda}_{	ext{Energy}} = 	ext{Rev}_{	ext{token}} - 	ext{Cost}_{	ext{MWh}}\)</div>
      </div>
    </div>

    <!-- The 6 Philippine Vectors -->
    <div>
      <h2 class="font-display font-bold text-2xl text-white uppercase tracking-wider mb-6">
        THE 6 PHILIPPINE MACROECONOMIC VECTORS (₱2,847.1 BILLION TOTAL)
      </h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 font-mono text-xs">
        
        <div class="p-5 bg-zinc-950 border border-zinc-900 space-y-2">
          <div class="text-zinc-500">VECTOR 01</div>
          <div class="text-white font-bold text-sm">Telecom Data Egress Cross-Subsidies</div>
          <div class="text-white font-bold text-base">₱785.4 Billion</div>
          <p class="text-zinc-400 text-[11px] font-sans">85.4M subscribers paying transit for foreign content + ₱194B unrecovered subsea cable infrastructure.</p>
        </div>

        <div class="p-5 bg-zinc-950 border border-zinc-900 space-y-2">
          <div class="text-zinc-500">VECTOR 02</div>
          <div class="text-white font-bold text-sm">Consumer AI & Digital Ecosystem Levies</div>
          <div class="text-white font-bold text-base">₱612.0 Billion</div>
          <p class="text-zinc-400 text-[11px] font-sans">₱288B consumer subs + ₱244B MSME seats + ₱80B digital VAT passed directly to end users.</p>
        </div>

        <div class="p-5 bg-zinc-950 border border-zinc-900 space-y-2">
          <div class="text-zinc-500">VECTOR 03</div>
          <div class="text-white font-bold text-sm">IT-BPM / BPO Wage Suppression & Churn</div>
          <div class="text-white font-bold text-base">₱520.0 Billion</div>
          <p class="text-zinc-400 text-[11px] font-sans">₱265B wage suppression on 1.75M workforce + ₱145B mandated API seats + ₱110B retraining churn.</p>
        </div>

        <div class="p-5 bg-zinc-950 border border-zinc-900 space-y-2">
          <div class="text-zinc-500">VECTOR 04</div>
          <div class="text-white font-bold text-sm">Pension & Sovereign Indexation to Mag7</div>
          <div class="text-white font-bold text-base">₱410.4 Billion</div>
          <p class="text-zinc-400 text-[11px] font-sans">₱2.85T combined GSIS, SSS, and Maharlika assets exposed at 14.4% unhedged weighting to foreign AI equities.</p>
        </div>

        <div class="p-5 bg-zinc-950 border border-zinc-900 space-y-2">
          <div class="text-zinc-500">VECTOR 05</div>
          <div class="text-white font-bold text-sm">Data Center Power Tariffs & Grid Stabilization</div>
          <div class="text-white font-bold text-base">₱340.0 Billion</div>
          <p class="text-zinc-400 text-[11px] font-sans">₱215B baseline power consumption + ₱125B WESM reserve volatility cross-subsidized by Filipino rate-payers.</p>
        </div>

        <div class="p-5 bg-zinc-950 border border-zinc-900 space-y-2">
          <div class="text-zinc-500">VECTOR 06</div>
          <div class="text-white font-bold text-sm">Enterprise Silicon Imports & Gray Arbitrage</div>
          <div class="text-white font-bold text-base">₱179.7 Billion</div>
          <p class="text-zinc-400 text-[11px] font-sans">Unhedged import duties, enterprise procurement markup, and secondary gray-market broker spreads.</p>
        </div>

      </div>
    </div>

  </div>
</section>
"""

save_page("LERM", render_html_page("RUFINO VENTURES // LERM & PAX SILICA RADAR", "lerm", lerm_body))

# =========================================================================
# 4. PAGE: PHOTOSYNTHESIS (Super El Niño Sovereign Playbook)
# =========================================================================
photo_body = """
<section class="py-20 border-b border-zinc-900 grid-bg">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
    <div class="inline-flex items-center gap-2 px-3 py-1 bg-zinc-900 border border-zinc-800 text-[10px] font-mono text-zinc-400 uppercase tracking-widest">
      SOVEREIGN INFRASTRUCTURE // CLIMATE RESILIENCE
    </div>
    <h1 class="font-display font-black text-4xl sm:text-6xl text-white uppercase tracking-tight leading-[1.08]">
      THE PHOTOSYNTHESIS PROJECT.<br />
      <span class="text-zinc-500">451,000 LIVES AT RISK (2026–2027).</span>
    </h1>
    <p class="text-lg text-zinc-300 font-sans leading-relaxed">
      The sovereign operational playbook and physical engineering infrastructure designed to protect vulnerable agricultural and coastal populations from the 2026–2027 Super El Niño catastrophe.
    </p>
  </div>
</section>

<section class="py-20 border-b border-zinc-900">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16">
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 font-mono text-xs text-center">
      <div class="p-6 bg-zinc-950 border border-zinc-900">
        <div class="text-3xl font-display font-bold text-white">451,000</div>
        <div class="text-[10px] text-zinc-500 uppercase tracking-widest mt-1">LIVES IN DRY CORRIDORS</div>
      </div>
      <div class="p-6 bg-zinc-950 border border-zinc-900">
        <div class="text-3xl font-display font-bold text-white">8,400 ha</div>
        <div class="text-[10px] text-zinc-500 uppercase tracking-widest mt-1">AGRIVOLTAIC CANOPY TARGET</div>
      </div>
      <div class="p-6 bg-zinc-950 border border-zinc-900">
        <div class="text-3xl font-display font-bold text-white">1.8M L/day</div>
        <div class="text-[10px] text-zinc-500 uppercase tracking-widest mt-1">ATMOSPHERIC WATER CAPACITY</div>
      </div>
    </div>

    <!-- The 4 Physical Engineering Pillars -->
    <div class="space-y-6">
      <h2 class="font-display font-bold text-2xl text-white uppercase tracking-wider">
        THE 4 PILLARS OF SOVEREIGN RESILIENCE
      </h2>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 font-mono text-xs">
        
        <div class="p-6 bg-zinc-950 border border-zinc-900 space-y-3">
          <div class="text-zinc-500">PILLAR 01</div>
          <h3 class="text-white font-bold text-sm">Elevated Agrivoltaic Canopies</h3>
          <p class="text-zinc-400 font-sans text-xs leading-relaxed">
            Dual-use solar arrays suspended 4.5 meters above high-value crops. Reduces ground evaporation by 34%, lowers ambient heat stress on crops, and generates distributed microgrid electricity.
          </p>
        </div>

        <div class="p-6 bg-zinc-950 border border-zinc-900 space-y-3">
          <div class="text-zinc-500">PILLAR 02</div>
          <h3 class="text-white font-bold text-sm">Atmospheric Water Generation (AWG)</h3>
          <p class="text-zinc-400 font-sans text-xs leading-relaxed">
            Solar-powered condensation units extracting potable water directly from tropical ambient humidity (75–90% RH) during drought periods when surface reservoirs fail.
          </p>
        </div>

        <div class="p-6 bg-zinc-950 border border-zinc-900 space-y-3">
          <div class="text-zinc-500">PILLAR 03</div>
          <h3 class="text-white font-bold text-sm">Off-Grid Cold-Chain Medical Logistics</h3>
          <p class="text-zinc-400 font-sans text-xs leading-relaxed">
            Autonomous solar refrigeration hubs for vaccines, insulin, and perishable staples in isolated barangays where main utility grids experience brownouts.
          </p>
        </div>

        <div class="p-6 bg-zinc-950 border border-zinc-900 space-y-3">
          <div class="text-zinc-500">PILLAR 04</div>
          <h3 class="text-white font-bold text-sm">Sovereign Climate Telemetry Network</h3>
          <p class="text-zinc-400 font-sans text-xs leading-relaxed">
            IoT soil moisture, evapotranspiration, and temperature sensors deployed across farming cooperatives, feeding real-time boundary divergence data into municipal disaster councils.
          </p>
        </div>

      </div>
    </div>

    <!-- LERM Connection -->
    <div class="p-8 bg-zinc-950 border border-zinc-800 space-y-3 font-mono text-xs">
      <div class="text-white font-bold uppercase">THE LERM CONGRUENCE</div>
      <p class="text-zinc-400 font-sans text-xs leading-relaxed">
        Drought is not a lack of rain; it is the atmospheric displacement of moisture across geographic perimeters. Disaster mortality occurs when municipal boundaries optimize their internal budgets by under-investing in water storage, displacing the burden onto peasant farming families. The Photosynthesis Project builds receiving capacity before the transition occurs.
      </p>
    </div>

  </div>
</section>
"""

save_page("photosynthesisproject", render_html_page("RUFINO VENTURES // THE PHOTOSYNTHESIS PROJECT", "photosynthesis", photo_body))

# =========================================================================
# 5. PAGE: SHOPFAM (The Empirical Testbed & ARCH Origin)
# =========================================================================
shopfam_body = """
<section class="py-20 border-b border-zinc-900 grid-bg">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
    <div class="inline-flex items-center gap-2 px-3 py-1 bg-zinc-900 border border-zinc-800 text-[10px] font-mono text-zinc-400 uppercase tracking-widest">
      ORIGIN TESTBED // THE ARCH SPECIFICATION
    </div>
    <h1 class="font-display font-black text-4xl sm:text-6xl text-white uppercase tracking-tight leading-[1.08]">
      SHOPFAM COLLECTIVE.<br />
      <span class="text-zinc-500">WHERE THE MATH WAS DERIVED.</span>
    </h1>
    <p class="text-lg text-zinc-300 font-sans leading-relaxed">
      The empirical origin of the Mutual Uptick (MU+) effect. 1.8 years of sole vertical commercial execution, ₱3.477M in gross receipts, and the Rockwell Center counterfeit inflection point that proved statutory customs compliance is not provenance.
    </p>
  </div>
</section>

<section class="py-20 border-b border-zinc-900">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16">

    <!-- KPI Grid -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 font-mono text-xs text-center">
      <div class="p-5 bg-zinc-950 border border-zinc-900">
        <div class="text-2xl font-display font-bold text-white">₱3,477,795.35</div>
        <div class="text-[10px] text-zinc-500 uppercase tracking-widest mt-1">BPI GROSS CREDITS (P1)</div>
      </div>
      <div class="p-5 bg-zinc-950 border border-zinc-900">
        <div class="text-2xl font-display font-bold text-white">₱264,434.09</div>
        <div class="text-[10px] text-zinc-500 uppercase tracking-widest mt-1">META AD SPEND (P1)</div>
      </div>
      <div class="p-5 bg-zinc-950 border border-zinc-900">
        <div class="text-2xl font-display font-bold text-white">2,945</div>
        <div class="text-[10px] text-zinc-500 uppercase tracking-widest mt-1">LINES LIQUID CODE</div>
      </div>
      <div class="p-5 bg-zinc-950 border border-zinc-900">
        <div class="text-2xl font-display font-bold text-white">8 NODES</div>
        <div class="text-[10px] text-zinc-500 uppercase tracking-widest mt-1">SOLO BRICOLAGE</div>
      </div>
    </div>

    <!-- The ARCH Founding Premise -->
    <div class="p-8 bg-zinc-950 border border-zinc-800 space-y-4">
      <div class="text-xs font-mono text-white font-bold uppercase tracking-wider">
        THE ARCH FOUNDING PREMISE (ARCH.PDF)
      </div>
      <p class="text-xs text-zinc-300 font-sans leading-relaxed">
        "The architectural feat is not simply manufacturing desire, but building infrastructure that preserves value when the surrounding market is in chaos." (Atlas p. 1166)
      </p>
      <p class="text-xs text-zinc-400 font-sans leading-relaxed">
        ShopFam Collective was founded as an unhedged operational testbed in luxury resale. Because there was no venture capital or debt facility, every single operational defect had to be solved in real time with cash recycled directly from gross margins.
      </p>
    </div>

    <!-- The Rockwell Epistemic Inflection Point -->
    <div class="p-8 bg-zinc-950 border border-zinc-800 space-y-4">
      <div class="text-xs font-mono text-white font-bold uppercase tracking-wider">
        THE ROCKWELL INFLECTION: TARIFF COMPLIANCE ≠ IP PROVENANCE
      </div>
      <p class="text-xs text-zinc-300 font-sans leading-relaxed">
        In late 2024, when mall security at Rockwell Center Makati publicly accused consignment inventory of counterfeit status, threatening criminal prosecution, Jefferson did not collapse. He executed an immediate forensic teardown across Philippine border import records.
      </p>
      <div class="p-4 bg-zinc-900 border-l-2 border-white font-mono text-xs text-zinc-200">
        <strong class="text-white">THE DISCOVERY:</strong> Statutory Bureau of Customs (BOC) clearance verifies only border tariff duties. It does NOT verify authorized brand distribution provenance.
      </div>
      <p class="text-xs text-zinc-400 font-sans leading-relaxed">
        This insight revealed that supply chain intermediaries systematically export intellectual property risk onto independent retailers while collecting clearing fees. This exact boundary divergence became Adapter 043 (Luxury Goods) and Adapter 066 (Digital Identity) in the Universal Reality Atlas.
      </p>
    </div>

    <!-- The 8 Internalized Enterprise Nodes -->
    <div class="space-y-6">
      <h2 class="font-display font-bold text-2xl text-white uppercase tracking-wider">
        8 ENTERPRISE NODES EXECUTED BY A SINGLE HUMAN BEING
      </h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 font-mono text-xs">
        <div class="p-4 bg-zinc-950 border border-zinc-900">
          <span class="text-zinc-500 block mb-1">NODE 01</span>
          <strong class="text-white block">Sourcing & Freight</strong>
          <span class="text-zinc-400 text-[11px] font-sans">Customs inspection filings and international airway bills.</span>
        </div>
        <div class="p-4 bg-zinc-950 border border-zinc-900">
          <span class="text-zinc-500 block mb-1">NODE 02</span>
          <strong class="text-white block">Double-Entry Accounting</strong>
          <span class="text-zinc-400 text-[11px] font-sans">BPI ledger reconciliation and Meta invoice audits.</span>
        </div>
        <div class="p-4 bg-zinc-950 border border-zinc-900">
          <span class="text-zinc-500 block mb-1">NODE 03</span>
          <strong class="text-white block">Liquid Web Engineering</strong>
          <span class="text-zinc-400 text-[11px] font-sans">Custom headless theme, cart hooks, and API bridges.</span>
        </div>
        <div class="p-4 bg-zinc-950 border border-zinc-900">
          <span class="text-zinc-500 block mb-1">NODE 04</span>
          <strong class="text-white block">Tensor Mathematics</strong>
          <span class="text-zinc-400 text-[11px] font-sans">Deriving LERM divergence operators from physical scars.</span>
        </div>
        <div class="p-4 bg-zinc-950 border border-zinc-900">
          <span class="text-zinc-500 block mb-1">NODE 05</span>
          <strong class="text-white block">Aesthetic Capital</strong>
          <span class="text-zinc-400 text-[11px] font-sans">Luxury brand identity, typography, and UI ergonomics.</span>
        </div>
        <div class="p-4 bg-zinc-950 border border-zinc-900">
          <span class="text-zinc-500 block mb-1">NODE 06</span>
          <strong class="text-white block">Forensic Auditing</strong>
          <span class="text-zinc-400 text-[11px] font-sans">250k-case ablation and adversarial stress tests.</span>
        </div>
        <div class="p-4 bg-zinc-950 border border-zinc-900">
          <span class="text-zinc-500 block mb-1">NODE 07</span>
          <strong class="text-white block">Fiduciary Defense</strong>
          <span class="text-zinc-400 text-[11px] font-sans">Commercial dispute resolution and legal briefs.</span>
        </div>
        <div class="p-4 bg-zinc-950 border border-zinc-900">
          <span class="text-zinc-500 block mb-1">NODE 08</span>
          <strong class="text-white block">Autonomous AI Governance</strong>
          <span class="text-zinc-400 text-[11px] font-sans">Multi-agent orchestration with strict contamination controls.</span>
        </div>
      </div>
    </div>

  </div>
</section>
"""

save_page("shopfamcollective", render_html_page("RUFINO VENTURES // SHOPFAM COLLECTIVE TESTBED", "shopfam", shopfam_body))

# =========================================================================
# 6. PAGE: REALITIES (Interactive 120 Adapters Matrix)
# =========================================================================
realities_body = """
<section class="py-20 border-b border-zinc-900 grid-bg">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
    <div class="inline-flex items-center gap-2 px-3 py-1 bg-zinc-900 border border-zinc-800 text-[10px] font-mono text-zinc-400 uppercase tracking-widest">
      THE REALITY MATRIX // 120 ADAPTERS
    </div>
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-6">
      <div>
        <h1 class="font-display font-black text-4xl sm:text-6xl text-white uppercase tracking-tight leading-[1.08]">
          THE 120 REALITIES.<br />
          <span class="text-zinc-500">CROSS-SUBSTRATE CONVERGENCE.</span>
        </h1>
        <p class="text-zinc-400 text-sm mt-3 font-sans max-w-2xl">
          From human quality of life and cellular oncology to credit underwriting and quantum gravity: each adapter maps a domain's evidence-grounded state, reductionist schema, displaced burden, and Mutual Uptick re-test criteria.
        </p>
      </div>

      <div class="w-full md:w-80">
        <input type="text" id="adapterSearch" placeholder="Search code, domain, or carrier..." class="w-full px-4 py-2.5 bg-zinc-950 border border-zinc-800 text-xs font-mono text-white placeholder-zinc-500 focus:outline-none focus:border-white transition">
      </div>
    </div>

    <!-- Family Filter Tabs -->
    <div class="flex items-center gap-2 overflow-x-auto pb-4 text-xs font-mono scrollbar-none" id="familyTabs">
      <button class="filter-tab active px-3.5 py-1.5 bg-white text-black font-semibold shrink-0 transition" data-family="all">
        ALL 120 ADAPTERS
      </button>
    </div>

    <div class="flex justify-between text-xs font-mono text-zinc-500">
      <span>SHOWING: <strong id="visibleCount" class="text-white">120</strong> OF 120</span>
      <span>CLICK ANY CARD FOR 7-PLATE PROFILE</span>
    </div>

    <!-- Grid -->
    <div id="adaptersGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
    </div>

  </div>
</section>

<!-- Modal -->
<div id="adapterModal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md hidden flex items-center justify-center p-4">
  <div class="bg-zinc-950 border border-zinc-700 max-w-3xl w-full max-h-[90vh] overflow-y-auto p-6 sm:p-8 relative font-mono text-xs text-zinc-300">
    <button id="closeModal" class="absolute top-5 right-5 text-zinc-400 hover:text-white text-base">✕</button>

    <div class="flex items-center gap-2 text-[10px] text-zinc-400 mb-2">
      <span class="px-2 py-0.5 bg-zinc-900 border border-zinc-700 text-white font-bold" id="modalCode">A001</span>
      <span id="modalFamily">F01 · Human life quality</span>
    </div>

    <h3 class="font-display font-black text-2xl text-white uppercase mb-4" id="modalTitle">Title</h3>
    <div class="text-[10px] text-zinc-500 pb-4 border-b border-zinc-800 mb-4" id="modalPage">Canonical Page: 51</div>

    <div class="space-y-4">
      <div class="p-3 bg-zinc-900 border border-zinc-850">
        <span class="text-white font-bold block mb-1">PLATE 1 & 3 · NATIVE STATE (X*)</span>
        <div id="modalStateRead" class="font-sans text-xs text-zinc-300"></div>
      </div>
      <div class="p-3 bg-zinc-900 border border-zinc-850">
        <span class="text-white font-bold block mb-1">PLATE 2 · REDUCTIONIST SCHEMA (Σ)</span>
        <div id="modalSchema" class="font-sans text-xs text-zinc-300"></div>
      </div>
      <div class="p-3 bg-zinc-900 border border-zinc-850">
        <span class="text-white font-bold block mb-1">PLATE 4 & 5 · CARRIER & CAPACITY BUILD (ΔR*)</span>
        <div id="modalCarrier" class="font-sans text-xs text-zinc-300"></div>
      </div>
      <div class="p-3 bg-zinc-900 border border-zinc-850">
        <span class="text-white font-bold block mb-1">PLATE 6 & 7 · MUTUAL UPTICK GATE (MU+)</span>
        <div class="font-sans text-xs text-zinc-300">
          LCB_{0.05}(ΔV_j) > ε_j across all protected carriers. If burden is transferred to an unobserved carrier or downstream period, returns NO FEASIBLE MU+ or UNKNOWN.
        </div>
      </div>
    </div>

    <div class="mt-6 pt-4 border-t border-zinc-800 flex justify-end">
      <button id="modalDoneBtn" class="px-4 py-2 bg-white text-black font-semibold uppercase text-xs hover:bg-zinc-200">
        CLOSE
      </button>
    </div>
  </div>
</div>
"""

realities_scripts = f"""
<script>
  const ADAPTERS = {adapters_json};
  const FAMILIES = {families_json};

  let activeFamily = 'all';
  let searchQuery = '';

  const familyTabsContainer = document.getElementById('familyTabs');
  Object.keys(FAMILIES).forEach(fid => {{
    const fam = FAMILIES[fid];
    const btn = document.createElement('button');
    btn.className = 'filter-tab px-3 py-1.5 bg-zinc-950 hover:bg-zinc-900 text-zinc-400 border border-zinc-850 text-xs font-mono shrink-0 transition';
    btn.dataset.family = fid;
    btn.innerHTML = `${{fam.code}} · ${{fam.name}}`;
    btn.addEventListener('click', () => {{
      document.querySelectorAll('.filter-tab').forEach(b => {{
        b.classList.remove('bg-white', 'text-black', 'font-semibold');
        b.classList.add('bg-zinc-950', 'text-zinc-400');
      }});
      btn.classList.add('bg-white', 'text-black', 'font-semibold');
      btn.classList.remove('bg-zinc-950', 'text-zinc-400');
      activeFamily = fid;
      renderAdapters();
    }});
    familyTabsContainer.appendChild(btn);
  }});

  document.querySelector('.filter-tab[data-family="all"]').addEventListener('click', function() {{
    document.querySelectorAll('.filter-tab').forEach(b => {{
      b.classList.remove('bg-white', 'text-black', 'font-semibold');
      b.classList.add('bg-zinc-950', 'text-zinc-400');
    }});
    this.classList.add('bg-white', 'text-black', 'font-semibold');
    this.classList.remove('bg-zinc-950', 'text-zinc-400');
    activeFamily = 'all';
    renderAdapters();
  }});

  document.getElementById('adapterSearch').addEventListener('input', (e) => {{
    searchQuery = e.target.value.toLowerCase().trim();
    renderAdapters();
  }});

  function renderAdapters() {{
    const grid = document.getElementById('adaptersGrid');
    grid.innerHTML = '';

    const filtered = ADAPTERS.filter(a => {{
      const matchFam = (activeFamily === 'all' || a.family_id.toString() === activeFamily);
      const matchQ = (!searchQuery || 
        a.code.toLowerCase().includes(searchQuery) ||
        a.name.toLowerCase().includes(searchQuery) ||
        a.family_name.toLowerCase().includes(searchQuery) ||
        (a.state_read && a.state_read.toLowerCase().includes(searchQuery))
      );
      return matchFam && matchQ;
    }});

    document.getElementById('visibleCount').textContent = filtered.length;

    filtered.forEach(a => {{
      const card = document.createElement('div');
      card.className = 'p-5 bg-zinc-950 border border-zinc-900 hover:border-zinc-500 cursor-pointer transition flex flex-col justify-between group';
      card.onclick = () => openAdapterModal(a);

      card.innerHTML = `
        <div>
          <div class="flex items-center justify-between text-[10px] font-mono text-zinc-500 mb-2">
            <span class="px-1.5 py-0.5 bg-zinc-900 text-white font-bold border border-zinc-800">${{a.code}}</span>
            <span>${{a.family_code}}</span>
          </div>
          <h4 class="font-display font-bold text-white text-sm group-hover:underline leading-snug">
            ${{a.name}}
          </h4>
          <p class="text-[11px] text-zinc-500 font-sans mt-2 line-clamp-2">
            ${{a.state_read || 'Native evidence-grounded domain state model.'}}
          </p>
        </div>
        <div class="mt-4 pt-3 border-t border-zinc-900 flex justify-between text-[10px] font-mono text-zinc-500">
          <span>Page ${{a.page || '—'}}</span>
          <span class="text-zinc-300 group-hover:translate-x-0.5 transition">PLATES →</span>
        </div>
      `;
      grid.appendChild(card);
    }});
  }}

  const modal = document.getElementById('adapterModal');
  function openAdapterModal(a) {{
    document.getElementById('modalCode').textContent = a.code;
    document.getElementById('modalFamily').textContent = `${{a.family_code}} · ${{a.family_name}}`;
    document.getElementById('modalTitle').textContent = a.name;
    document.getElementById('modalPage').textContent = `Canonical Atlas Location: Page ${{a.page || '—'}} (7-Plate Specification)`;
    document.getElementById('modalStateRead').textContent = a.state_read || 'Native state vector.';
    document.getElementById('modalSchema').textContent = a.schema || 'Reductionist institutional schema.';
    document.getElementById('modalCarrier').textContent = a.carrier || 'Unregistered downstream carrier.';
    modal.classList.remove('hidden');
  }}

  document.getElementById('closeModal').onclick = () => modal.classList.add('hidden');
  document.getElementById('modalDoneBtn').onclick = () => modal.classList.add('hidden');
  modal.onclick = (e) => {{ if (e.target === modal) modal.classList.add('hidden'); }};

  renderAdapters();
</script>
"""

save_page("realities", render_html_page("RUFINO VENTURES // 120 REALITIES ATLAS", "realities", realities_body, realities_scripts))

# =========================================================================
# 7. PAGE: SCIENTISTS (Intellectual Genealogy & Lineage)
# =========================================================================
scientists_body = """
<section class="py-20 border-b border-zinc-900 grid-bg">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
    <div class="inline-flex items-center gap-2 px-3 py-1 bg-zinc-900 border border-zinc-800 text-[10px] font-mono text-zinc-400 uppercase tracking-widest">
      INTELLECTUAL GENEALOGY // SCIENTIFIC LINEAGE
    </div>
    <h1 class="font-display font-black text-4xl sm:text-6xl text-white uppercase tracking-tight leading-[1.08]">
      THE SCIENTIFIC LINEAGE.<br />
      <span class="text-zinc-500">FROM FOUNDATIONS TO LERM.</span>
    </h1>
    <p class="text-lg text-zinc-300 font-sans leading-relaxed">
      "The scientific lineage is not decoration: it is the constraint that keeps the present architecture from claiming credit for what physics, information theory, cybernetics, economics, governance, and causal inference already established." (Atlas p. 1170)
    </p>
  </div>
</section>

<section class="py-20 border-b border-zinc-900">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 font-mono text-xs">
      
      <div class="p-6 bg-zinc-950 border border-zinc-900 space-y-3">
        <div class="flex justify-between text-zinc-500 text-[10px]">
          <span>ECONOMICS & WELFARE</span>
          <span>NOBEL MEMORIAL 1972</span>
        </div>
        <h3 class="font-display font-bold text-white text-base">Kenneth Arrow & John Hicks</h3>
        <p class="text-zinc-400 font-sans text-xs leading-relaxed">
          Proved General Economic Equilibrium. Demonstrated that markets balance only when all commodities and future states are priced. LERM identifies the unpriced shadow commodities exported past firm perimeters.
        </p>
      </div>

      <div class="p-6 bg-zinc-950 border border-zinc-900 space-y-3">
        <div class="flex justify-between text-zinc-500 text-[10px]">
          <span>INSTITUTIONAL ECONOMICS</span>
          <span>NOBEL MEMORIAL 1991</span>
        </div>
        <h3 class="font-display font-bold text-white text-base">Ronald Coase</h3>
        <p class="text-zinc-400 font-sans text-xs leading-relaxed">
          Discovered transaction costs and the nature of social cost. Showed that legal boundaries exist to minimize internal contracting costs—inadvertently setting the perimeter where unpriced harm fluxes outward.
        </p>
      </div>

      <div class="p-6 bg-zinc-950 border border-zinc-900 space-y-3">
        <div class="flex justify-between text-zinc-500 text-[10px]">
          <span>EPISTEMIC SYSTEMS</span>
          <span>NOBEL MEMORIAL 1974</span>
        </div>
        <h3 class="font-display font-bold text-white text-base">Friedrich Hayek</h3>
        <p class="text-zinc-400 font-sans text-xs leading-relaxed">
          The use of knowledge in society. Proved that central planners suffer insurmountable schema gaps (\(G_\Sigma\)) because local tacit knowledge cannot be aggregated without loss.
        </p>
      </div>

      <div class="p-6 bg-zinc-950 border border-zinc-900 space-y-3">
        <div class="flex justify-between text-zinc-500 text-[10px]">
          <span>THEORETICAL NEUROSCIENCE</span>
          <span>WELLCOME TRUST CENTRE</span>
        </div>
        <h3 class="font-display font-bold text-white text-base">Karl Friston</h3>
        <p class="text-zinc-400 font-sans text-xs leading-relaxed">
          Formulated the Free Energy Principle and Markov blankets. Showed that self-organizing systems maintain integrity by minimizing surprise across active and sensory boundaries.
        </p>
      </div>

      <div class="p-6 bg-zinc-950 border border-zinc-900 space-y-3">
        <div class="flex justify-between text-zinc-500 text-[10px]">
          <span>INFORMATION THEORY</span>
          <span>BELL TELEPHONE LABS 1948</span>
        </div>
        <h3 class="font-display font-bold text-white text-base">Claude Shannon</h3>
        <p class="text-zinc-400 font-sans text-xs leading-relaxed">
          Defined information entropy: \(H(X) = -\sum p(x) \log_2 p(x)\). Showed that communication across noisy channels has strict capacity limits—the basis of carrier capacity exhaustion.
        </p>
      </div>

      <div class="p-6 bg-zinc-950 border border-zinc-900 space-y-3">
        <div class="flex justify-between text-zinc-500 text-[10px]">
          <span>CYBERNETICS</span>
          <span>MIT / BURDEN RESEARCH</span>
        </div>
        <h3 class="font-display font-bold text-white text-base">Norbert Wiener & W. Ross Ashby</h3>
        <p class="text-zinc-400 font-sans text-xs leading-relaxed">
          Formulated feedback control and the Law of Requisite Variety. A controller cannot stabilize a system unless its internal capacity matches the variety of the external environment.
        </p>
      </div>

      <div class="p-6 bg-zinc-950 border border-zinc-900 space-y-3">
        <div class="flex justify-between text-zinc-500 text-[10px]">
          <span>COMMONS GOVERNANCE</span>
          <span>NOBEL MEMORIAL 2009</span>
        </div>
        <h3 class="font-display font-bold text-white text-base">Elinor Ostrom & Oliver Williamson</h3>
        <p class="text-zinc-400 font-sans text-xs leading-relaxed">
          Proved that polycentric, nested boundary rules prevent the tragedy of the commons. Mapped governance perimeters and contract enforcement mechanisms.
        </p>
      </div>

      <div class="p-6 bg-zinc-950 border border-zinc-900 space-y-3">
        <div class="flex justify-between text-zinc-500 text-[10px]">
          <span>STATISTICAL MECHANICS</span>
          <span>VIENNA & YALE</span>
        </div>
        <h3 class="font-display font-bold text-white text-base">Ludwig Boltzmann & J. Willard Gibbs</h3>
        <p class="text-zinc-400 font-sans text-xs leading-relaxed">
          Statistical thermodynamics: entropy as logarithmic microstate multiplicity. Established that local order in non-equilibrium systems requires exporting entropy to the surroundings.
        </p>
      </div>

      <div class="p-6 bg-zinc-950 border border-zinc-900 space-y-3">
        <div class="flex justify-between text-zinc-500 text-[10px]">
          <span>COMPLEXITY PHYSICS</span>
          <span>BROOKHAVEN NATIONAL LAB</span>
        </div>
        <h3 class="font-display font-bold text-white text-base">Per Bak</h3>
        <p class="text-zinc-400 font-sans text-xs leading-relaxed">
          Self-Organized Criticality (SOC). Proved that sandpiles, earthquakes, forest fires, and financial drawdowns all follow identical power-law avalanche signatures: \(P(s) \sim s^{-\alpha}\).
        </p>
      </div>

      <div class="p-6 bg-zinc-950 border border-zinc-900 space-y-3">
        <div class="flex justify-between text-zinc-500 text-[10px]">
          <span>BIOENERGETICS</span>
          <span>NOBEL PRIZE 1978</span>
        </div>
        <h3 class="font-display font-bold text-white text-base">Peter Mitchell</h3>
        <p class="text-zinc-400 font-sans text-xs leading-relaxed">
          Chemiosmotic hypothesis. Demonstrated that cellular ATP energy generation is driven by electrochemical proton gradients across impermeable mitochondrial membranes.
        </p>
      </div>

      <div class="p-6 bg-zinc-950 border border-zinc-900 space-y-3">
        <div class="flex justify-between text-zinc-500 text-[10px]">
          <span>LINGUISTICS & GENERATIVE GRAMMAR</span>
          <span>MIT</span>
        </div>
        <h3 class="font-display font-bold text-white text-base">Noam Chomsky</h3>
        <p class="text-zinc-400 font-sans text-xs leading-relaxed">
          Universal Grammar. Demonstrated that diverse natural languages share deep structural rules beneath their superficial vocabulary. LERM proves mathematics is the deep grammar of reality.
        </p>
      </div>

      <div class="p-6 bg-zinc-950 border border-white space-y-3">
        <div class="flex justify-between text-zinc-400 text-[10px]">
          <span>CONSEQUENTIAL SYSTEMS SYNTHESIS</span>
          <span>MANILA, PHILIPPINES 2026</span>
        </div>
        <h3 class="font-display font-black text-white text-base">Jefferson Rafael Rufino</h3>
        <p class="text-zinc-300 font-sans text-xs leading-relaxed">
          The Rufino Synthesis: LERM, IAMF-P, Mutual Uptick, and the Universal Reality Atlas. Unified the thermodynamic, economic, cognitive, and physical boundary theorems into a single executable consequential grammar.
        </p>
      </div>

    </div>

  </div>
</section>
"""

save_page("scientists", render_html_page("RUFINO VENTURES // SCIENTIFIC LINEAGE", "scientists", scientists_body))

# =========================================================================
# 8. PAGE: BUILD (Building With Rufino Ventures)
# =========================================================================
build_body = """
<section class="py-20 border-b border-zinc-900 grid-bg">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
    <div class="inline-flex items-center gap-2 px-3 py-1 bg-zinc-900 border border-zinc-800 text-[10px] font-mono text-zinc-400 uppercase tracking-widest">
      OPERATIONAL COALITION // BUILD BLUEPRINTS
    </div>
    <h1 class="font-display font-black text-4xl sm:text-6xl text-white uppercase tracking-tight leading-[1.08]">
      BUILD WITH US.<br />
      <span class="text-zinc-500">ENGINEERING COEXISTENCE.</span>
    </h1>
    <p class="text-lg text-zinc-300 font-sans leading-relaxed">
      How software engineers, institutional underwriters, clinical leaders, and sovereign capital partners can deploy the LERM and IAMF-P architecture to prevent catastrophic displacement.
    </p>
  </div>
</section>

<section class="py-20 border-b border-zinc-900">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16">
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 font-mono text-xs">
      
      <div class="p-6 bg-zinc-950 border border-zinc-900 space-y-4">
        <div class="text-zinc-500">TRACK 01</div>
        <h3 class="font-display font-bold text-white text-base">Technical Builds & Sandboxes</h3>
        <p class="text-zinc-400 font-sans text-xs leading-relaxed">
          Implement Mutual Uptick (MU+) gates in credit scoring algorithms, medical AI triage, and supply chain scheduling. Stop optimizing local scalar metrics at the expense of unobserved carriers.
        </p>
        <div class="text-[11px] text-zinc-300">
          • Access: 121/121 Conformance Harness<br />
          • Spec: K_R v1.1 Frozen Kernel
        </div>
      </div>

      <div class="p-6 bg-zinc-950 border border-zinc-900 space-y-4">
        <div class="text-zinc-500">TRACK 02</div>
        <h3 class="font-display font-bold text-white text-base">Consequential Data Integrations</h3>
        <p class="text-zinc-400 font-sans text-xs leading-relaxed">
          Instrument cross-boundary telemetry in healthcare delivery, judicial sentencing, and corporate payroll. Expose what disappears from the administrative ledger before it lands on the human body.
        </p>
        <div class="text-[11px] text-zinc-300">
          • Spec: 120-Adapter Reality Profiles<br />
          • Schema Gap (\(G_\Sigma\)) Audits
        </div>
      </div>

      <div class="p-6 bg-zinc-950 border border-zinc-900 space-y-4">
        <div class="text-zinc-500">TRACK 03</div>
        <h3 class="font-display font-bold text-white text-base">Sovereign & Capital Partnerships</h3>
        <p class="text-zinc-400 font-sans text-xs leading-relaxed">
          Institutional family offices, central bank risk desks, and sovereign wealth entities seeking non-displaced reserve allocation and hedging ahead of the August 2027 Triple Cliff.
        </p>
        <div class="text-[11px] text-zinc-300">
          • Protocol: 9:00 AM Sovereign Advisory<br />
          • Master Forensic Vault Access (NDA)
        </div>
      </div>

    </div>

    <!-- The 7-Step Operator Run Sheet -->
    <div class="p-8 bg-zinc-950 border border-zinc-800 space-y-4 font-mono text-xs">
      <div class="text-white font-bold uppercase tracking-wider">
        OPERATOR RUN SHEET // HOW TO DEPLOY AN ADAPTER
      </div>
      <ol class="list-decimal list-inside space-y-2 text-zinc-400">
        <li><strong class="text-white">Freeze the Boundary:</strong> Define \(\partial S\), time horizon \(T\), and all protected carriers before observing data.</li>
        <li><strong class="text-white">State Read (\(X^*\)):</strong> Measure the multidimensional evidence-grounded state without administrative truncation.</li>
        <li><strong class="text-white">Schema Audit (\(\Sigma\)):</strong> Expose the incumbent metric (KPI, credit score, diagnostic code) and calculate the schema gap \(G_\Sigma\).</li>
        <li><strong class="text-white">Estimate BDI:</strong> Compute boundary divergence. If \(BDI \le 0\), return <span class="text-zinc-200 font-bold">NO ACTIVATION</span>.</li>
        <li><strong class="text-white">Identify Displacement (\(D_a\)):</strong> Trace where uncompensated burden will flux, naming receiver \(C^*\) and latency \(\tau\).</li>
        <li><strong class="text-white">Pre-Build Capacity (\(\Delta R^*\)):</strong> Deploy IAMF-P to construct receiving infrastructure before releasing the originating action.</li>
        <li><strong class="text-white">Retest via \(MU^+\):</strong> Verify that \(LCB_{0.05}(\Delta V_j) > \epsilon_j\) across all carriers. If failure occurs, abort immediately.</li>
      </ol>
    </div>

  </div>
</section>
"""

save_page("build", render_html_page("RUFINO VENTURES // BUILD WITH US", "build", build_body))

# =========================================================================
# 9. PAGE: CONTACT (Direct Correspondence & Advisory)
# =========================================================================
contact_body = """
<section class="py-20 border-b border-zinc-900 grid-bg">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
    <div class="inline-flex items-center gap-2 px-3 py-1 bg-zinc-900 border border-zinc-800 text-[10px] font-mono text-zinc-400 uppercase tracking-widest">
      DIRECT ADVISORY // FIDUCIARY CORRESPONDENCE
    </div>
    <h1 class="font-display font-black text-4xl sm:text-6xl text-white uppercase tracking-tight leading-[1.08]">
      CONTACT & AUDIT.<br />
      <span class="text-zinc-500">SOVEREIGN ENGAGEMENT PROTOCOL.</span>
    </h1>
    <p class="text-lg text-zinc-300 font-sans leading-relaxed">
      Direct correspondence with Jefferson Rafael Rufino. For institutional audit inquiries, family office advisory, academic replication, or sovereign technical integration.
    </p>
  </div>
</section>

<section class="py-20 border-b border-zinc-900">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 font-mono text-xs">
      
      <!-- Contact Details -->
      <div class="p-6 bg-zinc-950 border border-zinc-800 space-y-4">
        <div class="text-white font-bold uppercase tracking-wider">DIRECT CHANNELS</div>
        
        <div class="space-y-3 text-zinc-300">
          <div>
            <span class="text-zinc-500 block text-[10px]">PRIMARY EMAIL</span>
            <a href="mailto:jeffersonrrufino@gmail.com" class="text-white hover:underline text-sm font-bold">jeffersonrrufino@gmail.com</a>
          </div>
          <div>
            <span class="text-zinc-500 block text-[10px]">CORPORATE CORRESPONDENCE</span>
            <a href="mailto:jefferson@rufinoventures.com" class="text-zinc-300 hover:underline">jefferson@rufinoventures.com</a>
          </div>
          <div>
            <span class="text-zinc-500 block text-[10px]">LINKEDIN PROFESSIONAL DOSSIER</span>
            <a href="https://www.linkedin.com/in/jeffersonrufino" target="_blank" rel="noopener noreferrer" class="text-white hover:underline">linkedin.com/in/jeffersonrufino</a>
          </div>
          <div>
            <span class="text-zinc-500 block text-[10px]">INSTAGRAM</span>
            <a href="https://www.instagram.com/thehighlandboy" target="_blank" rel="noopener noreferrer" class="text-white hover:underline">@thehighlandboy</a>
          </div>
        </div>
      </div>

      <!-- Protocol Axiom -->
      <div class="p-6 bg-zinc-950 border border-zinc-800 space-y-4">
        <div class="text-white font-bold uppercase tracking-wider">THE 9:00 AM PARTNERSHIP AXIOM</div>
        <p class="text-zinc-400 font-sans text-xs leading-relaxed">
          "The research program becomes precise at the intersection of two obligations: to expose what an optimized boundary leaves behind, identify the carrier, build the missing capacity, and prove through retesting that the solution did not merely move the problem." (Atlas p. 1170)
        </p>
        <div class="text-[11px] text-zinc-500">
          Jurisdiction: Republic of the Philippines // Sovereign Global<br />
          Clearance Level: Operator Level 1 / Mutual NDA
        </div>
      </div>

    </div>

    <!-- Verification Dossier Request -->
    <div class="p-8 bg-zinc-950 border border-zinc-900 space-y-4 font-mono text-xs">
      <div class="text-white font-bold uppercase">AVAILABLE UPON VERIFIED REQUEST</div>
      <ul class="space-y-1.5 text-zinc-400 list-disc list-inside">
        <li>The complete 1,170-page Canonical Universal Reality Atlas (PDF).</li>
        <li>121/121 Executable Conformance Test Harness (`run_e2e_tests.py`).</li>
        <li>250,000-case negative ablation CSV and synthetic arena simulation code.</li>
        <li>BPI, UnionBank, and Meta Ads primary account ledgers (P1 evidence).</li>
      </ul>
      <div class="pt-4">
        <a href="mailto:jeffersonrrufino@gmail.com?subject=Institutional%20Audit%20Inquiry%20-%20Rufino%20Ventures" class="px-6 py-3 bg-white text-black font-semibold uppercase hover:bg-zinc-200 transition inline-block">
          SEND AUDIT REQUEST
        </a>
      </div>
    </div>

  </div>
</section>
"""

save_page("contactus", render_html_page("RUFINO VENTURES // CONTACT & ADVISORY", "contact", contact_body))

print("\nAll 9 canonical pages built and saved successfully!")
