#!/usr/bin/env python3
"""
Update RUFINOVENTURES.html and index.html to follow the exact narrative flow requested:
1. Landing Warning: 451,000 lives at risk globally, ~6,500 Filipinos.
2. Global Financial Cost: Trillions in unhedged exposure & market disruption.
3. What the World Has Now: Why passive adaptation fails & exports burden.
4. What We Bring to the Table: The Photosynthesis Catchment Node (Solar, Water, Agrivoltaics, Clinics).
5. 54 Nations Matrix & Philippine First Pilot.
6. The Rufino Synthesis Doctrine: Positive-Sum Economics & Non-Displacement.
7. Why Support the Project: Infrastructure outlives the crisis.
8. Interactive Simulator.
9. Support the Project: Email Jefferson Rufino (jeffersonrrufino@gmail.com).
"""
import os
import re

def update_html():
    base_dir = "/Users/thehighlandboy/Downloads/RUFINOVENTURES"
    index_path = os.path.join(base_dir, "index.html")

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update Title and Meta
    html = re.sub(
        r'<title>.*?</title>',
        '<title>451,000 LIVES AT RISK // THE PHOTOSYNTHESIS PROJECT & THE RUFINO SYNTHESIS</title>',
        html,
        count=1
    )

    # 2. Update Hero Section Header and Lead Copy
    old_hero_pattern = r'(<section id="hero".*?)(<h1.*?>)(.*?)(</h1>)(.*?)(<h2.*?>)(.*?)(</h2>)(.*?)(<p class="text-zinc-300.*?>)(.*?)(</p>)'
    
    new_h1 = '''<div class="inline-flex items-center gap-2 px-3.5 py-1.5 bg-red-500/10 border border-red-500/30 text-[11px] font-mono tracking-[0.25em] uppercase text-red-400 mb-6">
          <span class="w-2 h-2 rounded-full bg-red-500 animate-ping"></span>
          PLANETARY HEAT WARNING &bull; 2026–2027 SUPER EL NIÑO
        </div>
        <h1 class="text-4xl sm:text-6xl lg:text-7xl xl:text-8xl font-black uppercase tracking-tight text-white leading-[0.98] mb-6 font-display">
          451,000 LIVES ARE PROJECTED TO BE AT RISK FROM EXTREME HEAT IN THIS SUPER EL NIÑO.<br />
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-red-400 via-amber-300 to-telemetry-cyan">AROUND 6,500 OF THEM COULD BE FILIPINOS.</span>
        </h1>'''

    new_h2 = '''<h2 class="text-xl sm:text-2xl lg:text-3xl font-bold uppercase tracking-wider text-zinc-300 mb-6 font-sans">
          THE PHOTOSYNTHESIS PROJECT <span class="text-zinc-500 font-light">&bull;</span> THE RUFINO SYNTHESIS END-TO-END PLAYBOOK
        </h2>'''

    new_p = '''<p class="text-zinc-300 text-base sm:text-xl font-normal leading-relaxed max-w-4xl mb-8">
          The 2026–27 Super El Niño is not a hypothetical scenario. Climate Impact Lab models <strong>451,000 excess heat-related deaths globally</strong>, with the Philippines ranked 9th carrying <strong>6,500 ± 410 projected casualties</strong>. Conventional warnings and schedule shifts merely force citizens to supply the missing infrastructure with their own bodies, lost wages, and depleted savings. <br class="hidden sm:inline" />
          <strong>Prediction is not reconciliation.</strong> A forecast becomes a lifesaving system only when physical response capacity is built where the burden will land, faster than unresolved burden accumulates.
        </p>'''

    # Apply replacement to Hero
    hero_target = re.search(r'<section id="hero".*?</section>', html, re.DOTALL)
    if hero_target:
        hero_content = hero_target.group(0)
        
        # Replace the main text area in hero
        # Find from <p class="font-mono text-xs sm:text-sm tracking-[0.3em] text-telemetry-cyan to the CTA buttons
        hero_sub = re.sub(
            r'<p class="font-mono text-xs sm:text-sm tracking-\[0\.3em\] text-telemetry-cyan.*?</p>\s*<h1.*?>.*?</h1>\s*<h2.*?>.*?</h2>\s*<p class="text-zinc-300.*?</p>',
            f'{new_h1}\n{new_h2}\n{new_p}',
            hero_content,
            flags=re.DOTALL
        )
        html = html.replace(hero_content, hero_sub)

    # 3. Update Pane 01: The Macroeconomic & Global Financial Cost
    # Find pane-telemetry and give it the prominent "HOW MUCH IT WILL COST THE GLOBAL FINANCIAL MARKET" framing
    pane_telemetry_target = re.search(r'<section id="pane-telemetry".*?</section>', html, re.DOTALL)
    if pane_telemetry_target:
        pt_content = pane_telemetry_target.group(0)
        # Update the header in pane-telemetry
        pt_content_new = re.sub(
            r'<h2 class="text-3xl sm:text-5xl font-black text-white uppercase tracking-tight font-display mb-4">.*?</h2>',
            '<h2 class="text-3xl sm:text-5xl font-black text-white uppercase tracking-tight font-display mb-4">WHAT IT WILL COST THE GLOBAL FINANCIAL MARKET: TRILLIONS IN UNPRICED CLIMATE DEBT</h2>',
            pt_content,
            count=1
        )
        pt_content_new = re.sub(
            r'<p class="text-zinc-300 text-sm sm:text-base leading-relaxed max-w-3xl mb-8">.*?</p>',
            '<p class="text-zinc-300 text-sm sm:text-base leading-relaxed max-w-3xl mb-8">The humanitarian catastrophe is matched by catastrophic financial exposure. Crop failures cascade into food price spikes, emergency food imports, and farmer insolvencies. Extreme cooling demand triggers transformer burnouts and blackouts. WFP/FAO warns of an immediate $202M anticipatory emergency across 22 countries, but unhedged systemic losses across power, water, agriculture, and labor productivity exceed hundreds of billions of dollars. Anticipatory action yields up to $7 in avoided losses for every $1 invested.</p>',
            pt_content_new,
            count=1
        )
        html = html.replace(pt_content, pt_content_new)

    # 4. Update Pane 02: What the World Currently Has (Why Passive Adaptation Fails)
    pane_solar_target = re.search(r'<section id="pane-solar".*?</section>', html, re.DOTALL)
    if pane_solar_target:
        ps_content = pane_solar_target.group(0)
        ps_content_new = re.sub(
            r'<h2 class="text-3xl sm:text-5xl font-black text-white uppercase tracking-tight font-display mb-4">.*?</h2>',
            '<h2 class="text-3xl sm:text-5xl font-black text-white uppercase tracking-tight font-display mb-4">WHAT THE WORLD CURRENTLY HAS: PASSIVE ADAPTATION IS FAILING</h2>',
            ps_content,
            count=1
        )
        ps_content_new = re.sub(
            r'<p class="text-zinc-300 text-sm sm:text-base leading-relaxed max-w-3xl mb-8">.*?</p>',
            '<p class="text-zinc-300 text-sm sm:text-base leading-relaxed max-w-3xl mb-8">Conventional policy relies on behavioral adjustments: moving school hours earlier, telling workers to avoid midday heat, and rationing water. The problem is not that these measures are useless—it is that they treat human bodies, lost wages, and depleted family savings as the unpaid infrastructure. Running more conventional air-conditioning spikes peak electricity loads, trips grid transformers, and emits exhaust heat outdoors. We must replace passive suffering with physical catchment infrastructure: solar canopies, battery storage, and ice/chilled-water thermal storage.</p>',
            ps_content_new,
            count=1
        )
        html = html.replace(ps_content, ps_content_new)

    # 5. Update Pane 06 (pane-doctrine): Why Support The Project? (Positive-Sum Economics & The Rufino Inversion)
    pane_doctrine_target = re.search(r'<section id="pane-doctrine".*?</section>', html, re.DOTALL)
    if pane_doctrine_target:
        pd_content = pane_doctrine_target.group(0)
        pd_content_new = re.sub(
            r'<h2 class="text-3xl sm:text-5xl font-black text-white uppercase tracking-tight font-display mb-4">.*?</h2>',
            '<h2 class="text-3xl sm:text-5xl font-black text-white uppercase tracking-tight font-display mb-4">WHY SUPPORT THE PROJECT? PREVENTATIVE INFRASTRUCTURE OUTLIVES THE CRISIS</h2>',
            pd_content,
            count=1
        )
        pd_content_new = re.sub(
            r'<p class="text-zinc-300 text-sm sm:text-base leading-relaxed max-w-3xl mb-8">.*?</p>',
            '<p class="text-zinc-300 text-sm sm:text-base leading-relaxed max-w-3xl mb-8">The financing thesis of the Rufino Synthesis is simple: <strong>capture value created by prevention, not value created by catastrophe.</strong> Disaster finance traditionally pays after destruction. Anticipatory action pays before loss. The Photosynthesis Project adds a third layer: <strong>infrastructure that produces recurring commercial and fiscal value even when the disaster is absent.</strong> The key inversion: do not make a company profitable because more people suffer. Make it profitable because fewer people suffer, and the infrastructure keeps producing clean energy, water, and food for decades to come.</p>',
            pd_content_new,
            count=1
        )
        html = html.replace(pd_content, pd_content_new)

    # 6. Update Pane 09 (pane-contact): Direct Support Call to Action (Support the Project: Email Me)
    pane_contact_target = re.search(r'<section id="pane-contact".*?</section>', html, re.DOTALL)
    if pane_contact_target:
        pc_content = pane_contact_target.group(0)
        pc_content_new = re.sub(
            r'<h2 class="text-3xl sm:text-5xl lg:text-6xl font-black uppercase text-white font-display leading-tight mb-6">.*?</h2>',
            '<h2 class="text-3xl sm:text-5xl lg:text-6xl font-black uppercase text-white font-display leading-tight mb-6">TO SUPPORT THE PHOTOSYNTHESIS PROJECT:<br /><span class="text-transparent bg-clip-text bg-gradient-to-r from-telemetry-cyan via-white to-amber-400">EMAIL JEFFERSON RAFAEL RUFINO DIRECTLY</span></h2>',
            pc_content,
            count=1
        )
        pc_content_new = re.sub(
            r'<p class="text-zinc-300 text-base sm:text-xl font-normal leading-relaxed max-w-3xl mx-auto mb-10">.*?</p>',
            '<p class="text-zinc-300 text-base sm:text-xl font-normal leading-relaxed max-w-3xl mx-auto mb-10">Every week of lead time before peak Super El Niño must be converted into physical capacity that saves lives and produces enduring value. Sovereign ministers, municipal leaders, clean energy developers, agricultural cooperatives, and resilience financiers: reach out directly to fund or deploy a pilot node.</p>',
            pc_content_new,
            count=1
        )
        html = html.replace(pc_content, pc_content_new)

    # Write out to index.html and RUFINOVENTURES.html and PHOTOSYNTHESIS_PROJECT_PREVIEW.html
    for fname in ["index.html", "RUFINOVENTURES.html", "PHOTOSYNTHESIS_PROJECT_PREVIEW.html"]:
        target = os.path.join(base_dir, fname)
        with open(target, "w", encoding="utf-8") as out:
            out.write(html)
        print(f"✓ Updated {fname} ({len(html)} bytes)")

if __name__ == "__main__":
    update_html()
