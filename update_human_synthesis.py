#!/usr/bin/env python3
"""
Convert the mathematical formulas in The Rufino Synthesis pane into deeply resonant,
simple, human principles that an elementary student can understand and care about.
"""
import os
import re

def update():
    base_dir = "/Users/thehighlandboy/Downloads/RUFINOVENTURES"
    index_path = os.path.join(base_dir, "index.html")

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # The new kid-friendly, deeply resonant Rufino Synthesis Pane
    human_synthesis_pane = '''  <!-- ========================================================================= -->
  <!-- DEDICATED PANE: THE RUFINO SYNTHESIS // SIMPLE HUMAN PRINCIPLES             -->
  <!-- Contextual HD Image: High-Tech Engineering Nexus & Pure Water Currents      -->
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
        <span class="font-mono text-xs text-amber-400 uppercase tracking-widest font-bold">SIMPLE HUMAN TRUTHS</span>
        <span class="text-zinc-600">/</span>
        <span class="font-mono text-xs text-white font-bold">THE RUFINO SYNTHESIS</span>
      </div>
      <div class="font-mono text-xs text-zinc-400 hidden sm:block">
        RULES SO CLEAR EVEN A 10-YEAR-OLD GETS IT &bull; ZERO COMPLICATED JARGON
      </div>
    </div>

    <!-- Main Content Grid -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto my-auto py-12 grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
      <div class="lg:col-span-7">
        <div class="inline-flex items-center gap-2 px-3 py-1 bg-amber-500/10 border border-amber-500/30 text-[11px] font-mono tracking-widest uppercase text-amber-400 mb-4 font-semibold">
          <span>//</span> WHY YOU SHOULD CARE ABOUT THIS
        </div>
        <h2 class="text-4xl sm:text-6xl font-black uppercase tracking-tight text-white mb-6 font-display leading-none">
          THE RUFINO <br/>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-400 via-yellow-200 to-white">SYNTHESIS</span>
        </h2>
        
        <p class="text-zinc-100 text-lg sm:text-xl leading-relaxed mb-6 font-medium max-w-2xl">
          You don't need a math degree to understand what is wrong with the world today.
        </p>

        <p class="text-zinc-300 text-sm sm:text-base leading-relaxed mb-6 max-w-2xl">
          When big disasters happen, powerful institutions usually protect their own budgets and leave the hardest hit people to suffer in silence—construction workers sweating in 45°C heat, kids dizzy in boiling classrooms, and mothers lining up for water buckets at 3 AM. 
        </p>

        <p class="text-zinc-400 text-sm sm:text-base leading-relaxed mb-8 max-w-2xl">
          The Rufino Synthesis is simply a set of <strong>four unshakeable human rules</strong> designed to stop anyone from cheating vulnerable people during a crisis:
        </p>

        <!-- The 6-Step Loop in Plain Human Terms -->
        <div class="p-4 bg-black/90 border border-amber-400/40 font-mono text-xs text-amber-300 mb-8 max-w-2xl space-y-2">
          <div class="text-zinc-400 text-[10px] tracking-widest uppercase">// OUR 6-STEP PROMISE TO EVERY COMMUNITY:</div>
          <div class="text-white font-bold tracking-wider leading-relaxed text-xs sm:text-sm">
            1. Look closely &rarr; 2. Find who's taking the hit &rarr; 3. Build real shelter &amp; water &rarr; 4. Turn the heat into clean power &rarr; 5. Give it to the people &rarr; 6. Make sure nobody was left behind.
          </div>
        </div>

        <div class="flex flex-wrap gap-4">
          <a href="#pane-origins" class="btn-spacex-white">
            READ OUR ORIGINS &amp; STORY &rarr;
          </a>
          <a href="mailto:jeffersonrrufino@gmail.com?subject=Support%20The%20Rufino%20Synthesis" class="btn-spacex-cyan">
            SUPPORT THIS VISION (EMAIL ME) &rarr;
          </a>
        </div>
      </div>

      <!-- Right Column: 4 Simple Human Rules (Elementary-Level Resonance) -->
      <div class="lg:col-span-5 space-y-4">
        
        <!-- Rule 1 -->
        <div class="hud-box p-5 border-l-4 border-l-amber-400 bg-space-900/90">
          <div class="flex items-center justify-between mb-1">
            <span class="font-mono text-[10px] uppercase tracking-widest text-amber-400 font-bold">RULE #1</span>
            <span class="font-mono text-[10px] text-zinc-500 uppercase">NO PASSING THE BUCK</span>
          </div>
          <div class="text-lg sm:text-xl font-display font-bold text-white mb-2">
            "If someone else has to suffer in secret, it's not a solution."
          </div>
          <p class="text-xs text-zinc-300 leading-relaxed">
            When a power company or government brags about "saving money" by cutting services, but outdoor workers are collapsing from heatstroke and classrooms turn into ovens, that's not savings—that's stealing safety from the weak. We make sure every hidden cost is counted.
          </p>
        </div>

        <!-- Rule 2 -->
        <div class="hud-box p-5 border-l-4 border-l-red-400 bg-space-900/90">
          <div class="flex items-center justify-between mb-1">
            <span class="font-mono text-[10px] uppercase tracking-widest text-red-400 font-bold">RULE #2</span>
            <span class="font-mono text-[10px] text-zinc-500 uppercase">THE FIREFIGHTER RULE</span>
          </div>
          <div class="text-lg sm:text-xl font-display font-bold text-white mb-2">
            "Build help faster than the danger arrives."
          </div>
          <p class="text-xs text-zinc-300 leading-relaxed">
            If a house is catching fire, you don't start inventing a fire truck after the roof falls in. Heatwaves are forecast months in advance. We put cold water, shaded hubs, and battery power in place <em>before</em> the temperature spikes, not after ambulances are full.
          </p>
        </div>

        <!-- Rule 3 -->
        <div class="hud-box p-5 border-l-4 border-l-telemetry-cyan bg-space-900/90">
          <div class="flex items-center justify-between mb-1">
            <span class="font-mono text-[10px] uppercase tracking-widest text-telemetry-cyan font-bold">RULE #3</span>
            <span class="font-mono text-[10px] text-zinc-500 uppercase">THE SUPERPOWER RULE</span>
          </div>
          <div class="text-lg sm:text-xl font-display font-bold text-white mb-2">
            "Turn the blazing sun into free power and cold water."
          </div>
          <p class="text-xs text-zinc-300 leading-relaxed">
            We don't just ask people to endure the heat. The very thing causing the emergency—intense, blazing sunlight—is also free energy. We catch that sunlight with solar roofs to make clean drinking water, chill medical clinics, and protect farm crops underneath.
          </p>
        </div>

        <!-- Rule 4 -->
        <div class="hud-box p-5 border-l-4 border-l-emerald-400 bg-space-900/90">
          <div class="flex items-center justify-between mb-1">
            <span class="font-mono text-[10px] uppercase tracking-widest text-emerald-400 font-bold">RULE #4</span>
            <span class="font-mono text-[10px] text-zinc-500 uppercase">THE PERMANENT GIFT</span>
          </div>
          <div class="text-lg sm:text-xl font-display font-bold text-white mb-2">
            "Build things that stay forever."
          </div>
          <p class="text-xs text-zinc-300 leading-relaxed">
            Most disaster aid is like a paper bandage: it disappears once the cameras leave. The solar microgrids, atmospheric water harvesters, and shaded cooling stations we build stay in your community for 25+ years—giving your kids clean water and power long after El Niño is history.
          </p>
        </div>

      </div>
    </div>

    <!-- Bottom HUD Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-t border-white/10 pt-4 font-mono text-[11px] text-zinc-500">
      <div>THE RUFINO SYNTHESIS // ETHICS, INTEGRITY, &amp; COMMUNITY SAFETY</div>
      <div class="text-zinc-400">DIRECT INQUIRIES: jeffersonrrufino@gmail.com</div>
    </div>
  </section>'''

    # Replace pane-rufino-synthesis
    html = re.sub(
        r'<section id="pane-rufino-synthesis".*?</section>',
        human_synthesis_pane,
        html,
        flags=re.DOTALL
    )

    # Save to all 3 files
    for fname in ["index.html", "RUFINOVENTURES.html", "PHOTOSYNTHESIS_PROJECT_PREVIEW.html"]:
        target = os.path.join(base_dir, fname)
        with open(target, "w", encoding="utf-8") as out:
            out.write(html)
        print(f"✓ Updated {fname} with human-readable Rufino Synthesis ({len(html)} bytes)")

if __name__ == "__main__":
    update()
