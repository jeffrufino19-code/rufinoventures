#!/usr/bin/env python3
"""
Generator for RUFINOVENTURES.html:
The Photosynthesis Project & The Rufino Synthesis
End-to-End Playbook for the 2026-27 Super El Niño
Pristine SpaceX-inspired aesthetic with high-definition contextual imagery behind every pane.
Direct all inquiries to jeffersonrrufino@gmail.com
"""

import os
import json

def build_html():
    return """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>THE PHOTOSYNTHESIS PROJECT // THE RUFINO SYNTHESIS — 2026-27 SUPER EL NIÑO PLAYBOOK</title>
  
  <!-- Meta tags for high-signal engineering clarity -->
  <meta name="description" content="The definitive SpaceX-inspired operational playbook and engineering infrastructure to protect sovereign nations from the 2026-2027 Super El Niño. Solar canopies, atmospheric water harvesting, agrivoltaics, and off-grid cold-chain medical logistics." />
  <meta name="keywords" content="Super El Nino, Photosynthesis Project, Rufino Synthesis, Agrivoltaics, Atmospheric Water Generation, Climate Telemetry, Disaster Mitigation, Jefferson Rufino" />
  <link rel="canonical" href="https://rufinoventures.com/" />
  
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://rufinoventures.com/" />
  <meta property="og:title" content="THE PHOTOSYNTHESIS PROJECT // THE RUFINO SYNTHESIS — 2026-27 SUPER EL NIÑO PLAYBOOK" />
  <meta property="og:description" content="The definitive SpaceX-inspired operational playbook and engineering infrastructure to protect sovereign nations from the 2026-2027 Super El Niño. Solar canopies, atmospheric water harvesting, agrivoltaics, and off-grid cold-chain medical logistics." />
  <meta property="og:image" content="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1200&q=80" />

  <!-- Twitter Meta -->
  <meta property="twitter:card" content="summary_large_image" />
  <meta property="twitter:url" content="https://rufinoventures.com/" />
  <meta property="twitter:title" content="THE PHOTOSYNTHESIS PROJECT // THE RUFINO SYNTHESIS — 2026-27 SUPER EL NIÑO PLAYBOOK" />
  <meta property="twitter:description" content="The definitive SpaceX-inspired operational playbook and engineering infrastructure to protect sovereign nations from the 2026-2027 Super El Niño." />
  <meta property="twitter:image" content="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1200&q=80" />

  <!-- Aerospace Telemetry Favicon -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Cpolygon points='16,2 30,9 30,23 16,30 2,23 2,9' fill='%23000000' stroke='%2300e5ff' stroke-width='2'/%3E%3Ccircle cx='16' cy='16' r='4' fill='%2300e5ff'/%3E%3C/svg%3E">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- Google Fonts: Space Grotesk, Inter, JetBrains Mono (Swiss Grotesk + Aerospace Telemetry) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700;800;900&family=Inter:wght@200;300;400;500;600;700;800;900&family=JetBrains+Mono:wght@300;400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['Geist', 'Inter', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
            display: ['Space Grotesk', 'Geist', 'sans-serif'],
          },
          colors: {
            space: {
              950: '#030305',
              900: '#07070b',
              850: '#0d0d14',
              800: '#14141e',
              700: '#1e1e2d',
            },
            telemetry: {
              cyan: '#00e5ff',
              gold: '#f59e0b',
              emerald: '#10b981',
              crimson: '#ef4444',
            }
          }
        }
      }
    }
  </script>

  <style>
    /* Base resets & SpaceX aesthetic enhancements */
    html {
      scroll-behavior: smooth;
      background-color: #030305;
      color: #e4e4e7;
    }
    body {
      font-family: 'Geist', 'Inter', -apple-system, sans-serif;
      overflow-x: hidden;
      background-color: #030305;
    }
    
    /* SpaceX high-contrast buttons */
    .btn-spacex-white {
      position: relative;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background-color: #ffffff;
      color: #000000;
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      font-size: 0.75rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      padding: 0.9rem 2rem;
      border: 1px solid #ffffff;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
    }
    .btn-spacex-white:hover {
      background-color: transparent;
      color: #ffffff;
      box-shadow: 0 0 25px rgba(255, 255, 255, 0.35);
    }

    .btn-spacex-outline {
      position: relative;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background-color: rgba(3, 3, 5, 0.6);
      backdrop-filter: blur(12px);
      color: #ffffff;
      font-family: 'JetBrains Mono', monospace;
      font-weight: 600;
      font-size: 0.75rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      padding: 0.9rem 2rem;
      border: 1px solid rgba(255, 255, 255, 0.35);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
    }
    .btn-spacex-outline:hover {
      border-color: #ffffff;
      background-color: #ffffff;
      color: #000000;
      box-shadow: 0 0 20px rgba(255, 255, 255, 0.25);
    }

    .btn-spacex-cyan {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background-color: #00e5ff;
      color: #030305;
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      font-size: 0.75rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      padding: 0.85rem 1.8rem;
      border: 1px solid #00e5ff;
      transition: all 0.2s ease;
      cursor: pointer;
    }
    .btn-spacex-cyan:hover {
      background-color: transparent;
      color: #00e5ff;
      box-shadow: 0 0 20px rgba(0, 229, 255, 0.4);
    }

    /* HUD Reticle & Corner Brackets */
    .hud-box {
      position: relative;
      background: rgba(7, 7, 11, 0.78);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.12);
    }
    .hud-box::before {
      content: '';
      position: absolute;
      top: -1px;
      left: -1px;
      width: 8px;
      height: 8px;
      border-top: 2px solid rgba(255, 255, 255, 0.8);
      border-left: 2px solid rgba(255, 255, 255, 0.8);
    }
    .hud-box::after {
      content: '';
      position: absolute;
      bottom: -1px;
      right: -1px;
      width: 8px;
      height: 8px;
      border-bottom: 2px solid rgba(255, 255, 255, 0.8);
      border-right: 2px solid rgba(255, 255, 255, 0.8);
    }

    /* Subtle grid overlay */
    .bg-grid-pattern {
      background-image: radial-gradient(rgba(255, 255, 255, 0.08) 1px, transparent 1px);
      background-size: 28px 28px;
    }

    /* Pane backdrop scrims */
    .pane-scrim {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(3, 3, 5, 0.82) 0%, rgba(3, 3, 5, 0.45) 45%, rgba(3, 3, 5, 0.88) 100%);
      pointer-events: none;
    }

    .pane-scrim-heavy {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(3, 3, 5, 0.92) 0%, rgba(3, 3, 5, 0.65) 50%, rgba(3, 3, 5, 0.96) 100%);
      pointer-events: none;
    }

    /* Animated pulse dot */
    @keyframes hudPulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.85); }
    }
    .pulse-hud {
      animation: hudPulse 2s infinite ease-in-out;
    }

    /* Custom scrollbar */
    ::-webkit-scrollbar {
      width: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #030305;
    }
    ::-webkit-scrollbar-thumb {
      background: #27272a;
      border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #52525b;
    }
  </style>
</head>
<body class="bg-space-950 text-zinc-200 antialiased selection:bg-telemetry-cyan selection:text-black">

  <!-- TOP TELEMETRY HUD BAR (STICKY) -->
  <header class="fixed top-0 left-0 right-0 z-50 bg-space-950/90 backdrop-blur-md border-b border-white/10 transition-all duration-300">
    <div class="max-w-[1720px] mx-auto px-4 sm:px-8 py-3.5 flex items-center justify-between">
      
      <!-- Brand & Mission Designation -->
      <div class="flex items-center gap-6">
        <a href="#hero" class="flex items-center gap-3 group">
          <span class="w-3 h-3 bg-white group-hover:bg-telemetry-cyan transition-colors duration-200"></span>
          <span class="font-mono font-black text-sm tracking-widest text-white uppercase">RUFINO VENTURES</span>
        </a>
        <div class="hidden lg:flex items-center gap-2 px-3 py-1 bg-white/5 border border-white/10 font-mono text-[11px] text-zinc-400">
          <span class="text-telemetry-cyan font-bold">MISSION:</span>
          <span>THE PHOTOSYNTHESIS PROJECT</span>
          <span class="text-zinc-600">//</span>
          <span class="text-zinc-300">THE RUFINO SYNTHESIS</span>
        </div>
      </div>

      <!-- Live Center Telemetry Ticker -->
      <div class="hidden xl:flex items-center gap-6 font-mono text-[11px] text-zinc-400">
        <div class="flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-red-500 pulse-hud"></span>
          <span class="text-zinc-500">ONI INDEX:</span>
          <span class="text-red-400 font-bold">+2.85°C SUPER EL NIÑO</span>
        </div>
        <span class="text-zinc-700">|</span>
        <div class="flex items-center gap-2">
          <span class="text-zinc-500">CYCLE:</span>
          <span class="text-zinc-200 font-semibold">2026–2027 WINDOW</span>
        </div>
        <span class="text-zinc-700">|</span>
        <div class="flex items-center gap-2">
          <span class="text-zinc-500">UTC CLOCK:</span>
          <span id="utc-clock" class="text-telemetry-cyan font-bold font-mono">--:--:-- UTC</span>
        </div>
      </div>

      <!-- Desktop Nav & Direct Inquiry CTA -->
      <div class="flex items-center gap-4 sm:gap-6">
        <nav class="hidden 2xl:flex items-center gap-5 font-mono text-[10.5px] uppercase tracking-wider text-zinc-400">
          <a href="#pane-telemetry" class="hover:text-white transition-colors">01 Satellite</a>
          <a href="#pane-solar" class="hover:text-white transition-colors">02 Solar Storage</a>
          <a href="#pane-agrivoltaics" class="hover:text-white transition-colors">03 Agrivoltaics</a>
          <a href="#pane-water" class="hover:text-white transition-colors">04 Water/Aquifer</a>
          <a href="#pane-medical" class="hover:text-white transition-colors">05 Cold Clinics</a>
          <a href="#pane-nations" class="hover:text-white transition-colors text-telemetry-cyan">06 54 Nations</a>
          <a href="#pane-doctrine" class="hover:text-white transition-colors">07 Synthesis</a>
          <a href="#pane-calculator" class="hover:text-white transition-colors text-amber-400 font-bold">08 Simulator</a>
        </nav>

        <a href="#pane-contact" class="btn-spacex-outline !py-2 !px-4 text-[10px] sm:text-[11px] font-mono tracking-widest border-telemetry-cyan/60 text-telemetry-cyan hover:bg-telemetry-cyan hover:text-black">
          TRANSMIT INQUIRY
        </a>

        <!-- Mobile Menu Toggle Button -->
        <button id="mobile-menu-btn" aria-label="Toggle Menu" class="2xl:hidden text-zinc-300 hover:text-white focus:outline-none p-1">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path>
          </svg>
        </button>
      </div>

    </div>

    <!-- Mobile Drawer Menu -->
    <div id="mobile-menu" class="hidden 2xl:hidden bg-space-950/98 border-b border-white/10 px-6 py-6 font-mono text-xs uppercase tracking-wider space-y-4">
      <div class="grid grid-cols-2 gap-3 text-zinc-300">
        <a href="#pane-telemetry" class="p-2 border border-white/10 hover:border-white transition block">01 Satellite Telemetry</a>
        <a href="#pane-solar" class="p-2 border border-white/10 hover:border-white transition block">02 Solar Storage</a>
        <a href="#pane-agrivoltaics" class="p-2 border border-white/10 hover:border-white transition block">03 Agrivoltaic Shield</a>
        <a href="#pane-water" class="p-2 border border-white/10 hover:border-white transition block">04 Water & Aquifer</a>
        <a href="#pane-medical" class="p-2 border border-white/10 hover:border-white transition block">05 Cold-Chain Clinics</a>
        <a href="#pane-nations" class="p-2 border border-white/10 hover:border-white transition block text-telemetry-cyan">06 54 Nations Matrix</a>
        <a href="#pane-doctrine" class="p-2 border border-white/10 hover:border-white transition block">07 Strategic Doctrine</a>
        <a href="#pane-calculator" class="p-2 border border-white/10 hover:border-white transition block text-amber-400">08 Crisis Calculator</a>
      </div>
      <div class="pt-3 border-t border-white/10 flex items-center justify-between text-[11px] text-zinc-400">
        <span>DIRECT DISPATCH:</span>
        <a href="mailto:jeffersonrrufino@gmail.com" class="text-telemetry-cyan underline">jeffersonrrufino@gmail.com</a>
      </div>
    </div>
  </header>


  <!-- ========================================================================= -->
  <!-- PANE 00: MASTER HERO VIEWPORT // SPACEX AESTHETIC FULL BLEED               -->
  <!-- Contextual HD Image: Earth Atmosphere & Ocean Thermals from Orbit          -->
  <!-- ========================================================================= -->
  <section id="hero" class="relative min-h-screen w-full flex flex-col justify-between pt-24 pb-12 px-6 sm:px-12 lg:px-20 overflow-hidden bg-space-950">
    <!-- HD Background Image -->
    <div class="absolute inset-0 z-0">
      <img 
        src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=2560&q=85" 
        alt="Orbital view of Earth atmospheric thermals" 
        class="w-full h-full object-cover object-center filter brightness-[0.75] contrast-[1.15]" 
        loading="eager"
      />
      <div class="pane-scrim"></div>
      <div class="absolute inset-0 bg-grid-pattern opacity-40"></div>
    </div>

    <!-- Top Telemetry HUD Strip -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-b border-white/15 pb-4 pt-6">
      <div class="flex items-center gap-3">
        <span class="inline-block w-2.5 h-2.5 bg-red-500 rounded-full animate-ping"></span>
        <span class="font-mono text-[11px] tracking-[0.25em] text-red-400 uppercase font-semibold">GLOBAL CLIMATE EMERGENCE // TIER 1 ALERT</span>
      </div>
      <div class="font-mono text-[11px] tracking-[0.2em] text-zinc-400 hidden sm:block">
        LAT 00°00'00" / LON 160°00'00"W &bull; EQUATORIAL PACIFIC NINO 3.4
      </div>
      <div class="font-mono text-[11px] tracking-[0.2em] text-zinc-300">
        SPEC // REV-2026.4
      </div>
    </div>

    <!-- Main Center Hero Content -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto my-auto py-12">
      <div class="max-w-5xl">
        <p class="font-mono text-xs sm:text-sm tracking-[0.3em] text-telemetry-cyan uppercase mb-4 font-semibold flex items-center gap-2">
          <span>[</span> MISSION DIRECTIVE 2026–2027 <span>]</span>
          <span class="text-zinc-400">// PLANETARY RESILIENCE ARCHITECTURE</span>
        </p>
        
        <h1 class="text-5xl sm:text-7xl lg:text-8xl font-black uppercase tracking-tight text-white leading-[0.95] mb-6 font-display">
          THE PHOTOSYNTHESIS <br class="hidden sm:inline" />
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-white via-zinc-200 to-zinc-400">PROJECT</span>
        </h1>
        
        <h2 class="text-2xl sm:text-3xl lg:text-4xl font-bold uppercase tracking-wide text-zinc-200 mb-8 font-sans">
          THE RUFINO SYNTHESIS <span class="text-zinc-500 font-light">&bull;</span> END-TO-END PLAYBOOK FOR THE 2026–27 SUPER EL NIÑO
        </h2>

        <p class="text-zinc-300 text-base sm:text-xl font-normal leading-relaxed max-w-3xl mb-10">
          The incoming 2026–2027 Super El Niño threatens 1.42 billion people across 54 equator-adjacent nations with catastrophic drought, hydroelectric grid collapses, and acute agricultural crop scorching. The Photosynthesis Project provides the world's only unified thermodynamic defense: transforming extreme planetary solar flux into decentralized megawatt power, atmospheric water generation, protected agrivoltaic biospheres, and off-grid cold-chain life support.
        </p>

        <!-- CTA Row -->
        <div class="flex flex-wrap items-center gap-4 sm:gap-6 mb-12">
          <a href="#pane-telemetry" class="btn-spacex-white">
            EXPLORE THE PLAYBOOK &darr;
          </a>
          <a href="#pane-calculator" class="btn-spacex-outline border-amber-400 text-amber-300 hover:bg-amber-400 hover:text-black">
            LAUNCH TELEMETRY SIMULATOR
          </a>
          <a href="#pane-contact" class="btn-spacex-cyan">
            ENGAGE MISSION CONTROL
          </a>
        </div>
      </div>

      <!-- Telemetry Metric Strip -->
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6 max-w-6xl mt-6">
        <div class="hud-box p-5">
          <div class="font-mono text-[10px] uppercase tracking-widest text-zinc-400 mb-1">Peak Pacific Anomaly</div>
          <div class="text-2xl sm:text-4xl font-black font-mono text-red-400">+2.85°C</div>
          <div class="font-mono text-[11px] text-zinc-500 mt-1">Exceeds 1997 & 2015 historical crests</div>
        </div>

        <div class="hud-box p-5">
          <div class="font-mono text-[10px] uppercase tracking-widest text-zinc-400 mb-1">Population in Vulnerability Belt</div>
          <div class="text-2xl sm:text-4xl font-black font-mono text-white">1.42 BILLION</div>
          <div class="font-mono text-[11px] text-zinc-500 mt-1">15°N to 15°S equatorial exposure</div>
        </div>

        <div class="hud-box p-5">
          <div class="font-mono text-[10px] uppercase tracking-widest text-zinc-400 mb-1">Target Sovereign States</div>
          <div class="text-2xl sm:text-4xl font-black font-mono text-telemetry-cyan">54 NATIONS</div>
          <div class="font-mono text-[11px] text-zinc-500 mt-1">Ranked by compound caloric deficit</div>
        </div>

        <div class="hud-box p-5">
          <div class="font-mono text-[10px] uppercase tracking-widest text-zinc-400 mb-1">Mitigated Capital Deficit</div>
          <div class="text-2xl sm:text-4xl font-black font-mono text-emerald-400">$140 BILLION</div>
          <div class="font-mono text-[11px] text-zinc-500 mt-1">Preemptive deployment vs. reactive aid</div>
        </div>
      </div>
    </div>

    <!-- Bottom Indicator -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-t border-white/10 pt-4 font-mono text-[11px] text-zinc-500">
      <div class="flex items-center gap-2">
        <span class="w-1.5 h-1.5 bg-telemetry-cyan rounded-full"></span>
        <span>EXECUTIVE DIRECTIVE: JEFFERSONRRAFAEL RUFINO</span>
      </div>
      <a href="#pane-telemetry" class="flex items-center gap-2 text-zinc-300 hover:text-white transition tracking-widest uppercase">
        <span>SCROLL TO ENGAGE PANE 01</span>
        <svg class="w-4 h-4 animate-bounce" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path></svg>
      </a>
      <div class="hidden sm:block">
        INQUIRIES: <a href="mailto:jeffersonrrufino@gmail.com" class="text-zinc-300 hover:text-telemetry-cyan transition">jeffersonrrufino@gmail.com</a>
      </div>
    </div>
  </section>


  <!-- ========================================================================= -->
  <!-- PANE 01: SATELLITE INFRARED CLIMATE TRACKING & OCEANIC TELEMETRY          -->
  <!-- Contextual HD Image: Space Observation Satellite & Pacific Orbit          -->
  <!-- ========================================================================= -->
  <section id="pane-telemetry" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-space-950 border-t border-white/10">
    <!-- HD Background Image -->
    <div class="absolute inset-0 z-0">
      <img 
        src="https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?auto=format&fit=crop&w=2560&q=85" 
        alt="Space satellite monitoring Pacific ocean climate" 
        class="w-full h-full object-cover object-center filter brightness-[0.68] contrast-[1.2]" 
        loading="lazy"
      />
      <div class="pane-scrim"></div>
    </div>

    <!-- HUD Top Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-b border-white/15 pb-4">
      <div class="flex items-center gap-3">
        <span class="font-mono text-xs text-telemetry-cyan uppercase tracking-widest font-bold">PANE 01 // TELEMETRY VECTOR</span>
        <span class="text-zinc-600">/</span>
        <span class="font-mono text-xs text-zinc-400">ORBITAL INFRARED OCEAN RECONNAISSANCE</span>
      </div>
      <div class="font-mono text-xs text-zinc-400 hidden sm:block">
        SENSOR PAYLOAD: TIR 10.5µm–12.5µm &bull; RESOLUTION: 250M
      </div>
    </div>

    <!-- Main Content Grid -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto my-auto py-12 grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
      
      <div class="lg:col-span-7">
        <p class="font-mono text-xs tracking-[0.25em] text-red-400 uppercase mb-3 font-semibold">
          THERMAL ANOMALY RADAR // 90-DAY PREEMPTIVE WARNING
        </p>
        <h2 class="text-4xl sm:text-6xl font-black uppercase tracking-tight text-white mb-6 font-display leading-none">
          REAL-TIME SATELLITE <br/>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-red-400 via-amber-300 to-white">INFRARED TRACKING</span>
        </h2>
        
        <p class="text-zinc-300 text-base sm:text-lg leading-relaxed mb-6 font-normal max-w-2xl">
          Super El Niño is an unprecedented planetary heat redistribution. As trade winds collapse along the equator, deep subsurface oceanic Kelvin waves surge eastward across the Pacific, depressing the thermocline down to 180 meters off the South American coast while leaving the Western Pacific warm pool completely desiccated.
        </p>

        <p class="text-zinc-400 text-sm sm:text-base leading-relaxed mb-8 max-w-2xl">
          The Rufino Synthesis utilizes low-earth orbit and geostationary satellite radiometry to capture multi-spectral sea surface temperature (SST) signatures. This grants sovereign governments, agricultural ministries, and utility operators a vital <strong class="text-white">90-day preemptive operational window</strong>—allowing hardware to be manufactured, shipped, and installed long before surface reservoirs dry up and seasonal crops fail.
        </p>

        <div class="flex flex-wrap gap-4">
          <button onclick="openModal('modal-telemetry')" class="btn-spacex-white">
            INSPECT SENSOR TELEMETRY &rarr;
          </button>
          <a href="#pane-solar" class="btn-spacex-outline">
            PROCEED TO SOLAR CANOPIES &darr;
          </a>
        </div>
      </div>

      <!-- Right Column: Telemetry Readouts -->
      <div class="lg:col-span-5 space-y-4">
        <div class="hud-box p-6 border-l-4 border-l-red-500">
          <div class="flex items-center justify-between mb-2">
            <span class="font-mono text-xs uppercase tracking-widest text-zinc-400">Niño 3.4 SST Thermal Anomaly</span>
            <span class="font-mono text-xs text-red-400 font-bold">CRITICAL</span>
          </div>
          <div class="text-3xl sm:text-4xl font-mono font-black text-white">+2.85°C</div>
          <p class="text-xs text-zinc-400 mt-2">
            Continuous 3-month rolling average exceeds the super-event threshold (+2.0°C), triggering automated sovereign resilience protocols.
          </p>
          <div class="w-full bg-zinc-900 h-1.5 mt-4 overflow-hidden">
            <div class="bg-gradient-to-r from-yellow-500 via-orange-500 to-red-500 h-full w-[92%]"></div>
          </div>
        </div>

        <div class="hud-box p-6 border-l-4 border-l-telemetry-cyan">
          <div class="flex items-center justify-between mb-2">
            <span class="font-mono text-xs uppercase tracking-widest text-zinc-400">Kelvin Wave Propagation Velocity</span>
            <span class="font-mono text-xs text-telemetry-cyan font-bold">TRACKING ACTIVE</span>
          </div>
          <div class="text-3xl sm:text-4xl font-mono font-black text-white">2.74 m/s</div>
          <p class="text-xs text-zinc-400 mt-2">
            Sub-surface oceanic thermal crest transiting eastward along 140°W to 90°W longitude, suppressing normal coastal upwelling.
          </p>
        </div>

        <div class="hud-box p-6 border-l-4 border-l-amber-400">
          <div class="flex items-center justify-between mb-2">
            <span class="font-mono text-xs uppercase tracking-widest text-zinc-400">Preemptive Lead Time</span>
            <span class="font-mono text-xs text-amber-400 font-bold">ACTION WINDOW</span>
          </div>
          <div class="text-3xl sm:text-4xl font-mono font-black text-white">90–120 DAYS</div>
          <p class="text-xs text-zinc-400 mt-2">
            Provides sovereign cabinets actionable lead-time to commission agrivoltaic shading, reserve water harvesting, and cold-chain hubs.
          </p>
        </div>
      </div>

    </div>

    <!-- Bottom HUD Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-t border-white/10 pt-4 font-mono text-[11px] text-zinc-500">
      <div>ORBITAL TELEMETRY DATA STREAM // SATELLITE ARRAY: GEO-18 &bull; NOAA-21 &bull; SENTINEL-3</div>
      <div class="text-zinc-400">LATENCY: 42 SECONDS &bull; REFRESH: CONTINUOUS</div>
    </div>
  </section>


  <!-- ========================================================================= -->
  <!-- PANE 02: SOLAR CANOPIES & MEGAWATT THERMAL STORAGE NODES                  -->
  <!-- Contextual HD Image: High-efficiency solar arrays under high insolation   -->
  <!-- ========================================================================= -->
  <section id="pane-solar" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-space-950 border-t border-white/10">
    <!-- HD Background Image -->
    <div class="absolute inset-0 z-0">
      <img 
        src="https://images.unsplash.com/photo-1497440001374-f26997328c1b?auto=format&fit=crop&w=2560&q=85" 
        alt="Solar photovoltaic array under intense sunlight" 
        class="w-full h-full object-cover object-center filter brightness-[0.65] contrast-[1.2]" 
        loading="lazy"
      />
      <div class="pane-scrim"></div>
    </div>

    <!-- HUD Top Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-b border-white/15 pb-4">
      <div class="flex items-center gap-3">
        <span class="font-mono text-xs text-amber-400 uppercase tracking-widest font-bold">PANE 02 // ENERGY VECTOR</span>
        <span class="text-zinc-600">/</span>
        <span class="font-mono text-xs text-zinc-400">THERMODYNAMIC SOLAR HARVESTING & STORAGE</span>
      </div>
      <div class="font-mono text-xs text-zinc-400 hidden sm:block">
        PEAK IRRADIANCE: 1,380 W/m² &bull; CELL EFFICIENCY: 24.8% BIFACIAL
      </div>
    </div>

    <!-- Main Content Grid -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto my-auto py-12 grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
      
      <div class="lg:col-span-7">
        <p class="font-mono text-xs tracking-[0.25em] text-amber-400 uppercase mb-3 font-semibold">
          GRID RESILIENCE ARCHITECTURE // ZERO-EMISSION BASELOAD
        </p>
        <h2 class="text-4xl sm:text-6xl font-black uppercase tracking-tight text-white mb-6 font-display leading-none">
          MEGAWATT SOLAR CANOPIES & <br/>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-400 via-yellow-200 to-white">THERMAL STORAGE NODES</span>
        </h2>
        
        <p class="text-zinc-300 text-base sm:text-lg leading-relaxed mb-6 font-normal max-w-2xl">
          Super El Niño produces persistent high-pressure atmospheric heat domes with lethal cloudless insolation. While conventional municipal grids falter as hydroelectric dams run dry, The Rufino Synthesis treats this extreme solar flux as a high-density primary asset.
        </p>

        <p class="text-zinc-400 text-sm sm:text-base leading-relaxed mb-8 max-w-2xl">
          We deploy modular bifacial solar canopies across water reservoirs, irrigation canals, and industrial corridors. Paired with phase-change thermal storage batteries and containerized Lithium-Iron-Phosphate (LFP) banks, these nodes generate 24/7 dispatchable power to run municipal water pumps, cold clinics, and agricultural chillers—completely immune to nationwide blackouts.
        </p>

        <div class="flex flex-wrap gap-4">
          <button onclick="openModal('modal-solar')" class="btn-spacex-white">
            VIEW ENGINEERING BLUEPRINT &rarr;
          </button>
          <a href="#pane-agrivoltaics" class="btn-spacex-outline">
            ADVANCE TO AGRIVOLTAICS &darr;
          </a>
        </div>
      </div>

      <!-- Right Column: Technical Spec Cards -->
      <div class="lg:col-span-5 space-y-4">
        <div class="hud-box p-6 border-l-4 border-l-amber-400">
          <div class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-1">Modular Deployable Microgrid</div>
          <div class="text-3xl sm:text-4xl font-mono font-black text-white">850 MW</div>
          <p class="text-xs text-zinc-400 mt-2">
            Scalable containerized solar-storage cluster deployable within 45 days along vulnerable grid corridors.
          </p>
        </div>

        <div class="hud-box p-6 border-l-4 border-l-telemetry-cyan">
          <div class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-1">Reservoir Evaporation Reduction</div>
          <div class="text-3xl sm:text-4xl font-mono font-black text-telemetry-cyan">62% SAVED</div>
          <p class="text-xs text-zinc-400 mt-2">
            Floating canopy deployment (Floatovoltaics) physically shades municipal reservoirs, saving hundreds of millions of liters of potable water.
          </p>
        </div>

        <div class="hud-box p-6 border-l-4 border-l-emerald-400">
          <div class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-1">Thermal Phase-Change Reserve</div>
          <div class="text-3xl sm:text-4xl font-mono font-black text-white">72-HOUR BUFFER</div>
          <p class="text-xs text-zinc-400 mt-2">
            Molten-salt and latent heat PCM thermal storage provides uninterrupted cooling power even during catastrophic grid outages.
          </p>
        </div>
      </div>

    </div>

    <!-- Bottom HUD Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-t border-white/10 pt-4 font-mono text-[11px] text-zinc-500">
      <div>DEPLOYMENT SPECIFICATION: PHOTOVOLTAIC BIFACIAL HETEROJUNCTION &bull; INVERTER: GRID-FORMING SOLID STATE</div>
      <div class="text-zinc-400">BLACK-START CERTIFIED // ZERO DIESEL LOGISTICS</div>
    </div>
  </section>


  <!-- ========================================================================= -->
  <!-- PANE 03: AGRIVOLTAICS & DROUGHT-RESILIENT BIOSPHERE AGRICULTURE           -->
  <!-- Contextual HD Image: High-tech greenhouse & agrivoltaic crops             -->
  <!-- ========================================================================= -->
  <section id="pane-agrivoltaics" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-space-950 border-t border-white/10">
    <!-- HD Background Image -->
    <div class="absolute inset-0 z-0">
      <img 
        src="https://images.unsplash.com/photo-1595974482597-4b8da8879bc5?auto=format&fit=crop&w=2560&q=85" 
        alt="Agrivoltaics elevated solar panels over agricultural crops" 
        class="w-full h-full object-cover object-center filter brightness-[0.62] contrast-[1.25]" 
        loading="lazy"
      />
      <div class="pane-scrim"></div>
    </div>

    <!-- HUD Top Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-b border-white/15 pb-4">
      <div class="flex items-center gap-3">
        <span class="font-mono text-xs text-emerald-400 uppercase tracking-widest font-bold">PANE 03 // BIOSPHERE VECTOR</span>
        <span class="text-zinc-600">/</span>
        <span class="font-mono text-xs text-zinc-400">CLIMATE-PROOF AGRIVOLTAIC FOOD PRODUCTION</span>
      </div>
      <div class="font-mono text-xs text-zinc-400 hidden sm:block">
        SOIL MOISTURE RETENTION: +42% &bull; CANOPY CLEARANCE: 3.8M
      </div>
    </div>

    <!-- Main Content Grid -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto my-auto py-12 grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
      
      <div class="lg:col-span-7">
        <p class="font-mono text-xs tracking-[0.25em] text-emerald-400 uppercase mb-3 font-semibold">
          STAPLE CROP PROTECTION // PHOTOSYNTHETIC PRESERVATION
        </p>
        <h2 class="text-4xl sm:text-6xl font-black uppercase tracking-tight text-white mb-6 font-display leading-none">
          AGRIVOLTAIC CANOPIES & <br/>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 via-teal-200 to-white">DROUGHT-PROOF CROPS</span>
        </h2>
        
        <p class="text-zinc-300 text-base sm:text-lg leading-relaxed mb-6 font-normal max-w-2xl">
          When ambient temperatures exceed 36°C, plant stomata close to prevent desiccation—shutting down natural photosynthesis and destroying yields across rice, maize, cassava, and vegetable staples. Open-field farming collapses during Super El Niño events.
        </p>

        <p class="text-zinc-400 text-sm sm:text-base leading-relaxed mb-8 max-w-2xl">
          The Photosynthesis Project solves this by mounting elevated bifacial solar canopies 3.8 meters above active arable land. This generates an engineered microclimate that reduces ground temperature by 5.2°C, slashes soil evapotranspiration by 42%, and powers automated sub-surface pulsed drip irrigation that preserves agricultural yield while generating exportable clean electricity.
        </p>

        <div class="flex flex-wrap gap-4">
          <button onclick="openModal('modal-agri')" class="btn-spacex-white">
            INSPECT AGRIVOLTAIC SCHEMATICS &rarr;
          </button>
          <a href="#pane-water" class="btn-spacex-outline">
            PROCEED TO WATER HARVESTING &darr;
          </a>
        </div>
      </div>

      <!-- Right Column: Agronomic Data -->
      <div class="lg:col-span-5 space-y-4">
        <div class="hud-box p-6 border-l-4 border-l-emerald-400">
          <div class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-1">Microclimate Temperature Delta</div>
          <div class="text-3xl sm:text-4xl font-mono font-black text-emerald-400">-5.2°C UNDER CANOPY</div>
          <p class="text-xs text-zinc-400 mt-2">
            Prevents thermal leaf scorching and maintains active enzymatic photosynthesis during midday solar radiation peaks.
          </p>
        </div>

        <div class="hud-box p-6 border-l-4 border-l-telemetry-cyan">
          <div class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-1">Agricultural Irrigation Savings</div>
          <div class="text-3xl sm:text-4xl font-mono font-black text-white">48% LESS WATER</div>
          <p class="text-xs text-zinc-400 mt-2">
            Sub-surface precision drip delivery combined with mycorrhizal biochar ensures zero irrigation water is lost to surface evaporation.
          </p>
        </div>

        <div class="hud-box p-6 border-l-4 border-l-amber-400">
          <div class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-1">Dual-Output Yield Multiplier</div>
          <div class="text-3xl sm:text-4xl font-mono font-black text-white">120 kWh/HA/DAY</div>
          <p class="text-xs text-zinc-400 mt-2">
            Guarantees 92% baseline caloric yield retention while transforming smallholder farming plots into distributed power generation hubs.
          </p>
        </div>
      </div>

    </div>

    <!-- Bottom HUD Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-t border-white/10 pt-4 font-mono text-[11px] text-zinc-500">
      <div>CROPPING SYSTEMS: CASSAVA &bull; UPLAND RICE &bull; SORGHUM &bull; SWEET POTATO &bull; HIGH-VALUE VEGETABLES</div>
      <div class="text-zinc-400">WIND LOAD RATED: 240 KM/H (CATEGORY 5 CYCLONE RESISTANT)</div>
    </div>
  </section>


  <!-- ========================================================================= -->
  <!-- PANE 04: ATMOSPHERIC WATER GENERATION, HYPERFILTRATION & AQUIFER RECHARGE -->
  <!-- Contextual HD Image: High-purity water currents & hydrodynamics           -->
  <!-- ========================================================================= -->
  <section id="pane-water" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-space-950 border-t border-white/10">
    <!-- HD Background Image -->
    <div class="absolute inset-0 z-0">
      <img 
        src="https://images.unsplash.com/photo-1518837695005-2083093ee35b?auto=format&fit=crop&w=2560&q=85" 
        alt="Pure water currents symbolizing atmospheric harvesting and deep aquifer injection" 
        class="w-full h-full object-cover object-center filter brightness-[0.62] contrast-[1.25]" 
        loading="lazy"
      />
      <div class="pane-scrim"></div>
    </div>

    <!-- HUD Top Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-b border-white/15 pb-4">
      <div class="flex items-center gap-3">
        <span class="font-mono text-xs text-telemetry-cyan uppercase tracking-widest font-bold">PANE 04 // HYDROLOGICAL VECTOR</span>
        <span class="text-zinc-600">/</span>
        <span class="font-mono text-xs text-zinc-400">CLOSED-LOOP ATMOSPHERIC EXTRACTION & AQUIFER BANKING</span>
      </div>
      <div class="font-mono text-xs text-zinc-400 hidden sm:block">
        CONDENSATION YIELD: 50,000 L/DAY/POD &bull; PURITY: WHO / ISO 24510
      </div>
    </div>

    <!-- Main Content Grid -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto my-auto py-12 grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
      
      <div class="lg:col-span-7">
        <p class="font-mono text-xs tracking-[0.25em] text-telemetry-cyan uppercase mb-3 font-semibold">
          ZERO-DEPLETION HYDROLOGY // SUBTERRANEAN STRATEGIC RESERVES
        </p>
        <h2 class="text-4xl sm:text-6xl font-black uppercase tracking-tight text-white mb-6 font-display leading-none">
          ATMOSPHERIC WATER & <br/>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-telemetry-cyan via-blue-200 to-white">DEEP AQUIFER RECHARGE</span>
        </h2>
        
        <p class="text-zinc-300 text-base sm:text-lg leading-relaxed mb-6 font-normal max-w-2xl">
          Even during the most punishing tropical El Niño droughts, the atmosphere contains massive volumes of precipitable moisture. High ambient air temperatures increase moisture-holding capacity, creating an invisible, inexhaustible ocean in the sky.
        </p>

        <p class="text-zinc-400 text-sm sm:text-base leading-relaxed mb-8 max-w-2xl">
          The Rufino Synthesis deploys containerized industrial Atmospheric Water Generators (AWG) operating on solid-state desiccant wheels and thermodynamic condensation, powered 100% by daytime solar overproduction. Excess potable yields are pressurized directly into deep subterranean aquifer boreholes (120m–300m)—banking millions of cubic meters safely underground away from the desiccating surface atmosphere.
        </p>

        <div class="flex flex-wrap gap-4">
          <button onclick="openModal('modal-water')" class="btn-spacex-white">
            VIEW HYDRO-INJECTION BLUEPRINT &rarr;
          </button>
          <a href="#pane-medical" class="btn-spacex-outline">
            PROCEED TO COLD-CHAIN CLINICS &darr;
          </a>
        </div>
      </div>

      <!-- Right Column: Hydrological Data -->
      <div class="lg:col-span-5 space-y-4">
        <div class="hud-box p-6 border-l-4 border-l-telemetry-cyan">
          <div class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-1">Standard AWG Module Capacity</div>
          <div class="text-3xl sm:text-4xl font-mono font-black text-telemetry-cyan">50,000 L / DAY</div>
          <p class="text-xs text-zinc-400 mt-2">
            ISO-40ft containerized units producing medical-grade potable water directly from 60–90% ambient relative humidity air.
          </p>
        </div>

        <div class="hud-box p-6 border-l-4 border-l-emerald-400">
          <div class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-1">Deep Subterranean Water Banking</div>
          <div class="text-3xl sm:text-4xl font-mono font-black text-white">300M INJECTION</div>
          <p class="text-xs text-zinc-400 mt-2">
            Managed Aquifer Recharge (MAR) wells prevent 100% of the surface reservoir evaporation that destroys conventional municipal dams.
          </p>
        </div>

        <div class="hud-box p-6 border-l-4 border-l-amber-400">
          <div class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-1">Brackish & Seawater Hyperfiltration</div>
          <div class="text-3xl sm:text-4xl font-mono font-black text-white">0.0001µm MEMBRANE</div>
          <p class="text-xs text-zinc-400 mt-2">
            Solar-powered reverse osmosis skid systems neutralizing coastal salinity intrusion across river deltas and island aquifers.
          </p>
        </div>
      </div>

    </div>

    <!-- Bottom HUD Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-t border-white/10 pt-4 font-mono text-[11px] text-zinc-500">
      <div>FILTRATION: ULTRAFILTRATION &bull; ACTIVATED CARBON &bull; UV-C DISINFECTION &bull; MINERAL RE-BALANCE</div>
      <div class="text-zinc-400">INSPECTION STANDARD: WHO GUIDELINES FOR DRINKING-WATER QUALITY (4TH ED)</div>
    </div>
  </section>


  <!-- ========================================================================= -->
  <!-- PANE 05: EMERGENCY COLD-CHAIN MEDICAL LOGISTICS & PASSIVE-COOLING CLINICS  -->
  <!-- Contextual HD Image: High-tech emergency cleanroom and medical logistics  -->
  <!-- ========================================================================= -->
  <section id="pane-medical" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-space-950 border-t border-white/10">
    <!-- HD Background Image -->
    <div class="absolute inset-0 z-0">
      <img 
        src="https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?auto=format&fit=crop&w=2560&q=85" 
        alt="Sterile high-tech emergency medical cold-chain logistics" 
        class="w-full h-full object-cover object-center filter brightness-[0.62] contrast-[1.25]" 
        loading="lazy"
      />
      <div class="pane-scrim"></div>
    </div>

    <!-- HUD Top Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-b border-white/15 pb-4">
      <div class="flex items-center gap-3">
        <span class="font-mono text-xs text-red-400 uppercase tracking-widest font-bold">PANE 05 // LIFE SUPPORT VECTOR</span>
        <span class="text-zinc-600">/</span>
        <span class="font-mono text-xs text-zinc-400">COLD-CHAIN MEDICAL LOGISTICS & HEATSTROKE TRIAGE</span>
      </div>
      <div class="font-mono text-xs text-zinc-400 hidden sm:block">
        TEMPERATURE ENVELOPE: +2.0°C TO +8.0°C &bull; AEROGEL THERMAL SHIELD
      </div>
    </div>

    <!-- Main Content Grid -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto my-auto py-12 grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
      
      <div class="lg:col-span-7">
        <p class="font-mono text-xs tracking-[0.25em] text-red-400 uppercase mb-3 font-semibold">
          CRITICAL PHARMACEUTICAL STABILIZATION // HYPERTHERMIA DEFENSE
        </p>
        <h2 class="text-4xl sm:text-6xl font-black uppercase tracking-tight text-white mb-6 font-display leading-none">
          EMERGENCY COLD-CHAIN & <br/>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-red-400 via-rose-200 to-white">OFF-GRID FIELD CLINICS</span>
        </h2>
        
        <p class="text-zinc-300 text-base sm:text-lg leading-relaxed mb-6 font-normal max-w-2xl">
          During wet-bulb temperature spikes above 31°C, human mortality spikes exponentially and power grids crash under cooling loads. When grids black out, essential supplies—insulin, pediatric vaccines, oxytocin, snakebite antivenom, and blood products—spoil within hours.
        </p>

        <p class="text-zinc-400 text-sm sm:text-base leading-relaxed mb-8 max-w-2xl">
          The Photosynthesis Project delivers rapid-deploy ISO field clinics equipped with vacuum-insulated aerogel panels and phase-change salt cooling cells. Operating 100% off-grid with dedicated rooftop solar, each unit preserves critical pharmaceuticals at a rock-solid +2°C to +8°C for 72 continuous hours without sunlight, while providing negative-pressure cooling chambers to treat acute heatstroke casualties.
        </p>

        <div class="flex flex-wrap gap-4">
          <button onclick="openModal('modal-medical')" class="btn-spacex-white">
            EXPLORE CLINIC SPECIFICATION &rarr;
          </button>
          <a href="#pane-nations" class="btn-spacex-outline">
            VIEW 54 NATIONS MATRIX &darr;
          </a>
        </div>
      </div>

      <!-- Right Column: Medical Infrastructure Metrics -->
      <div class="lg:col-span-5 space-y-4">
        <div class="hud-box p-6 border-l-4 border-l-red-500">
          <div class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-1">Cold-Chain Temperature Stability</div>
          <div class="text-3xl sm:text-4xl font-mono font-black text-white">+2°C TO +8°C</div>
          <p class="text-xs text-zinc-400 mt-2">
            Zero-electricity thermal holding capacity for 72 hours via vacuum insulated panels (VIP) and latent heat eutectic reservoirs.
          </p>
        </div>

        <div class="hud-box p-6 border-l-4 border-l-telemetry-cyan">
          <div class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-1">Acute Heatstroke Resuscitation</div>
          <div class="text-3xl sm:text-4xl font-mono font-black text-telemetry-cyan">&lt; 18 MIN COOLING</div>
          <p class="text-xs text-zinc-400 mt-2">
            Chilled saline infusion suites and conductive evaporative cooling beds rapidly reverse lethal core hyperthermia from 41°C to safe levels.
          </p>
        </div>

        <div class="hud-box p-6 border-l-4 border-l-emerald-400">
          <div class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-1">Triage Throughput Per Mobile Pod</div>
          <div class="text-3xl sm:text-4xl font-mono font-black text-white">250 PATIENTS/DAY</div>
          <p class="text-xs text-zinc-400 mt-2">
            Includes autonomous solar oxygen generation, clinical illumination, and satellite telemedicine uplinks to central medical ministries.
          </p>
        </div>
      </div>

    </div>

    <!-- Bottom HUD Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-t border-white/10 pt-4 font-mono text-[11px] text-zinc-500">
      <div>CERTIFICATION: WHO PQS PREQUALIFIED &bull; THERMAL SHIELD: SILICA AEROGEL (λ = 0.015 W/m·K)</div>
      <div class="text-zinc-400">LOGISTICS FOOTPRINT: ISO 20FT / 40FT INTERMODAL COMPATIBLE</div>
    </div>
  </section>


  <!-- ========================================================================= -->
  <!-- PANE 06: GLOBAL HEATMAP VULNERABILITY MATRIX & 54 EQUATOR-ADJACENT NATIONS-->
  <!-- Contextual HD Image: Equatorial coastline & high-heat vulnerability vista  -->
  <!-- ========================================================================= -->
  <section id="pane-nations" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-space-950 border-t border-white/10">
    <!-- HD Background Image -->
    <div class="absolute inset-0 z-0">
      <img 
        src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=2560&q=85" 
        alt="Equatorial tropical oceanic coastline representing the 54 vulnerable nations" 
        class="w-full h-full object-cover object-center filter brightness-[0.58] contrast-[1.3]" 
        loading="lazy"
      />
      <div class="pane-scrim-heavy"></div>
    </div>

    <!-- HUD Top Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-b border-white/15 pb-4">
      <div class="flex items-center gap-3">
        <span class="font-mono text-xs text-telemetry-cyan uppercase tracking-widest font-bold">PANE 06 // SOVEREIGN RISK MATRIX</span>
        <span class="text-zinc-600">/</span>
        <span class="font-mono text-xs text-zinc-400">54 EQUATOR-ADJACENT NATIONS HEATMAP RANKING</span>
      </div>
      <div class="font-mono text-xs text-zinc-400 hidden sm:block">
        POPULATION MONITORED: 1.42B &bull; REGIONS: 5 CONTINENTAL ZONES
      </div>
    </div>

    <!-- Main Content -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto my-auto py-10">
      
      <div class="max-w-4xl mb-8">
        <p class="font-mono text-xs tracking-[0.25em] text-red-400 uppercase mb-2 font-semibold">
          EXPOSURE CLASSIFICATION &bull; 2026–2027 THREAT INDEX
        </p>
        <h2 class="text-3xl sm:text-5xl font-black uppercase tracking-tight text-white mb-4 font-display">
          GLOBAL HEATMAP RANKING: <span class="text-telemetry-cyan">54 EQUATORIAL NATIONS</span>
        </h2>
        <p class="text-zinc-300 text-sm sm:text-base leading-relaxed">
          The 2026-27 Super El Niño converges directly upon the equatorial belt. We have indexed and ranked all 54 sovereign territories by compound exposure: sea surface thermal anomaly, projected rainfall deficit, hydroelectric reliance, and crop caloric vulnerability.
        </p>
      </div>

      <!-- Interactive Filtering & Search Controls -->
      <div class="hud-box p-4 mb-6 flex flex-wrap items-center justify-between gap-4">
        
        <!-- Region Filter Buttons -->
        <div class="flex flex-wrap items-center gap-2 font-mono text-[11px] uppercase tracking-wider" id="region-filters">
          <button onclick="filterNations('ALL')" class="region-btn px-3 py-1.5 bg-white text-black font-bold border border-white transition" data-region="ALL">ALL (54)</button>
          <button onclick="filterNations('SEA')" class="region-btn px-3 py-1.5 bg-transparent text-zinc-300 hover:text-white border border-white/20 hover:border-white transition" data-region="SEA">SE Asia & Pacific (14)</button>
          <button onclick="filterNations('AFRICA')" class="region-btn px-3 py-1.5 bg-transparent text-zinc-300 hover:text-white border border-white/20 hover:border-white transition" data-region="AFRICA">Sub-Saharan Africa (13)</button>
          <button onclick="filterNations('LATAM')" class="region-btn px-3 py-1.5 bg-transparent text-zinc-300 hover:text-white border border-white/20 hover:border-white transition" data-region="LATAM">Latin America & Carib (12)</button>
          <button onclick="filterNations('SOUTHASIA')" class="region-btn px-3 py-1.5 bg-transparent text-zinc-300 hover:text-white border border-white/20 hover:border-white transition" data-region="SOUTHASIA">South Asia (6)</button>
          <button onclick="filterNations('ISLANDS')" class="region-btn px-3 py-1.5 bg-transparent text-zinc-300 hover:text-white border border-white/20 hover:border-white transition" data-region="ISLANDS">Equatorial Islands (9)</button>
        </div>

        <!-- Search Input -->
        <div class="w-full sm:w-72 relative">
          <input 
            type="text" 
            id="nation-search" 
            placeholder="SEARCH NATION OR THREAT..." 
            class="w-full bg-space-900 border border-white/20 px-3 py-1.5 font-mono text-xs text-white placeholder-zinc-500 focus:outline-none focus:border-telemetry-cyan"
            oninput="searchNations()"
          />
          <span class="absolute right-3 top-2 text-zinc-500 font-mono text-xs">&#x2315;</span>
        </div>

      </div>

      <!-- Dynamic Nations Table / Scroll Container -->
      <div class="hud-box overflow-hidden">
        <div class="overflow-x-auto max-h-[480px] overflow-y-auto">
          <table class="w-full text-left border-collapse font-mono text-xs">
            <thead class="bg-white/5 border-b border-white/10 text-zinc-400 uppercase text-[10.5px] sticky top-0 backdrop-blur-md z-10">
              <tr>
                <th class="py-3 px-4">Rank & Country</th>
                <th class="py-3 px-4">Region</th>
                <th class="py-3 px-4">Vulnerability</th>
                <th class="py-3 px-4">Primary Threat Vector</th>
                <th class="py-3 px-4">Caloric Deficit</th>
                <th class="py-3 px-4">Rufino Synthesis Module</th>
                <th class="py-3 px-4 text-right">Status</th>
              </tr>
            </thead>
            <tbody id="nations-table-body" class="divide-y divide-white/10 text-zinc-300">
              <!-- Dynamically populated via JS -->
            </tbody>
          </table>
        </div>
        
        <!-- Table Footnote & Summary Bar -->
        <div class="p-3 bg-white/5 border-t border-white/10 flex flex-wrap items-center justify-between text-[11px] font-mono text-zinc-400">
          <div id="nation-count">SHOWING 54 OF 54 SOVEREIGN ENTITIES</div>
          <div class="flex items-center gap-4">
            <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-red-500"></span> TIER 1: CRITICAL (SCORE &gt; 90)</span>
            <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-amber-400"></span> TIER 2: SEVERE (85–90)</span>
            <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-blue-400"></span> TIER 3: ELEVATED (&lt; 85)</span>
          </div>
        </div>
      </div>

    </div>

    <!-- Bottom HUD Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-t border-white/10 pt-4 font-mono text-[11px] text-zinc-500">
      <div>DATA HARMONIZATION: NOAA CPC &bull; ECMWF SYSTEM-5 &bull; UN WFP VULNERABILITY ATLAS &bull; RUFINO LERM V3</div>
      <a href="#pane-doctrine" class="text-zinc-300 hover:text-white transition tracking-wider uppercase">ADVANCE TO STRATEGIC DOCTRINE &darr;</a>
    </div>
  </section>


  <!-- ========================================================================= -->
  <!-- PANE 07: THE RUFINO SYNTHESIS STRATEGIC DOCTRINE & CAPITAL ARCHITECTURE    -->
  <!-- Contextual HD Image: High-contrast architectural glass & monumental nexus -->
  <!-- ========================================================================= -->
  <section id="pane-doctrine" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-space-950 border-t border-white/10">
    <!-- HD Background Image -->
    <div class="absolute inset-0 z-0">
      <img 
        src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=2560&q=85" 
        alt="Monumental high-tech architectural infrastructure symbolizing the Rufino Synthesis" 
        class="w-full h-full object-cover object-center filter brightness-[0.55] contrast-[1.25]" 
        loading="lazy"
      />
      <div class="pane-scrim"></div>
    </div>

    <!-- HUD Top Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-b border-white/15 pb-4">
      <div class="flex items-center gap-3">
        <span class="font-mono text-xs text-white uppercase tracking-widest font-bold">PANE 07 // STRATEGIC DOCTRINE</span>
        <span class="text-zinc-600">/</span>
        <span class="font-mono text-xs text-zinc-400">THERMODYNAMIC CAPITAL DEPLOYMENT ARCHITECTURE</span>
      </div>
      <div class="font-mono text-xs text-zinc-400 hidden sm:block">
        GLOBAL MITIGATION SHORTFALL: $140 BILLION &bull; REQUISITION CYCLE: &lt;45 DAYS
      </div>
    </div>

    <!-- Main Content Grid -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto my-auto py-12 grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
      
      <div class="lg:col-span-6">
        <p class="font-mono text-xs tracking-[0.25em] text-zinc-400 uppercase mb-3 font-semibold">
          OPERATIONAL DIRECTIVE // ARCHITECTURAL REORIENTATION
        </p>
        <h2 class="text-4xl sm:text-6xl font-black uppercase tracking-tight text-white mb-6 font-display leading-none">
          THE RUFINO SYNTHESIS: <br/>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-white via-zinc-300 to-zinc-500">PREEMPTIVE CAPITAL</span>
        </h2>
        
        <p class="text-zinc-300 text-base sm:text-lg leading-relaxed mb-6 font-normal">
          Conventional multilateral climate mechanisms fail because they are intrinsically <em class="text-white font-semibold not-italic">reactive</em>: mobilizing donor funds only after famines, blackout collapses, and displacement crises make international headlines.
        </p>

        <p class="text-zinc-400 text-sm sm:text-base leading-relaxed mb-8">
          The Rufino Synthesis replaces slow bureaucracy with <strong class="text-white">Preemptive Thermodynamic Requisition</strong>. By pairing orbital ENSO telemetry with pre-certified ISO containerized hardware manifests, capital is deployed before crop planting windows close and aquifers dry out.
        </p>

        <div class="flex flex-wrap gap-4">
          <a href="#pane-calculator" class="btn-spacex-white">
            RUN RESOURCE SIMULATOR &rarr;
          </a>
          <a href="mailto:jeffersonrrufino@gmail.com?subject=The%20Rufino%20Synthesis%20-%20Sovereign%20Resilience%20Inquiry" class="btn-spacex-outline">
            COMMISSION PROTOCOL DISPATCH
          </a>
        </div>
      </div>

      <!-- Right Column: 3 Pillars Grid -->
      <div class="lg:col-span-6 grid grid-cols-1 sm:grid-cols-2 gap-4">
        
        <div class="hud-box p-6 sm:col-span-2 border-t-2 border-t-telemetry-cyan">
          <div class="font-mono text-xs text-telemetry-cyan uppercase tracking-widest font-bold mb-1">PILLAR I // THERMODYNAMIC RE-ROUTING</div>
          <h3 class="text-lg font-bold text-white mb-2">Solar Excess as Primary Defense</h3>
          <p class="text-xs text-zinc-400 leading-relaxed">
            Converting destructive atmospheric heat domes and cloudless insolation into megawatt power for continuous atmospheric condensation, aquifer re-pressurization, and passive cold-chain preservation.
          </p>
        </div>

        <div class="hud-box p-6 border-t-2 border-t-amber-400">
          <div class="font-mono text-xs text-amber-400 uppercase tracking-widest font-bold mb-1">PILLAR II // PRE-EMPTION</div>
          <h3 class="text-lg font-bold text-white mb-2">Sovereign Resilience Bonds</h3>
          <p class="text-xs text-zinc-400 leading-relaxed">
            Automated parametric liquidity contracts triggered instantly when Pacific Niño 3.4 SST passes +1.5°C for 60 consecutive days, bypassing legislative delays.
          </p>
        </div>

        <div class="hud-box p-6 border-t-2 border-t-emerald-400">
          <div class="font-mono text-xs text-emerald-400 uppercase tracking-widest font-bold mb-1">PILLAR III // HARDWARE</div>
          <h3 class="text-lg font-bold text-white mb-2">Intermodal Standardization</h3>
          <p class="text-xs text-zinc-400 leading-relaxed">
            All modules (AWG harvesters, agrivoltaic structural spans, cold clinics) engineered into standard ISO shipping frames for immediate global air and sea delivery.
          </p>
        </div>

      </div>

    </div>

    <!-- Bottom HUD Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-t border-white/10 pt-4 font-mono text-[11px] text-zinc-500">
      <div>ORIGINATOR & LEAD ARCHITECT: JEFFERSON RAFAEL RUFINO // RUFINO VENTURES</div>
      <div class="text-zinc-400">INQUIRIES: JEFFERSONRRUFINO@GMAIL.COM</div>
    </div>
  </section>


  <!-- ========================================================================= -->
  <!-- PANE 08: INTERACTIVE CRISIS TELEMETRY SIMULATOR & RESOURCE CALCULATOR     -->
  <!-- Contextual HD Image: High-tech aerospace computing console & server grid -->
  <!-- ========================================================================= -->
  <section id="pane-calculator" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-space-950 border-t border-white/10">
    <!-- HD Background Image -->
    <div class="absolute inset-0 z-0">
      <img 
        src="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=2560&q=85" 
        alt="Aerospace computing and server grid telemetry console" 
        class="w-full h-full object-cover object-center filter brightness-[0.55] contrast-[1.3]" 
        loading="lazy"
      />
      <div class="pane-scrim-heavy"></div>
    </div>

    <!-- HUD Top Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-b border-white/15 pb-4">
      <div class="flex items-center gap-3">
        <span class="font-mono text-xs text-amber-400 uppercase tracking-widest font-bold">PANE 08 // SIMULATION ENGINE</span>
        <span class="text-zinc-600">/</span>
        <span class="font-mono text-xs text-zinc-400">INTERACTIVE TELEMETRY & HARDWARE CALCULATOR</span>
      </div>
      <div class="font-mono text-xs text-zinc-400 hidden sm:block">
        MODEL: LERM-CLIMATE V3.2 &bull; MONTE CARLO SENSITIVITY SWEEPS
      </div>
    </div>

    <!-- Main Content Area -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto my-auto py-10">
      
      <div class="max-w-4xl mb-8">
        <p class="font-mono text-xs tracking-[0.25em] text-amber-400 uppercase mb-2 font-semibold">
          INTERACTIVE DECISION TELEMETRY // REAL-TIME RESOURCE COMPUTATION
        </p>
        <h2 class="text-3xl sm:text-5xl font-black uppercase tracking-tight text-white mb-4 font-display">
          SUPER EL NIÑO <span class="text-amber-400">DEPLOYMENT CALCULATOR</span>
        </h2>
        <p class="text-zinc-300 text-sm sm:text-base leading-relaxed">
          Calibrate regional exposure variables below to simulate municipal deficits and calculate the precise Rufino Synthesis hardware deployment manifest required to neutralize crop loss, water starvation, and power grid collapse.
        </p>
      </div>

      <!-- Calculator Layout -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        
        <!-- Controls Column -->
        <div class="lg:col-span-5 hud-box p-6 space-y-6">
          <div class="border-b border-white/10 pb-3 flex items-center justify-between">
            <span class="font-mono text-xs uppercase tracking-widest text-white font-bold">1. CALIBRATE ANOMALY INPUTS</span>
            <span class="font-mono text-[10px] text-telemetry-cyan">LIVE MODEL</span>
          </div>

          <!-- Slider 1: SST Anomaly -->
          <div>
            <div class="flex items-center justify-between font-mono text-xs mb-2">
              <span class="text-zinc-400">PACIFIC SST ANOMALY:</span>
              <span id="calc-sst-display" class="text-red-400 font-bold text-sm">+2.85°C</span>
            </div>
            <input 
              type="range" 
              id="calc-sst" 
              min="1.0" 
              max="4.5" 
              step="0.05" 
              value="2.85" 
              class="w-full accent-red-500 cursor-pointer"
              oninput="recalculateModel()"
            />
            <div class="flex justify-between font-mono text-[10px] text-zinc-500 mt-1">
              <span>+1.0°C (Moderate)</span>
              <span>+2.85°C (Current Forecast)</span>
              <span>+4.5°C (Extreme)</span>
            </div>
          </div>

          <!-- Slider 2: Population Exposed -->
          <div>
            <div class="flex items-center justify-between font-mono text-xs mb-2">
              <span class="text-zinc-400">POPULATION EXPOSURE:</span>
              <span id="calc-pop-display" class="text-white font-bold text-sm">1,500,000</span>
            </div>
            <input 
              type="range" 
              id="calc-pop" 
              min="100000" 
              max="10000000" 
              step="50000" 
              value="1500000" 
              class="w-full accent-telemetry-cyan cursor-pointer"
              oninput="recalculateModel()"
            />
            <div class="flex justify-between font-mono text-[10px] text-zinc-500 mt-1">
              <span>100K</span>
              <span>1.5M (Metro/Provincial)</span>
              <span>10M (Mega-Region)</span>
            </div>
          </div>

          <!-- Slider 3: Drought Duration -->
          <div>
            <div class="flex items-center justify-between font-mono text-xs mb-2">
              <span class="text-zinc-400">DROUGHT DURATION:</span>
              <span id="calc-days-display" class="text-amber-400 font-bold text-sm">180 DAYS</span>
            </div>
            <input 
              type="range" 
              id="calc-days" 
              min="30" 
              max="365" 
              step="15" 
              value="180" 
              class="w-full accent-amber-400 cursor-pointer"
              oninput="recalculateModel()"
            />
            <div class="flex justify-between font-mono text-[10px] text-zinc-500 mt-1">
              <span>30 Days</span>
              <span>180 Days (Half-Year)</span>
              <span>365 Days</span>
            </div>
          </div>

          <!-- Geography Profile -->
          <div>
            <label class="font-mono text-xs text-zinc-400 block mb-2">REGIONAL TOPOGRAPHY PROFILE:</label>
            <select id="calc-geography" onchange="recalculateModel()" class="w-full bg-space-900 border border-white/20 p-2 font-mono text-xs text-white focus:outline-none focus:border-telemetry-cyan">
              <option value="coastal">Archipelagic & Coastal (Philippines, Indonesia, Peru)</option>
              <option value="riverine">Inland Riverine Basin (Vietnam Mekong, Colombia)</option>
              <option value="arid">Arid Highland & Dry Corridor (Guatemala, Kenya, Ethiopia)</option>
              <option value="atoll">Pacific Atoll / Island State (Kiribati, Tuvalu, Vanuatu)</option>
            </select>
          </div>

          <div class="pt-2">
            <button onclick="exportCalculatorReport()" class="w-full btn-spacex-outline !py-2.5 text-xs text-center justify-center">
              EXPORT COMPUTED DEPLOYMENT SPECIFICATION &rarr;
            </button>
          </div>
        </div>

        <!-- Telemetry Output Display Column -->
        <div class="lg:col-span-7 space-y-6">
          <div class="hud-box p-6">
            <div class="border-b border-white/10 pb-3 flex items-center justify-between mb-6">
              <span class="font-mono text-xs uppercase tracking-widest text-zinc-400 font-bold">2. PROJECTED DEFICITS (UNMITIGATED)</span>
              <span class="font-mono text-[10px] text-red-400 animate-pulse">COLLAPSE VECTOR</span>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-6">
              <div class="bg-black/50 p-4 border border-white/10">
                <div class="font-mono text-[10px] uppercase text-zinc-400 mb-1">Daily Potable Water Gap</div>
                <div id="out-water-deficit" class="text-2xl sm:text-3xl font-mono font-black text-telemetry-cyan">42.8 ML/D</div>
                <div class="font-mono text-[10px] text-zinc-500 mt-1">Million Liters Daily Shortfall</div>
              </div>

              <div class="bg-black/50 p-4 border border-white/10">
                <div class="font-mono text-[10px] uppercase text-zinc-400 mb-1">Peak Power Deficit</div>
                <div id="out-power-deficit" class="text-2xl sm:text-3xl font-mono font-black text-amber-400">537 MW</div>
                <div class="font-mono text-[10px] text-zinc-500 mt-1">Cooling & Pumping Deficit</div>
              </div>

              <div class="bg-black/50 p-4 border border-white/10">
                <div class="font-mono text-[10px] uppercase text-zinc-400 mb-1">Caloric Crop Threat</div>
                <div id="out-crop-risk" class="text-2xl sm:text-3xl font-mono font-black text-red-400">39,550 MT</div>
                <div class="font-mono text-[10px] text-zinc-500 mt-1">Metric Tons at Acute Risk</div>
              </div>
            </div>

            <div class="border-t border-b border-white/10 py-3 flex items-center justify-between my-4">
              <span class="font-mono text-xs uppercase tracking-widest text-white font-bold">3. RUFINO SYNTHESIS REQUIRED HARDWARE MANIFEST</span>
              <span class="font-mono text-[10px] text-emerald-400 font-bold">PREEMPTIVE ALLOCATION</span>
            </div>

            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center">
              <div class="p-3 bg-white/5 border border-white/10">
                <div id="out-agri-ha" class="text-xl sm:text-2xl font-mono font-bold text-emerald-400">7,480 HA</div>
                <div class="font-mono text-[10px] text-zinc-400 mt-1 uppercase">Agrivoltaics Canopy</div>
              </div>

              <div class="p-3 bg-white/5 border border-white/10">
                <div id="out-awg-units" class="text-xl sm:text-2xl font-mono font-bold text-telemetry-cyan">856 PODS</div>
                <div class="font-mono text-[10px] text-zinc-400 mt-1 uppercase">AWG-50k Harvesters</div>
              </div>

              <div class="p-3 bg-white/5 border border-white/10">
                <div id="out-aquifer-wells" class="text-xl sm:text-2xl font-mono font-bold text-white">103 WELLS</div>
                <div class="font-mono text-[10px] text-zinc-400 mt-1 uppercase">Deep Recharge Hubs</div>
              </div>

              <div class="p-3 bg-white/5 border border-white/10">
                <div id="out-cold-clinics" class="text-xl sm:text-2xl font-mono font-bold text-red-400">60 PODS</div>
                <div class="font-mono text-[10px] text-zinc-400 mt-1 uppercase">Cold Triage Clinics</div>
              </div>
            </div>

            <div class="mt-6 p-4 bg-emerald-950/20 border border-emerald-500/30 flex flex-wrap items-center justify-between gap-4">
              <div>
                <div class="font-mono text-[11px] text-emerald-400 uppercase font-bold">Preemptive Capital Investment Required:</div>
                <div id="out-capital" class="text-3xl font-mono font-black text-white">$552.4 MILLION USD</div>
              </div>
              <div class="text-right">
                <div class="font-mono text-[11px] text-zinc-400 uppercase">Estimated Loss Prevented:</div>
                <div id="out-loss-prevented" class="text-2xl font-mono font-bold text-emerald-400">$3.82 BILLION USD</div>
              </div>
            </div>

            <div class="mt-4 flex justify-end">
              <a href="mailto:jeffersonrrufino@gmail.com?subject=The%20Photosynthesis%20Project%20-%20Calculated%20Deployment%20Allocation" class="btn-spacex-cyan text-xs">
                TRANSMIT SPECIFICATION TO MISSION CONTROL &rarr;
              </a>
            </div>

          </div>
        </div>

      </div>

    </div>

    <!-- Bottom HUD Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-t border-white/10 pt-4 font-mono text-[11px] text-zinc-500">
      <div>FORMULATION: LERM THERMODYNAMIC ENTROPY THEOREM &bull; CALIBRATION: 2026-27 SUPER EL NIÑO PARAMETERS</div>
      <div class="text-zinc-400">DIRECT COMMISSION: JEFFERSONRRUFINO@GMAIL.COM</div>
    </div>
  </section>


  <!-- ========================================================================= -->
  <!-- PANE 09: MISSION DIRECTIVE & GLOBAL ENGAGEMENT NEXUS (DIRECT CONTACT)     -->
  <!-- Contextual HD Image: Starry deep space horizon & launch orbital trajectory -->
  <!-- ========================================================================= -->
  <section id="pane-contact" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-space-950 border-t border-white/10">
    <!-- HD Background Image -->
    <div class="absolute inset-0 z-0">
      <img 
        src="https://images.unsplash.com/photo-1516849841032-87cbac4d88f7?auto=format&fit=crop&w=2560&q=85" 
        alt="Deep starry space horizon symbolizing cosmic perspective and planetary mission" 
        class="w-full h-full object-cover object-center filter brightness-[0.55] contrast-[1.25]" 
        loading="lazy"
      />
      <div class="pane-scrim-heavy"></div>
    </div>

    <!-- HUD Top Bar -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto flex items-center justify-between border-b border-white/15 pb-4">
      <div class="flex items-center gap-3">
        <span class="font-mono text-xs text-telemetry-cyan uppercase tracking-widest font-bold">PANE 09 // MISSION CONTROL</span>
        <span class="text-zinc-600">/</span>
        <span class="font-mono text-xs text-zinc-400">SOVEREIGN ENGAGEMENT & DIPLOMATIC INQUIRIES</span>
      </div>
      <div class="font-mono text-xs text-zinc-400 hidden sm:block">
        DIRECT CHANNEL: JEFFERSONRRUFINO@GMAIL.COM &bull; PGP VERIFIED
      </div>
    </div>

    <!-- Main Contact & Dispatch Grid -->
    <div class="relative z-10 max-w-[1720px] w-full mx-auto my-auto py-12 grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
      
      <div class="lg:col-span-6">
        <p class="font-mono text-xs tracking-[0.3em] text-telemetry-cyan uppercase mb-3 font-semibold">
          ACTIVATE SOVEREIGN CONTINGENCY // 2026–2027 WINDOW
        </p>
        <h2 class="text-4xl sm:text-6xl lg:text-7xl font-black uppercase tracking-tight text-white mb-6 font-display leading-[0.95]">
          COMMISSION <br/>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-white via-zinc-200 to-zinc-400">THE SYNTHESIS</span>
        </h2>
        
        <p class="text-zinc-300 text-base sm:text-lg leading-relaxed mb-6 font-normal">
          The 2026–2027 Super El Niño is an unavoidable planetary thermodynamic reality. The catastrophe, however, is completely preventable.
        </p>

        <p class="text-zinc-400 text-sm sm:text-base leading-relaxed mb-8">
          We invite heads of state, ministers of water, energy, and agriculture, disaster risk management agencies, sovereign wealth funds, and multilateral defense organizations to commission <strong class="text-white">The Photosynthesis Project</strong>. Our team provides end-to-end hardware procurement, telemetry calibration, and rapid modular deployment across all 54 target nations.
        </p>

        <!-- Direct Email Card -->
        <div class="hud-box p-6 border-l-4 border-l-telemetry-cyan mb-6">
          <div class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-1">Primary Transmission Protocol</div>
          <div class="text-xl sm:text-2xl font-mono font-bold text-white break-all select-all">
            jeffersonrrufino@gmail.com
          </div>
          <div class="mt-4 flex flex-wrap gap-3">
            <button onclick="copyEmailToClipboard()" id="copy-email-btn" class="btn-spacex-white !py-2 !px-4 text-[11px]">
              COPY EMAIL ADDRESS
            </button>
            <a href="mailto:jeffersonrrufino@gmail.com?subject=The%20Photosynthesis%20Project%20-%20High-Level%20Executive%20Briefing" class="btn-spacex-outline !py-2 !px-4 text-[11px]">
              OPEN EMAIL CLIENT &rarr;
            </a>
          </div>
          <div id="copy-notification" class="hidden text-xs font-mono text-emerald-400 mt-2">
            ✓ EMAIL ADDRESS COPIED TO CLIPBOARD
          </div>
        </div>

        <div class="font-mono text-xs text-zinc-500 space-y-1">
          <div>COMMAND HQ: RUFINO VENTURES &bull; MANILA // GLOBAL SOVEREIGN DEPLOYMENT</div>
          <div>FOUNDER & LEAD ARCHITECT: JEFFERSON RAFAEL RUFINO</div>
          <div>INQUIRY ROUTING: HIGH PRIORITY EXECUTIVE QUEUE</div>
        </div>
      </div>

      <!-- Right Column: Interactive Dispatch Form -->
      <div class="lg:col-span-6">
        <div class="hud-box p-6 sm:p-8">
          <div class="border-b border-white/10 pb-4 mb-6">
            <span class="font-mono text-xs uppercase tracking-widest text-white font-bold">SOVEREIGN TRANSMISSION DISPATCH</span>
            <p class="text-xs text-zinc-400 mt-1">Direct pipeline to Jefferson Rafael Rufino. Expect response within 12 hours.</p>
          </div>

          <form id="contact-form" onsubmit="handleFormSubmit(event)" class="space-y-4 font-mono text-xs">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-zinc-400 uppercase tracking-wider mb-1">Sovereign State / Organization *</label>
                <input 
                  type="text" 
                  id="form-org" 
                  required 
                  placeholder="e.g. Republic of the Philippines" 
                  class="w-full bg-space-900 border border-white/20 p-2.5 text-white placeholder-zinc-600 focus:outline-none focus:border-telemetry-cyan"
                />
              </div>

              <div>
                <label class="block text-zinc-400 uppercase tracking-wider mb-1">Official Contact Email *</label>
                <input 
                  type="email" 
                  id="form-email" 
                  required 
                  placeholder="e.g. minister@energy.gov" 
                  class="w-full bg-space-900 border border-white/20 p-2.5 text-white placeholder-zinc-600 focus:outline-none focus:border-telemetry-cyan"
                />
              </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-zinc-400 uppercase tracking-wider mb-1">Target Geographic Zone</label>
                <select id="form-region" class="w-full bg-space-900 border border-white/20 p-2.5 text-white focus:outline-none focus:border-telemetry-cyan">
                  <option value="Southeast Asia">Southeast Asia & Pacific Rim</option>
                  <option value="Sub-Saharan Africa">Sub-Saharan Africa</option>
                  <option value="Latin America">Latin America & Caribbean</option>
                  <option value="South Asia">South Asia</option>
                  <option value="Equatorial Island State">Equatorial Island States</option>
                  <option value="Multilateral / Global">Multilateral Institution / NGO</option>
                </select>
              </div>

              <div>
                <label class="block text-zinc-400 uppercase tracking-wider mb-1">Estimated Exposed Population</label>
                <select id="form-pop" class="w-full bg-space-900 border border-white/20 p-2.5 text-white focus:outline-none focus:border-telemetry-cyan">
                  <option value="< 500,000">&lt; 500,000 (Provincial)</option>
                  <option value="500,000 - 2,000,000">500,000 – 2,000,000 (Metro/District)</option>
                  <option value="2,000,000 - 10,000,000">2,000,000 – 10,000,000 (Regional)</option>
                  <option value="> 10,000,000">&gt; 10,000,000 (National Crisis)</option>
                </select>
              </div>
            </div>

            <!-- Modules of Interest Checkboxes -->
            <div>
              <label class="block text-zinc-400 uppercase tracking-wider mb-2">Priority Operational Vectors Requested:</label>
              <div class="grid grid-cols-2 gap-2 text-[11px] text-zinc-300">
                <label class="flex items-center gap-2 p-2 bg-white/5 border border-white/10 cursor-pointer hover:border-white/30">
                  <input type="checkbox" id="mod-satellite" checked class="accent-telemetry-cyan" />
                  <span>Satellite Telemetry</span>
                </label>
                <label class="flex items-center gap-2 p-2 bg-white/5 border border-white/10 cursor-pointer hover:border-white/30">
                  <input type="checkbox" id="mod-solar" checked class="accent-telemetry-cyan" />
                  <span>Solar Canopies & Storage</span>
                </label>
                <label class="flex items-center gap-2 p-2 bg-white/5 border border-white/10 cursor-pointer hover:border-white/30">
                  <input type="checkbox" id="mod-agri" checked class="accent-telemetry-cyan" />
                  <span>Agrivoltaic Biospheres</span>
                </label>
                <label class="flex items-center gap-2 p-2 bg-white/5 border border-white/10 cursor-pointer hover:border-white/30">
                  <input type="checkbox" id="mod-water" checked class="accent-telemetry-cyan" />
                  <span>AWG & Aquifer Recharge</span>
                </label>
                <label class="flex items-center gap-2 p-2 bg-white/5 border border-white/10 cursor-pointer hover:border-white/30 col-span-2">
                  <input type="checkbox" id="mod-medical" checked class="accent-telemetry-cyan" />
                  <span>Off-Grid Cold-Chain Triage Field Clinics</span>
                </label>
              </div>
            </div>

            <div>
              <label class="block text-zinc-400 uppercase tracking-wider mb-1">Brief Statement of Emergency / Requirements</label>
              <textarea 
                id="form-message" 
                rows="3" 
                required 
                placeholder="Detail current rainfall deficits, reservoir depletion status, or requested briefing timeline..."
                class="w-full bg-space-900 border border-white/20 p-2.5 text-white placeholder-zinc-600 focus:outline-none focus:border-telemetry-cyan"
              ></textarea>
            </div>

            <button type="submit" class="w-full btn-spacex-cyan text-center justify-center !py-3">
              TRANSMIT HIGH-PRIORITY DISPATCH TO JEFFERSONRRUFINO@GMAIL.COM &rarr;
            </button>
          </form>

          <div id="form-success" class="hidden mt-4 p-4 bg-emerald-950/40 border border-emerald-500/50 text-emerald-300 font-mono text-xs">
            ✓ TRANSMISSION INITIALIZED: Opening your official mail client with formatted diplomatic dispatch addressed to <strong>jeffersonrrufino@gmail.com</strong>.
          </div>
        </div>
      </div>

    </div>

    <!-- Master Footer -->
    <footer class="relative z-10 max-w-[1720px] w-full mx-auto border-t border-white/15 pt-8 pb-4">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4 font-mono text-xs text-zinc-500">
        <div class="flex items-center gap-3">
          <span class="w-2 h-2 bg-white"></span>
          <span class="text-zinc-300 font-bold uppercase">THE PHOTOSYNTHESIS PROJECT &bull; THE RUFINO SYNTHESIS</span>
        </div>
        <div>
          PRISTINE SPACEX-INSPIRED RESILIENCE SPECIFICATION // 2026–2027 SUPER EL NIÑO
        </div>
        <div>
          DIRECT INQUIRIES: <a href="mailto:jeffersonrrufino@gmail.com" class="text-telemetry-cyan hover:underline">jeffersonrrufino@gmail.com</a>
        </div>
      </div>
      <div class="text-[10px] font-mono text-zinc-600 mt-4 text-center sm:text-left">
        &copy; 2026 RUFINO VENTURES. ALL RIGHTS RESERVED. SOVEREIGN CRISIS ARCHITECTURE. REPRODUCTION OR FORWARDING PERMITTED FOR HUMANITARIAN & INTERGOVERNMENTAL EMERGENCY PLANNING.
      </div>
    </footer>
  </section>


  <!-- ========================================================================= -->
  <!-- INTERACTIVE MODAL COMPONENT (ENGINEERING SCHEMATICS & PROTOCOLS)          -->
  <!-- ========================================================================= -->
  <div id="modal-container" class="fixed inset-0 z-50 hidden bg-black/85 backdrop-blur-xl flex items-center justify-center p-4 sm:p-8">
    <div class="relative max-w-4xl w-full max-h-[90vh] overflow-y-auto hud-box p-6 sm:p-10 border-white/30 text-zinc-300">
      
      <!-- Close Button -->
      <button onclick="closeModal()" class="absolute top-6 right-6 font-mono text-zinc-400 hover:text-white text-xl">
        ✕
      </button>

      <!-- Dynamic Content Wrapper -->
      <div id="modal-content">
        <!-- Injected via openModal(type) -->
      </div>

    </div>
  </div>


  <!-- ========================================================================= -->
  <!-- JAVASCRIPT: DATA, INTERACTIVE CALCULATOR, MODAL, CLOCK & FORM             -->
  <!-- ========================================================================= -->
  <script>
    // -----------------------------------------------------------------------
    // 54 EQUATOR-ADJACENT NATIONS DATABASE
    // -----------------------------------------------------------------------
    const NATIONS_DATA = [
      { rank: 1, name: "Philippines", region: "SEA", code: "PHL", score: 98.4, threat: "Agricultural Drought & Hydro Grid Blackout", deficit: "-42% Rice/Corn", module: "Agrivoltaics & Modular AWG Pods", tier: "TIER 1" },
      { rank: 2, name: "Indonesia", region: "SEA", code: "IDN", score: 96.2, threat: "Peatland Wildfires & Crop Desiccation", deficit: "-38% Palm/Rice", module: "Floating Solar & Aquifer Wells", tier: "TIER 1" },
      { rank: 3, name: "Peru", region: "LATAM", code: "PER", score: 96.8, threat: "Coastal Flash Deluge & Anchoveta Fishery Collapse", deficit: "-48% Marine Yield", module: "Cold-Chain Logistics & Drainage", tier: "TIER 1" },
      { rank: 4, name: "Kenya", region: "AFRICA", code: "KEN", score: 95.6, threat: "Multi-Season Drought & Pastoral Collapse", deficit: "-45% Maize/Legumes", module: "Deep Aquifer Injection & Solar", tier: "TIER 1" },
      { rank: 5, name: "India (Peninsular Belt)", region: "SOUTHASIA", code: "IND", score: 93.9, threat: "Monsoon Disruption & Thermal Grid Blackout", deficit: "-32% Kharif Crops", module: "Megawatt Solar & Cold Triage", tier: "TIER 1" },
      { rank: 6, name: "Somalia", region: "AFRICA", code: "SOM", score: 97.1, threat: "Groundwater Exhaustion & Acute Famine", deficit: "-55% Sorghum", module: "High-Yield AWG & Clinics", tier: "TIER 1" },
      { rank: 7, name: "Ethiopia", region: "AFRICA", code: "ETH", score: 94.8, threat: "Highland Crop Failure & Water Reservoir Drop", deficit: "-36% Teff/Wheat", module: "Microgrid Pumping & Agrivoltaics", tier: "TIER 1" },
      { rank: 8, name: "Papua New Guinea", region: "SEA", code: "PNG", score: 94.1, threat: "Highland Frost followed by Extreme Drought", deficit: "-44% Sweet Potato", module: "Modular Cold-Chain & AWG", tier: "TIER 1" },
      { rank: 9, name: "Vietnam (Mekong Delta)", region: "SEA", code: "VNM", score: 91.8, threat: "Mekong River Upstream Drop & Salinity Intrusion", deficit: "-34% Delta Rice", module: "Solar Desalination & Aquifers", tier: "TIER 1" },
      { rank: 10, name: "Madagascar (Grand Sud)", region: "AFRICA", code: "MDG", score: 92.4, threat: "Severe Aridity & Cassava Desiccation", deficit: "-49% Cassava", module: "Solar Desalination & Food Hubs", tier: "TIER 1" },
      { rank: 11, name: "Colombia", region: "LATAM", code: "COL", score: 91.4, threat: "Hydro Reservoir Depletion & Forest Fires", deficit: "-29% Coffee/Plantain", module: "Floating Solar & Grid Buffer", tier: "TIER 1" },
      { rank: 12, name: "Bangladesh", region: "SOUTHASIA", code: "BGD", score: 91.5, threat: "Flash Salinity Intrusion & Rice Blast", deficit: "-31% Boro Rice", module: "Reverse Osmosis & Solar Canopies", tier: "TIER 1" },
      { rank: 13, name: "Ecuador", region: "LATAM", code: "ECU", score: 95.1, threat: "Flash Flooding & Export Banana Scour", deficit: "-39% Export Crops", module: "Rapid Drainage & Cold Clinics", tier: "TIER 1" },
      { rank: 14, name: "Sudan", region: "AFRICA", code: "SDN", score: 91.3, threat: "Sahelian Heatwaves & Blue Nile Drop", deficit: "-41% Sorghum/Millet", module: "Off-Grid AWG & Shading Canopies", tier: "TIER 1" },
      { rank: 15, name: "Mozambique", region: "AFRICA", code: "MOZ", score: 90.8, threat: "Erratic Deluge & Southern Aridity", deficit: "-35% Maize", module: "Emergency Triage & Microgrids", tier: "TIER 1" },
      { rank: 16, name: "Kiribati", region: "ISLANDS", code: "KIR", score: 93.2, threat: "Freshwater Lens Salinization & Sea Surge", deficit: "-52% Potable Lens", module: "Solar Distillation & AWG Pods", tier: "TIER 1" },
      { rank: 17, name: "Guatemala (Dry Corridor)", region: "LATAM", code: "GTM", score: 90.2, threat: "Dry Corridor Starvation & Water Collapse", deficit: "-41% Maize/Beans", module: "Agrivoltaics & Water Recharge", tier: "TIER 1" },
      { rank: 18, name: "Solomon Islands", region: "SEA", code: "SLB", score: 90.4, threat: "Outer Atoll Water Scarcity", deficit: "-37% Root Staples", module: "Containerized AWG & Solar Clinics", tier: "TIER 1" },
      { rank: 19, name: "Tuvalu", region: "ISLANDS", code: "TUV", score: 92.0, threat: "Total Rain Catchment Exhaustion", deficit: "-60% Potable Water", module: "AWG Systems & Solar Pods", tier: "TIER 1" },
      { rank: 20, name: "South Sudan", region: "AFRICA", code: "SSD", score: 93.5, threat: "Severe Heat & Displaced Civilian Water Gap", deficit: "-46% Sorghum", module: "Off-Grid Cold Clinics & AWG", tier: "TIER 1" },
      { rank: 21, name: "Brazil (Northeast Sertão)", region: "LATAM", code: "BRA", score: 92.0, threat: "Sertão Semi-Arid Drought & Hydro Loss", deficit: "-37% Beans/Cassava", module: "High-Efficiency Microgrids", tier: "TIER 1" },
      { rank: 22, name: "Haiti", region: "LATAM", code: "HTI", score: 92.8, threat: "Severe Drought on Fragile Grid", deficit: "-42% Local Staples", module: "Containerized Food/Water Hubs", tier: "TIER 1" },
      { rank: 23, name: "Sri Lanka", region: "SOUTHASIA", code: "LKA", score: 89.2, threat: "Yala Season Monsoon Failure & Hydro Cut", deficit: "-28% Rice/Tea", module: "Agrivoltaics & Floating Solar", tier: "TIER 2" },
      { rank: 24, name: "Zimbabwe", region: "AFRICA", code: "ZWE", score: 89.7, threat: "Kariba Dam Hydro Outage & Maize Scorch", deficit: "-44% Maize", module: "Megawatt Solar & Aquifer Wells", tier: "TIER 2" },
      { rank: 25, name: "Honduras", region: "LATAM", code: "HND", score: 89.8, threat: "Central Dry Corridor Agricultural Collapse", deficit: "-38% Basic Grains", module: "Shading Canopies & AWG Units", tier: "TIER 2" },
      { rank: 26, name: "Thailand", region: "SEA", code: "THA", score: 89.5, threat: "Chao Phraya Reservoir Water Rationing", deficit: "-26% Sugar/Rice", module: "Canal Solar Canopies & Drip", tier: "TIER 2" },
      { rank: 27, name: "Bolivia", region: "LATAM", code: "BOL", score: 89.1, threat: "Altiplano Lake Desiccation & Aridity", deficit: "-33% Quinoa/Potato", module: "Subsurface Water Banking", tier: "TIER 2" },
      { rank: 28, name: "Zambia", region: "AFRICA", code: "ZMB", score: 88.9, threat: "Extended Load-Shedding & Arable Burn", deficit: "-39% Maize", module: "Solar Microgrids & Cold Logistics", tier: "TIER 2" },
      { rank: 29, name: "Timor-Leste", region: "SEA", code: "TLS", score: 89.0, threat: "Delayed Rainy Season & Lean Season Famine", deficit: "-35% Corn/Rice", module: "Mobile AWG & Nutrition Hubs", tier: "TIER 2" },
      { rank: 30, name: "Vanuatu", region: "SEA", code: "VUT", score: 88.6, threat: "Volcanic Island Water Shortage", deficit: "-32% Yam/Banana", module: "Desalination & Solar Triage", tier: "TIER 2" },
      { rank: 31, name: "Panama", region: "LATAM", code: "PAN", score: 88.5, threat: "Gatun Lake Freshwater Level Drop", deficit: "-40% Watershed Flow", module: "Aquifer Injections & Watershed Solar", tier: "TIER 2" },
      { rank: 32, name: "El Salvador", region: "LATAM", code: "SLV", score: 88.4, threat: "Groundwater Drop & Wet-Bulb Stress", deficit: "-30% Basic Grains", module: "Agrivoltaic Bio-Shields", tier: "TIER 2" },
      { rank: 33, name: "Myanmar (Dry Zone)", region: "SEA", code: "MMR", score: 88.1, threat: "Central Dry Zone Water Scarcity", deficit: "-33% Sesame/Pulses", module: "Deep Aquifer Injections", tier: "TIER 2" },
      { rank: 34, name: "Pakistan (Southern Belt)", region: "SOUTHASIA", code: "PAK", score: 88.0, threat: "Indus Basin Heatwaves & Crop Scorch", deficit: "-29% Cotton/Wheat", module: "Radiant Shelters & Cold Pods", tier: "TIER 2" },
      { rank: 35, name: "Nicaragua", region: "LATAM", code: "NIC", score: 87.9, threat: "Pacific Coast Agricultural Drought", deficit: "-31% Sorghum", module: "Microgrid Water Systems", tier: "TIER 2" },
      { rank: 36, name: "Malawi", region: "AFRICA", code: "MWI", score: 87.5, threat: "Shire River Hydro Blackouts", deficit: "-36% Maize/Legumes", module: "Decentralized Solar Storage", tier: "TIER 2" },
      { rank: 37, name: "Fiji", region: "SEA", code: "FJI", score: 87.2, threat: "Western Division Cane Field Drought", deficit: "-27% Sugar Cane", module: "Rain Catchment & Solar Shading", tier: "TIER 2" },
      { rank: 38, name: "Mexico (Southern Belt)", region: "LATAM", code: "MEX", score: 86.7, threat: "Oaxaca/Chiapas Heat Waves", deficit: "-25% Corn/Coffee", module: "Agrivoltaics & Canopies", tier: "TIER 2" },
      { rank: 39, name: "Cambodia", region: "SEA", code: "KHM", score: 86.4, threat: "Tonle Sap Lake Inflow Failure", deficit: "-30% Fisheries/Padi", module: "Off-Grid Solar Pumping", tier: "TIER 2" },
      { rank: 40, name: "Micronesia (FSM)", region: "ISLANDS", code: "FSM", score: 85.5, threat: "Outer Island Freshwater Depletion", deficit: "-34% Breadfruit/Taro", module: "Emergency Desalination Pods", tier: "TIER 2" },
      { rank: 41, name: "Tanzania", region: "AFRICA", code: "TZA", score: 85.2, threat: "Central Plateau Crop Burn", deficit: "-28% Maize/Sunflower", module: "Agrivoltaic Microgrids", tier: "TIER 2" },
      { rank: 42, name: "Marshall Islands", region: "ISLANDS", code: "MHL", score: 89.6, threat: "Atoll Freshwater Lens Infiltration", deficit: "-45% Potable Supply", module: "Solar Distillers & AWG", tier: "TIER 2" },
      { rank: 43, name: "Maldives", region: "ISLANDS", code: "MDV", score: 90.1, threat: "Groundwater Salinization & Heat", deficit: "-50% Fresh Water", module: "Modular Solar Desalination", tier: "TIER 2" },
      { rank: 44, name: "Uganda", region: "AFRICA", code: "UGA", score: 84.1, threat: "Cattle Corridor Pastoral Drought", deficit: "-26% Dairy/Matooke", module: "Livestock Solar Shading", tier: "TIER 3" },
      { rank: 45, name: "Samoa", region: "ISLANDS", code: "WSM", score: 83.0, threat: "Groundwater Deficit & Crop Stress", deficit: "-24% Taro", module: "Agrivoltaic Canopies", tier: "TIER 3" },
      { rank: 46, name: "Namibia", region: "AFRICA", code: "NAM", score: 82.7, threat: "Kalahari Margin Heat Extremes", deficit: "-31% Grazing", module: "Deep Well Pumping & Cold Chain", tier: "TIER 3" },
      { rank: 47, name: "Nepal (Terai Belt)", region: "SOUTHASIA", code: "NPL", score: 82.4, threat: "Terai Belt Monsoon Dry Spells", deficit: "-23% Rice", module: "Solar Pumping & Gravity Feeds", tier: "TIER 3" },
      { rank: 48, name: "Tonga", region: "ISLANDS", code: "TON", score: 82.2, threat: "Outer Island Rain Shortage", deficit: "-25% Rainwater Reserves", module: "Containerized AWG Pods", tier: "TIER 3" },
      { rank: 49, name: "Dominican Republic", region: "LATAM", code: "DOM", score: 81.9, threat: "Southwestern Border Aridity", deficit: "-24% Plantain/Beans", module: "Agrivoltaic Canopies", tier: "TIER 3" },
      { rank: 50, name: "Mauritius", region: "ISLANDS", code: "MUS", score: 81.4, threat: "Reservoir Catchment Deficit", deficit: "-20% Vegetables", module: "Floating Solar Canopies", tier: "TIER 3" },
      { rank: 51, name: "Malaysia", region: "SEA", code: "MYS", score: 81.2, threat: "Peninsular Extreme Heat & Water Cuts", deficit: "-22% Padi/Oil Palm", module: "Floatovoltaics & AWG", tier: "TIER 3" },
      { rank: 52, name: "Seychelles", region: "ISLANDS", code: "SYC", score: 80.8, threat: "Granitic Island Catchment Drought", deficit: "-25% Catchment", module: "Reverse Osmosis Solar Units", tier: "TIER 3" },
      { rank: 53, name: "French Polynesia", region: "ISLANDS", code: "PYF", score: 80.5, threat: "Atoll Rain Catchment Shortfall", deficit: "-30% Rain Catchment", module: "Solar Atmospheric Generators", tier: "TIER 3" },
      { rank: 54, name: "São Tomé and Príncipe", region: "AFRICA", code: "STP", score: 79.5, threat: "Equatorial Fishery Migration", deficit: "-21% Local Fish Catch", module: "Cold-Chain Processing Hubs", tier: "TIER 3" },
    ];

    let currentFilter = 'ALL';

    function renderNations(data) {
      const tbody = document.getElementById('nations-table-body');
      tbody.innerHTML = '';

      if (data.length === 0) {
        tbody.innerHTML = `<tr><td colspan="7" class="py-8 text-center text-zinc-500 font-mono">NO SOVEREIGN NATIONS MATCH CRITERIA</td></tr>`;
        document.getElementById('nation-count').innerText = `SHOWING 0 OF 54 SOVEREIGN ENTITIES`;
        return;
      }

      data.forEach(n => {
        let badgeColor = 'bg-red-950/80 text-red-400 border border-red-500/50';
        if (n.score < 85) badgeColor = 'bg-blue-950/80 text-blue-300 border border-blue-500/50';
        else if (n.score < 90) badgeColor = 'bg-amber-950/80 text-amber-300 border border-amber-500/50';

        const tr = document.createElement('tr');
        tr.className = 'hover:bg-white/5 transition-colors duration-150 cursor-pointer';
        tr.onclick = () => openNationDetail(n);
        tr.innerHTML = `
          <td class="py-3 px-4 font-bold text-white flex items-center gap-2">
            <span class="text-zinc-500 text-[10px]">#${String(n.rank).padStart(2, '0')}</span>
            <span>${n.name}</span>
          </td>
          <td class="py-3 px-4 text-zinc-400 text-[11px]">${n.region}</td>
          <td class="py-3 px-4">
            <div class="flex items-center gap-2">
              <span class="font-bold text-white">${n.score.toFixed(1)}</span>
              <div class="w-16 bg-zinc-800 h-1.5 hidden sm:block">
                <div class="bg-red-500 h-full" style="width: ${n.score}%"></div>
              </div>
            </div>
          </td>
          <td class="py-3 px-4 text-zinc-300">${n.threat}</td>
          <td class="py-3 px-4 text-red-400 font-semibold">${n.deficit}</td>
          <td class="py-3 px-4 text-telemetry-cyan text-[11px]">${n.module}</td>
          <td class="py-3 px-4 text-right">
            <span class="px-2 py-0.5 text-[9px] font-bold rounded-sm ${badgeColor}">${n.tier}</span>
          </td>
        `;
        tbody.appendChild(tr);
      });

      document.getElementById('nation-count').innerText = `SHOWING ${data.length} OF 54 SOVEREIGN ENTITIES`;
    }

    function filterNations(region) {
      currentFilter = region;
      document.querySelectorAll('.region-btn').forEach(btn => {
        if (btn.getAttribute('data-region') === region) {
          btn.className = 'region-btn px-3 py-1.5 bg-white text-black font-bold border border-white transition';
        } else {
          btn.className = 'region-btn px-3 py-1.5 bg-transparent text-zinc-300 hover:text-white border border-white/20 hover:border-white transition';
        }
      });
      searchNations();
    }

    function searchNations() {
      const q = document.getElementById('nation-search').value.toLowerCase().trim();
      let filtered = NATIONS_DATA;
      if (currentFilter !== 'ALL') {
        filtered = filtered.filter(n => n.region === currentFilter);
      }
      if (q) {
        filtered = filtered.filter(n => 
          n.name.toLowerCase().includes(q) ||
          n.threat.toLowerCase().includes(q) ||
          n.module.toLowerCase().includes(q) ||
          n.tier.toLowerCase().includes(q)
        );
      }
      renderNations(filtered);
    }

    function openNationDetail(nation) {
      const content = `
        <div class="font-mono text-xs uppercase tracking-widest text-telemetry-cyan mb-2">SOVEREIGN RESILIENCE PROFILE // ${nation.code}</div>
        <h3 class="text-3xl font-black uppercase text-white font-display mb-4">${nation.name} &bull; VULNERABILITY ${nation.score}/100</h3>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 my-6">
          <div class="hud-box p-4 border-l-2 border-red-500">
            <div class="text-[10px] text-zinc-400">Primary El Niño Threat</div>
            <div class="text-base font-bold text-white mt-1">${nation.threat}</div>
          </div>
          <div class="hud-box p-4 border-l-2 border-amber-400">
            <div class="text-[10px] text-zinc-400">Projected Caloric Deficit</div>
            <div class="text-base font-bold text-red-400 mt-1">${nation.deficit}</div>
          </div>
        </div>

        <div class="p-4 bg-white/5 border border-white/10 mb-6 font-mono text-xs">
          <div class="text-telemetry-cyan font-bold mb-2">COMMISSIONED RUFINO SYNTHESIS SPECIFICATION:</div>
          <p class="text-zinc-300 leading-relaxed mb-3">
            Deploy <strong class="text-white">${nation.module}</strong> across vulnerable agricultural zones and municipal centers. Pre-emptive requisition window: <strong>30-45 days</strong> prior to seasonal SST peak.
          </p>
          <ul class="list-disc list-inside space-y-1 text-zinc-400">
            <li>Phase 1: Pre-positioning of ISO-containerized hardware and reverse osmosis skids</li>
            <li>Phase 2: Installation of bifacial elevated solar canopies over prime arable fields</li>
            <li>Phase 3: Connection of phase-change cold-chain medical pods for vaccine/insulin protection</li>
            <li>Phase 4: Real-time satellite telemetry calibration via Rufino Mission Control</li>
          </ul>
        </div>

        <div class="flex flex-wrap items-center justify-between gap-4 pt-4 border-t border-white/10">
          <a href="mailto:jeffersonrrufino@gmail.com?subject=Commissioning%20Rufino%20Synthesis%20for%20${encodeURIComponent(nation.name)}" class="btn-spacex-cyan text-xs">
            INITIATE DEPLOYMENT DISPATCH FOR ${nation.name.toUpperCase()} &rarr;
          </a>
          <button onclick="closeModal()" class="btn-spacex-outline text-xs">
            CLOSE INSPECTION
          </button>
        </div>
      `;
      document.getElementById('modal-content').innerHTML = content;
      document.getElementById('modal-container').classList.remove('hidden');
    }

    // -----------------------------------------------------------------------
    // INTERACTIVE CALCULATOR MODEL (LERM-CLIMATE V3.2)
    // -----------------------------------------------------------------------
    function recalculateModel() {
      const sst = parseFloat(document.getElementById('calc-sst').value);
      const pop = parseInt(document.getElementById('calc-pop').value);
      const days = parseInt(document.getElementById('calc-days').value);
      const geo = document.getElementById('calc-geography').value;

      document.getElementById('calc-sst-display').innerText = (sst >= 0 ? '+' : '') + sst.toFixed(2) + '°C';
      document.getElementById('calc-pop-display').innerText = pop.toLocaleString();
      document.getElementById('calc-days-display').innerText = days + ' DAYS';

      // Geographic severity multiplier
      let geoFactor = 1.0;
      if (geo === 'coastal') geoFactor = 1.15;
      else if (geo === 'riverine') geoFactor = 1.05;
      else if (geo === 'arid') geoFactor = 1.30;
      else if (geo === 'atoll') geoFactor = 1.45;

      // Deficits calculation
      const waterPerPersonDailyLiters = 25 + (sst - 1.0) * 7.5 * geoFactor;
      const totalDailyWaterML = (pop * waterPerPersonDailyLiters) / 1000000;
      const powerDeficitMW = (pop * 0.00032 * (1 + (sst - 1.0) * 0.18)) * geoFactor;
      const cropRiskMT = (pop / 1000) * (20 + (sst - 1.0) * 9.5) * geoFactor * (days / 180);

      // Hardware requirements
      const agriHa = Math.round((pop * 0.0042 * (sst / 2.0)) * geoFactor);
      const awgUnits = Math.round((totalDailyWaterML * 1000000 * 0.70) / 50000);
      const aquiferWells = Math.max(2, Math.round(awgUnits * 0.12));
      const coldClinics = Math.max(2, Math.round(pop / 25000));

      // Financials ($M USD)
      const capitalRequired = (agriHa * 0.038) + (awgUnits * 0.18) + (aquiferWells * 0.45) + (coldClinics * 0.25);
      const lossPrevented = capitalRequired * 6.8;

      // Update DOM
      document.getElementById('out-water-deficit').innerText = totalDailyWaterML.toFixed(1) + ' ML/D';
      document.getElementById('out-power-deficit').innerText = Math.round(powerDeficitMW) + ' MW';
      document.getElementById('out-crop-risk').innerText = Math.round(cropRiskMT).toLocaleString() + ' MT';

      document.getElementById('out-agri-ha').innerText = agriHa.toLocaleString() + ' HA';
      document.getElementById('out-awg-units').innerText = awgUnits.toLocaleString() + ' PODS';
      document.getElementById('out-aquifer-wells').innerText = aquiferWells.toLocaleString() + ' WELLS';
      document.getElementById('out-cold-clinics').innerText = coldClinics.toLocaleString() + ' PODS';

      document.getElementById('out-capital').innerText = '$' + capitalRequired.toFixed(1) + ' MILLION USD';
      document.getElementById('out-loss-prevented').innerText = '$' + lossPrevented.toFixed(2) + ' BILLION USD';
    }

    function exportCalculatorReport() {
      const sst = document.getElementById('calc-sst-display').innerText;
      const pop = document.getElementById('calc-pop-display').innerText;
      const days = document.getElementById('calc-days-display').innerText;
      const water = document.getElementById('out-water-deficit').innerText;
      const power = document.getElementById('out-power-deficit').innerText;
      const crops = document.getElementById('out-crop-risk').innerText;
      const agri = document.getElementById('out-agri-ha').innerText;
      const awg = document.getElementById('out-awg-units').innerText;
      const wells = document.getElementById('out-aquifer-wells').innerText;
      const clinics = document.getElementById('out-cold-clinics').innerText;
      const capital = document.getElementById('out-capital').innerText;

      const reportText = `RUFINO VENTURES // THE PHOTOSYNTHESIS PROJECT
TELEMETRY MODEL REPORT: 2026-27 SUPER EL NIÑO PLAYBOOK
===========================================================
INPUT ANOMALY PARAMETERS:
- Pacific SST Anomaly: ${sst}
- Population Exposed: ${pop}
- Drought Duration: ${days}

PROJECTED DEFICITS:
- Daily Potable Water Gap: ${water}
- Grid Cooling & Power Deficit: ${power}
- Caloric Crop Exposure Risk: ${crops}

RECOMMENDED RUFINO SYNTHESIS DEPLOYMENT MANIFEST:
- Bifacial Agrivoltaic Canopies: ${agri}
- AWG-50k Atmospheric Harvesters: ${awg}
- Subterranean Aquifer Injection Wells: ${wells}
- Off-Grid Cold-Chain Triage Clinics: ${clinics}

CAPITAL ESTIMATE: ${capital}
DIRECT ALL INQUIRIES TO: jeffersonrrufino@gmail.com
===========================================================`;

      const content = `
        <div class="font-mono text-xs uppercase tracking-widest text-amber-400 mb-2">SIMULATION EXPORT // READY TO TRANSMIT</div>
        <h3 class="text-2xl font-black uppercase text-white font-display mb-4">DEPLOYMENT SPECIFICATION MANIFEST</h3>
        <textarea readonly class="w-full h-64 bg-space-900 border border-white/20 p-4 font-mono text-xs text-white leading-relaxed select-all">${reportText}</textarea>
        <div class="flex flex-wrap items-center justify-between gap-4 mt-6">
          <a href="mailto:jeffersonrrufino@gmail.com?subject=The%20Photosynthesis%20Project%20-%20Simulation%20Manifest&body=${encodeURIComponent(reportText)}" class="btn-spacex-cyan text-xs">
            SEND DIRECTLY TO JEFFERSONRRUFINO@GMAIL.COM &rarr;
          </a>
          <button onclick="closeModal()" class="btn-spacex-outline text-xs">
            CLOSE WINDOW
          </button>
        </div>
      `;
      document.getElementById('modal-content').innerHTML = content;
      document.getElementById('modal-container').classList.remove('hidden');
    }

    // -----------------------------------------------------------------------
    // ENGINEERING MODALS (SCHEMATICS)
    // -----------------------------------------------------------------------
    function openModal(type) {
      let content = '';

      if (type === 'modal-telemetry') {
        content = `
          <div class="font-mono text-xs uppercase tracking-widest text-telemetry-cyan mb-2">SPECIFICATION // ORBITAL INFRARED RADIOMETRY</div>
          <h3 class="text-3xl font-black uppercase text-white font-display mb-4">SATELLITE THERMAL & SST TELEMETRY SPEC</h3>
          <p class="text-zinc-300 text-sm leading-relaxed mb-6">
            Equatorial Pacific SST monitoring operates via coupled geostationary (GOES-18, Himawari-9) and sun-synchronous polar orbiters (Sentinel-3 SLSTR, NOAA-21 VIIRS) measuring dual-channel thermal infrared (10.8µm and 12.0µm) alongside sea surface height altimetry.
          </p>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 font-mono text-xs mb-6">
            <div class="bg-black/50 p-4 border border-white/10">
              <span class="text-zinc-400 uppercase">Thermal Noise Equivalent Delta-T:</span>
              <div class="text-white font-bold text-base mt-1">&lt; 0.04 K (Ultra-precision)</div>
            </div>
            <div class="bg-black/50 p-4 border border-white/10">
              <span class="text-zinc-400 uppercase">Kelvin Wave Depth Resolution:</span>
              <div class="text-white font-bold text-base mt-1">10m increments to 300m depth</div>
            </div>
          </div>
          <div class="border-t border-white/10 pt-4 flex justify-end">
            <button onclick="closeModal()" class="btn-spacex-outline text-xs">CLOSE TELEMETRY SPEC</button>
          </div>
        `;
      } else if (type === 'modal-solar') {
        content = `
          <div class="font-mono text-xs uppercase tracking-widest text-amber-400 mb-2">ENGINEERING BLUEPRINT // THERMODYNAMIC GENERATION</div>
          <h3 class="text-3xl font-black uppercase text-white font-display mb-4">BIFACIAL MEGAWATT CANOPY & THERMAL STORAGE</h3>
          <p class="text-zinc-300 text-sm leading-relaxed mb-6">
            High-efficiency N-type TOPCon bifacial modules with 80% bifaciality factor. Installed over elevated tubular steel trusses with anti-corrosion marine galvanization (C5-M rating).
          </p>
          <div class="space-y-3 font-mono text-xs mb-6">
            <div class="p-3 bg-white/5 border border-white/10">
              <span class="text-amber-400 font-bold">1. Floating Floatovoltaic Pontoon Subsystem:</span> High-density UV-stabilized polyethylene HDPE pontoons with anchoring designed to handle 30m reservoir level fluctuations.
            </div>
            <div class="p-3 bg-white/5 border border-white/10">
              <span class="text-amber-400 font-bold">2. Thermal Phase-Change Buffer:</span> Sodium acetate trihydrate / paraffin wax latent heat modules storing 4.8 MWh thermal chill/heat buffer per 40ft container.
            </div>
          </div>
          <div class="border-t border-white/10 pt-4 flex justify-end">
            <button onclick="closeModal()" class="btn-spacex-outline text-xs">CLOSE BLUEPRINT</button>
          </div>
        `;
      } else if (type === 'modal-agri') {
        content = `
          <div class="font-mono text-xs uppercase tracking-widest text-emerald-400 mb-2">AGRONOMIC PROTOCOL // BIOSPHERE SHIELD</div>
          <h3 class="text-3xl font-black uppercase text-white font-display mb-4">3.8M ELEVATED AGRIVOLTAIC CANOPY</h3>
          <p class="text-zinc-300 text-sm leading-relaxed mb-6">
            Structural clearance of 3.8 meters accommodates standard agricultural tractors and combine harvesters. Light transmission optimized to 60% Photosynthetically Active Radiation (PAR), blocking excess infrared heat while allowing crop photosynthesis.
          </p>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 font-mono text-xs mb-6">
            <div class="bg-black/50 p-4 border border-white/10">
              <span class="text-emerald-400 font-bold">Sub-Surface Pulsed Drip:</span>
              <p class="text-zinc-400 mt-1">Emitters buried at 20cm depth deliver water directly to rhizosphere, preventing 100% of surface evaporative loss.</p>
            </div>
            <div class="bg-black/50 p-4 border border-white/10">
              <span class="text-emerald-400 font-bold">Biochar Soil Inoculation:</span>
              <p class="text-zinc-400 mt-1">Increases soil water-holding capacity by 34% and hosts mycorrhizal fungi to enhance drought resilience.</p>
            </div>
          </div>
          <div class="border-t border-white/10 pt-4 flex justify-end">
            <button onclick="closeModal()" class="btn-spacex-outline text-xs">CLOSE SCHEMATICS</button>
          </div>
        `;
      } else if (type === 'modal-water') {
        content = `
          <div class="font-mono text-xs uppercase tracking-widest text-telemetry-cyan mb-2">HYDRODYNAMICS SPEC // CLOSED-LOOP EXTRACTION</div>
          <h3 class="text-3xl font-black uppercase text-white font-display mb-4">AWG-50K HARVESTER & DEEP AQUIFER RECHARGE</h3>
          <p class="text-zinc-300 text-sm leading-relaxed mb-6">
            Extracts moisture from ambient tropical air using rotating metal-organic framework (MOF) solid-state desiccant wheels, regenerated with low-grade solar thermal heat (65°C).
          </p>
          <div class="space-y-3 font-mono text-xs mb-6">
            <div class="p-3 bg-white/5 border border-white/10">
              <span class="text-telemetry-cyan font-bold">Pressurized Aquifer Injection:</span> High-pressure multistage pumps inject purified water into deep sandstone/limestone aquifers at 300m depth, building a sovereign strategic water bank safe from evaporation.
            </div>
            <div class="p-3 bg-white/5 border border-white/10">
              <span class="text-telemetry-cyan font-bold">Remineralization Skid:</span> Injects calcium, magnesium, and bicarbonate to ensure water meets international physiological drinking standards.
            </div>
          </div>
          <div class="border-t border-white/10 pt-4 flex justify-end">
            <button onclick="closeModal()" class="btn-spacex-outline text-xs">CLOSE HYDRO SPEC</button>
          </div>
        `;
      } else if (type === 'modal-medical') {
        content = `
          <div class="font-mono text-xs uppercase tracking-widest text-red-400 mb-2">CLINICAL DEFENSE // ISO MOBILE TRIAGE POD</div>
          <h3 class="text-3xl font-black uppercase text-white font-display mb-4">COLD-CHAIN LIFE SUPPORT & HEATSTROKE CLINIC</h3>
          <p class="text-zinc-300 text-sm leading-relaxed mb-6">
            Engineered within ISO 20ft and 40ft high-cube shipping containers, lined with 50mm silica aerogel insulation. Features double airlock vestibules maintaining sterile negative-pressure interior environment.
          </p>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 font-mono text-xs mb-6">
            <div class="bg-black/50 p-4 border border-white/10">
              <span class="text-red-400 font-bold">Vaccine & Drug Cold Bank:</span>
              <p class="text-zinc-400 mt-1">Dual-redundant Stirling engine coolers + PCM packs holding +2°C to +8°C for 72 hours under zero external power.</p>
            </div>
            <div class="bg-black/50 p-4 border border-white/10">
              <span class="text-red-400 font-bold">Heatstroke Cooling Suite:</span>
              <p class="text-zinc-400 mt-1">Evaporative misting tents and conductive chilled water mattress reanimation bays for critical heatstroke patients.</p>
            </div>
          </div>
          <div class="border-t border-white/10 pt-4 flex justify-end">
            <button onclick="closeModal()" class="btn-spacex-outline text-xs">CLOSE CLINICAL SPEC</button>
          </div>
        `;
      }

      document.getElementById('modal-content').innerHTML = content;
      document.getElementById('modal-container').classList.remove('hidden');
    }

    function closeModal() {
      document.getElementById('modal-container').classList.add('hidden');
    }

    // Close on background click
    document.getElementById('modal-container').addEventListener('click', function(e) {
      if (e.target === this) closeModal();
    });

    // Close on Escape key
    window.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') closeModal();
    });

    // -----------------------------------------------------------------------
    // COPY EMAIL & FORM DISPATCH
    // -----------------------------------------------------------------------
    function copyEmailToClipboard() {
      const email = 'jeffersonrrufino@gmail.com';
      navigator.clipboard.writeText(email).then(() => {
        const notif = document.getElementById('copy-notification');
        notif.classList.remove('hidden');
        const btn = document.getElementById('copy-email-btn');
        btn.innerText = 'COPIED TO CLIPBOARD ✓';
        setTimeout(() => {
          notif.classList.add('hidden');
          btn.innerText = 'COPY EMAIL ADDRESS';
        }, 3000);
      });
    }

    function handleFormSubmit(e) {
      e.preventDefault();
      const org = document.getElementById('form-org').value;
      const email = document.getElementById('form-email').value;
      const region = document.getElementById('form-region').value;
      const pop = document.getElementById('form-pop').value;
      const message = document.getElementById('form-message').value;

      const mods = [];
      if (document.getElementById('mod-satellite').checked) mods.push('Satellite Telemetry');
      if (document.getElementById('mod-solar').checked) mods.push('Solar Canopies & Storage');
      if (document.getElementById('mod-agri').checked) mods.push('Agrivoltaic Biospheres');
      if (document.getElementById('mod-water').checked) mods.push('AWG & Aquifer Recharge');
      if (document.getElementById('mod-medical').checked) mods.push('Cold-Chain Clinics');

      const subject = `The Photosynthesis Project Inquiry - ${org}`;
      const body = `TO: JEFFERSON RAFAEL RUFINO (RUFINO VENTURES)
RE: THE PHOTOSYNTHESIS PROJECT & THE RUFINO SYNTHESIS DISPATCH
==============================================================
ORGANIZATION / SOVEREIGN ENTITY: ${org}
OFFICIAL CONTACT EMAIL: ${email}
TARGET REGION: ${region}
EXPOSED POPULATION: ${pop}

OPERATIONAL VECTORS REQUESTED:
- ${mods.join('\\n- ')}

EMERGENCY STATEMENT & REQUIREMENTS:
${message}
==============================================================
TRANSMITTED VIA RUFINOVENTURES.COM MISSION CONTROL`;

      const mailtoUrl = `mailto:jeffersonrrufino@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
      
      document.getElementById('form-success').classList.remove('hidden');
      window.location.href = mailtoUrl;
    }

    // -----------------------------------------------------------------------
    // LIVE UTC CLOCK
    // -----------------------------------------------------------------------
    function updateUtcClock() {
      const now = new Date();
      const utcString = now.toUTCString().split(' ')[4] + ' UTC';
      const clockEl = document.getElementById('utc-clock');
      if (clockEl) clockEl.innerText = utcString;
    }
    setInterval(updateUtcClock, 1000);
    updateUtcClock();

    // -----------------------------------------------------------------------
    // MOBILE MENU TOGGLE
    // -----------------------------------------------------------------------
    const mobileBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    if (mobileBtn && mobileMenu) {
      mobileBtn.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
      });
      // Close menu when a link is clicked
      mobileMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
          mobileMenu.classList.add('hidden');
        });
      });
    }

    // Initialize page components
    window.addEventListener('DOMContentLoaded', () => {
      renderNations(NATIONS_DATA);
      recalculateModel();
    });
  </script>

</body>
</html>
"""

if __name__ == '__main__':
    html_content = build_html()
    base_dir = '/Users/thehighlandboy/Downloads/RUFINOVENTURES'
    targets = [
        os.path.join(base_dir, 'index.html'),
        os.path.join(base_dir, 'RUFINOVENTURES.html'),
        os.path.join(base_dir, 'PHOTOSYNTHESIS_PROJECT_PREVIEW.html')
    ]
    for target in targets:
        with open(target, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Successfully generated {target} ({len(html_content)} bytes)")

