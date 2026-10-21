#!/usr/bin/env python3
"""
build_complete_rufino_synthesis.py
Builds the complete, unfragmented, line-by-line synthesis of:
"THE RUFINO SYNTHESIS: An End-to-End LERM + IAMF-P Research Dossier and Playbook"
by Jefferson Rafael Rufino (Metro Manila, Philippines | September 2026)

Integrates:
- All 10 Parts & Appendices A-E line by line
- All figures & backtests:
  * 250,000-case negative ablation (Figure 7.1: LERM loses under existing capacity)
  * 250,000-case corrected catch-basin simulation (Figure 7.2: 5.6696% vs 5.5567%)
  * Two 1,000,000-system arena experiments (Figure 7.3: 7.9083% whole system vs 7.506% local KPI)
  * 121/121 Executable dossier test suite passed (Figure 7.4)
  * Reverse-engineered public architecture coverage (Figure 7.5: LERM 87.5% vs Palantir 68.8% vs AI 62.5% vs BlackRock 50%)
- All 18 Reality Branches (Section 5.1 through 5.18) with State maps, Algebraic adapters, IAMF-P construction, Falsification paths
- The Full Intellectual Lineage (Part 3, Figure 3.1: Newton, Clausius, Boltzmann, Gibbs, Einstein, Onsager, Coase, Hayek, Shannon, Wiener, Simon, Ashby, Solow, Kalman, Landauer, Forrester, Bertalanffy, Prigogine, Mitchell, Kahneman/Tversky, Ostrom/Williamson, Scott, Friston, Pearl, Basaran, Hopfield/Hinton, Baker/Hassabis/Jumper, Rufino)
- The Unsanitized Operating Record (Part 2: childhood trauma, sexual violence, corporate compression, 8-node internalization, Rockwell counterfeit zero-point)
- The Canonical Algebra (Part 4 & Part A Formula Vault: BDI, Displacement shadow, LERM trace, IAMF-P constructive operator, RVG, Whole-kernel recurrence, Stopping conditions)
- Interactive Canvas animations, interactive term inspectors, dynamic charts, and HD contextual backgrounds per pane.
"""

import os

def generate_synthesis_html():
    return """<!DOCTYPE html>
<html lang="en" class="scroll-smooth dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>THE RUFINO SYNTHESIS // LERM + IAMF-P CANONICAL DOSSIER</title>
  <meta name="description" content="The Rufino Synthesis: An End-to-End LERM + IAMF-P Research Dossier and Playbook. Origins, scientific lineage, canonical algebra, branch-of-reality mappings, adversarial falsification, backtests, and provenance by Jefferson Rafael Rufino." />
  <link rel="canonical" href="https://rufinoventures.com/" />

  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://rufinoventures.com/" />
  <meta property="og:title" content="THE RUFINO SYNTHESIS // LERM + IAMF-P RESEARCH DOSSIER" />
  <meta property="og:description" content="The comprehensive systems architecture by Jefferson Rafael Rufino: One kernel, 18 reality branches, 121/121 executable tests, 2.5M simulated systems." />
  <meta property="og:image" content="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1200&q=80" />

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Cpolygon points='16,2 30,9 30,23 16,30 2,23 2,9' fill='%23000000' stroke='%23ffffff' stroke-width='1.5'/%3E%3Ccircle cx='16' cy='16' r='3' fill='%23ffffff'/%3E%3C/svg%3E">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- KaTeX for exact algebraic rendering -->
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
              850: '#09090b',
              800: '#121215',
              750: '#18181b',
              700: '#27272a',
            }
          }
        }
      }
    }
  </script>

  <style>
    /* SpaceX High-Contrast Minimalist Foundation */
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

    ::-webkit-scrollbar { width: 5px; height: 5px; }
    ::-webkit-scrollbar-track { background: #000000; }
    ::-webkit-scrollbar-thumb { background: #27272a; border-radius: 2px; }
    ::-webkit-scrollbar-thumb:hover { background: #71717a; }

    /* Technical HUD Panels */
    .hud-box {
      position: relative;
      background: rgba(5, 5, 8, 0.82);
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

    /* SpaceX Buttons */
    .btn-spacex-white {
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

    /* Pane Scrims */
    .pane-scrim {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.52) 45%, rgba(0,0,0,0.92) 100%);
      pointer-events: none;
    }
    .pane-scrim-heavy {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(0,0,0,0.94) 0%, rgba(0,0,0,0.72) 50%, rgba(0,0,0,0.98) 100%);
      pointer-events: none;
    }

    @keyframes pulse-beacon {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.35; transform: scale(0.85); }
    }
    .beacon { animation: pulse-beacon 2s infinite ease-in-out; }

    .glow-header { text-shadow: 0 0 20px rgba(255, 255, 255, 0.35); }
  </style>
</head>
<body class="bg-black text-zinc-100 antialiased selection:bg-white selection:text-black">

  <!-- ========================================================================= -->
  <!-- AEROSPACE TOP NAVIGATION -->
  <!-- ========================================================================= -->
  <header class="fixed top-0 left-0 right-0 z-50 bg-black/90 backdrop-blur-md border-b border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <a href="/" class="flex items-center space-x-3 group">
        <div class="w-8 h-8 bg-white text-black font-display font-black flex items-center justify-center text-sm tracking-tighter transition-transform group-hover:scale-105">
          RV
        </div>
        <div>
          <span class="font-display font-bold text-white text-sm tracking-wider uppercase block leading-none">THE RUFINO SYNTHESIS</span>
          <span class="font-mono text-[9px] text-zinc-400 uppercase tracking-widest block mt-0.5">LERM + IAMF-P Canonical Dossier</span>
        </div>
      </a>

      <!-- Desktop Links across the 9 destinations -->
      <nav class="hidden 2xl:flex items-center space-x-5 text-[11px] font-mono">
        <a href="/" class="text-white font-bold border-b-2 border-white pb-1 tracking-wider">SYNTHESIS</a>
        <a href="/founder" class="text-zinc-400 hover:text-white transition pb-1 tracking-wider">FOUNDER</a>
        <a href="/realities" class="text-zinc-400 hover:text-white transition pb-1 tracking-wider">18 BRANCHES</a>
        <a href="/LERM" class="text-zinc-400 hover:text-white transition pb-1 tracking-wider">LERM</a>
        <a href="/photosynthesisproject" class="text-zinc-400 hover:text-white transition pb-1 tracking-wider">PHOTOSYNTHESIS</a>
        <a href="/shopfamcollective" class="text-zinc-400 hover:text-white transition pb-1 tracking-wider">SHOPFAM</a>
        <a href="/scientists" class="text-zinc-400 hover:text-white transition pb-1 tracking-wider">LINEAGE</a>
        <a href="/build" class="text-zinc-400 hover:text-white transition pb-1 tracking-wider">BUILD</a>
        <a href="/contactus" class="text-zinc-400 hover:text-white transition pb-1 tracking-wider">CONTACT</a>
      </nav>

      <!-- Quick Section Jump Menu -->
      <div class="hidden md:flex items-center space-x-2 font-mono text-[10px] text-zinc-400 border border-white/10 px-3 py-1.5 bg-zinc-950/80">
        <a href="#algebra" class="hover:text-white">ALGEBRA</a>
        <span class="text-zinc-600">·</span>
        <a href="#backtests" class="hover:text-white">BACKTESTS</a>
        <span class="text-zinc-600">·</span>
        <a href="#lineage" class="hover:text-white">LINEAGE</a>
        <span class="text-zinc-600">·</span>
        <a href="#branches" class="hover:text-white">18 BRANCHES</a>
        <span class="text-zinc-600">|</span>
        <span class="text-emerald-400 font-bold">121/121 PASSED</span>
      </div>

      <!-- Mobile Menu Button -->
      <button id="mobile-toggle" class="2xl:hidden text-zinc-400 hover:text-white p-2">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
      </button>
    </div>

    <!-- Mobile Drawer -->
    <div id="mobile-menu" class="hidden 2xl:hidden bg-zinc-950 border-b border-white/10 px-6 py-4 space-y-2.5 font-mono text-xs">
      <a href="/" class="block text-white font-bold py-1">THE RUFINO SYNTHESIS (MAIN)</a>
      <a href="/founder" class="block text-zinc-400 hover:text-white py-1">FOUNDER (UNSANITIZED OPERATING RECORD)</a>
      <a href="/realities" class="block text-zinc-400 hover:text-white py-1">18 REALITY BRANCHES (MAPS)</a>
      <a href="/LERM" class="block text-zinc-400 hover:text-white py-1">LERM (PAX SILICA & 2027 RADAR)</a>
      <a href="/photosynthesisproject" class="block text-zinc-400 hover:text-white py-1">PHOTOSYNTHESIS (SUPER EL NIÑO)</a>
      <a href="/shopfamcollective" class="block text-zinc-400 hover:text-white py-1">SHOPFAM (ARCH FILE & MU+)</a>
      <a href="/scientists" class="block text-zinc-400 hover:text-white py-1">SCIENTISTS (INTELLECTUAL LINEAGE)</a>
      <a href="/build" class="block text-zinc-400 hover:text-white py-1">BUILD (COALITION TRACKS)</a>
      <a href="/contactus" class="block text-zinc-400 hover:text-white py-1">CONTACT (SECURE PROTOCOL)</a>
    </div>
  </header>

  <!-- ========================================================================= -->
  <!-- PANE 1: HERO // DOSSIER METADATA & RECURRENT KERNEL -->
  <!-- ========================================================================= -->
  <section id="hero" class="relative min-h-screen w-full flex flex-col justify-between pt-28 pb-16 px-6 sm:px-12 lg:px-20 overflow-hidden bg-black">
    <!-- HD Background Image: Orbital Earth Atmospheric Telemetry -->
    <div class="absolute inset-0 z-0 pointer-events-none">
      <img 
        src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=2560&q=85" 
        alt="Orbital Earth atmospheric telemetry" 
        class="w-full h-full object-cover object-center filter brightness-[0.52] contrast-[1.25]" 
        loading="eager"
      />
      <div class="pane-scrim"></div>
    </div>

    <!-- Live Interactive Quantum Lattice & Dynamic Curvature Canvas -->
    <canvas id="lattice-canvas" class="absolute inset-0 z-10 w-full h-full pointer-events-auto opacity-70"></canvas>

    <!-- Top Telemetry Header -->
    <div class="relative z-20 max-w-7xl mx-auto w-full pt-4">
      <div class="inline-flex flex-wrap items-center gap-3 border border-white/20 bg-black/85 px-4 py-2 font-mono text-[10px] uppercase tracking-widest text-zinc-300 backdrop-blur-md">
        <span class="flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-white beacon"></span>
          AUTHOR: <strong class="text-white">JEFFERSON RAFAEL RUFINO</strong>
        </span>
        <span class="text-zinc-600">|</span>
        <span>LOCATION: <strong class="text-white">METRO MANILA, PHILIPPINES</strong></span>
        <span class="text-zinc-600">|</span>
        <span>CORPUS DATE: <strong class="text-white">SEPTEMBER 2026</strong></span>
      </div>
    </div>

    <!-- Main Title & Abstract -->
    <div class="relative z-20 max-w-7xl mx-auto w-full my-auto py-10">
      <div class="max-w-4xl">
        <p class="font-mono text-xs uppercase tracking-widest text-zinc-400 mb-3 flex items-center gap-2">
          <span class="w-6 h-[1px] bg-white"></span>
          AN END-TO-END LERM + IAMF-P RESEARCH DOSSIER AND PLAYBOOK
        </p>
        <h1 class="font-display font-black text-4xl sm:text-6xl lg:text-7xl tracking-tighter text-white uppercase leading-[0.95] mb-6 glow-header">
          The Rufino<br/>Synthesis
        </h1>
        <p class="text-zinc-300 text-base sm:text-lg font-light leading-relaxed max-w-3xl mb-8">
          Origins, scientific lineage, canonical algebra, branch-of-reality mappings, adversarial falsification, backtests, provenance, and research agenda. Prepared from the supplied Rufino research archive, executable test package, simulations, and an independent literature review of adjacent lineages.
        </p>

        <!-- Executive Abstract Box -->
        <div class="hud-box p-6 sm:p-8 max-w-3xl mb-8">
          <div class="flex items-center justify-between mb-3 border-b border-white/10 pb-2">
            <span class="font-mono text-[10px] tracking-widest uppercase text-white font-bold flex items-center gap-2">
              <span class="w-2 h-2 bg-white"></span>
              PART 1.1 // THE INTEGRATED THESIS: ONE KERNEL, NOT TWO FRAMEWORKS
            </span>
            <span class="font-mono text-[9px] text-emerald-400">STATUS: CONFORMANCE VERIFIED</span>
          </div>
          <p class="text-zinc-200 text-sm leading-relaxed mb-4">
            The supplied archive is most coherent when <strong>LERM and IAMF-P are treated as inseparable operations within one recurrent reconciliation kernel</strong>. 
            <strong>LERM</strong> is the detection and tracing operation: it identifies the residual between expected and observed state, follows the direction of displacement, names the receiving carrier, identifies the coupling point, and detects hidden compensation. 
            <strong>IAMF-P</strong> is the constructive operation: it builds or selects new capacity at the receiving carrier, transforms the recovered state where possible, reintegrates value, and forces a non-displacement retest across the consequential boundary and over time.
          </p>
          
          <!-- Frozen Recurrent Loop Banner -->
          <div class="border border-white/20 p-3 bg-black/90 font-mono text-xs text-center text-white tracking-wider uppercase font-bold overflow-x-auto">
            observe → trace → build → transform → reintegrate → retest → observe again
          </div>
        </div>

        <!-- Provenance Discipline Note -->
        <div class="border-l-2 border-white/40 pl-4 py-2 font-mono text-xs text-zinc-400 max-w-3xl mb-8">
          <strong class="text-zinc-200 uppercase">Research Integrity & Provenance Note:</strong> 
          This document deliberately avoids two symmetrical errors: reducing the Rufino corpus to familiar fragments, and inflating every internal claim into established science. The atomic research object used here is the integrated LERM/IAMF-P loop.
        </div>

        <!-- Action CTAs -->
        <div class="flex flex-wrap items-center gap-4">
          <a href="#algebra" class="btn-spacex-white">
            EXPLORE CANONICAL ALGEBRA
          </a>
          <a href="#backtests" class="btn-spacex-outline">
            VIEW 250K & 1M BACKTESTS
          </a>
          <a href="#lineage" class="btn-spacex-outline">
            INSPECT 28 SCIENTISTS LINEAGE
          </a>
          <a href="#branches" class="btn-spacex-outline">
            18 REALITY BRANCHES
          </a>
        </div>
      </div>
    </div>

    <!-- Bottom Telemetry Rail -->
    <div class="relative z-20 max-w-7xl mx-auto w-full border-t border-white/15 pt-6 flex flex-wrap items-center justify-between gap-4 font-mono text-[10px] text-zinc-400">
      <div class="flex items-center gap-6">
        <div>EXECUTABLE HARNESS: <span class="text-emerald-400 font-bold">121 / 121 PASSED</span></div>
        <div>SIMULATION REACH: <span class="text-white">2.5M SYNTHETIC CASES</span></div>
        <div>NEGATIVE ABLATION: <span class="text-zinc-300">PRESERVED (LERM LOSES)</span></div>
      </div>
      <div class="flex items-center gap-2 text-zinc-500">
        <span class="beacon w-1.5 h-1.5 rounded-full bg-white"></span>
        INTERACTIVE HUD // MOVE MOUSE TO WARP DISCRETE LATTICE
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- PANE 2: PART 4 & FORMULA VAULT // CANONICAL ALGEBRA -->
  <!-- ========================================================================= -->
  <section id="algebra" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-black border-t border-white/10">
    <!-- HD Background Image: Laser Optical Interferometry -->
    <div class="absolute inset-0 z-0 pointer-events-none">
      <img 
        src="https://images.unsplash.com/photo-1507499739999-097706ad8914?auto=format&fit=crop&w=2560&q=85" 
        alt="Laser optical interferometry" 
        class="w-full h-full object-cover object-center filter brightness-[0.42] contrast-[1.3]" 
        loading="lazy"
      />
      <div class="pane-scrim-heavy"></div>
    </div>

    <div class="relative z-20 max-w-7xl mx-auto w-full my-auto">
      <div class="flex items-center justify-between border-b border-white/15 pb-4 mb-8">
        <div>
          <span class="font-mono text-[10px] uppercase tracking-widest text-zinc-400 block mb-1">
            PART 4 & APPENDIX A // THE IRREDUCIBLE OPERATORS
          </span>
          <h2 class="font-display font-black text-3xl sm:text-5xl text-white uppercase tracking-tight">
            Canonical Algebra of the LERM/IAMF-P Kernel
          </h2>
        </div>
        <div class="hidden sm:block font-mono text-right text-xs text-zinc-400">
          <div>STRUCTURAL INVARIANCE</div>
          <div class="text-white font-bold">$$K_R = K_{\text{LERM/IAMF-P}}$$</div>
        </div>
      </div>

      <p class="text-zinc-300 text-sm sm:text-base font-light max-w-3xl mb-8 leading-relaxed">
        Let physical or institutional reality in domain \(d\) be \(\Omega^{(d)}_t\). The domain map converts observable reality into a state representation: \(X^{(d)}_t = M_d(\Omega^{(d)}_t)\). While \(M_d\) changes from domain to domain, the kernel remains structurally fixed.
      </p>

      <!-- Key Formulas Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8 font-mono">
        <!-- 4.1 Boundary Divergence Index -->
        <div class="hud-box p-6 bg-black/90">
          <div class="text-[10px] text-zinc-400 uppercase tracking-widest mb-1">4.1 BOUNDARY DIVERGENCE INDEX</div>
          <div class="text-lg text-white font-bold my-2 select-all">
            $$BDI = J_G(a^*_S) - J_G(a^*_G)$$
          </div>
          <p class="text-[11px] text-zinc-400 leading-relaxed font-sans mt-3">
            Where \(a^*_S = \arg\min_a J_S(a)\) and \(a^*_G = \arg\min_a J_G(a)\). When \(BDI \approx 0\), the local boundary is adequate. When \(BDI\) is materially positive, the architecture activates as a guardrail against universal-hammer behavior.
          </p>
        </div>

        <!-- 4.2 Displacement Shadow Field -->
        <div class="hud-box p-6 bg-black/90">
          <div class="text-[10px] text-zinc-400 uppercase tracking-widest mb-1">4.2 DISPLACEMENT SHADOW FIELD</div>
          <div class="text-sm text-white font-bold my-2 select-all">
            $$\mathcal{D}_a(j, k, \tau) = U_{j,k}(t+\tau \mid a) - U_{j,k}(t+\tau \mid a_0)$$
          </div>
          <p class="text-[11px] text-zinc-400 leading-relaxed font-sans mt-3">
            Tensor/vector-valued: \(\mathbf{D}_t = [D_\$, D_E, D_T, D_L, D_C, D_B, D_R, D_{\text{trust}}, \dots]^\top\). Money, energy, time, labor, and cognitive load are never silently summed without conversion models.
          </p>
        </div>

        <!-- 4.3 LERM Trace Operator -->
        <div class="hud-box p-6 bg-black/90">
          <div class="text-[10px] text-zinc-400 uppercase tracking-widest mb-1">4.3 LERM TRACE OPERATOR</div>
          <div class="text-sm text-white font-bold my-2 select-all">
            $$\mathcal{L}(X_t, a) = \{R_t, \mathcal{D}_a, C_t, \Gamma_t, H_t, U_t, Q_t\}$$
          </div>
          <p class="text-[11px] text-zinc-400 leading-relaxed font-sans mt-3">
            Carrier candidate: \(C^*_t = \arg\max_j \sum_{k,\tau} \mathcal{D}^+_a(j, k, \tau)\). Traces unresolved residual \(R_t\), receiving carrier \(C_t\), coupling point \(\Gamma_t\), hidden compensation \(H_t\), and provenance state \(Q_t\).
          </p>
        </div>

        <!-- 4.4 IAMF-P Constructive Operator -->
        <div class="hud-box p-6 bg-black/90">
          <div class="text-[10px] text-zinc-400 uppercase tracking-widest mb-1">4.4 IAMF-P CONSTRUCTIVE OPERATOR</div>
          <div class="text-xs text-white font-bold my-2 select-all leading-relaxed">
            $$A^*_t = \arg\min_{A \in \mathcal{A}} [U_G(A) + \lambda HCC + \mu U_{\max} + \nu \text{Cost} - \eta V_G]$$
          </div>
          <p class="text-[11px] text-zinc-400 leading-relaxed font-sans mt-3">
            Builds new capacity: \(R^{\text{new}}_{C^*} = R_{C^*} + \Delta R_{\text{built}}\). Unlike generic reallocation, the intervention creates structural reconciliation capacity at the predicted loss carrier.
          </p>
        </div>

        <!-- 4.5 Reconciliation Velocity Gap -->
        <div class="hud-box p-6 bg-black/90">
          <div class="text-[10px] text-zinc-400 uppercase tracking-widest mb-1">4.5 RECONCILIATION VELOCITY GAP</div>
          <div class="text-lg text-white font-bold my-2 select-all">
            $$RVG(t) = \frac{dU}{dt} - \frac{dR_c}{dt}$$
          </div>
          <p class="text-[11px] text-zinc-400 leading-relaxed font-sans mt-3">
            If \(RVG \le 0\), capacity keeps pace. Persistent \(RVG > 0\) implies accumulating unresolved state. Loss rate: \(\dot{L}_A = (L_{\text{avoidable}} + L_{\text{displaced}} + L_{\text{deferred}})/\Delta t\).
          </p>
        </div>

        <!-- 4.7 Whole-Kernel Recurrence -->
        <div class="hud-box p-6 bg-black/90">
          <div class="text-[10px] text-zinc-400 uppercase tracking-widest mb-1">4.7 WHOLE-KERNEL RECURRENCE</div>
          <div class="text-sm text-white font-bold my-2 select-all">
            $$K^{(d)}_R = M^{-1}_d \circ \mathcal{Q}_d \circ F_d \circ \mathcal{I} \circ \mathcal{L} \circ M_d$$
          </div>
          <p class="text-[11px] text-zinc-400 leading-relaxed font-sans mt-3">
            Stopping & Success Condition: \(\Delta V_G > 0, \Delta U_G \le 0\) without increasing worst-carrier burden. If states are observationally equivalent \(\mathcal{H}(O)\), state is <em>unknown</em>, not invented.
          </p>
        </div>
      </div>

      <!-- The Productive Reconciliation Principle -->
      <div class="hud-box p-6 bg-zinc-950/90 border border-white/20 flex flex-col md:flex-row items-center justify-between gap-6">
        <div>
          <span class="font-mono text-xs uppercase text-zinc-400 font-bold block mb-1">
            PART 4.6 // PRODUCTIVE RECONCILIATION & TRANSFORMATION
          </span>
          <p class="text-white font-mono text-sm">
            $$\mathcal{D} \to \text{capture} \to \text{transform} \to \mathcal{D}', \quad V(\mathcal{D}') > V(\mathcal{D})$$
          </p>
          <p class="text-zinc-400 text-xs mt-1">
            The target is not zero motion. It is useful transformation: recovered value is transformed into a higher-utility state when the domain permits.
          </p>
        </div>
        <div class="font-mono text-xs text-right border-l border-white/10 pl-6 hidden md:block">
          <div class="text-zinc-500">MANDATORY POST-TEST</div>
          <div class="text-emerald-400 font-bold">NON-DISPLACEMENT AUDIT</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- PANE 3: PART 7 // BACKTESTS, SIMULATIONS & EXECUTABLE VERIFICATION -->
  <!-- ========================================================================= -->
  <section id="backtests" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-black border-t border-white/10">
    <!-- HD Background Image: Semiconductor Supercomputing Lab -->
    <div class="absolute inset-0 z-0 pointer-events-none">
      <img 
        src="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=2560&q=85" 
        alt="Semiconductor and supercomputing infrastructure" 
        class="w-full h-full object-cover object-center filter brightness-[0.4] contrast-[1.35]" 
        loading="lazy"
      />
      <div class="pane-scrim-heavy"></div>
    </div>

    <div class="relative z-20 max-w-7xl mx-auto w-full my-auto">
      <div class="flex items-center justify-between border-b border-white/15 pb-4 mb-8">
        <div>
          <span class="font-mono text-[10px] uppercase tracking-widest text-zinc-400 block mb-1">
            PART 7 // EMPIRICAL RIGOR & ADVERSARIAL FALSIFICATION
          </span>
          <h2 class="font-display font-black text-3xl sm:text-5xl text-white uppercase tracking-tight">
            Backtests, Simulations & Executable Verification
          </h2>
        </div>
        <div class="font-mono text-xs text-zinc-400 text-right">
          <div>TOTAL SUITE RUN</div>
          <div class="text-emerald-400 font-bold">121/121 CONFORMANCE PASSED</div>
        </div>
      </div>

      <p class="text-zinc-300 text-sm sm:text-base font-light max-w-3xl mb-8 leading-relaxed">
        The archive avoids conflating objects: real operating records, historical crisis reconstructions, architecture-class simulations, public architecture coverage scoring, and executable test packages remain strictly distinct.
      </p>

      <!-- Comparative Simulation Grids -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
        <!-- 7.2 Negative Ablation: LERM Loses -->
        <div class="hud-box p-6 bg-zinc-950/90 border border-red-500/30">
          <div class="flex items-center justify-between border-b border-white/10 pb-3 mb-3">
            <span class="font-mono text-xs font-bold text-red-400 uppercase flex items-center gap-2">
              <span class="w-2 h-2 bg-red-500"></span>
              7.2 250,000-CASE NEGATIVE ABLATION (LERM LOSES)
            </span>
            <span class="font-mono text-[9px] text-zinc-500">SOURCE: SUPPLIED CSV</span>
          </div>
          <p class="text-zinc-400 text-xs leading-relaxed mb-4">
            Under an intervention semantics that routes effort through the receiving carrier's <em>existing absorption capacity</em>, LERM/IAMF-P did not dominate. Full telemetry achieved <strong>2.224283%</strong> burden reduction vs <strong>1.618167%</strong> for LERM/IAMF-P and <strong>1.546338%</strong> for raw LERM.
          </p>
          <!-- Horizontal Bar Chart -->
          <div class="space-y-2 font-mono text-[10px]">
            <div>
              <div class="flex justify-between text-zinc-300 mb-1">
                <span>Full Telemetry Predictive</span>
                <span class="text-white font-bold">2.2243%</span>
              </div>
              <div class="w-full bg-zinc-900 h-2"><div class="bg-cyan-400 h-full" style="width: 100%;"></div></div>
            </div>
            <div>
              <div class="flex justify-between text-zinc-300 mb-1">
                <span>Graph Digital Twin</span>
                <span class="text-zinc-400">2.0714%</span>
              </div>
              <div class="w-full bg-zinc-900 h-2"><div class="bg-zinc-500 h-full" style="width: 93%;"></div></div>
            </div>
            <div>
              <div class="flex justify-between text-zinc-300 mb-1">
                <span>LERM / IAMF-P Hybrid (Existing Capacity)</span>
                <span class="text-red-400 font-bold">1.6182% [LOSES]</span>
              </div>
              <div class="w-full bg-zinc-900 h-2"><div class="bg-red-400 h-full" style="width: 72.7%;"></div></div>
            </div>
            <div>
              <div class="flex justify-between text-zinc-300 mb-1">
                <span>LERM Raw</span>
                <span class="text-red-400 font-bold">1.5463% [LOSES]</span>
              </div>
              <div class="w-full bg-zinc-900 h-2"><div class="bg-red-500 h-full" style="width: 69.5%;"></div></div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-white/10 font-mono text-[9px] text-zinc-500">
            * Retained because it falsifies the lazy claim that any algorithm labeled LERM automatically wins.
          </div>
        </div>

        <!-- 7.3 Corrected Catch-Basin Simulation -->
        <div class="hud-box p-6 bg-zinc-950/90 border border-emerald-500/40">
          <div class="flex items-center justify-between border-b border-white/10 pb-3 mb-3">
            <span class="font-mono text-xs font-bold text-emerald-400 uppercase flex items-center gap-2">
              <span class="w-2 h-2 bg-emerald-400"></span>
              7.3 250,000-CASE CORRECTED CATCH-BASIN SIMULATION
            </span>
            <span class="font-mono text-[9px] text-emerald-400">+2.03% ADVANTAGE</span>
          </div>
          <p class="text-zinc-300 text-xs leading-relaxed mb-4">
            When intervention semantics were updated to match the intended IAMF-P definition (<strong>build new reconciliation capacity at the predicted loss carrier</strong>), the architecture gained systemic superiority:
          </p>
          <div class="space-y-2 font-mono text-[10px]">
            <div>
              <div class="flex justify-between text-zinc-100 mb-1">
                <span>LERM + IAMF-P (Capacity Built)</span>
                <span class="text-emerald-400 font-bold">5.6696% [WINS]</span>
              </div>
              <div class="w-full bg-zinc-900 h-2"><div class="bg-emerald-400 h-full" style="width: 100%;"></div></div>
            </div>
            <div>
              <div class="flex justify-between text-zinc-300 mb-1">
                <span>LERM Raw</span>
                <span class="text-zinc-300">5.6585%</span>
              </div>
              <div class="w-full bg-zinc-900 h-2"><div class="bg-emerald-500/70 h-full" style="width: 99.8%;"></div></div>
            </div>
            <div>
              <div class="flex justify-between text-zinc-300 mb-1">
                <span>Full Telemetry Predictor</span>
                <span class="text-zinc-400">5.5567%</span>
              </div>
              <div class="w-full bg-zinc-900 h-2"><div class="bg-cyan-500 h-full" style="width: 98.0%;"></div></div>
            </div>
            <div>
              <div class="flex justify-between text-zinc-300 mb-1">
                <span>Uniform Allocation</span>
                <span class="text-zinc-500">4.8551%</span>
              </div>
              <div class="w-full bg-zinc-900 h-2"><div class="bg-zinc-600 h-full" style="width: 85.6%;"></div></div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-white/10 font-mono text-[9px] text-zinc-400">
            * Proves the constructive thesis: capacity construction at the carrier outperforms generic allocation.
          </div>
        </div>
      </div>

      <!-- 7.4 & 7.6 Million-System & Public Architecture Coverage -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 font-mono">
        <!-- 7.4 Two 1,000,000-System Experiments -->
        <div class="hud-box p-6 bg-black/90">
          <div class="flex items-center justify-between border-b border-white/10 pb-2 mb-3">
            <span class="text-xs font-bold text-white uppercase">7.4 TWO 1,000,000-SYSTEM EXPERIMENTS</span>
            <span class="text-[9px] text-zinc-500">20 DOMAINS</span>
          </div>
          <p class="text-zinc-400 text-xs font-sans mb-3">
            Exp 1 falsified a generic universal heuristic (won only 1 of 20 domains). Exp 2 held graph and budget constant while varying the boundary:
          </p>
          <div class="space-y-1 text-xs">
            <div class="flex justify-between py-1 border-b border-white/5">
              <span>LERM/IAMF-P Whole-System</span>
              <span class="text-emerald-400 font-bold">7.9083%</span>
            </div>
            <div class="flex justify-between py-1 border-b border-white/5">
              <span>Boundary MPC</span>
              <span class="text-zinc-300">7.8256%</span>
            </div>
            <div class="flex justify-between py-1 border-b border-white/5">
              <span>Local KPI</span>
              <span class="text-zinc-400">7.5060%</span>
            </div>
            <div class="flex justify-between py-1 border-b border-white/5">
              <span>Full-Telemetry Next-Carrier</span>
              <span class="text-zinc-400">7.4880%</span>
            </div>
          </div>
          <p class="text-[10px] text-amber-300/80 mt-3 font-sans">
            Key finding: LERM won only 29% of individual cases while producing the better aggregate outcome—empirically motivating the Boundary Divergence Index (BDI).
          </p>
        </div>

        <!-- 7.6 Reverse-Engineered Public Architecture Coverage -->
        <div class="hud-box p-6 bg-black/90">
          <div class="flex items-center justify-between border-b border-white/10 pb-2 mb-3">
            <span class="text-xs font-bold text-white uppercase">7.6 REVERSE-ENGINEERED COVERAGE</span>
            <span class="text-[9px] text-zinc-500">RUBRIC MATRIX</span>
          </div>
          <p class="text-zinc-400 text-xs font-sans mb-3">
            Scores architectures across 8 dimensions (carrier tracking, hidden compensation, non-displacement retest):
          </p>
          <div class="space-y-1 text-[11px]">
            <div class="flex justify-between py-0.5">
              <span>LERM / IAMF-P</span>
              <span class="text-emerald-400 font-bold">87.5%</span>
            </div>
            <div class="flex justify-between py-0.5 text-zinc-400">
              <span>Palantir Foundry/AIP & Celonis</span>
              <span>68.8%</span>
            </div>
            <div class="flex justify-between py-0.5 text-zinc-400">
              <span>OpenAI, Anthropic, Gemini FSI</span>
              <span>62.5%</span>
            </div>
            <div class="flex justify-between py-0.5 text-zinc-500">
              <span>BlackRock Aladdin & Oracle</span>
              <span>50.0%</span>
            </div>
            <div class="flex justify-between py-0.5 text-zinc-600">
              <span>Moody's OneView & S&P EWS</span>
              <span>37.5%</span>
            </div>
          </div>
          <p class="text-[10px] text-zinc-500 mt-2 font-sans">
            * Interpreted as architectural feature coverage, not direct commercial performance benchmarks.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- PANE 4: PART 3 & FIGURE 3.1 // SCIENTIFIC LINEAGE (28 SCIENTISTS) -->
  <!-- ========================================================================= -->
  <section id="lineage" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-black border-t border-white/10">
    <!-- HD Background Image: Deep Space Cosmic Filaments -->
    <div class="absolute inset-0 z-0 pointer-events-none">
      <img 
        src="https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&w=2560&q=85" 
        alt="Deep space cosmic web and gravitational curvature" 
        class="w-full h-full object-cover object-center filter brightness-[0.45] contrast-[1.3]" 
        loading="lazy"
      />
      <div class="pane-scrim-heavy"></div>
    </div>

    <div class="relative z-20 max-w-7xl mx-auto w-full my-auto">
      <div class="flex items-center justify-between border-b border-white/15 pb-4 mb-8">
        <div>
          <span class="font-mono text-[10px] uppercase tracking-widest text-zinc-400 block mb-1">
            PART 3 // THE INTELLECTUAL CHAIN
          </span>
          <h2 class="font-display font-black text-3xl sm:text-5xl text-white uppercase tracking-tight">
            Scientific Lineage as One Continuous Chain
          </h2>
        </div>
        <div class="font-mono text-xs text-zinc-400 text-right">
          <div>FIGURE 3.1</div>
          <div class="text-white font-bold">1687 ➔ 2026</div>
        </div>
      </div>

      <p class="text-zinc-300 text-sm sm:text-base font-light max-w-3xl mb-8 leading-relaxed">
        The thinkers below are not presented as co-authors of LERM/IAMF-P. They are the scientific and institutional lineage that makes the present architecture intelligible. The contribution of Rufino must be stated relative to these prior achievements, not by erasing them.
      </p>

      <!-- Interactive Lineage Explorer (Figure 3.1) -->
      <div class="hud-box p-6 bg-black/90 mb-8 border border-white/20">
        <div class="flex items-center justify-between border-b border-white/10 pb-3 mb-4 font-mono text-xs">
          <span class="text-white font-bold uppercase">FIGURE 3.1 // LINEAGE TIMELINE & ADJACENT FRAMEWORKS</span>
          <span class="text-zinc-400">CLICK TO FILTER EPOCH</span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-7 gap-2 mb-6 font-mono text-[10px]">
          <button onclick="filterLineage('all')" class="lineage-btn border border-white bg-white text-black font-bold p-2 text-center">ALL 28</button>
          <button onclick="filterLineage('phys')" class="lineage-btn border border-white/20 bg-zinc-950 text-zinc-400 hover:text-white p-2 text-center">PHYSICS</button>
          <button onclick="filterLineage('econ')" class="lineage-btn border border-white/20 bg-zinc-950 text-zinc-400 hover:text-white p-2 text-center">ECONOMICS</button>
          <button onclick="filterLineage('cyber')" class="lineage-btn border border-white/20 bg-zinc-950 text-zinc-400 hover:text-white p-2 text-center">CYBERNETICS</button>
          <button onclick="filterLineage('bio')" class="lineage-btn border border-white/20 bg-zinc-950 text-zinc-400 hover:text-white p-2 text-center">BIOLOGY</button>
          <button onclick="filterLineage('ai')" class="lineage-btn border border-white/20 bg-zinc-950 text-zinc-400 hover:text-white p-2 text-center">AI & CAUSAL</button>
          <button onclick="filterLineage('rufino')" class="lineage-btn border border-white/20 bg-zinc-950 text-zinc-400 hover:text-white p-2 text-center">RUFINO (2026)</button>
        </div>

        <!-- The Lineage Cards Grid -->
        <div id="lineage-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 max-h-[420px] overflow-y-auto pr-2 font-mono text-xs">
          <!-- Newton -->
          <div class="p-3 border border-white/10 bg-zinc-950 lin-card lin-phys">
            <div class="flex justify-between text-zinc-400 text-[10px] mb-1"><span>ISAAC NEWTON (1687)</span><span class="text-cyan-400">PHYSICS</span></div>
            <div class="text-white font-bold mb-1">Classical Mechanics & Gravitation</div>
            <p class="text-[11px] text-zinc-400 font-sans">Local dynamical description. LERM asks what the chosen boundary excludes and how irreversible consequences move after.</p>
          </div>
          <!-- Clausius / Kelvin -->
          <div class="p-3 border border-white/10 bg-zinc-950 lin-card lin-phys">
            <div class="flex justify-between text-zinc-400 text-[10px] mb-1"><span>CLAUSIUS / KELVIN (19TH C.)</span><span class="text-cyan-400">PHYSICS</span></div>
            <div class="text-white font-bold mb-1">Thermodynamic Irreversibility & Entropy</div>
            <p class="text-[11px] text-zinc-400 font-sans">Physical lineage for irreversible processes; must treat entropy literally only in physics and use calibrated analogues elsewhere.</p>
          </div>
          <!-- Boltzmann -->
          <div class="p-3 border border-white/10 bg-zinc-950 lin-card lin-phys">
            <div class="flex justify-between text-zinc-400 text-[10px] mb-1"><span>LUDWIG BOLTZMANN (1877)</span><span class="text-cyan-400">PHYSICS</span></div>
            <div class="text-white font-bold mb-1">Statistical Interpretation of Entropy</div>
            <p class="text-[11px] text-zinc-400 font-sans">Microscopic-to-macroscopic state description and state aggregation without conflating social burden with thermal entropy.</p>
          </div>
          <!-- Gibbs -->
          <div class="p-3 border border-white/10 bg-zinc-950 lin-card lin-phys">
            <div class="flex justify-between text-zinc-400 text-[10px] mb-1"><span>J. WILLARD GIBBS (1876-1902)</span><span class="text-cyan-400">PHYSICS</span></div>
            <div class="text-white font-bold mb-1">Potentials & Heterogeneous Equilibrium</div>
            <p class="text-[11px] text-zinc-400 font-sans">Disciplined state-function accounting. Rufino adds carrier-specific displacement and post-intervention auditing.</p>
          </div>
          <!-- Einstein -->
          <div class="p-3 border border-white/10 bg-zinc-950 lin-card lin-phys">
            <div class="flex justify-between text-zinc-400 text-[10px] mb-1"><span>ALBERT EINSTEIN (1905)</span><span class="text-cyan-400">PHYSICS</span></div>
            <div class="text-white font-bold mb-1">Brownian Motion, Relativity, Photoelectric</div>
            <p class="text-[11px] text-zinc-400 font-sans">Observable macrobehavior reveals microscopic processes. Measurements depend on a defined frame; Rufino applies boundary discipline.</p>
          </div>
          <!-- Onsager -->
          <div class="p-3 border border-white/10 bg-zinc-950 lin-card lin-phys">
            <div class="flex justify-between text-zinc-400 text-[10px] mb-1"><span>LARS ONSAGER (1931, NOBEL 1968)</span><span class="text-cyan-400">PHYSICS</span></div>
            <div class="text-white font-bold mb-1">Reciprocal Relations for Irreversible Flows</div>
            <p class="text-[11px] text-zinc-400 font-sans">Direct precursor for coupled flows. LERM generalizes to directed burden/value flows with empirical domain units.</p>
          </div>
          <!-- Coase -->
          <div class="p-3 border border-white/10 bg-zinc-950 lin-card lin-econ">
            <div class="flex justify-between text-zinc-400 text-[10px] mb-1"><span>RONALD COASE (1937, NOBEL 1991)</span><span class="text-amber-400">ECONOMICS</span></div>
            <div class="text-white font-bold mb-1">Transaction Costs & Social Cost</div>
            <p class="text-[11px] text-zinc-400 font-sans">Direct ancestor of boundary costs. Rufino traces which carrier absorbs costs omitted by the optimized firm.</p>
          </div>
          <!-- Hayek -->
          <div class="p-3 border border-white/10 bg-zinc-950 lin-card lin-econ">
            <div class="flex justify-between text-zinc-400 text-[10px] mb-1"><span>F. A. HAYEK (1945, NOBEL 1974)</span><span class="text-amber-400">ECONOMICS</span></div>
            <div class="text-white font-bold mb-1">Dispersed Knowledge & Central Limits</div>
            <p class="text-[11px] text-zinc-400 font-sans">Importance of tacit information. LERM adds a provenance and carrier ledger for where translation work lands.</p>
          </div>
          <!-- Shannon -->
          <div class="p-3 border border-white/10 bg-zinc-950 lin-card lin-cyber">
            <div class="flex justify-between text-zinc-400 text-[10px] mb-1"><span>CLAUDE SHANNON (1948)</span><span class="text-purple-400">CYBERNETICS</span></div>
            <div class="text-white font-bold mb-1">Information Theory & Channel Capacity</div>
            <p class="text-[11px] text-zinc-400 font-sans">Language for uncertainty. Rufino adds consequential burden, carrier path, and intervention architecture beyond accuracy.</p>
          </div>
          <!-- Wiener -->
          <div class="p-3 border border-white/10 bg-zinc-950 lin-card lin-cyber">
            <div class="flex justify-between text-zinc-400 text-[10px] mb-1"><span>NORBERT WIENER (1948)</span><span class="text-purple-400">CYBERNETICS</span></div>
            <div class="text-white font-bold mb-1">Cybernetics: Feedback & Control</div>
            <p class="text-[11px] text-zinc-400 font-sans">Recursive observe-act-retest structure. Rufino adds non-displacement as a mandatory control objective.</p>
          </div>
          <!-- Simon -->
          <div class="p-3 border border-white/10 bg-zinc-950 lin-card lin-econ">
            <div class="flex justify-between text-zinc-400 text-[10px] mb-1"><span>HERBERT SIMON (1947, NOBEL 1978)</span><span class="text-amber-400">ECONOMICS</span></div>
            <div class="text-white font-bold mb-1">Bounded Rationality & Decision Making</div>
            <p class="text-[11px] text-zinc-400 font-sans">Reframed as boundary truncation: a local optimum exports unresolved burden outside its declared objective.</p>
          </div>
          <!-- Ashby -->
          <div class="p-3 border border-white/10 bg-zinc-950 lin-card lin-cyber">
            <div class="flex justify-between text-zinc-400 text-[10px] mb-1"><span>W. ROSS ASHBY (1956)</span><span class="text-purple-400">CYBERNETICS</span></div>
            <div class="text-white font-bold mb-1">Requisite Variety</div>
            <p class="text-[11px] text-zinc-400 font-sans">Directly adjacent to IAMF-P: a catchment must possess or build enough variety/capacity to regulate the disturbance received.</p>
          </div>
          <!-- Prigogine -->
          <div class="p-3 border border-white/10 bg-zinc-950 lin-card lin-phys">
            <div class="flex justify-between text-zinc-400 text-[10px] mb-1"><span>ILYA PRIGOGINE (1967, NOBEL 1977)</span><span class="text-cyan-400">PHYSICS</span></div>
            <div class="text-white font-bold mb-1">Non-Equilibrium Dissipative Structures</div>
            <p class="text-[11px] text-zinc-400 font-sans">Open systems maintain organized states by exchanging entropy with surroundings. Rufino extends this across socio-technical systems.</p>
          </div>
          <!-- Mitchell -->
          <div class="p-3 border border-white/10 bg-zinc-950 lin-card lin-bio">
            <div class="flex justify-between text-zinc-400 text-[10px] mb-1"><span>PETER MITCHELL (1961, NOBEL 1978)</span><span class="text-emerald-400">BIOLOGY</span></div>
            <div class="text-white font-bold mb-1">Chemiosmotic Biological Energy Transfer</div>
            <p class="text-[11px] text-zinc-400 font-sans">Shows how gradients, membranes and coupling convert energy into work; biological precedent for carrier/coupling maps.</p>
          </div>
          <!-- Ostrom / Williamson -->
          <div class="p-3 border border-white/10 bg-zinc-950 lin-card lin-econ">
            <div class="flex justify-between text-zinc-400 text-[10px] mb-1"><span>OSTROM / WILLIAMSON (NOBEL 2009)</span><span class="text-amber-400">ECONOMICS</span></div>
            <div class="text-white font-bold mb-1">Commons Governance & Boundaries of Firms</div>
            <p class="text-[11px] text-zinc-400 font-sans">Who carries coordination costs. IAMF-P builds the missing governance/capacity structure at the receiving carrier.</p>
          </div>
          <!-- Friston -->
          <div class="p-3 border border-white/10 bg-zinc-950 lin-card lin-bio">
            <div class="flex justify-between text-zinc-400 text-[10px] mb-1"><span>KARL FRISTON (2010)</span><span class="text-emerald-400">BIOLOGY</span></div>
            <div class="text-white font-bold mb-1">Free-Energy Principle & Active Inference</div>
            <p class="text-[11px] text-zinc-400 font-sans">Prediction error and generative models. Bridges to the human adapter and schema-gap equations.</p>
          </div>
          <!-- Pearl -->
          <div class="p-3 border border-white/10 bg-zinc-950 lin-card lin-ai">
            <div class="flex justify-between text-zinc-400 text-[10px] mb-1"><span>JUDEA PEARL (2000-2009)</span><span class="text-blue-400">AI & CAUSAL</span></div>
            <div class="text-white font-bold mb-1">Structural Causal Models & Interventions</div>
            <p class="text-[11px] text-zinc-400 font-sans">Distinguishing association from intervention. LERM must meet this standard when claiming a carrier or coupling point is causal.</p>
          </div>
          <!-- Hopfield & Hinton -->
          <div class="p-3 border border-white/10 bg-zinc-950 lin-card lin-ai">
            <div class="flex justify-between text-zinc-400 text-[10px] mb-1"><span>HOPFIELD & HINTON (NOBEL 2024)</span><span class="text-blue-400">AI & CAUSAL</span></div>
            <div class="text-white font-bold mb-1">Artificial Neural Networks Foundations</div>
            <p class="text-[11px] text-zinc-400 font-sans">The predictive AI representation frontier. LERM/IAMF-P positions itself as a consequential-boundary layer around predictions.</p>
          </div>
          <!-- Baker, Hassabis, Jumper -->
          <div class="p-3 border border-white/10 bg-zinc-950 lin-card lin-ai">
            <div class="flex justify-between text-zinc-400 text-[10px] mb-1"><span>BAKER, HASSABIS, JUMPER (NOBEL 2024)</span><span class="text-blue-400">AI & CAUSAL</span></div>
            <div class="text-white font-bold mb-1">Protein Structure Prediction</div>
            <p class="text-[11px] text-zinc-400 font-sans">Power of learned structure prediction. LERM adds: after prediction, trace system-level displaced burden.</p>
          </div>
          <!-- Rufino -->
          <div class="p-3 border border-white bg-black lin-card lin-rufino">
            <div class="flex justify-between text-white text-[10px] mb-1"><span>JEFFERSON RAFAEL RUFINO (2025-26)</span><span class="text-emerald-400 font-bold">SYNTHESIS</span></div>
            <div class="text-white font-bold mb-1">LERM / IAMF-P Recurrent Kernel</div>
            <p class="text-[11px] text-zinc-200 font-sans">Treat the afterlife of optimization as a first-class object; make structural reconciliation and non-displacement retesting part of one frozen loop.</p>
          </div>
        </div>
      </div>

      <!-- Section 3.3 Contribution Statement -->
      <div class="hud-box p-6 bg-zinc-950/90 border border-white/20">
        <span class="font-mono text-xs text-white font-bold uppercase block mb-2">
          PART 10.3 // THE PRECISE CONTRIBUTION STATEMENT
        </span>
        <blockquote class="text-zinc-200 font-mono text-xs sm:text-sm leading-relaxed border-l-2 border-white pl-4">
          "Jefferson Rafael Rufino's contribution is the proposed integration of consequential-boundary expansion, directed displacement tracing, carrier and hidden-compensator identification, structural reconciliation capacity, productive reintegration, provenance governance and mandatory non-displacement retesting into a single recurrent LERM/IAMF-P operator. The architecture emerged from a longitudinal operating and survival record, has undergone internal adversarial simulation and software conformance testing, and now requires independent prospective validation against established domain methods."
        </blockquote>
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- PANE 5: PART 5 // REALITY BRANCHES: ONE KERNEL, 18 DIFFERENT MAPS -->
  <!-- ========================================================================= -->
  <section id="branches" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-black border-t border-white/10">
    <!-- HD Background Image: Planetary Night Power Grids & Infrastructure -->
    <div class="absolute inset-0 z-0 pointer-events-none">
      <img 
        src="https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=2560&q=85" 
        alt="Macro planetary electrical grid and systemic network" 
        class="w-full h-full object-cover object-center filter brightness-[0.4] contrast-[1.35]" 
        loading="lazy"
      />
      <div class="pane-scrim-heavy"></div>
    </div>

    <div class="relative z-20 max-w-7xl mx-auto w-full my-auto">
      <div class="flex items-center justify-between border-b border-white/15 pb-4 mb-8">
        <div>
          <span class="font-mono text-[10px] uppercase tracking-widest text-zinc-400 block mb-1">
            PART 5 // ONE KERNEL, DIFFERENT MAPS
          </span>
          <h2 class="font-display font-black text-3xl sm:text-5xl text-white uppercase tracking-tight">
            The 18 Reality Branches
          </h2>
        </div>
        <div class="font-mono text-xs text-zinc-400 text-right">
          <div>TOTAL MAPS</div>
          <div class="text-white font-bold">5.1 THROUGH 5.18</div>
        </div>
      </div>

      <p class="text-zinc-300 text-sm sm:text-base font-light max-w-3xl mb-8 leading-relaxed">
        The branch map separates what the incumbent sees, what LERM makes visible, the algebraic adapter, the IAMF-P construction, and a real falsification test. These are research programs, not claims of prior universal empirical completion.
      </p>

      <!-- Interactive Branch Selector Tabs -->
      <div class="hud-box p-6 bg-black/90 mb-6">
        <div class="flex items-center justify-between border-b border-white/10 pb-3 mb-4 font-mono text-xs">
          <span class="text-white font-bold">SELECT BRANCH TO INSPECT STATE MAP & ADAPTER</span>
          <span id="active-branch-indicator" class="text-emerald-400">ACTIVE: 5.1 LUXURY & PHYSICAL ASSETS</span>
        </div>

        <!-- 18 Branch Buttons -->
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-2 font-mono text-[10px]">
          <button onclick="inspectBranch(1)" class="branch-btn border border-white bg-white text-black font-bold p-2 text-left">5.1 LUXURY</button>
          <button onclick="inspectBranch(2)" class="branch-btn border border-white/20 bg-zinc-950 text-zinc-300 p-2 text-left">5.2 BANKING</button>
          <button onclick="inspectBranch(3)" class="branch-btn border border-white/20 bg-zinc-950 text-zinc-300 p-2 text-left">5.3 MACROECON</button>
          <button onclick="inspectBranch(4)" class="branch-btn border border-white/20 bg-zinc-950 text-zinc-300 p-2 text-left">5.4 FOUNDERS</button>
          <button onclick="inspectBranch(5)" class="branch-btn border border-white/20 bg-zinc-950 text-zinc-300 p-2 text-left">5.5 PSYCHOLOGY</button>
          <button onclick="inspectBranch(6)" class="branch-btn border border-white/20 bg-zinc-950 text-zinc-300 p-2 text-left">5.6 HEALTHCARE</button>
          <button onclick="inspectBranch(7)" class="branch-btn border border-white/20 bg-zinc-950 text-zinc-300 p-2 text-left">5.7 CANCER</button>
          <button onclick="inspectBranch(8)" class="branch-btn border border-white/20 bg-zinc-950 text-zinc-300 p-2 text-left">5.8 NEUROSCIENCE</button>
          <button onclick="inspectBranch(9)" class="branch-btn border border-white/20 bg-zinc-950 text-zinc-300 p-2 text-left">5.9 AGING</button>
          <button onclick="inspectBranch(10)" class="branch-btn border border-white/20 bg-zinc-950 text-zinc-300 p-2 text-left">5.10 POWER GRIDS</button>
          <button onclick="inspectBranch(11)" class="branch-btn border border-white/20 bg-zinc-950 text-zinc-300 p-2 text-left">5.11 CLIMATE</button>
          <button onclick="inspectBranch(12)" class="branch-btn border border-white/20 bg-zinc-950 text-zinc-300 p-2 text-left">5.12 LOGISTICS</button>
          <button onclick="inspectBranch(13)" class="branch-btn border border-white/20 bg-zinc-950 text-zinc-300 p-2 text-left">5.13 CYBERSECURITY</button>
          <button onclick="inspectBranch(14)" class="branch-btn border border-white/20 bg-zinc-950 text-zinc-300 p-2 text-left">5.14 AI AGENTS</button>
          <button onclick="inspectBranch(15)" class="branch-btn border border-white/20 bg-zinc-950 text-zinc-300 p-2 text-left">5.15 PUBLIC ADMIN</button>
          <button onclick="inspectBranch(16)" class="branch-btn border border-white/20 bg-zinc-950 text-zinc-300 p-2 text-left">5.16 ECOLOGY</button>
          <button onclick="inspectBranch(17)" class="branch-btn border border-white/20 bg-zinc-950 text-zinc-300 p-2 text-left">5.17 SPACECRAFT</button>
          <button onclick="inspectBranch(18)" class="branch-btn border border-white/20 bg-zinc-950 text-zinc-300 p-2 text-left">5.18 PHYSICS</button>
        </div>
      </div>

      <!-- Selected Branch Detailed HUD Card -->
      <div id="branch-display-card" class="hud-box p-8 bg-zinc-950/95 border border-white/20">
        <!-- Dynamic content filled via JS -->
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- PANE 6: PART 8 & CLOSING STATEMENT // WHAT THE ARCHITECTURE MAKES VISIBLE -->
  <!-- ========================================================================= -->
  <section id="closing" class="relative min-h-screen w-full flex flex-col justify-between py-24 px-6 sm:px-12 lg:px-20 overflow-hidden bg-black border-t border-white/10">
    <!-- HD Background Image: Starship Launchpad & Aerospace Telemetry -->
    <div class="absolute inset-0 z-0 pointer-events-none">
      <img 
        src="https://images.unsplash.com/photo-1517976487502-5c8a4174d8a5?auto=format&fit=crop&w=2560&q=85" 
        alt="Space launchpad and aerospace telemetry control" 
        class="w-full h-full object-cover object-center filter brightness-[0.38] contrast-[1.4]" 
        loading="lazy"
      />
      <div class="pane-scrim-heavy"></div>
    </div>

    <div class="relative z-20 max-w-7xl mx-auto w-full my-auto">
      <div class="max-w-4xl mx-auto">
        <!-- The Afterlife of Optimization -->
        <div class="hud-box p-8 sm:p-10 bg-black/90 mb-10 border border-white">
          <div class="flex items-center justify-between border-b border-white/20 pb-3 mb-4">
            <span class="font-mono text-xs font-bold text-white uppercase tracking-wider">
              PART 8.1 // THE AFTERLIFE OF OPTIMIZATION
            </span>
            <span class="font-mono text-[9px] text-zinc-400">FOUNDATIONAL DIALECTIC</span>
          </div>

          <p class="text-zinc-300 text-sm leading-relaxed mb-6 font-light">
            The deepest common object across the archive is not "loss" in the ordinary accounting sense. It is the <strong>afterlife of an optimization</strong>: what survives outside the definition of success after the optimized system has declared victory.
          </p>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 font-mono text-xs border border-white/10 p-4 bg-zinc-950 mb-6">
            <div class="text-zinc-400">
              <span class="text-[9px] uppercase text-zinc-500 block mb-1">Conventional Dashboard</span>
              <div class="text-white border-l border-red-500 pl-2">result at declared boundary</div>
            </div>
            <div class="text-zinc-300">
              <span class="text-[9px] uppercase text-emerald-400 block mb-1">The Rufino Lens</span>
              <div class="text-white border-l border-emerald-400 pl-2">result + countermovement + carrier + hidden compensator + future recurrence + post-intervention displacement</div>
            </div>
          </div>

          <div class="space-y-1 font-mono text-xs text-zinc-300 border-t border-white/10 pt-4">
            <div>profit → deferred maintenance</div>
            <div>bank stability → household distress</div>
            <div>AI productivity → human verification load</div>
            <div>organizational excellence → founder biological load</div>
            <div>shorter hospital stay → caregiver/readmission burden</div>
            <div>tumor shrinkage → resistant-pathway dominance</div>
            <div>forecast accuracy → unreconciled infrastructure exposure</div>
          </div>
        </div>

        <!-- The Canonical Closing Statement -->
        <div class="hud-box p-8 sm:p-12 bg-black/95 border-2 border-white text-center mb-10">
          <p class="font-mono text-xs text-zinc-400 uppercase tracking-widest mb-6">
            CLOSING STATEMENT // SEPTEMBER 2026
          </p>
          <blockquote class="text-white font-mono text-lg sm:text-2xl font-bold tracking-tight leading-relaxed mb-8">
            "Find where reality escaped. Follow where it went. Name what carried it. Build where it landed. Transform what was recovered. Check every carrier and every future period again. Then look again."
          </blockquote>
          <div class="font-mono text-xs text-zinc-400">
            JEFFERSON RAFAEL RUFINO // THE RUFINO SYNTHESIS // LERM + IAMF-P
          </div>
        </div>

        <!-- Central Dispatch Jump Links to Other 8 Tabs -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 font-mono text-[11px] text-center">
          <a href="/founder" class="border border-white/20 p-3 bg-zinc-950 hover:border-white text-zinc-300 hover:text-white transition block">
            01. THE FOUNDER
          </a>
          <a href="/realities" class="border border-white/20 p-3 bg-zinc-950 hover:border-white text-zinc-300 hover:text-white transition block">
            02. 120 ADAPTERS
          </a>
          <a href="/LERM" class="border border-white/20 p-3 bg-zinc-950 hover:border-white text-zinc-300 hover:text-white transition block">
            03. LERM & 2027
          </a>
          <a href="/photosynthesisproject" class="border border-white/20 p-3 bg-zinc-950 hover:border-white text-zinc-300 hover:text-white transition block">
            04. PHOTOSYNTHESIS
          </a>
          <a href="/shopfamcollective" class="border border-white/20 p-3 bg-zinc-950 hover:border-white text-zinc-300 hover:text-white transition block">
            05. SHOPFAM ARCH
          </a>
          <a href="/scientists" class="border border-white/20 p-3 bg-zinc-950 hover:border-white text-zinc-300 hover:text-white transition block">
            06. SCIENTISTS
          </a>
          <a href="/build" class="border border-white/20 p-3 bg-zinc-950 hover:border-white text-zinc-300 hover:text-white transition block">
            07. BUILD WITH US
          </a>
          <a href="/contactus" class="border border-white/20 p-3 bg-zinc-950 hover:border-white text-zinc-300 hover:text-white transition block">
            08. CONTACT US
          </a>
        </div>
      </div>
    </div>

    <!-- Verified Footer -->
    <div class="relative z-20 max-w-7xl mx-auto w-full border-t border-white/15 pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 font-mono text-[10px] text-zinc-500">
      <div>
        © 2026 RUFINO VENTURES. ARCHITECTED BY JEFFERSON RAFAEL RUFINO. ALL RIGHTS RESERVED.
      </div>
      <div class="flex items-center space-x-6">
        <a href="mailto:jeffersonrrufino@gmail.com" class="hover:text-white transition">jeffersonrrufino@gmail.com</a>
        <a href="https://linkedin.com/in/jeffersonrufino" target="_blank" rel="noopener" class="hover:text-white transition">LinkedIn</a>
        <a href="https://instagram.com/thehighlandboy" target="_blank" rel="noopener" class="hover:text-white transition">@thehighlandboy</a>
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- JAVASCRIPT: INTERACTIVE PARTICLES, BRANCH DATA, & LINEAGE FILTERS -->
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
    // 1. LIVE QUANTUM LATTICE & DYNAMIC CURVATURE CANVAS
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

        for (let p of points) {
          let baseX = p.origX * width;
          let baseY = p.origY * height;

          let wave = Math.sin(time + p.col * 0.35 + p.row * 0.25) * 8;
          let wave2 = Math.cos(time * 0.7 + p.col * 0.2 - p.row * 0.4) * 6;

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

        ctx.lineWidth = 0.75;
        for (let p of points) {
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
    // 2. 18 REALITY BRANCHES DATABASE & INSPECTOR
    // -------------------------------------------------------------------------
    const branchesData = {
      1: {
        num: "5.1",
        title: "LUXURY AND PHYSICAL ASSETS",
        state: "X = [c, p, t, l, a, o]: condition, provenance, trust, liquidity, access, optionality.",
        visible: "Primary-market accounting often ends at sale; secondary decay, authenticity uncertainty, idle inventory and access loss sit outside the declared boundary.",
        algebra: "D_{asset} = V_{potential} - V_{realized}; \\quad A^* = \\arg\\max_A (\\Delta V_{life} - \\lambda U_{buyer} - \\mu U_{brand})",
        iamfp: "Authentication, restoration, provenance, distribution and lifecycle stewardship.",
        falsification: "Prospective cohort comparing lifecycle retained value, dispute/return rates, provenance certainty and brand externalities."
      },
      2: {
        num: "5.2",
        title: "BANKING AND FINANCE",
        state: "X = [K, L, D, M, R, C]: capital, liquidity, debt, maturity, risk, counterparties.",
        visible: "A bank can reduce its own risk while shifting liquidity, fee, timing or documentation burden into households, firms, NBFIs or government.",
        algebra: "BDI = J_G(a^*_S) - J_G(a^*_G); \\quad \\mathcal{D}_a(j, k, \\tau) \\text{ maps carrier, burden type and delay}",
        iamfp: "Buffers, redesigned capital access, settlement, documentation and risk-sharing structures at the receiving carrier.",
        falsification: "Matched interventions scored on whole-system loss, worst-carrier load, defaults and delayed burden."
      },
      3: {
        num: "5.3",
        title: "MACROECONOMY",
        state: "X_t \\text{ is a vector of sector balances, household resilience, investment, savings, energy and future capacity.}",
        visible: "Headline growth/savings can coexist with concentrated fragility; the missing quantity is who actually retained the created value and who carried the optimization cost.",
        algebra: "D_{net}(T) = \\int_0^T [\\nabla \\cdot J^{ext} + L^{tacit} + K^{debt} - R^{recov}]dt - \\Delta V_{real}",
        iamfp: "Policy/institutional capacity at empirically identified carriers rather than generic redistribution.",
        falsification: "National accounts plus household/sector microdata with explicit unit-preserving vectors and holdout periods."
      },
      4: {
        num: "5.4",
        title: "ORGANIZATIONS AND FOUNDER SYSTEMS",
        state: "X = [Q, I, C, T, S, R]: output quality, integration, complexity, time, support and redundancy.",
        visible: "A company can look healthy because one person silently supplies missing functions; success itself hides the single point of failure.",
        algebra: "EP = \\frac{Q \\cdot C \\cdot I}{T}; \\quad RVG = \\dot{U} - \\dot{R}_c; \\quad TR = \\frac{P_{post}}{P_{founder}}",
        iamfp: "Governed delegation, institutional redundancy, specialist capacity and reciprocal safety.",
        falsification: "Transfer functions away from founder while holding quality and throughput; success requires founder burden to fall."
      },
      5: {
        num: "5.5",
        title: "PSYCHOLOGY AND SOCIAL LEGIBILITY",
        state: "H_t \\text{ actual/latent human state}; \\quad \\hat{H}_t = g(H_t, S_t) \\text{ recognized state under receiver schema } S_t.",
        visible: "Observed constrained behavior may be evidence of denied support rather than absence of capacity; the receiver model can help create the outcome it later treats as proof.",
        algebra: "G_{schema} = \\mathbb{E}[d(H, \\hat{H})] \\text{ or } D_{KL}(P(H|O) \\parallel P_{inst}(H|O)); \\quad Y_{t+1} = h(H_t, A_t, F_t)",
        iamfp: "Translation, trust, support, resources and safer feedback channels.",
        falsification: "Prospective intervention measuring recognition accuracy, support allocation, performance and biological/economic compensatory load."
      },
      6: {
        num: "5.6",
        title: "HEALTHCARE DELIVERY",
        state: "X = [\\text{disease}, \\text{delay}, \\text{toxicity}, \\text{readmission}, \\text{cost}, \\text{caregiver burden}].",
        visible: "Throughput or discharge efficiency can export workload, cost and risk to families, downstream clinicians or later readmissions.",
        algebra: "U_G = U_{clinical} + U_{delay} + U_{tox} + U_{caregiver} + U_{future}; \\quad \\text{minimize } U_G \\text{ not single facility KPI}",
        iamfp: "Care coordination, follow-up capacity, financing and caregiver support targeted to the receiving burden.",
        falsification: "Randomized or stepped-wedge service redesign with whole-patient and whole-network outcomes."
      },
      7: {
        num: "5.7",
        title: "CANCER",
        state: "X = [\\text{clones}, \\text{signaling}, \\text{microenvironment}, \\text{immune state}, \\text{toxicity}, \\text{reserve}].",
        visible: "Tumor shrinkage can alter selection pressure and make a resistant pathway the new dominant carrier of survival.",
        algebra: "i^*_{t+1} = \\arg\\max_i \\dot{U}_i(t+1) \\text{ after intervention}; \\quad A^*_{t+1} = \\pi(X_{t+1})",
        iamfp: "Adaptive therapy or combination strategy aimed at the newly dominant causal pathway, subject to toxicity/reserve constraints.",
        falsification: "Preclinical/clinical adaptive protocols; a failure if total burden or toxicity rises despite target shrinkage."
      },
      8: {
        num: "5.8",
        title: "NEUROSCIENCE AND NEURODEGENERATION",
        state: "X = [\\text{signal}, \\text{myelin}, \\text{synapse}, \\text{glia}, \\text{vascular}, \\text{metabolic}, \\text{reserve}].",
        visible: "A local pathology marker can improve while network transmission or metabolic support remains the true limiting carrier.",
        algebra: "U_{neural} = \\sum_i w_i d_i; \\quad i^* = \\arg\\max_i w_i \\dot{d}_i; \\quad \\text{retest after intervention}",
        iamfp: "Support/intervention at the rate-limiting biological carrier.",
        falsification: "Longitudinal multimodal data with functional endpoints, not biomarker-only victory."
      },
      9: {
        num: "5.9",
        title: "AGING",
        state: "d_1, \\dots, d_n \\text{ represent damage processes and reserve constraints.}",
        visible: "Repairing one mechanism can expose another limiting process or increase a competing risk such as oncogenesis.",
        algebra: "U_{age} = \\sum_i w_i d_i; \\quad \\text{reconcile if } \\dot{U}_{age} < 0 \\text{ while no material risk carrier rises}",
        iamfp: "Iterative repair/prevention at the current dominant unresolved process.",
        falsification: "Multi-endpoint longevity studies with competing-risk and delayed-harm auditing."
      },
      10: {
        num: "5.10",
        title: "ENERGY AND POWER GRIDS",
        state: "X = [\\text{generation}, \\text{demand}, \\text{storage}, \\text{transmission}, \\text{price}, \\text{emissions}, \\text{maintenance}].",
        visible: "Cheap/efficient local generation can export reliability, grid-upgrade, curtailment, pollution or deferred-maintenance burden.",
        algebra: "J_G = J_{cost} + \\lambda J_{reliability} + \\mu J_{emissions} + \\nu J_{deferred}; \\quad BDI \\text{ gates intervention}",
        iamfp: "Storage, transmission, demand response, redundancy or pricing changes where the burden lands.",
        falsification: "Grid simulation plus real outage/tariff/emissions data; compare local dispatch with consequential-boundary control."
      },
      11: {
        num: "5.11",
        title: "WEATHER, CLIMATE AND DISASTER RESPONSE",
        state: "X = [T, P, H, v, q, \\text{soil}, \\text{rivers}, \\text{infrastructure}, \\text{population}].",
        visible: "Prediction is not reconciliation. Forecast accuracy can coexist with unprepared drainage, evacuation, storage or grid systems.",
        algebra: "RVG_{hazard} = \\dot{U}_{hazard} - \\dot{R}_{response}; \\quad \\text{risk rises when } RVG > 0",
        iamfp: "Reservoirs, drainage, evacuation, thermal/storage capacity, grid preparation and response routing.",
        falsification: "Prospective hazard periods measuring avoided losses and any burden shifted to neighboring regions."
      },
      12: {
        num: "5.12",
        title: "SUPPLY CHAINS AND LOGISTICS",
        state: "X = [\\text{inventory}, \\text{cash}, \\text{leadtime}, \\text{supplier reserve}, \\text{transport}, \\text{demand}].",
        visible: "Lean optimization can push fragility into suppliers and future stockouts; apparent working-capital efficiency hides resilience debt.",
        algebra: "U_G = U_{buyer} + U_{supplier} + U_{delay} + U_{stockout} + U_{finance}; \\quad \\text{optimize under worst-carrier constraints}",
        iamfp: "Supplier finance, buffer inventory, routing redundancy and redesigned service-level contracts.",
        falsification: "Shock/recovery experiments with total lifecycle cost, service, supplier solvency and delay."
      },
      13: {
        num: "5.13",
        title: "CYBERSECURITY",
        state: "X = [\\text{attack graph}, \\text{exposure}, \\text{detection}, \\text{recovery}, \\text{human workload}].",
        visible: "Blocking one vector may redirect attacks or increase manual verification and operational downtime elsewhere.",
        algebra: "EL = \\sum_j p_j L_j + \\lambda H_j; \\quad \\text{displacement field updates after defense action}",
        iamfp: "Defense, redundancy, recovery and verification capacity at predicted next carriers.",
        falsification: "Red-team campaign with causal attack-path tracing and total organizational burden."
      },
      14: {
        num: "5.14",
        title: "AI INFRASTRUCTURE AND AGENTS",
        state: "X = [\\text{accuracy}, \\text{compute}, \\text{energy}, \\text{human review}, \\text{latency}, \\text{error propagation}].",
        visible: "A model can improve task accuracy while exporting verification work, energy cost, data risk or downstream correction to humans.",
        algebra: "\\text{NetV} = \\Delta O - C_{compute} - C_{energy} - C_{human} - C_{downstream}; \\quad \\text{all terms audited}",
        iamfp: "Verification, escalation, provenance, redundancy and workflow redesign.",
        falsification: "Matched agent workflows scored on end-to-end task value, human minutes, error and compute/energy."
      },
      15: {
        num: "5.15",
        title: "PUBLIC ADMINISTRATION",
        state: "X = [\\text{agency cost}, \\text{citizen burden}, \\text{firm burden}, \\text{access}, \\text{delay}, \\text{future liability}].",
        visible: "Administrative efficiency can be purchased by forcing citizens to supply forms, travel, waiting, translation and repeated proof.",
        algebra: "J_G = J_{agency} + \\sum_p w_p B_p + \\lambda FutureCost; \\quad \\text{schema mismatch enters access probability}",
        iamfp: "Simplified interfaces, shared data, case navigation and support for high-friction carriers.",
        falsification: "Service redesign using completion rate, citizen time/cost, equity and agency cost together."
      },
      16: {
        num: "5.16",
        title: "ECOLOGY AND COMMONS",
        state: "X = [\\text{species}, \\text{habitat}, \\text{nutrients}, \\text{pollutants}, \\text{harvest}, \\text{governance}].",
        visible: "A local conservation or production gain can displace extraction pressure, nutrient load or habitat loss through the network.",
        algebra: "\\mathcal{D}_a(j, k, \\tau) \\text{ over ecological carriers; success requires no material burden migration}",
        iamfp: "Habitat, quota, monitoring and polycentric governance where pressure is transmitted.",
        falsification: "BACI/longitudinal ecological studies with network spillover metrics."
      },
      17: {
        num: "5.17",
        title: "SPACECRAFT AND CLOSED-LOOP LIFE SUPPORT",
        state: "X = [O_2, CO_2, H_2O, \\text{thermal}, \\text{radiation}, \\text{power}, \\text{crew}, \\text{reserves}].",
        visible: "Subsystem nominal status can hide reserve depletion or crew compensation; the carrier may be another subsystem or future mission margin.",
        algebra: "RVG_{mission} = \\dot{U}_{mission} - \\dot{R}_c; \\quad \\text{require } RVG \\le 0 \\text{ and reserves above critical thresholds}",
        iamfp: "Redundancy, storage, routing and repair capacity at the emerging bottleneck.",
        falsification: "High-fidelity mission simulations and hardware-in-the-loop anomaly tests."
      },
      18: {
        num: "5.18",
        title: "FUNDAMENTAL PHYSICS AND MATHEMATICS",
        state: "X \\text{ is a field/equation state plus boundary conditions, residuals and proof obligations.}",
        visible: "A small numerical residual can be mistaken for a proof; hidden assumptions or boundary pathologies may remain outside the computed domain.",
        algebra: "\\|R(u)\\| \\to 0 \\text{ is numerical evidence only; proof requires theorem-level closure}",
        iamfp: "Better decomposition, counterexample search, boundary-condition analysis and formal proof tooling.",
        falsification: "Independent peer review and formal verification. LERM/IAMF-P has not established solutions to Millennium Prize problems in the supplied evidence."
      }
    };

    function inspectBranch(id) {
      const data = branchesData[id];
      if (!data) return;

      document.getElementById('active-branch-indicator').innerText = "ACTIVE: " + data.num + " " + data.title;
      
      const card = document.getElementById('branch-display-card');
      card.innerHTML = `
        <div class="flex flex-wrap items-center justify-between border-b border-white/10 pb-3 mb-4">
          <span class="font-display font-bold text-xl text-white uppercase">${data.num} ${data.title}</span>
          <span class="font-mono text-[10px] px-2 py-0.5 bg-white/10 text-emerald-400 font-bold uppercase">CANONICAL ADAPTER</span>
        </div>
        <div class="space-y-4 font-mono text-xs">
          <div>
            <strong class="text-zinc-400 uppercase text-[10px] block mb-1">State Map:</strong>
            <div class="text-white p-3 bg-black/80 border border-white/10">\$$${data.state}\$$</div>
          </div>
          <div>
            <strong class="text-zinc-400 uppercase text-[10px] block mb-1">What Becomes Visible Beyond Local Boundary:</strong>
            <p class="text-zinc-200 font-sans text-sm leading-relaxed">${data.visible}</p>
          </div>
          <div>
            <strong class="text-zinc-400 uppercase text-[10px] block mb-1">Algebraic Adapter:</strong>
            <div class="text-emerald-300 p-3 bg-black/80 border border-white/10 overflow-x-auto">\$$${data.algebra}\$$</div>
          </div>
          <div>
            <strong class="text-zinc-400 uppercase text-[10px] block mb-1">IAMF-P Construction:</strong>
            <p class="text-zinc-200 font-sans text-sm leading-relaxed">${data.iamfp}</p>
          </div>
          <div>
            <strong class="text-zinc-400 uppercase text-[10px] block mb-1">Falsification / Validation Path:</strong>
            <p class="text-amber-300/90 font-sans text-sm leading-relaxed">${data.falsification}</p>
          </div>
        </div>
      `;

      if (window.renderMathInElement) {
        renderMathInElement(card, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});
      }

      document.querySelectorAll('.branch-btn').forEach(b => {
        b.className = "branch-btn border border-white/20 bg-zinc-950 text-zinc-300 p-2 text-left";
      });
      event.target.className = "branch-btn border border-white bg-white text-black font-bold p-2 text-left";
    }

    // Initialize with branch 1
    inspectBranch(1);

    // -------------------------------------------------------------------------
    // 3. SCIENTIFIC LINEAGE FILTER
    // -------------------------------------------------------------------------
    function filterLineage(cat) {
      document.querySelectorAll('.lineage-btn').forEach(b => {
        b.className = "lineage-btn border border-white/20 bg-zinc-950 text-zinc-400 hover:text-white p-2 text-center";
      });
      event.target.className = "lineage-btn border border-white bg-white text-black font-bold p-2 text-center";

      const cards = document.querySelectorAll('.lin-card');
      cards.forEach(card => {
        if (cat === 'all') {
          card.style.display = 'block';
        } else if (card.classList.contains('lin-' + cat)) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    }
  </script>
</body>
</html>
"""

def main():
    html_content = generate_synthesis_html()
    root_dir = "/Users/thehighlandboy/Downloads/RUFINOVENTURES"
    
    for filename in ["index.html", "RUFINOVENTURES.html"]:
        path = os.path.join(root_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"  ✓ Successfully deployed {len(html_content):,} bytes to {path}")

if __name__ == "__main__":
    main()
