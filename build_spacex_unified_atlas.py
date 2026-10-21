#!/usr/bin/env python3
"""
build_spacex_unified_atlas.py
Generates the definitive, SpaceX-minimalist, fully-animated, interactive
RUFINO VENTURES / UNIVERSAL REALITY ATLAS landing page incorporating:
- The 2-Page Executive Summary: "Unified Field & Metamaterial Synthesis (21,000-Page Empirical Corpus)"
- Full animations: Dynamic canvas quantum-lattice particle field, wave propagation visualizer, interactive HUD telemetry
- Interactive parts: Master equation term inspector, 3-scale frontier comparison switcher, live empirical validation labs (99.98% Phase Coherence, Zero-Loss Dispersion, Gravitational-EM Coupling)
- Interactive diagrams: Predecessor smooth Riemannian manifold vs. Discrete dynamic metamaterial lattice, 3-Frontier Bridge SVG
- HD background imagery per pane with dark scrim overlays
- Full 9-tab navigation network
"""

import os

def generate_page():
    html = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>RUFINO VENTURES // UNIFIED FIELD & METAMATERIAL SYNTHESIS</title>
  <meta name="description" content="Unified Field & Metamaterial Synthesis. 21,000-page empirical corpus and the Universal Reality Atlas by Jefferson Rafael Rufino." />
  <link rel="canonical" href="https://rufinoventures.com/" />
  
  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://rufinoventures.com/" />
  <meta property="og:title" content="RUFINO VENTURES // UNIFIED FIELD & METAMATERIAL SYNTHESIS" />
  <meta property="og:description" content="21,000-Page Empirical Corpus: Unification of gravitation, quantum coupling, and structural stress-tensors across macro and micro scales." />
  <meta property="og:image" content="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1200&q=80" />

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Cpolygon points='16,2 30,9 30,23 16,30 2,23 2,9' fill='%23000000' stroke='%23ffffff' stroke-width='1.5'/%3E%3Ccircle cx='16' cy='16' r='3' fill='%23ffffff'/%3E%3C/svg%3E">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- KaTeX for pristine mathematical rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\\\(', right: '\\\\)', display: false}]});"></script>

  <!-- Google Fonts: Space Grotesk, Inter, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700;800;900&family=Inter:wght@200;300;400;500;600;700;800;900&family=JetBrains+Mono:wght@300;400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['Geist', 'Inter', '-apple-system', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
            display: ['Space Grotesk', 'Geist', 'sans-serif'],
          },
          colors: {
            space: {
              950: '#000000',
              900: '#050505',
              850: '#0a0a0a',
              800: '#121212',
              750: '#18181b',
              700: '#27272a',
            }
          }
        }
      }
    }
  </script>

  <style>
    /* SpaceX Minimalist Resets */
    html {
      scroll-behavior: smooth;
      background-color: #000000;
      color: #f4f4f5;
    }
    body {
      font-family: 'Inter', -apple-system, sans-serif;
      background-color: #000000;
      overflow-x: hidden;
    }

    /* Custom high-contrast scrollbars */
    ::-webkit-scrollbar { width: 5px; height: 5px; }
    ::-webkit-scrollbar-track { background: #000000; }
    ::-webkit-scrollbar-thumb { background: #27272a; border-radius: 2px; }
    ::-webkit-scrollbar-thumb:hover { background: #71717a; }

    /* HUD Reticle & Corner Brackets */
    .hud-box {
      position: relative;
      background: rgba(5, 5, 8, 0.78);
      backdrop-filter: blur(20px);
      border: 1px solid rgba(255, 255, 255, 0.12);
    }
    .hud-box::before {
      content: '';
      position: absolute;
      top: -1px;
      left: -1px;
      width: 10px;
      height: 10px;
      border-top: 2px solid #ffffff;
      border-left: 2px solid #ffffff;
    }
    .hud-box::after {
      content: '';
      position: absolute;
      bottom: -1px;
      right: -1px;
      width: 10px;
      height: 10px;
      border-bottom: 2px solid #ffffff;
      border-right: 2px solid #ffffff;
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
      padding: 0.85rem 2rem;
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
      background-color: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(12px);
      color: #ffffff;
      font-family: 'JetBrains Mono', monospace;
      font-weight: 600;
      font-size: 0.75rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      padding: 0.85rem 2rem;
      border: 1px solid rgba(255, 255, 255, 0.3);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
    }
    .btn-spacex-outline:hover {
      border-color: #ffffff;
      background-color: #ffffff;
      color: #000000;
      box-shadow: 0 0 20px rgba(255, 255, 255, 0.25);
    }

    /* HD Pane Scrims */
    .pane-scrim {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.55) 45%, rgba(0,0,0,0.92) 100%);
      pointer-events: none;
    }
    .pane-scrim-heavy {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(0,0,0,0.92) 0%, rgba(0,0,0,0.72) 50%, rgba(0,0,0,0.98) 100%);
      pointer-events: none;
    }

    /* Animated pulse dot */
    @keyframes pulse-dot {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.35; transform: scale(0.8); }
    }
    .pulse-beacon {
      animation: pulse-dot 2s infinite ease-in-out;
    }

    /* Monospace Grid overlay */
    .tech-grid {
      background-image: radial-gradient(rgba(255, 255, 255, 0.08) 1px, transparent 1px);
      background-size: 32px 32px;
    }

    /* Glow utilities */
    .text-glow {
      text-shadow: 0 0 15px rgba(255, 255, 255, 0.4);
    }
  </style>
</head>
<body class="bg-black text-zinc-100 antialiased selection:bg-white selection:text-black">

  <!-- ========================================================================= -->
  <!-- AEROSPACE TOP NAVIGATION (ALL 9 TABS) -->
  <!-- ========================================================================= -->
  <header class="fixed top-0 left-0 right-0 z-50 bg-black/85 backdrop-blur-md border-b border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <!-- Logo & Identity -->
      <a href="/" class="flex items-center space-x-3 group">
        <div class="w-8 h-8 bg-white text-black font-display font-black flex items-center justify-center text-sm tracking-tighter transition-transform group-hover:scale-105">
          RV
        </div>
        <div>
          <span class="font-display font-bold text-white text-sm tracking-wider uppercase block leading-none">RUFINO VENTURES</span>
          <span class="font-mono text-[9px] text-zinc-400 uppercase tracking-widest block mt-0.5">Unified Field Synthesis // 21,000p</span>
        </div>
      </a>

      <!-- Desktop Links (All 9 Tabs) -->
      <nav class="hidden xl:flex items-center space-x-6 text-[11px] font-mono">
        <a href="/" class="text-white font-bold border-b-2 border-white pb-1 tracking-wider">ATLAS</a>
        <a href="/founder" class="text-zinc-400 hover:text-white transition pb-1 tracking-wider">FOUNDER</a>
        <a href="/realities" class="text-zinc-400 hover:text-white transition pb-1 tracking-wider">REALITIES</a>
        <a href="/LERM" class="text-zinc-400 hover:text-white transition pb-1 tracking-wider">LERM</a>
        <a href="/photosynthesisproject" class="text-zinc-400 hover:text-white transition pb-1 tracking-wider">PHOTOSYNTHESIS</a>
        <a href="/shopfamcollective" class="text-zinc-400 hover:text-white transition pb-1 tracking-wider">SHOPFAM</a>
        <a href="/scientists" class="text-zinc-400 hover:text-white transition pb-1 tracking-wider">SCIENTISTS</a>
        <a href="/build" class="text-zinc-400 hover:text-white transition pb-1 tracking-wider">BUILD</a>
        <a href="/contactus" class="text-zinc-400 hover:text-white transition pb-1 tracking-wider">CONTACT</a>
      </nav>

      <!-- HUD Status Badge -->
      <div class="hidden md:flex items-center space-x-3 font-mono text-[10px] text-zinc-400 border border-white/10 px-3 py-1.5 bg-zinc-950/80">
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 pulse-beacon"></span>
        <span class="text-zinc-300">PHASE COHERENCE: <strong class="text-white">99.98%</strong></span>
        <span class="text-zinc-600">|</span>
        <span>CORPUS: <strong class="text-white">21,000p</strong></span>
      </div>

      <!-- Mobile Menu Button -->
      <button id="mobile-toggle" class="xl:hidden text-zinc-400 hover:text-white p-2">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
      </button>
    </div>

    <!-- Mobile Drawer -->
    <div id="mobile-menu" class="hidden xl:hidden bg-zinc-950 border-b border-white/10 px-6 py-4 space-y-3 font-mono text-xs">
      <a href="/" class="block text-white font-bold py-1">ATLAS (UNIFIED SYNTHESIS)</a>
      <a href="/founder" class="block text-zinc-400 hover:text-white py-1">FOUNDER (UNSANITIZED ODYSSEY)</a>
      <a href="/realities" class="block text-zinc-400 hover:text-white py-1">REALITIES (120 ADAPTERS)</a>
      <a href="/LERM" class="block text-zinc-400 hover:text-white py-1">LERM (PAX SILICA & 2027 RADAR)</a>
      <a href="/photosynthesisproject" class="block text-zinc-400 hover:text-white py-1">PHOTOSYNTHESIS (SUPER EL NIÑO)</a>
      <a href="/shopfamcollective" class="block text-zinc-400 hover:text-white py-1">SHOPFAM (ARCH FILE & MU+)</a>
      <a href="/scientists" class="block text-zinc-400 hover:text-white py-1">SCIENTISTS (INTELLECTUAL LINEAGE)</a>
      <a href="/build" class="block text-zinc-400 hover:text-white py-1">BUILD (COALITION & CAPITAL)</a>
      <a href="/contactus" class="block text-zinc-400 hover:text-white py-1">CONTACT (SECURE PROTOCOL)</a>
    </div>
  </header>

  <!-- ========================================================================= -->
  <!-- PANE 1: HERO // UNIFIED FIELD & METAMATERIAL SYNTHESIS -->
  <!-- ========================================================================= -->
  <section id="hero" class="relative min-h-screen w-full flex flex-col justify-between pt-28 pb-16 px-6 sm:px-12 lg:px-20 overflow-hidden bg-black">
    <!-- HD Background Image (Orbital Space & Earth Curvature) -->
    <div class="absolute inset-0 z-0 pointer-events-none">
      <img 
        src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=2560&q=85" 
        alt="Orbital view of Earth and space curvature" 
        class="w-full h-full object-cover object-center filter brightness-[0.55] contrast-[1.25]" 
        loading="eager"
      />
      <div class="pane-scrim"></div>
    </div>

    <!-- Live Interactive Quantum Lattice & Dynamic Curvature Canvas -->
    <canvas id="lattice-canvas" class="absolute inset-0 z-10 w-full h-full pointer-events-auto opacity-70"></canvas>

    <!-- Top Telemetry Header -->
    <div class="relative z-20 max-w-7xl mx-auto w-full pt-4">
      <div class="inline-flex flex-wrap items-center gap-3 border border-white/20 bg-black/80 px-4 py-2 font-mono text-[10px] uppercase tracking-widest text-zinc-300 backdrop-blur-md">
        <span class="flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-white pulse-beacon"></span>
          SOURCE SCOPE: <strong class="text-white">21,000-PAGE EMPIRICAL CORPUS</strong>
        </span>
        <span class="text-zinc-600">|</span>
        <span>DOMAIN: <strong class="text-white">THEORETICAL PHYSICS & STRUCTURE</strong></span>
        <span class="text-zinc-600">|</span>
        <span>STATUS: <strong class="text-white">EXECUTIVE SUMMARY</strong></span>
      </div>
    </div>

    <!-- Main Title & Core Axiom -->
    <div class="relative z-20 max-w-7xl mx-auto w-full my-auto py-12">
      <div class="max-w-4xl">
        <p class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-3 flex items-center gap-2">
          <span class="w-6 h-[1px] bg-white"></span>
          CANONICAL SCIENTIFIC DISCLOSURE // OCTOBER 2026
        </p>
        <h1 class="font-display font-black text-4xl sm:text-6xl lg:text-7xl tracking-tighter text-white uppercase leading-[0.95] mb-6 text-glow">
          Unified Field &<br/>Metamaterial Synthesis
        </h1>
        <p class="text-zinc-300 text-base sm:text-lg lg:text-xl font-light leading-relaxed max-w-3xl mb-8">
          Condensing the monumental <strong>21,000-page foundational manuscript</strong> into a rigorous overview of its core mathematical, empirical, and structural breakthroughs. Originating from multi-decade empirical observation and advanced computational modeling, the source text bridges <em>quantum electrodynamics</em>, <em>general relativity</em>, and <em>non-Euclidean structural topologies</em> into a single unified framework.
        </p>

        <!-- Core Axiom Card -->
        <div class="hud-box p-6 sm:p-8 max-w-3xl mb-8">
          <div class="flex items-center justify-between mb-3 border-b border-white/10 pb-2">
            <span class="font-mono text-[10px] tracking-widest uppercase text-white font-bold flex items-center gap-2">
              <span class="w-2 h-2 bg-white"></span>
              CORE AXIOM OF META-SPATIAL EQUIVALENCE
            </span>
            <span class="font-mono text-[9px] text-zinc-500">CORPUS SEC. 1.0</span>
          </div>
          <p class="text-white font-mono text-sm sm:text-base leading-relaxed tracking-wide">
            "Physical state space is defined as an interactive matrix where mass-energy distributions and spatial curvature are emergent properties of underlying information-density fluctuations governed by high-dimensional manifold transformations."
          </p>
        </div>

        <!-- Action CTAs -->
        <div class="flex flex-wrap items-center gap-4">
          <a href="#master-equation" class="btn-spacex-white">
            EXPLORE MASTER EQUATION
          </a>
          <a href="#frontiers" class="btn-spacex-outline">
            INSPECT 3 FRONTIERS
          </a>
          <a href="#empirical-validation" class="btn-spacex-outline">
            RUN EMPIRICAL TESTS (99.98%)
          </a>
        </div>
      </div>
    </div>

    <!-- Bottom HUD Telemetry Rail -->
    <div class="relative z-20 max-w-7xl mx-auto w-full border-t border-white/15 pt-6 flex flex-wrap items-center justify-between gap-4 font-mono text-[10px] text-zinc-400">
      <div class="flex items-center gap-6">
        <div>COORDINATES: <span class="text-white">14.5995° N, 120.9842° E</span></div>
        <div>FIELD TENSOR: <span class="text-white">ACTIVE (NON-ABELIAN)</span></div>
        <div>DISPERSION: <span class="text-white">ZERO-LOSS BOUNDARY</span></div>
      </div>
      <div class="flex items-center gap-2 text-zinc-500">
        <span class="pulse-beacon w-1.5 h-1.5 rounded-full bg-white"></span>
        INTERACTIVE CANVAS ACTIVE // MOVE CURSOR TO WARP TENSOR LATTICE
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- PANE 2: MASTER EQUATION & INTERACTIVE TERM INSPECTOR -->
  <!-- ========================================================================= -->
  <section id="master-equation" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-black border-t border-white/10">
    <!-- HD Background Image (Laser Optics & Quantum Interferometry) -->
    <div class="absolute inset-0 z-0 pointer-events-none">
      <img 
        src="https://images.unsplash.com/photo-1507499739999-097706ad8914?auto=format&fit=crop&w=2560&q=85" 
        alt="Laser interferometry and quantum optical coherence" 
        class="w-full h-full object-cover object-center filter brightness-[0.45] contrast-[1.3]" 
        loading="lazy"
      />
      <div class="pane-scrim-heavy"></div>
    </div>

    <div class="relative z-20 max-w-7xl mx-auto w-full my-auto">
      <!-- Section Header -->
      <div class="flex items-center justify-between border-b border-white/15 pb-4 mb-8">
        <div>
          <span class="font-mono text-[10px] uppercase tracking-widest text-zinc-400 block mb-1">
            SECTION 2.0 // CONSOLIDATED MATHEMATICS
          </span>
          <h2 class="font-display font-black text-3xl sm:text-5xl text-white uppercase tracking-tight">
            Consolidated Master Equations
          </h2>
        </div>
        <div class="hidden sm:block font-mono text-right text-xs text-zinc-400">
          <div>SCALE UNIFICATION</div>
          <div class="text-white font-bold">MACRO ⇄ MICRO</div>
        </div>
      </div>

      <p class="text-zinc-300 text-base sm:text-lg font-light max-w-3xl mb-8 leading-relaxed">
        The primary breakthrough of the corpus is the <strong>unification of gravitation, quantum coupling, and structural stress-tensors</strong> across macro and micro physical scales:
      </p>

      <!-- Massive Interactive Equation Display -->
      <div class="hud-box p-8 sm:p-12 mb-8 bg-black/90">
        <div class="text-center overflow-x-auto py-6">
          <div class="text-2xl sm:text-4xl lg:text-5xl text-white font-mono tracking-tight leading-relaxed select-all">
            $$\Psi(x, t) = \int_{\Omega} \left[ \nabla \times (G_{\mu\nu} + \Lambda g_{\mu\nu}) \right] \cdot \exp\left( \frac{i}{\hbar} \sum_{k=1}^N \alpha_k \Phi_k(x) \right) d\Omega$$
          </div>
        </div>

        <p class="font-mono text-[10px] text-zinc-400 text-center tracking-widest uppercase mt-2">
          [ CLICK ANY TERM BELOW TO INSPECT ITS MATHEMATICAL DECOMPOSITION & PHYSICAL REALITY ]
        </p>

        <!-- Interactive Term Selector Buttons -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mt-6">
          <button onclick="inspectTerm('psi')" id="btn-psi" class="term-btn border border-white bg-white text-black font-mono text-xs py-3 px-2 text-center uppercase tracking-wider font-bold transition">
            Ψ(x, t)
          </button>
          <button onclick="inspectTerm('curl')" id="btn-curl" class="term-btn border border-white/20 bg-zinc-950/80 text-zinc-300 hover:border-white font-mono text-xs py-3 px-2 text-center uppercase tracking-wider font-bold transition">
            ∇ × (G_μν + Λg_μν)
          </button>
          <button onclick="inspectTerm('phase')" id="btn-phase" class="term-btn border border-white/20 bg-zinc-950/80 text-zinc-300 hover:border-white font-mono text-xs py-3 px-2 text-center uppercase tracking-wider font-bold transition">
            exp( i/ℏ ∑ α_k Φ_k )
          </button>
          <button onclick="inspectTerm('domain')" id="btn-domain" class="term-btn border border-white/20 bg-zinc-950/80 text-zinc-300 hover:border-white font-mono text-xs py-3 px-2 text-center uppercase tracking-wider font-bold transition">
            ∫_Ω ... dΩ
          </button>
        </div>
      </div>

      <!-- Dynamic Term Inspector HUD -->
      <div id="inspector-display" class="hud-box p-6 sm:p-8 bg-zinc-950/90 border border-white/20">
        <div class="flex flex-wrap items-center justify-between border-b border-white/10 pb-3 mb-4">
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 bg-emerald-400"></span>
            <span id="inspect-title" class="font-display font-bold text-lg text-white uppercase tracking-wider">
              Ψ(x, t) — CONSOLIDATED STATE TENSOR & WAVEFUNCTION
            </span>
          </div>
          <span id="inspect-tag" class="font-mono text-[10px] px-2 py-0.5 bg-white/10 text-white uppercase">
            TOTAL SYSTEM MANIFESTATION
          </span>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div class="lg:col-span-2 space-y-3">
            <p id="inspect-desc" class="text-zinc-300 text-sm leading-relaxed font-light">
              The overarching state wavefunction bridging microscopic probability densities and macroscopic spacetime curvature. It represents physical reality not as separated particles in a detached container, but as an interactive information-density matrix.
            </p>
            <div class="border border-white/10 p-3 bg-black/60 font-mono text-xs text-zinc-300 space-y-1">
              <div><strong>Classical Analogue:</strong> <span id="inspect-classical" class="text-zinc-400">Schrödinger state vector |Ψ⟩ decoupled from Einstein metric g_μν</span></div>
              <div><strong>Novel Synthesis:</strong> <span id="inspect-novel" class="text-white">Simultaneous coupling of structural elasticity and field dynamics via non-Abelian symmetry</span></div>
              <div><strong>Empirical Measurement:</strong> <span id="inspect-empirical" class="text-emerald-400">Phase coherence verified to 99.98% agreement in synthetic crystal lattices</span></div>
            </div>
          </div>

          <!-- Live Term Waveform Simulator -->
          <div class="border border-white/10 p-3 bg-black/80 flex flex-col justify-between">
            <div class="font-mono text-[10px] text-zinc-400 uppercase tracking-widest mb-1 flex items-center justify-between">
              <span>REAL-TIME FIELD HARMONIC</span>
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 pulse-beacon"></span>
            </div>
            <canvas id="term-wave-canvas" class="w-full h-24 bg-zinc-950 border border-white/5"></canvas>
            <div class="font-mono text-[9px] text-zinc-500 mt-2 flex justify-between">
              <span>RES: 1024 PTS</span>
              <span id="wave-mode">HARMONIC MODE: COUPLED</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- PANE 3: STRUCTURAL LINEAGE // PREDECESSORS VS NOVEL TOPOLOGY -->
  <!-- ========================================================================= -->
  <section id="lineage" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-black border-t border-white/10">
    <!-- HD Background Image (Semiconductor Metamaterial Array) -->
    <div class="absolute inset-0 z-0 pointer-events-none">
      <img 
        src="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=2560&q=85" 
        alt="Metamaterial wafer topology and crystalline lattices" 
        class="w-full h-full object-cover object-center filter brightness-[0.4] contrast-[1.35]" 
        loading="lazy"
      />
      <div class="pane-scrim-heavy"></div>
    </div>

    <div class="relative z-20 max-w-7xl mx-auto w-full my-auto">
      <!-- Section Header -->
      <div class="flex items-center justify-between border-b border-white/15 pb-4 mb-8">
        <div>
          <span class="font-mono text-[10px] uppercase tracking-widest text-zinc-400 block mb-1">
            SECTION 3.0 // ARCHITECTURAL EVOLUTION
          </span>
          <h2 class="font-display font-black text-3xl sm:text-5xl text-white uppercase tracking-tight">
            Structural Lineage: Predecessors vs. Novel Models
          </h2>
        </div>
        <div class="font-mono text-xs text-zinc-400 text-right">
          <div>PARADIGM SHIFT</div>
          <div class="text-white font-bold">CONTINUOUS ➔ DISCRETE LATTICE</div>
        </div>
      </div>

      <!-- Interactive Predecessor vs Novel Topology Comparison -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">
        <!-- Classical Box -->
        <div class="hud-box p-8 bg-zinc-950/85 border border-white/15">
          <div class="flex items-center justify-between border-b border-white/10 pb-3 mb-4">
            <h3 class="font-display font-bold text-xl text-zinc-300 uppercase tracking-wider">
              Classical & Relativistic Foundations
            </h3>
            <span class="font-mono text-[9px] px-2 py-0.5 border border-zinc-700 text-zinc-400 uppercase">
              LEGACY REDUCTIONISM
            </span>
          </div>
          <p class="text-zinc-400 text-sm leading-relaxed mb-6">
            Relied on <strong>smooth pseudo-Riemannian manifolds</strong>, treating spacetime as a passive background stage and quantum mechanics as localized probabilistic perturbations.
          </p>
          <div class="space-y-3 font-mono text-xs text-zinc-400 border-t border-white/10 pt-4">
            <div class="flex items-start gap-2">
              <span class="text-red-400">✗</span>
              <span><strong>Spacetime:</strong> Passive container stage, unaffected by internal information boundaries.</span>
            </div>
            <div class="flex items-start gap-2">
              <span class="text-red-400">✗</span>
              <span><strong>Quantum Scale:</strong> Localized probabilistic perturbations prone to short-distance singularities ($r \to 0, \infty$).</span>
            </div>
            <div class="flex items-start gap-2">
              <span class="text-red-400">✗</span>
              <span><strong>Metric:</strong> Smooth differential manifold without intrinsic structural elasticity.</span>
            </div>
          </div>
        </div>

        <!-- Novel Metamaterial Box -->
        <div class="hud-box p-8 bg-black/90 border border-white">
          <div class="flex items-center justify-between border-b border-white/20 pb-3 mb-4">
            <h3 class="font-display font-bold text-xl text-white uppercase tracking-wider flex items-center gap-2">
              <span class="w-2.5 h-2.5 bg-white"></span>
              Novel Metamaterial Topology
            </h3>
            <span class="font-mono text-[9px] px-2 py-0.5 bg-white text-black font-bold uppercase">
              CANONICAL SYNTHESIS
            </span>
          </div>
          <p class="text-zinc-200 text-sm leading-relaxed mb-6 font-light">
            Introduces <strong>discrete dynamic lattice geometries</strong> where structural elasticity and field dynamics are coupled via non-Abelian symmetry operations.
          </p>
          <div class="space-y-3 font-mono text-xs text-zinc-200 border-t border-white/15 pt-4">
            <div class="flex items-start gap-2">
              <span class="text-emerald-400">✓</span>
              <span><strong>Spacetime:</strong> Discrete interactive matrix whose curvature is an emergent information density gradient.</span>
            </div>
            <div class="flex items-start gap-2">
              <span class="text-emerald-400">✓</span>
              <span><strong>Quantum Scale:</strong> Discrete topological flux chains eliminating short-distance infinities without renormalization tricks.</span>
            </div>
            <div class="flex items-start gap-2">
              <span class="text-emerald-400">✓</span>
              <span><strong>Field Coupling:</strong> Direct non-Abelian gauge operations linking mechanical stress-tensors and gravitational metrics.</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Interactive Architectural Comparison Diagram (SVG) -->
      <div class="hud-box p-6 bg-zinc-950/95 border border-white/20">
        <div class="flex items-center justify-between border-b border-white/10 pb-3 mb-4">
          <div class="font-mono text-xs font-bold text-white uppercase tracking-wider">
            TOPOLOGICAL COMPARISON DIAGRAM // GEOMETRIC DISCRETIZATION
          </div>
          <div class="flex items-center gap-2 font-mono text-[10px]">
            <button onclick="toggleDiagramMode('smooth')" id="btn-diag-smooth" class="px-3 py-1 border border-white/30 text-zinc-400 hover:text-white transition">
              1. SMOOTH MANIFOLD
            </button>
            <button onclick="toggleDiagramMode('lattice')" id="btn-diag-lattice" class="px-3 py-1 border border-white bg-white text-black font-bold transition">
              2. DYNAMIC LATTICE (NOVEL)
            </button>
          </div>
        </div>

        <!-- SVG Architecture Visualizer -->
        <div class="relative w-full h-64 sm:h-80 bg-black border border-white/10 flex items-center justify-center overflow-hidden">
          <svg id="diagram-svg" viewBox="0 0 800 300" class="w-full h-full">
            <!-- Dynamic elements generated via JS -->
          </svg>
          <div id="diagram-caption" class="absolute bottom-3 left-4 right-4 bg-black/80 px-3 py-2 border border-white/10 font-mono text-[10px] text-zinc-300 flex justify-between">
            <span>ACTIVE TOPOLOGY: NOVEL DYNAMIC LATTICE</span>
            <span class="text-emerald-400">COUPLING: NON-ABELIAN SYMMETRY OPERATIONS</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- PANE 4: TRANSLATION ACROSS EXTERNALITIES & 3 FRONTIERS -->
  <!-- ========================================================================= -->
  <section id="frontiers" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-black border-t border-white/10">
    <!-- HD Background Image (Deep Space Gravitational Lensing & Astrophysics) -->
    <div class="absolute inset-0 z-0 pointer-events-none">
      <img 
        src="https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&w=2560&q=85" 
        alt="Gravitational lensing and cosmic deep field" 
        class="w-full h-full object-cover object-center filter brightness-[0.45] contrast-[1.3]" 
        loading="lazy"
      />
      <div class="pane-scrim-heavy"></div>
    </div>

    <div class="relative z-20 max-w-7xl mx-auto w-full my-auto">
      <!-- Section Header -->
      <div class="flex items-center justify-between border-b border-white/15 pb-4 mb-8">
        <div>
          <span class="font-mono text-[10px] uppercase tracking-widest text-zinc-400 block mb-1">
            SECTION 4.0 // SCALE TRANSLATIONS
          </span>
          <h2 class="font-display font-black text-3xl sm:text-5xl text-white uppercase tracking-tight">
            Translation Across Externalities of Reality
          </h2>
        </div>
        <div class="font-mono text-xs text-zinc-400 text-right">
          <div>CORPUS SCOPE</div>
          <div class="text-white font-bold">21,000-PAGE TREATISE</div>
        </div>
      </div>

      <p class="text-zinc-300 text-base sm:text-lg font-light max-w-3xl mb-8 leading-relaxed">
        The original 21,000-page treatise maps mathematical transformations across distinct observational scales and boundary conditions (the "externalities" of physical systems):
      </p>

      <!-- Interactive 3-Frontier Switcher Tabs -->
      <div class="flex flex-wrap items-center gap-2 mb-6 font-mono text-xs">
        <button onclick="switchFrontier('all')" id="btn-f-all" class="frontier-tab border border-white bg-white text-black font-bold py-2 px-4 uppercase tracking-wider transition">
          ALL 3 SCALES (SYNTHESIS)
        </button>
        <button onclick="switchFrontier('quantum')" id="btn-f-quantum" class="frontier-tab border border-white/20 bg-zinc-950/80 text-zinc-300 hover:border-white py-2 px-4 uppercase tracking-wider transition">
          1. QUANTUM SCALE
        </button>
        <button onclick="switchFrontier('macro')" id="btn-f-macro" class="frontier-tab border border-white/20 bg-zinc-950/80 text-zinc-300 hover:border-white py-2 px-4 uppercase tracking-wider transition">
          2. MACRO / RELATIVISTIC
        </button>
        <button onclick="switchFrontier('cosmo')" id="btn-f-cosmo" class="frontier-tab border border-white/20 bg-zinc-950/80 text-zinc-300 hover:border-white py-2 px-4 uppercase tracking-wider transition">
          3. COSMOLOGICAL
        </button>
      </div>

      <!-- The Canonical Frontier Comparison Table (Interactive HUD) -->
      <div class="hud-box overflow-hidden mb-8 border border-white/20 bg-zinc-950/90">
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse">
            <thead>
              <tr class="border-b border-white/20 bg-white/5 font-mono text-[10px] text-zinc-400 uppercase tracking-wider">
                <th class="p-4 sm:p-5">Scale Domain</th>
                <th class="p-4 sm:p-5">Classical Formulation</th>
                <th class="p-4 sm:p-5">Unified Corpus Translation</th>
                <th class="p-4 sm:p-5">Empirical Shift</th>
                <th class="p-4 sm:p-5 text-right">Status</th>
              </tr>
            </thead>
            <tbody id="frontier-table-body" class="font-mono text-xs divide-y divide-white/10">
              <!-- Row 1: Quantum -->
              <tr id="row-quantum" class="hover:bg-white/5 transition">
                <td class="p-4 sm:p-5 font-bold text-white uppercase flex items-center gap-2">
                  <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                  Quantum Scale
                </td>
                <td class="p-4 sm:p-5 text-zinc-400">
                  Schrödinger Field Operators
                </td>
                <td class="p-4 sm:p-5 text-white font-bold">
                  Discrete Topological Flux Chains
                </td>
                <td class="p-4 sm:p-5 text-emerald-400 font-bold">
                  Eliminates short-distance infinities
                </td>
                <td class="p-4 sm:p-5 text-right text-zinc-400">
                  <span class="border border-emerald-400/50 text-emerald-300 text-[10px] px-2 py-0.5">RESOLVED</span>
                </td>
              </tr>

              <!-- Row 2: Macro/Relativistic -->
              <tr id="row-macro" class="hover:bg-white/5 transition">
                <td class="p-4 sm:p-5 font-bold text-white uppercase flex items-center gap-2">
                  <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                  Macro / Relativistic
                </td>
                <td class="p-4 sm:p-5 text-zinc-400">
                  Einstein Field Equations
                </td>
                <td class="p-4 sm:p-5 text-white font-bold">
                  Tensor-Lattice Dynamic Curvature
                </td>
                <td class="p-4 sm:p-5 text-emerald-400 font-bold">
                  Integrates stress-energy directly
                </td>
                <td class="p-4 sm:p-5 text-right text-zinc-400">
                  <span class="border border-emerald-400/50 text-emerald-300 text-[10px] px-2 py-0.5">RESOLVED</span>
                </td>
              </tr>

              <!-- Row 3: Cosmological -->
              <tr id="row-cosmo" class="hover:bg-white/5 transition">
                <td class="p-4 sm:p-5 font-bold text-white uppercase flex items-center gap-2">
                  <span class="w-2 h-2 rounded-full bg-purple-400"></span>
                  Cosmological
                </td>
                <td class="p-4 sm:p-5 text-zinc-400">
                  Standard Λ-CDM Model
                </td>
                <td class="p-4 sm:p-5 text-white font-bold">
                  Vacuum Energy Information Density
                </td>
                <td class="p-4 sm:p-5 text-emerald-400 font-bold">
                  Resolves dark energy discrepancy
                </td>
                <td class="p-4 sm:p-5 text-right text-zinc-400">
                  <span class="border border-emerald-400/50 text-emerald-300 text-[10px] px-2 py-0.5">RESOLVED</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Interactive 3-Frontier Bridge Diagram -->
      <div class="hud-box p-6 bg-black/90 border border-white/15">
        <div class="flex items-center justify-between border-b border-white/10 pb-3 mb-4">
          <span class="font-mono text-xs uppercase text-zinc-400 font-bold tracking-wider">
            UNIFIED CONTINUUM DIAGRAM // 3-SCALE TOPOLOGICAL BRIDGE
          </span>
          <span class="font-mono text-[9px] text-zinc-500">
            TOTAL INTEGRATION: 100%
          </span>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-center font-mono text-xs">
          <div class="border border-white/10 p-4 bg-zinc-950">
            <div class="text-cyan-400 font-bold mb-1">SCALE 1: 10⁻³⁵ m</div>
            <div class="text-white text-sm font-bold uppercase mb-2">Discrete Flux Chains</div>
            <p class="text-zinc-400 text-[11px] leading-relaxed">
              No singularities. Space is quantized as topological flux information nodes.
            </p>
          </div>
          <div class="border border-white/20 p-4 bg-zinc-950/80 border-t-2 border-t-white">
            <div class="text-amber-400 font-bold mb-1">SCALE 2: 10⁻¹⁵ m – 10¹² m</div>
            <div class="text-white text-sm font-bold uppercase mb-2">Tensor-Lattice Curvature</div>
            <p class="text-zinc-400 text-[11px] leading-relaxed">
              Stress-energy tensors couple directly into the dynamic lattice geometry.
            </p>
          </div>
          <div class="border border-white/10 p-4 bg-zinc-950">
            <div class="text-purple-400 font-bold mb-1">SCALE 3: 10²⁶ m</div>
            <div class="text-white text-sm font-bold uppercase mb-2">Vacuum Information Density</div>
            <p class="text-zinc-400 text-[11px] leading-relaxed">
              Eliminates the 120-order-of-magnitude cosmological constant catastrophe.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- PANE 5: EMPIRICAL VALIDATION & FINDINGS (VOLUMES 12–45) -->
  <!-- ========================================================================= -->
  <section id="empirical-validation" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-black border-t border-white/10">
    <!-- HD Background Image (Laser Accelerator & High-Flux Lab) -->
    <div class="absolute inset-0 z-0 pointer-events-none">
      <img 
        src="https://images.unsplash.com/photo-1532094349884-543bc11b234d?auto=format&fit=crop&w=2560&q=85" 
        alt="Laser accelerator and high energy laboratory" 
        class="w-full h-full object-cover object-center filter brightness-[0.45] contrast-[1.3]" 
        loading="lazy"
      />
      <div class="pane-scrim-heavy"></div>
    </div>

    <div class="relative z-20 max-w-7xl mx-auto w-full my-auto">
      <!-- Section Header -->
      <div class="flex items-center justify-between border-b border-white/15 pb-4 mb-8">
        <div>
          <span class="font-mono text-[10px] uppercase tracking-widest text-zinc-400 block mb-1">
            SECTION 5.0 // EXPERIMENTAL VERIFICATION
          </span>
          <h2 class="font-display font-black text-3xl sm:text-5xl text-white uppercase tracking-tight">
            Empirical Validation & Findings
          </h2>
        </div>
        <div class="font-mono text-xs text-zinc-400 text-right">
          <div>EVIDENCE BASE</div>
          <div class="text-white font-bold">VOLUMES 12–45</div>
        </div>
      </div>

      <p class="text-zinc-300 text-base sm:text-lg font-light max-w-3xl mb-8 leading-relaxed">
        The findings synthesized across <strong>Volumes 12–45</strong> of the source material detail extensive empirical testing across high-energy interferometry, metamaterial stress tests, and anomalous field measurements:
      </p>

      <!-- 3 Empirical Lab Cards & Simulators -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
        <!-- Lab 1: Phase Coherence Alignment -->
        <div class="hud-box p-6 bg-zinc-950/90 border border-white/20 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-white/10 pb-3 mb-3">
              <span class="font-mono text-xs font-bold text-white uppercase flex items-center gap-2">
                <span class="w-2 h-2 bg-emerald-400 pulse-beacon"></span>
                Phase Coherence Alignment
              </span>
              <span class="font-mono text-[10px] text-emerald-400 font-bold">99.98%</span>
            </div>
            <p class="text-zinc-400 text-xs leading-relaxed mb-4">
              Observed <strong>99.98% agreement</strong> with predicted structural resonance thresholds in synthetic crystal lattices.
            </p>
          </div>

          <!-- Interactive Coherence Simulator -->
          <div class="border border-white/10 p-3 bg-black/80">
            <div class="flex justify-between font-mono text-[10px] text-zinc-400 mb-1">
              <span>LATTICE TUNING FREQ</span>
              <span id="coherence-readout" class="text-white font-bold">99.98% COHERENCE</span>
            </div>
            <input type="range" min="9500" max="10000" value="9998" id="coherence-slider" oninput="updateCoherence(this.value)" class="w-full accent-white bg-zinc-800 cursor-pointer mb-2">
            <div class="w-full bg-zinc-900 h-2 rounded-none overflow-hidden">
              <div id="coherence-bar" class="bg-emerald-400 h-full" style="width: 99.98%;"></div>
            </div>
          </div>
        </div>

        <!-- Lab 2: Anomalous Dispersion Mitigation -->
        <div class="hud-box p-6 bg-zinc-950/90 border border-white/20 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-white/10 pb-3 mb-3">
              <span class="font-mono text-xs font-bold text-white uppercase flex items-center gap-2">
                <span class="w-2 h-2 bg-cyan-400"></span>
                Anomalous Dispersion Mitigation
              </span>
              <span class="font-mono text-[10px] text-cyan-400 font-bold">ZERO-LOSS</span>
            </div>
            <p class="text-zinc-400 text-xs leading-relaxed mb-4">
              Empirical evidence confirms <strong>zero-loss wave propagation</strong> along non-Euclidean boundary layers.
            </p>
          </div>

          <!-- Interactive Dispersion Simulator -->
          <div class="border border-white/10 p-3 bg-black/80 font-mono text-[10px]">
            <div class="flex justify-between text-zinc-400 mb-2">
              <span>WAVEGUIDE MODE:</span>
              <button onclick="toggleWaveguide()" id="btn-waveguide" class="text-white border border-white/30 px-2 py-0.5 hover:border-white">
                NON-EUCLIDEAN (ZERO-LOSS)
              </button>
            </div>
            <div class="space-y-1 text-[9px] text-zinc-400">
              <div class="flex justify-between">
                <span>CLASSICAL ATTENUATION:</span>
                <span class="text-red-400">-18.4 dB/cm (LOSSY)</span>
              </div>
              <div class="flex justify-between">
                <span>NOVEL BOUNDARY LOSS:</span>
                <span id="loss-readout" class="text-emerald-400 font-bold">0.000 dB (ZERO-LOSS)</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Lab 3: Gravitational-Electromagnetic Coupling -->
        <div class="hud-box p-6 bg-zinc-950/90 border border-white/20 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-white/10 pb-3 mb-3">
              <span class="font-mono text-xs font-bold text-white uppercase flex items-center gap-2">
                <span class="w-2 h-2 bg-amber-400"></span>
                Gravitational-EM Coupling
              </span>
              <span class="font-mono text-[10px] text-amber-400 font-bold">μN RESOLUTION</span>
            </div>
            <p class="text-zinc-400 text-xs leading-relaxed mb-4">
              Measured <strong>micro-Newton forces</strong> matching theoretical tensor expectations under ultra-high flux conditions.
            </p>
          </div>

          <!-- Interactive Force Gauge -->
          <div class="border border-white/10 p-3 bg-black/80 font-mono text-[10px]">
            <div class="flex justify-between text-zinc-400 mb-1">
              <span>HIGH-FLUX FIELD STRENGTH</span>
              <span id="force-readout" class="text-amber-400 font-bold">4.82 μN DETECTED</span>
            </div>
            <input type="range" min="10" max="100" value="72" id="flux-slider" oninput="updateFlux(this.value)" class="w-full accent-white bg-zinc-800 cursor-pointer mb-2">
            <div class="text-[9px] text-zinc-500 flex justify-between">
              <span>TENSOR CONCORDANCE: 99.94%</span>
              <span>CALIBRATION: INTERFEROMETER</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Live Empirical Verification HUD Terminal -->
      <div class="hud-box p-6 bg-black/95 border border-white/20 font-mono text-xs">
        <div class="flex items-center justify-between border-b border-white/10 pb-2 mb-3 text-[10px] text-zinc-400">
          <span class="text-white font-bold flex items-center gap-2">
            <span class="w-2 h-2 bg-emerald-400 pulse-beacon"></span>
            EXPERIMENTAL PROTOCOL EXECUTION // RUN IT
          </span>
          <span>CALIBRATED TO S&P 500 / VIX & USGS SEISMIC CAT</span>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 text-zinc-300">
          <div>
            <span class="text-[9px] text-zinc-500 uppercase block">Gutenberg-Richter b-Value</span>
            <span class="text-white font-bold text-sm">1.126 ± 0.042</span>
          </div>
          <div>
            <span class="text-[9px] text-zinc-500 uppercase block">Financial Heavy-Tail α</span>
            <span class="text-white font-bold text-sm">2.709 ± 0.081</span>
          </div>
          <div>
            <span class="text-[9px] text-zinc-500 uppercase block">Boundary Flux Equation</span>
            <span class="text-white font-bold text-sm">∮_∂S F·dA = ∫_V (∇·F)dV</span>
          </div>
          <div>
            <span class="text-[9px] text-zinc-500 uppercase block">Singularity Resolution</span>
            <span class="text-emerald-400 font-bold text-sm">100% REGULARIZED</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- PANE 6: INTERPRETATIONS & SIGNIFICANCE // WHY THIS CORPUS IS EXTRAORDINARY -->
  <!-- ========================================================================= -->
  <section id="significance" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-black border-t border-white/10">
    <!-- HD Background Image (Earth Night Illumination & Interconnection) -->
    <div class="absolute inset-0 z-0 pointer-events-none">
      <img 
        src="https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=2560&q=85" 
        alt="Macro planetary interconnection at night" 
        class="w-full h-full object-cover object-center filter brightness-[0.45] contrast-[1.3]" 
        loading="lazy"
      />
      <div class="pane-scrim-heavy"></div>
    </div>

    <div class="relative z-20 max-w-7xl mx-auto w-full my-auto">
      <div class="max-w-4xl mx-auto">
        <!-- Section Header -->
        <div class="text-center mb-10">
          <span class="font-mono text-xs uppercase tracking-widest text-zinc-400 block mb-2">
            SECTION 6.0 // PARADIGM TRANSFORMATION
          </span>
          <h2 class="font-display font-black text-3xl sm:text-5xl lg:text-6xl text-white uppercase tracking-tight text-glow">
            Interpretations & Significance
          </h2>
        </div>

        <!-- The Canonical Executive Statement -->
        <div class="hud-box p-8 sm:p-12 mb-10 bg-black/90 border border-white">
          <div class="border-b border-white/20 pb-4 mb-6 flex items-center justify-between">
            <span class="font-mono text-xs font-bold text-white uppercase tracking-widest flex items-center gap-2">
              <span class="w-3 h-3 bg-white"></span>
              WHY THIS CORPUS IS EXTRAORDINARY
            </span>
            <span class="font-mono text-[9px] text-zinc-400">CORPUS SEC. 6.0</span>
          </div>

          <blockquote class="text-white font-mono text-base sm:text-lg lg:text-xl leading-relaxed tracking-wide mb-8">
            "By condensing 21,000 pages of rigorous proof into a cohesive framework, this work transitions theoretical physics from passive observation to proactive structural design. It offers humanity the mathematical toolkit needed to engineer spacetime metrics, synthesize exotic metamaterials, and resolve long-standing paradoxes at the boundary of quantum mechanics and cosmology."
          </blockquote>

          <div class="grid grid-cols-1 sm:grid-cols-3 gap-6 pt-6 border-t border-white/10 font-mono text-xs">
            <div>
              <span class="text-zinc-500 uppercase text-[9px] block mb-1">01. TRANSITION</span>
              <strong class="text-white block mb-1">From Observation to Design</strong>
              <p class="text-zinc-400 text-[11px] leading-relaxed">
                Spacetime metrics become engineerable structures rather than immutable passive containers.
              </p>
            </div>
            <div>
              <span class="text-zinc-500 uppercase text-[9px] block mb-1">02. SYNTHESIS</span>
              <strong class="text-white block mb-1">Exotic Metamaterials</strong>
              <p class="text-zinc-400 text-[11px] leading-relaxed">
                Non-Abelian symmetries unlock zero-loss waveguides and mechanical-gravitational coupling.
              </p>
            </div>
            <div>
              <span class="text-zinc-500 uppercase text-[9px] block mb-1">03. RESOLUTION</span>
              <strong class="text-white block mb-1">Boundary Paradoxes Resolved</strong>
              <p class="text-zinc-400 text-[11px] leading-relaxed">
                Unifies short-distance quantum infinities and macroscopic dark energy discrepancies.
              </p>
            </div>
          </div>
        </div>

        <!-- Connection to the Universal Reality Atlas (12 Branches) -->
        <div class="text-center">
          <p class="font-mono text-xs text-zinc-400 uppercase tracking-widest mb-4">
            EXPANDED ACROSS ALL 12 REALITY BRANCHES // 120 REALITY ADAPTERS
          </p>
          <div class="flex flex-wrap justify-center gap-3">
            <a href="/realities" class="btn-spacex-white">
              INSPECT 120 ADAPTERS
            </a>
            <a href="/founder" class="btn-spacex-outline">
              READ THE FOUNDER'S ODYSSEY
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- PANE 7: MISSION DISPATCH // ALL 9 TABS ARCHITECTURE -->
  <!-- ========================================================================= -->
  <section id="dispatch" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-black border-t border-white/10">
    <!-- HD Background Image (SpaceX Starship Telemetry & Launchpad) -->
    <div class="absolute inset-0 z-0 pointer-events-none">
      <img 
        src="https://images.unsplash.com/photo-1517976487502-5c8a4174d8a5?auto=format&fit=crop&w=2560&q=85" 
        alt="Aerospace launch infrastructure and telemetry" 
        class="w-full h-full object-cover object-center filter brightness-[0.4] contrast-[1.35]" 
        loading="lazy"
      />
      <div class="pane-scrim-heavy"></div>
    </div>

    <div class="relative z-20 max-w-7xl mx-auto w-full my-auto">
      <!-- Section Header -->
      <div class="flex items-center justify-between border-b border-white/15 pb-4 mb-10">
        <div>
          <span class="font-mono text-[10px] uppercase tracking-widest text-zinc-400 block mb-1">
            RUFINOVENTURES.COM // CANONICAL ARCHITECTURE
          </span>
          <h2 class="font-display font-black text-3xl sm:text-5xl text-white uppercase tracking-tight">
            The Mission Architecture
          </h2>
        </div>
        <div class="font-mono text-xs text-zinc-400 text-right">
          <div>TOTAL DESTINATIONS</div>
          <div class="text-white font-bold">9 VERIFIED TABS</div>
        </div>
      </div>

      <!-- Grid of All 8 Other Tabs -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-12">
        <!-- Tab 1: Founder -->
        <a href="/founder" class="hud-box p-5 bg-zinc-950/80 hover:border-white transition block group">
          <div class="font-mono text-[9px] text-zinc-500 uppercase tracking-widest mb-2 group-hover:text-white transition">01 // CHRONOLOGY</div>
          <div class="font-display font-bold text-lg text-white uppercase mb-2">The Founder</div>
          <p class="text-zinc-400 text-xs font-light leading-relaxed mb-3">
            Unsanitized odyssey of Jefferson Rafael Rufino: Epochs I–VIII, homelessness, building LERM for AI communication, family coexistence.
          </p>
          <div class="font-mono text-[10px] text-zinc-300 group-hover:text-white flex items-center gap-1">
            ACCESS ODYSSEY →
          </div>
        </a>

        <!-- Tab 2: LERM -->
        <a href="/LERM" class="hud-box p-5 bg-zinc-950/80 hover:border-white transition block group">
          <div class="font-mono text-[9px] text-zinc-500 uppercase tracking-widest mb-2 group-hover:text-white transition">02 // FORENSIC RADAR</div>
          <div class="font-display font-bold text-lg text-white uppercase mb-2">LERM & Pax Silica</div>
          <p class="text-zinc-400 text-xs font-light leading-relaxed mb-3">
            The Liquidity Evaporation Radar Model. Forensic proof why the August 2027 Triple Cliff timeline remains locked despite local delays.
          </p>
          <div class="font-mono text-[10px] text-zinc-300 group-hover:text-white flex items-center gap-1">
            INSPECT 2027 RADAR →
          </div>
        </a>

        <!-- Tab 3: Photosynthesis -->
        <a href="/photosynthesisproject" class="hud-box p-5 bg-zinc-950/80 hover:border-white transition block group">
          <div class="font-mono text-[9px] text-zinc-500 uppercase tracking-widest mb-2 group-hover:text-white transition">03 // PLAYBOOK</div>
          <div class="font-display font-bold text-lg text-white uppercase mb-2">Photosynthesis</div>
          <p class="text-zinc-400 text-xs font-light leading-relaxed mb-3">
            2026–2027 Super El Niño action playbook: 451,000 lives, agrivoltaic solar canopies, AWG water systems, and decentralized cold chains.
          </p>
          <div class="font-mono text-[10px] text-zinc-300 group-hover:text-white flex items-center gap-1">
            VIEW PLAYBOOK →
          </div>
        </a>

        <!-- Tab 4: Realities -->
        <a href="/realities" class="hud-box p-5 bg-zinc-950/80 hover:border-white transition block group">
          <div class="font-mono text-[9px] text-zinc-500 uppercase tracking-widest mb-2 group-hover:text-white transition">04 // 120 ADAPTERS</div>
          <div class="font-display font-bold text-lg text-white uppercase mb-2">12 Reality Branches</div>
          <p class="text-zinc-400 text-xs font-light leading-relaxed mb-3">
            All 120 canonical reality adapters across 12 physical, biological, linguistic, and cosmological branches with 7-plate inspection.
          </p>
          <div class="font-mono text-[10px] text-zinc-300 group-hover:text-white flex items-center gap-1">
            INSPECT ADAPTERS →
          </div>
        </a>

        <!-- Tab 5: Shopfam Collective -->
        <a href="/shopfamcollective" class="hud-box p-5 bg-zinc-950/80 hover:border-white transition block group">
          <div class="font-mono text-[9px] text-zinc-500 uppercase tracking-widest mb-2 group-hover:text-white transition">05 // ARCH FILE</div>
          <div class="font-display font-bold text-lg text-white uppercase mb-2">ShopFam Collective</div>
          <p class="text-zinc-400 text-xs font-light leading-relaxed mb-3">
            The first empirical test of the unnamed MU+ effect: ₱3.477M BPI credits, ₱264K Meta tolls, Rockwell counterfeit revelation.
          </p>
          <div class="font-mono text-[10px] text-zinc-300 group-hover:text-white flex items-center gap-1">
            READ ARCH FILE →
          </div>
        </a>

        <!-- Tab 6: Scientists -->
        <a href="/scientists" class="hud-box p-5 bg-zinc-950/80 hover:border-white transition block group">
          <div class="font-mono text-[9px] text-zinc-500 uppercase tracking-widest mb-2 group-hover:text-white transition">06 // INTELLECTUAL LINEAGE</div>
          <div class="font-display font-bold text-lg text-white uppercase mb-2">The Lineage</div>
          <p class="text-zinc-400 text-xs font-light leading-relaxed mb-3">
            From Arrow, Coase, Friston, Shannon, Wiener, Boltzmann, Gibbs, and Bak to Einstein and Rufino: the unified lineage of systemic truth.
          </p>
          <div class="font-mono text-[10px] text-zinc-300 group-hover:text-white flex items-center gap-1">
            TRACE LINEAGE →
          </div>
        </a>

        <!-- Tab 7: Build -->
        <a href="/build" class="hud-box p-5 bg-zinc-950/80 hover:border-white transition block group">
          <div class="font-mono text-[9px] text-zinc-500 uppercase tracking-widest mb-2 group-hover:text-white transition">07 // COALITION</div>
          <div class="font-display font-bold text-lg text-white uppercase mb-2">Build With Us</div>
          <p class="text-zinc-400 text-xs font-light leading-relaxed mb-3">
            Four counterparty coalition tracks: Enterprise Sandbox, Research Coalition, Infrastructure Co-Build, and Direct Capital Allocation.
          </p>
          <div class="font-mono text-[10px] text-zinc-300 group-hover:text-white flex items-center gap-1">
            JOIN COALITION →
          </div>
        </a>

        <!-- Tab 8: Contact Us -->
        <a href="/contactus" class="hud-box p-5 bg-zinc-950/80 hover:border-white transition block group">
          <div class="font-mono text-[9px] text-zinc-500 uppercase tracking-widest mb-2 group-hover:text-white transition">08 // SECURE CHANNEL</div>
          <div class="font-display font-bold text-lg text-white uppercase mb-2">Contact Protocol</div>
          <p class="text-zinc-400 text-xs font-light leading-relaxed mb-3">
            Direct channels: jeffersonrrufino@gmail.com, LinkedIn, Instagram, under the strict 9:00 AM verification protocol.
          </p>
          <div class="font-mono text-[10px] text-zinc-300 group-hover:text-white flex items-center gap-1">
            INITIATE CONTACT →
          </div>
        </a>
      </div>

      <!-- Footer Telemetry Strip -->
      <footer class="border-t border-white/15 pt-8 flex flex-col md:flex-row items-center justify-between gap-4 font-mono text-[11px] text-zinc-500">
        <div>
          © 2026 RUFINO VENTURES. ARCHITECTED BY JEFFERSON RAFAEL RUFINO. ALL RIGHTS RESERVED.
        </div>
        <div class="flex items-center space-x-6">
          <a href="mailto:jeffersonrrufino@gmail.com" class="hover:text-white transition">jeffersonrrufino@gmail.com</a>
          <a href="https://linkedin.com/in/jeffersonrufino" target="_blank" rel="noopener" class="hover:text-white transition">LinkedIn</a>
          <a href="https://instagram.com/thehighlandboy" target="_blank" rel="noopener" class="hover:text-white transition">@thehighlandboy</a>
        </div>
      </footer>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- JAVASCRIPT: CANVAS ANIMATIONS & INTERACTIVE SYSTEMS -->
  <!-- ========================================================================= -->
  <script>
    // Mobile navigation toggle
    const mobileToggle = document.getElementById('mobile-toggle');
    const mobileMenu = document.getElementById('mobile-menu');
    if (mobileToggle && mobileMenu) {
      mobileToggle.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
      });
    }

    // -------------------------------------------------------------------------
    // 1. LIVE QUANTUM LATTICE & DYNAMIC CURVATURE CANVAS ANIMATION
    // -------------------------------------------------------------------------
    const canvas = document.getElementById('lattice-canvas');
    if (canvas) {
      const ctx = canvas.getContext('2d');
      let width, height;
      let mouseX = -1000, mouseY = -1000;
      let targetMouseX = -1000, targetMouseY = -1000;

      function resize() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
      }
      window.addEventListener('resize', resize);
      resize();

      window.addEventListener('mousemove', (e) => {
        const rect = canvas.getBoundingClientRect();
        targetMouseX = e.clientX - rect.left;
        targetMouseY = e.clientY - rect.top;
      });

      // Nodes in a discrete metamaterial grid
      const cols = 28;
      const rows = 16;
      const points = [];

      for (let i = 0; i < cols; i++) {
        for (let j = 0; j < rows; j++) {
          points.push({
            origX: (i / (cols - 1)) * 1.1 - 0.05,
            origY: (j / (rows - 1)) * 1.1 - 0.05,
            x: 0,
            y: 0,
            vx: 0,
            vy: 0,
            col: i,
            row: j
          });
        }
      }

      let time = 0;
      function animate() {
        time += 0.015;
        mouseX += (targetMouseX - mouseX) * 0.08;
        mouseY += (targetMouseY - mouseY) * 0.08;

        ctx.clearRect(0, 0, width, height);

        // Update positions
        for (let p of points) {
          let baseX = p.origX * width;
          let baseY = p.origY * height;

          // Natural non-Abelian quantum harmonic fluctuation
          let wave = Math.sin(time + p.col * 0.35 + p.row * 0.25) * 8;
          let wave2 = Math.cos(time * 0.7 + p.col * 0.2 - p.row * 0.4) * 6;

          // Tensor warping near mouse cursor (Non-Euclidean Curvature)
          let dx = mouseX - baseX;
          let dy = mouseY - baseY;
          let dist = Math.sqrt(dx * dx + dy * dy);
          let warpX = 0;
          let warpY = 0;

          if (dist < 280) {
            let force = (1 - dist / 280) * 45;
            warpX = (dx / dist) * -force;
            warpY = (dy / dist) * -force;
          }

          p.x = baseX + wave + warpX;
          p.y = baseY + wave2 + warpY;
        }

        // Draw discrete lattice connecting bonds
        ctx.lineWidth = 0.75;
        for (let p of points) {
          // Horizontal neighbor
          if (p.col < cols - 1) {
            let right = points.find(o => o.col === p.col + 1 && o.row === p.row);
            if (right) {
              let grad = ctx.createLinearGradient(p.x, p.y, right.x, right.y);
              grad.addColorStop(0, 'rgba(255, 255, 255, 0.18)');
              grad.addColorStop(1, 'rgba(255, 255, 255, 0.05)');
              ctx.strokeStyle = grad;
              ctx.beginPath();
              ctx.moveTo(p.x, p.y);
              ctx.lineTo(right.x, right.y);
              ctx.stroke();
            }
          }
          // Vertical neighbor
          if (p.row < rows - 1) {
            let down = points.find(o => o.col === p.col && o.row === p.row + 1);
            if (down) {
              ctx.strokeStyle = 'rgba(255, 255, 255, 0.12)';
              ctx.beginPath();
              ctx.moveTo(p.x, p.y);
              ctx.lineTo(down.x, down.y);
              ctx.stroke();
            }
          }

          // Node draw
          ctx.fillStyle = 'rgba(255, 255, 255, 0.65)';
          ctx.beginPath();
          ctx.arc(p.x, p.y, 1.4, 0, Math.PI * 2);
          ctx.fill();
        }

        requestAnimationFrame(animate);
      }
      animate();
    }

    // -------------------------------------------------------------------------
    // 2. INTERACTIVE MASTER EQUATION TERM INSPECTOR
    // -------------------------------------------------------------------------
    const termData = {
      psi: {
        title: "Ψ(x, t) — CONSOLIDATED STATE TENSOR & WAVEFUNCTION",
        tag: "TOTAL SYSTEM MANIFESTATION",
        desc: "The overarching state wavefunction bridging microscopic probability densities and macroscopic spacetime curvature. It represents physical reality not as separated particles in a detached container, but as an interactive information-density matrix.",
        classical: "Schrödinger state vector |Ψ⟩ decoupled from Einstein metric g_μν",
        novel: "Simultaneous coupling of structural elasticity and field dynamics via non-Abelian symmetry operations",
        empirical: "Phase coherence verified to 99.98% agreement in synthetic crystal lattices",
        mode: "HARMONIC MODE: COUPLED METRIC-WAVE"
      },
      curl: {
        title: "∇ × (G_μν + Λg_μν) — SPACETIME METRIC CURL & COSMOLOGICAL TENSION",
        tag: "BOUNDARY FLUX DEFORMATION",
        desc: "The rotational curl of the Einstein stress-energy metric tensor and cosmological vacuum tension. Resolves passive pseudo-Riemannian backgrounds by treating boundary deformation as active informational flux rather than rigid geometry.",
        classical: "Static Einstein Field Equations G_μν + Λg_μν = 8πT_μν on smooth passive manifold",
        novel: "Dynamic curl operator mapping boundary torque and non-linear stress accumulation directly",
        empirical: "Anomalous dispersion mitigated; zero-loss wave propagation along non-Euclidean boundary layers",
        mode: "HARMONIC MODE: METRIC ROTATIONAL TENSION"
      },
      phase: {
        title: "exp( i/ℏ ∑ α_k Φ_k(x) ) — NON-ABELIAN QUANTUM PHASE SUPERPOSITION",
        tag: "GAUGE INVARIANT COUPLING",
        desc: "The non-Abelian phase operator that couples gauge fields to physical elasticity. Guarantees that quantum phase coherence is preserved across macro-structural deformations without short-distance infinities.",
        classical: "U(1) Abelian electromagnetic phase factors decoupled from gravity",
        novel: "Non-Abelian multi-field superposition across N discrete topological flux chains",
        empirical: "Gravitational-EM coupling micro-Newton forces verified under ultra-high flux conditions",
        mode: "HARMONIC MODE: NON-ABELIAN SUPERPOSITION"
      },
      domain: {
        title: "∫_Ω ... dΩ — BOUNDARY DOMAIN MANIFOLD INVARIANCE",
        tag: "CONSERVATION AT SCALE",
        desc: "The global volume integration over the boundary domain Ω. By Gauss's Divergence Theorem, internal stress cannot be artificially eliminated without appearing as non-linear displacement flux across the boundary ∂Ω.",
        classical: "Local differential equations ignoring systemic cross-boundary externalities",
        novel: "Global boundary domain conservation applying identically from quantum lattices to macro economies",
        empirical: "Cross-system concordance: Seismology b-value (1.126) vs Financial heavy-tail (2.709)",
        mode: "HARMONIC MODE: DOMAIN BOUNDARY INTEGRAL"
      }
    };

    function inspectTerm(termKey) {
      const data = termData[termKey];
      if (!data) return;

      document.getElementById('inspect-title').innerText = data.title;
      document.getElementById('inspect-tag').innerText = data.tag;
      document.getElementById('inspect-desc').innerText = data.desc;
      document.getElementById('inspect-classical').innerText = data.classical;
      document.getElementById('inspect-novel').innerText = data.novel;
      document.getElementById('inspect-empirical').innerText = data.empirical;
      document.getElementById('wave-mode').innerText = data.mode;

      // Update button active styling
      document.querySelectorAll('.term-btn').forEach(btn => {
        btn.classList.remove('bg-white', 'text-black', 'border-white');
        btn.classList.add('bg-zinc-950/80', 'text-zinc-300', 'border-white/20');
      });
      const activeBtn = document.getElementById('btn-' + termKey);
      if (activeBtn) {
        activeBtn.classList.remove('bg-zinc-950/80', 'text-zinc-300', 'border-white/20');
        activeBtn.classList.add('bg-white', 'text-black', 'border-white');
      }
    }

    // Live Term Waveform Simulator Canvas
    const waveCanvas = document.getElementById('term-wave-canvas');
    if (waveCanvas) {
      const wCtx = waveCanvas.getContext('2d');
      let wTime = 0;
      function drawWave() {
        wTime += 0.04;
        wCtx.clearRect(0, 0, waveCanvas.width, waveCanvas.height);
        wCtx.strokeStyle = '#ffffff';
        wCtx.lineWidth = 1.5;
        wCtx.beginPath();
        for (let x = 0; x < waveCanvas.width; x++) {
          let y = waveCanvas.height / 2 + Math.sin(x * 0.05 + wTime) * 18 * Math.cos(x * 0.02 - wTime * 0.5);
          if (x === 0) wCtx.moveTo(x, y);
          else wCtx.lineTo(x, y);
        }
        wCtx.stroke();
        requestAnimationFrame(drawWave);
      }
      drawWave();
    }

    // -------------------------------------------------------------------------
    // 3. INTERACTIVE ARCHITECTURE DIAGRAM (SVG)
    // -------------------------------------------------------------------------
    function renderDiagram(mode) {
      const svg = document.getElementById('diagram-svg');
      const caption = document.getElementById('diagram-caption');
      if (!svg) return;

      if (mode === 'smooth') {
        svg.innerHTML = `
          <defs>
            <linearGradient id="smoothGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#3f3f46" />
              <stop offset="100%" stop-color="#18181b" />
            </linearGradient>
          </defs>
          <!-- Smooth Curved Metric lines -->
          <path d="M 50 150 Q 200 60, 400 150 T 750 150" fill="none" stroke="#71717a" stroke-width="1.5" stroke-dasharray="4,4" />
          <path d="M 50 180 Q 200 90, 400 180 T 750 180" fill="none" stroke="#71717a" stroke-width="1.5" stroke-dasharray="4,4" />
          <path d="M 50 120 Q 200 30, 400 120 T 750 120" fill="none" stroke="#71717a" stroke-width="1.5" stroke-dasharray="4,4" />
          <!-- Passive Container Grid -->
          <line x1="200" y1="40" x2="200" y2="260" stroke="#3f3f46" stroke-width="1" />
          <line x1="400" y1="40" x2="400" y2="260" stroke="#3f3f46" stroke-width="1" />
          <line x1="600" y1="40" x2="600" y2="260" stroke="#3f3f46" stroke-width="1" />
          <circle cx="400" cy="150" r="16" fill="rgba(239, 68, 68, 0.2)" stroke="#ef4444" stroke-width="1.5" />
          <text x="400" y="195" fill="#ef4444" font-family="JetBrains Mono" font-size="10" text-anchor="middle">SINGULARITY RISK (r -> 0, inf)</text>
          <text x="400" y="30" fill="#a1a1aa" font-family="JetBrains Mono" font-size="11" text-anchor="middle">PREDECESSOR: PASSIVE PSEUDO-RIEMANNIAN CONTINUUM</text>
        `;
        caption.innerHTML = `
          <span>ACTIVE TOPOLOGY: CLASSICAL PSEUDO-RIEMANNIAN MANIFOLD</span>
          <span class="text-red-400">PASSIVE BACKGROUND // LOCALIZED PERTURBATIONS</span>
        `;
        document.getElementById('btn-diag-smooth').className = "px-3 py-1 border border-white bg-white text-black font-bold transition";
        document.getElementById('btn-diag-lattice').className = "px-3 py-1 border border-white/30 text-zinc-400 hover:text-white transition";
      } else {
        svg.innerHTML = `
          <!-- Novel Discrete Dynamic Metamaterial Lattice -->
          <g stroke="#ffffff" stroke-width="1.2">
            <!-- Node rows and lattice links -->
            ${Array.from({length: 9}).map((_, i) => {
              let x1 = 100 + i * 75;
              return Array.from({length: 4}).map((_, j) => {
                let y1 = 70 + j * 50;
                let isCenter = (i >= 3 && i <= 5 && j >= 1 && j <= 2);
                let col = isCenter ? "#10b981" : "#ffffff";
                return `
                  <circle cx="${x1}" cy="${y1}" r="3" fill="${col}" />
                  ${i < 8 ? `<line x1="${x1}" y1="${y1}" x2="${x1 + 75}" y2="${y1}" stroke="${isCenter ? '#10b981' : 'rgba(255,255,255,0.25)'}" />` : ''}
                  ${j < 3 ? `<line x1="${x1}" y1="${y1}" x2="${x1}" y2="${y1 + 50}" stroke="${isCenter ? '#10b981' : 'rgba(255,255,255,0.25)'}" />` : ''}
                `;
              }).join('');
            }).join('')}
          </g>
          <rect x="300" y="105" width="200" height="70" fill="none" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3,3" />
          <text x="400" y="195" fill="#10b981" font-family="JetBrains Mono" font-size="10" text-anchor="middle">NON-ABELIAN LATTICE COUPLING (ZERO-LOSS)</text>
          <text x="400" y="30" fill="#ffffff" font-family="JetBrains Mono" font-size="11" text-anchor="middle">NOVEL: DISCRETE DYNAMIC METAMATERIAL TOPOLOGY</text>
        `;
        caption.innerHTML = `
          <span>ACTIVE TOPOLOGY: NOVEL DYNAMIC LATTICE</span>
          <span class="text-emerald-400">COUPLING: NON-ABELIAN SYMMETRY OPERATIONS</span>
        `;
        document.getElementById('btn-diag-lattice').className = "px-3 py-1 border border-white bg-white text-black font-bold transition";
        document.getElementById('btn-diag-smooth').className = "px-3 py-1 border border-white/30 text-zinc-400 hover:text-white transition";
      }
    }

    function toggleDiagramMode(mode) {
      renderDiagram(mode);
    }
    renderDiagram('lattice');

    // -------------------------------------------------------------------------
    // 4. INTERACTIVE 3-FRONTIER SWITCHER
    // -------------------------------------------------------------------------
    function switchFrontier(scale) {
      const rows = {
        quantum: document.getElementById('row-quantum'),
        macro: document.getElementById('row-macro'),
        cosmo: document.getElementById('row-cosmo')
      };

      document.querySelectorAll('.frontier-tab').forEach(btn => {
        btn.classList.remove('bg-white', 'text-black', 'border-white');
        btn.classList.add('bg-zinc-950/80', 'text-zinc-300', 'border-white/20');
      });
      const activeBtn = document.getElementById('btn-f-' + scale);
      if (activeBtn) {
        activeBtn.classList.remove('bg-zinc-950/80', 'text-zinc-300', 'border-white/20');
        activeBtn.classList.add('bg-white', 'text-black', 'border-white');
      }

      if (scale === 'all') {
        Object.values(rows).forEach(r => r.style.display = 'table-row');
      } else {
        Object.keys(rows).forEach(k => {
          rows[k].style.display = (k === scale) ? 'table-row' : 'none';
        });
      }
    }

    // -------------------------------------------------------------------------
    // 5. EMPIRICAL VALIDATION SIMULATORS (VOLUMES 12–45)
    // -------------------------------------------------------------------------
    function updateCoherence(val) {
      const pct = (val / 100).toFixed(2);
      document.getElementById('coherence-readout').innerText = pct + '% COHERENCE';
      document.getElementById('coherence-bar').style.width = pct + '%';
    }

    let isZeroLoss = true;
    function toggleWaveguide() {
      isZeroLoss = !isZeroLoss;
      const btn = document.getElementById('btn-waveguide');
      const loss = document.getElementById('loss-readout');
      if (isZeroLoss) {
        btn.innerText = "NON-EUCLIDEAN (ZERO-LOSS)";
        loss.innerText = "0.000 dB (ZERO-LOSS)";
        loss.className = "text-emerald-400 font-bold";
      } else {
        btn.innerText = "CLASSICAL LOSS MEDIUM";
        loss.innerText = "-18.42 dB (ATTENUATED)";
        loss.className = "text-red-400 font-bold";
      }
    }

    function updateFlux(val) {
      const uN = (val * 0.067).toFixed(2);
      document.getElementById('force-readout').innerText = uN + ' μN DETECTED';
    }
  </script>
</body>
</html>
"""
    return html

def main():
    content = generate_page()
    root_dir = "/Users/thehighlandboy/Downloads/RUFINOVENTURES"
    
    # Write to index.html and RUFINOVENTURES.html
    for target in ["index.html", "RUFINOVENTURES.html"]:
        target_path = os.path.join(root_dir, target)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Wrote {len(content):,} bytes to {target_path}")

if __name__ == "__main__":
    main()
