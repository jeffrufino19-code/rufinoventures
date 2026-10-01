#!/usr/bin/env python3
"""
Prerenders the 8 Philippine governing bodies cards directly inside #coalition-agency-matrix
AND injects the coalition JS engine right before window.addEventListener('DOMContentLoaded'.
Guarantees the cards are 100% visible on page load with zero blank spaces!
"""

import os
import re

def patch():
    base_dir = "/Users/thehighlandboy/Downloads/RUFINOVENTURES"
    
    with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
        html = f.read()

    ph_prerender = '''      <!-- Dynamic Country Agency Matrix Container (Prerendered: Philippines) -->
      <div id="coalition-agency-matrix" class="space-y-4">
        <div class="p-6 bg-space-900/90 border border-emerald-500/40 mb-6">
          <div class="flex items-center gap-3 mb-2">
            <span class="text-2xl">🇵🇭</span>
            <h4 class="text-xl sm:text-2xl font-bold font-display text-white">PHILIPPINES // INTER-AGENCY CONVERGENCE LEDGER</h4>
          </div>
          <p class="text-zinc-300 text-xs sm:text-sm leading-relaxed">
            6,500 ± 410 Filipino lives projected at risk. PAGASA warned on Sept 23, 2026 that a historic Super El Niño is active and strengthening through 2027. Existing programs across DOST, DA, DOH, and DOE are fragmented in departmental silos. The Photosynthesis Project provides the unified physical and data backbone connecting them into one non-displacement defense.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <!-- Agency 1: DOST-PAGASA -->
          <div class="p-5 bg-space-900/80 border border-white/10 hover:border-emerald-500/50 transition flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between gap-2 mb-2">
                <span class="font-mono text-sm font-black text-white tracking-wider">DOST-PAGASA</span>
                <span class="px-2 py-0.5 border text-[9px] font-mono font-bold uppercase tracking-wider text-blue-400 border-blue-500/30 bg-blue-500/10">CLIMATE TELEMETRY &amp; ADVISORIES</span>
              </div>
              <div class="text-[11px] font-mono text-zinc-400 mb-3">Philippine Atmospheric, Geophysical and Astronomical Services Administration</div>
              <div class="space-y-3 text-xs leading-relaxed">
                <div class="p-3 bg-black/60 border border-white/5">
                  <div class="font-mono text-[10px] text-amber-400 uppercase tracking-widest font-bold mb-1">// MANDATED OPERATIONAL DIRECTIVE:</div>
                  <p class="text-zinc-300">Issue 60–90 day lead-time advisories, monitor equatorial sea-surface temperatures (RONI), forecast regional rainfall deficits, and track dangerous Wet-Bulb Globe Temperatures (WBGT).</p>
                </div>
                <div class="p-3 bg-emerald-950/20 border border-emerald-500/30">
                  <div class="font-mono text-[10px] text-emerald-400 uppercase tracking-widest font-bold mb-1">// HOW WE HELP THEM (OUR INTERVENTION):</div>
                  <p class="text-zinc-200">We connect PAGASA's predictive forecast directly into automated physical dispatch triggers—turning meteorological warnings into active cooling shelter dispatch, water generation ramp-ups, and clinic surge staffing before the heat crests.</p>
                </div>
              </div>
            </div>
            <div class="pt-2 border-t border-white/5 flex items-center justify-between font-mono text-[10px] text-zinc-500">
              <span>INTER-AGENCY SYNERGY</span>
              <a href="mailto:jeffersonrrufino@gmail.com?subject=Work%20With%20Me%20•%20Philippines%20Coalition%20(DOST-PAGASA)" class="text-emerald-400 hover:text-white transition font-bold uppercase">
                Consult on DOST-PAGASA &rarr;
              </a>
            </div>
          </div>

          <!-- Agency 2: DOH -->
          <div class="p-5 bg-space-900/80 border border-white/10 hover:border-emerald-500/50 transition flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between gap-2 mb-2">
                <span class="font-mono text-sm font-black text-white tracking-wider">DOH (Department of Health)</span>
                <span class="px-2 py-0.5 border text-[9px] font-mono font-bold uppercase tracking-wider text-red-400 border-red-500/30 bg-red-500/10">HEALTH SURGE &amp; CLINICAL DEFENSE</span>
              </div>
              <div class="text-[11px] font-mono text-zinc-400 mb-3">Department of Health &amp; Rural Health Units (RHUs)</div>
              <div class="space-y-3 text-xs leading-relaxed">
                <div class="p-3 bg-black/60 border border-white/5">
                  <div class="font-mono text-[10px] text-amber-400 uppercase tracking-widest font-bold mb-1">// MANDATED OPERATIONAL DIRECTIVE:</div>
                  <p class="text-zinc-300">Manage hospital emergency admissions, treat heat-stroke and dehydration casualties, deploy oral rehydration therapy, and monitor cardiovascular heat stress in vulnerable elderly populations.</p>
                </div>
                <div class="p-3 bg-emerald-950/20 border border-emerald-500/30">
                  <div class="font-mono text-[10px] text-emerald-400 uppercase tracking-widest font-bold mb-1">// HOW WE HELP THEM (OUR INTERVENTION):</div>
                  <p class="text-zinc-200">We install off-grid solar + battery + ice thermal storage at barangay clinics and Rural Health Units (RHUs), guaranteeing 100% cold-chain preservation for insulin, vaccines, and emergency fluids even during complete grid collapse.</p>
                </div>
              </div>
            </div>
            <div class="pt-2 border-t border-white/5 flex items-center justify-between font-mono text-[10px] text-zinc-500">
              <span>INTER-AGENCY SYNERGY</span>
              <a href="mailto:jeffersonrrufino@gmail.com?subject=Work%20With%20Me%20•%20Philippines%20Coalition%20(DOH)" class="text-emerald-400 hover:text-white transition font-bold uppercase">
                Consult on DOH &rarr;
              </a>
            </div>
          </div>

          <!-- Agency 3: DA & NIA -->
          <div class="p-5 bg-space-900/80 border border-white/10 hover:border-emerald-500/50 transition flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between gap-2 mb-2">
                <span class="font-mono text-sm font-black text-white tracking-wider">DA &amp; NIA</span>
                <span class="px-2 py-0.5 border text-[9px] font-mono font-bold uppercase tracking-wider text-amber-400 border-amber-500/30 bg-amber-500/10">AGRICULTURE &amp; IRRIGATION DEFENSE</span>
              </div>
              <div class="text-[11px] font-mono text-zinc-400 mb-3">Department of Agriculture &amp; National Irrigation Administration</div>
              <div class="space-y-3 text-xs leading-relaxed">
                <div class="p-3 bg-black/60 border border-white/5">
                  <div class="font-mono text-[10px] text-amber-400 uppercase tracking-widest font-bold mb-1">// MANDATED OPERATIONAL DIRECTIVE:</div>
                  <p class="text-zinc-300">Operate irrigation canals, distribute drought-resistant seeds, maintain solar-powered irrigation pumps, and protect domestic food harvests against severe drought.</p>
                </div>
                <div class="p-3 bg-emerald-950/20 border border-emerald-500/30">
                  <div class="font-mono text-[10px] text-emerald-400 uppercase tracking-widest font-bold mb-1">// HOW WE HELP THEM (OUR INTERVENTION):</div>
                  <p class="text-zinc-200">We deploy elevated agrivoltaic bifacial solar canopies over crops and irrigation canals. This cuts canal water evaporation by 60%+, drops microclimate heat by 1–4°C, enhances water-use efficiency by 20–47%, and provides farmers with solar power sales to offset crop stress.</p>
                </div>
              </div>
            </div>
            <div class="pt-2 border-t border-white/5 flex items-center justify-between font-mono text-[10px] text-zinc-500">
              <span>INTER-AGENCY SYNERGY</span>
              <a href="mailto:jeffersonrrufino@gmail.com?subject=Work%20With%20Me%20•%20Philippines%20Coalition%20(DA%20%26%20NIA)" class="text-emerald-400 hover:text-white transition font-bold uppercase">
                Consult on DA &amp; NIA &rarr;
              </a>
            </div>
          </div>

          <!-- Agency 4: DOE & NGCP -->
          <div class="p-5 bg-space-900/80 border border-white/10 hover:border-emerald-500/50 transition flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between gap-2 mb-2">
                <span class="font-mono text-sm font-black text-white tracking-wider">DOE &amp; NGCP</span>
                <span class="px-2 py-0.5 border text-[9px] font-mono font-bold uppercase tracking-wider text-yellow-400 border-yellow-500/30 bg-yellow-500/10">POWER GRID STABILITY &amp; RELIEF</span>
              </div>
              <div class="text-[11px] font-mono text-zinc-400 mb-3">Department of Energy &amp; National Grid Corporation of the Philippines</div>
              <div class="space-y-3 text-xs leading-relaxed">
                <div class="p-3 bg-black/60 border border-white/5">
                  <div class="font-mono text-[10px] text-amber-400 uppercase tracking-widest font-bold mb-1">// MANDATED OPERATIONAL DIRECTIVE:</div>
                  <p class="text-zinc-300">Maintain grid frequency and reserves, dispatch peaker generation, prevent cascading yellow/red alerts, and manage soaring residential cooling demand.</p>
                </div>
                <div class="p-3 bg-emerald-950/20 border border-emerald-500/30">
                  <div class="font-mono text-[10px] text-emerald-400 uppercase tracking-widest font-bold mb-1">// HOW WE HELP THEM (OUR INTERVENTION):</div>
                  <p class="text-zinc-200">Our thermal ice storage nodes and distributed solar canopies absorb massive daytime cooling loads and discharge cold stored water during 1 PM–6 PM peak hours, shaving hundreds of megawatts off grid strain and preventing transformer burnouts.</p>
                </div>
              </div>
            </div>
            <div class="pt-2 border-t border-white/5 flex items-center justify-between font-mono text-[10px] text-zinc-500">
              <span>INTER-AGENCY SYNERGY</span>
              <a href="mailto:jeffersonrrufino@gmail.com?subject=Work%20With%20Me%20•%20Philippines%20Coalition%20(DOE%20%26%20NGCP)" class="text-emerald-400 hover:text-white transition font-bold uppercase">
                Consult on DOE &amp; NGCP &rarr;
              </a>
            </div>
          </div>

          <!-- Agency 5: NWRB & Concessionaires -->
          <div class="p-5 bg-space-900/80 border border-white/10 hover:border-emerald-500/50 transition flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between gap-2 mb-2">
                <span class="font-mono text-sm font-black text-white tracking-wider">NWRB &amp; Water Concessionaires</span>
                <span class="px-2 py-0.5 border text-[9px] font-mono font-bold uppercase tracking-wider text-telemetry-cyan border-cyan-500/30 bg-cyan-500/10">WATER SECURITY &amp; AQUIFER RECHARGE</span>
              </div>
              <div class="text-[11px] font-mono text-zinc-400 mb-3">National Water Resources Board, MWSS, Maynilad, Manila Water &amp; Water Districts</div>
              <div class="space-y-3 text-xs leading-relaxed">
                <div class="p-3 bg-black/60 border border-white/5">
                  <div class="font-mono text-[10px] text-amber-400 uppercase tracking-widest font-bold mb-1">// MANDATED OPERATIONAL DIRECTIVE:</div>
                  <p class="text-zinc-300">Manage Angat Dam and regional reservoir allocations, enforce water rationing schedules, and organize emergency potable water trucking to drought-stricken communities.</p>
                </div>
                <div class="p-3 bg-emerald-950/20 border border-emerald-500/30">
                  <div class="font-mono text-[10px] text-emerald-400 uppercase tracking-widest font-bold mb-1">// HOW WE HELP THEM (OUR INTERVENTION):</div>
                  <p class="text-zinc-200">We deploy decentralized solar atmospheric water condensation hubs producing 25,000+ liters/day per cluster, dispensing free pure drinking water directly to vulnerable citizens without drawing down critically depleted reservoirs.</p>
                </div>
              </div>
            </div>
            <div class="pt-2 border-t border-white/5 flex items-center justify-between font-mono text-[10px] text-zinc-500">
              <span>INTER-AGENCY SYNERGY</span>
              <a href="mailto:jeffersonrrufino@gmail.com?subject=Work%20With%20Me%20•%20Philippines%20Coalition%20(NWRB)" class="text-emerald-400 hover:text-white transition font-bold uppercase">
                Consult on NWRB &rarr;
              </a>
            </div>
          </div>

          <!-- Agency 6: DILG & LGUs -->
          <div class="p-5 bg-space-900/80 border border-white/10 hover:border-emerald-500/50 transition flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between gap-2 mb-2">
                <span class="font-mono text-sm font-black text-white tracking-wider">DILG &amp; Local Government Units</span>
                <span class="px-2 py-0.5 border text-[9px] font-mono font-bold uppercase tracking-wider text-emerald-400 border-emerald-500/30 bg-emerald-500/10">LOCAL CITIZEN PROTECTION &amp; REFUGES</span>
              </div>
              <div class="text-[11px] font-mono text-zinc-400 mb-3">Department of the Interior and Local Government, Governors, Mayors &amp; Barangays</div>
              <div class="space-y-3 text-xs leading-relaxed">
                <div class="p-3 bg-black/60 border border-white/5">
                  <div class="font-mono text-[10px] text-amber-400 uppercase tracking-widest font-bold mb-1">// MANDATED OPERATIONAL DIRECTIVE:</div>
                  <p class="text-zinc-300">Establish local evacuation and cooling centers, enforce heat-safety workplace protocols for outdoor laborers, and protect public markets and transport terminals.</p>
                </div>
                <div class="p-3 bg-emerald-950/20 border border-emerald-500/30">
                  <div class="font-mono text-[10px] text-emerald-400 uppercase tracking-widest font-bold mb-1">// HOW WE HELP THEM (OUR INTERVENTION):</div>
                  <p class="text-zinc-200">We retrofit public markets, bus interchanges, and barangay halls into shaded, cool-roof public cooling refuges with free clean drinking water and phone charging—allowing community commerce and normal life to survive without shut-downs.</p>
                </div>
              </div>
            </div>
            <div class="pt-2 border-t border-white/5 flex items-center justify-between font-mono text-[10px] text-zinc-500">
              <span>INTER-AGENCY SYNERGY</span>
              <a href="mailto:jeffersonrrufino@gmail.com?subject=Work%20With%20Me%20•%20Philippines%20Coalition%20(DILG%20%26%20LGUs)" class="text-emerald-400 hover:text-white transition font-bold uppercase">
                Consult on DILG &amp; LGUs &rarr;
              </a>
            </div>
          </div>

          <!-- Agency 7: DepEd -->
          <div class="p-5 bg-space-900/80 border border-white/10 hover:border-emerald-500/50 transition flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between gap-2 mb-2">
                <span class="font-mono text-sm font-black text-white tracking-wider">DepEd (Department of Education)</span>
                <span class="px-2 py-0.5 border text-[9px] font-mono font-bold uppercase tracking-wider text-purple-400 border-purple-500/30 bg-purple-500/10">STUDENT &amp; TEACHER WELFARE</span>
              </div>
              <div class="text-[11px] font-mono text-zinc-400 mb-3">Department of Education &amp; School Divisions</div>
              <div class="space-y-3 text-xs leading-relaxed">
                <div class="p-3 bg-black/60 border border-white/5">
                  <div class="font-mono text-[10px] text-amber-400 uppercase tracking-widest font-bold mb-1">// MANDATED OPERATIONAL DIRECTIVE:</div>
                  <p class="text-zinc-300">Safeguard schoolchildren and educators from dangerous classroom heat, determine school cancellation thresholds, and oversee transition to distance learning.</p>
                </div>
                <div class="p-3 bg-emerald-950/20 border border-emerald-500/30">
                  <div class="font-mono text-[10px] text-emerald-400 uppercase tracking-widest font-bold mb-1">// HOW WE HELP THEM (OUR INTERVENTION):</div>
                  <p class="text-zinc-200">We apply cool-roof reflective coatings, rooftop solar microgrids, and high-efficiency cross-ventilation so classrooms remain thermally safe below 32°C WBGT—ending the cycle of cancelled classes and learning loss.</p>
                </div>
              </div>
            </div>
            <div class="pt-2 border-t border-white/5 flex items-center justify-between font-mono text-[10px] text-zinc-500">
              <span>INTER-AGENCY SYNERGY</span>
              <a href="mailto:jeffersonrrufino@gmail.com?subject=Work%20With%20Me%20•%20Philippines%20Coalition%20(DepEd)" class="text-emerald-400 hover:text-white transition font-bold uppercase">
                Consult on DepEd &rarr;
              </a>
            </div>
          </div>

          <!-- Agency 8: NDRRMC & DSWD -->
          <div class="p-5 bg-space-900/80 border border-white/10 hover:border-emerald-500/50 transition flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between gap-2 mb-2">
                <span class="font-mono text-sm font-black text-white tracking-wider">NDRRMC &amp; DSWD</span>
                <span class="px-2 py-0.5 border text-[9px] font-mono font-bold uppercase tracking-wider text-pink-400 border-pink-500/30 bg-pink-500/10">ANTICIPATORY ACTION &amp; BLENDED FINANCE</span>
              </div>
              <div class="text-[11px] font-mono text-zinc-400 mb-3">National Disaster Risk Reduction and Management Council &amp; DSWD</div>
              <div class="space-y-3 text-xs leading-relaxed">
                <div class="p-3 bg-black/60 border border-white/5">
                  <div class="font-mono text-[10px] text-amber-400 uppercase tracking-widest font-bold mb-1">// MANDATED OPERATIONAL DIRECTIVE:</div>
                  <p class="text-zinc-300">Disburse Quick Response Funds, coordinate interagency disaster relief, and distribute anticipatory cash transfers to impoverished families before loss occurs.</p>
                </div>
                <div class="p-3 bg-emerald-950/20 border border-emerald-500/30">
                  <div class="font-mono text-[10px] text-emerald-400 uppercase tracking-widest font-bold mb-1">// HOW WE HELP THEM (OUR INTERVENTION):</div>
                  <p class="text-zinc-200">We provide an auditable non-displacement ledger and positive-sum financing structure, converting emergency relief spending into permanent physical infrastructure that outlives the El Niño, delivering up to $7 in avoided losses per $1 invested.</p>
                </div>
              </div>
            </div>
            <div class="pt-2 border-t border-white/5 flex items-center justify-between font-mono text-[10px] text-zinc-500">
              <span>INTER-AGENCY SYNERGY</span>
              <a href="mailto:jeffersonrrufino@gmail.com?subject=Work%20With%20Me%20•%20Philippines%20Coalition%20(NDRRMC)" class="text-emerald-400 hover:text-white transition font-bold uppercase">
                Consult on NDRRMC &rarr;
              </a>
            </div>
          </div>
        </div>
      </div>'''

    # Replace the empty coalition-agency-matrix div
    html = re.sub(
        r'<div id="coalition-agency-matrix" class="space-y-4">.*?</div>',
        ph_prerender,
        html,
        flags=re.DOTALL
    )

    # Now make sure the coalition JavaScript data and functions are injected right before window.addEventListener('DOMContentLoaded'
    coalition_js_code = '''
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
            body: "DILG & Local Government Units",
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
                Consult on ${a.body} &rarr;
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

    # Ensure coalition_js_code is present in <script>
    if "const COALITION_DATA =" not in html:
        html = html.replace(
            "window.addEventListener('DOMContentLoaded', () => {",
            coalition_js_code + "\n    window.addEventListener('DOMContentLoaded', () => {\n      renderCoalitionCountry('PH');"
        )

    # Save to all target files
    for fname in ["index.html", "RUFINOVENTURES.html", "PHOTOSYNTHESIS_PROJECT_PREVIEW.html"]:
        target = os.path.join(base_dir, fname)
        with open(target, "w", encoding="utf-8") as out:
            out.write(html)
        print(f"✓ Successfully generated {fname} with Prerendered Coalition Cards & Engine ({len(html)} bytes)")

if __name__ == "__main__":
    patch()
