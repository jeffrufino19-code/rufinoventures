import json, os

# Load rich adapters
with open('/tmp/canonical_120_adapters_rich.json') as f:
    adapters = json.load(f)

# Family metadata
families = {
    1: {"code": "F01", "name": "Human life quality", "desc": "Whole-person functional capacity, longevity, recovery, and domestic environment.", "range": "A001 – A010"},
    2: {"code": "F02", "name": "Psychology & meaning", "desc": "Self-model, intimacy, trust, purpose, affect regulation, and social legibility.", "range": "A011 – A020"},
    3: {"code": "F03", "name": "Biomedical & cellular", "desc": "Host reserve, clinical diagnostics, oncology, neurodegeneration, and immunology.", "range": "A021 – A030"},
    4: {"code": "F04", "name": "Education, justice & governance", "desc": "Child development, judicial sentencing, policing, corrections, and public administration.", "range": "A031 – A040"},
    5: {"code": "F05", "name": "Culture, beauty & experience", "desc": "Aesthetic capital, fashion, luxury provenance, gaming, hospitality, and cultural markets.", "range": "A041 – A050"},
    6: {"code": "F06", "name": "Money, markets & organizations", "desc": "Banking liquidity, credit underwriting, insurance, sovereign wealth, and venture creation.", "range": "A051 – A060"},
    7: {"code": "F07", "name": "Technology & information", "desc": "Artificial intelligence, software systems, cybersecurity, data infra, and digital identity.", "range": "A061 – A070"},
    8: {"code": "F08", "name": "Earth, infrastructure & ecology", "desc": "Energy grids, water, agrivoltaics, supply chains, circular materials, and climate resilience.", "range": "A071 – A080"},
    9: {"code": "F09", "name": "Physical, microscopic & formal", "desc": "Molecular biology, nanotechnology, chemical kinetics, electromagnetism, and pure mathematics.", "range": "A081 – A090"},
    10: {"code": "F10", "name": "Frontier, illicit & cosmic", "desc": "Causal inference, informal markets, orbital space economy, and astrobiology.", "range": "A091 – A100"},
    11: {"code": "F11", "name": "Conscious agency & responsibility", "desc": "Self-model topology, causal attribution, consent, addiction, and human-AI co-agency.", "range": "A101 – A110"},
    12: {"code": "F12", "name": "Evolution, emergence & coexistence closure", "desc": "Morphogenesis, emergence, dependency trees, cosmological structure, and cross-substrate closure.", "range": "A111 – A120"}
}

adapters_json = json.dumps(adapters)
families_json = json.dumps(families)

def render_html_page(title, current_tab, body_content, extra_scripts=""):
    tabs = [
        ("ATLAS", "/", "index"),
        ("FOUNDER", "/founder", "founder"),
        ("REALITIES", "/realities", "realities"),
        ("LERM", "/LERM", "lerm"),
        ("PHOTOSYNTHESIS", "/photosynthesisproject", "photosynthesis"),
        ("SHOPFAM", "/shopfamcollective", "shopfam"),
        ("SCIENTISTS", "/scientists", "scientists"),
        ("BUILD", "/build", "build"),
        ("CONTACT", "/contactus", "contact"),
    ]
    
    links_html = ""
    for label, url, key in tabs:
        active = "text-white font-bold border-b-2 border-white pb-1" if current_tab == key else "text-zinc-400 hover:text-white transition pb-1"
        links_html += f'<a href="{url}" class="{active} tracking-wider">{label}</a>\n'

    return f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="Rufino Ventures // Universal Reality Atlas. Consequential systems architecture by Jefferson Rafael Rufino." />
  <link rel="canonical" href="https://rufinoventures.com/" />
  
  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Cpolygon points='16,2 30,9 30,23 16,30 2,23 2,9' fill='%23000000' stroke='%23ffffff' stroke-width='1.5'/%3E%3Ccircle cx='16' cy='16' r='3' fill='%23ffffff'/%3E%3C/svg%3E">
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- KaTeX -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '\\\\(', right: '\\\\)', display: false}}]}});"></script>

  <!-- Google Fonts: Space Grotesk, Inter, JetBrains Mono (SpaceX Minimalist Aesthetic) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700;800;900&family=Inter:wght@200;300;400;500;600;700;800;900&family=JetBrains+Mono:wght@300;400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['Geist', 'Inter', '-apple-system', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
            display: ['Space Grotesk', 'Geist', 'sans-serif'],
          }},
          colors: {{
            space: {{
              950: '#000000',
              900: '#050505',
              850: '#0a0a0a',
              800: '#121212',
              750: '#18181b',
              700: '#27272a',
            }}
          }}
        }}
      }}
    }}
  </script>

  <style>
    ::-webkit-scrollbar {{ width: 4px; height: 4px; }}
    ::-webkit-scrollbar-track {{ background: #000000; }}
    ::-webkit-scrollbar-thumb {{ background: #27272a; border-radius: 2px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: #52525b; }}
    .grid-bg {{
      background-size: 32px 32px;
      background-image: 
        linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
    }}
  </style>
</head>

<body class="bg-black text-zinc-300 font-sans antialiased selection:bg-white selection:text-black">

  <!-- TOP TELEMETRY STRIP (SPACEX MINIMALIST) -->
  <div class="px-4 py-1.5 bg-zinc-950 border-b border-zinc-900 flex flex-wrap items-center justify-between text-[10px] font-mono text-zinc-500 uppercase tracking-widest">
    <div class="flex items-center space-x-3">
      <span class="text-zinc-300 font-semibold flex items-center">
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-1.5 animate-pulse"></span>
        CANONICAL ATLAS 1.0
      </span>
      <span>|</span>
      <span>LERM v2.0.0 // IAMF-P // K_R v1.1</span>
      <span>|</span>
      <span class="hidden md:inline">120 ADAPTERS · 1,170 PAGES</span>
    </div>
    <div class="flex items-center space-x-4">
      <span>PRINCIPAL: <span class="text-zinc-200 font-bold">JEFFERSON RAFAEL RUFINO</span></span>
      <span class="hidden sm:inline text-zinc-400">VARIANCE: 0.00%</span>
      <a href="/contactus" class="text-zinc-300 hover:text-white underline">DIRECT AUDIT</a>
    </div>
  </div>

  <!-- MAIN SPACEX MINIMALIST NAVBAR -->
  <header class="sticky top-0 z-50 backdrop-blur-md bg-black/90 border-b border-zinc-800">
    <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <a href="/" class="flex items-center space-x-2.5 group">
          <div class="w-8 h-8 bg-white text-black font-display font-black flex items-center justify-center text-sm tracking-tighter">
            RV
          </div>
          <div>
            <span class="font-display font-bold text-white text-sm tracking-wider uppercase block leading-none">RUFINO VENTURES</span>
            <span class="font-mono text-[9px] text-zinc-500 uppercase tracking-widest block mt-0.5">Universal Reality Atlas</span>
          </div>
        </a>
      </div>

      <!-- Links (Desktop) -->
      <div class="hidden xl:flex items-center space-x-6 text-[11px] font-mono">
        {links_html}
      </div>

      <!-- Quick Action Button -->
      <div class="flex items-center space-x-3 font-mono text-xs">
        <a href="/realities" class="px-3.5 py-1.5 border border-zinc-700 hover:border-white text-white text-[11px] uppercase tracking-wider transition">
          120 ADAPTERS
        </a>
        <a href="/founder" class="hidden sm:inline-block px-3.5 py-1.5 bg-white text-black font-semibold text-[11px] uppercase tracking-wider hover:bg-zinc-200 transition">
          FOUNDER DOSSIER
        </a>
      </div>
    </nav>
    <!-- Mobile Secondary Tab Strip -->
    <div class="xl:hidden flex items-center space-x-5 px-4 py-2 bg-zinc-950 border-t border-zinc-900 overflow-x-auto text-[10px] font-mono whitespace-nowrap scrollbar-none">
      {links_html}
    </div>
  </header>

  <main>
    {body_content}
  </main>

  <footer class="border-t border-zinc-900 bg-black py-12 font-mono text-[11px] text-zinc-500">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-6">
      <div class="space-y-1 text-center md:text-left">
        <div class="font-display font-bold text-white tracking-wider text-xs uppercase">RUFINO VENTURES · THE UNIVERSAL REALITY ATLAS</div>
        <div>Canonical Edition 1.0 // 1,170 Pages // October 9, 2026 Freeze</div>
        <div>© 2026 Jefferson Rafael Rufino. All Rights Reserved.</div>
      </div>
      <div class="flex flex-wrap items-center justify-center gap-6 text-zinc-400">
        <a href="/" class="hover:text-white transition">Atlas</a>
        <a href="/founder" class="hover:text-white transition">Founder</a>
        <a href="/realities" class="hover:text-white transition">120 Realities</a>
        <a href="/LERM" class="hover:text-white transition">LERM</a>
        <a href="/photosynthesisproject" class="hover:text-white transition">Photosynthesis</a>
        <a href="/shopfamcollective" class="hover:text-white transition">ShopFam</a>
        <a href="/scientists" class="hover:text-white transition">Scientists</a>
        <a href="/build" class="hover:text-white transition">Build</a>
        <a href="/contactus" class="hover:text-white transition">Contact</a>
      </div>
    </div>
  </footer>

  {extra_scripts}
</body>
</html>
"""

def save_page(route_name, html_str):
    # Save both root file and route directory index.html
    if route_name == "index":
        with open("index.html", "w") as f: f.write(html_str)
        with open("RUFINOVENTURES.html", "w") as f: f.write(html_str)
    else:
        with open(f"{route_name}.html", "w") as f: f.write(html_str)
        os.makedirs(route_name, exist_ok=True)
        with open(f"{route_name}/index.html", "w") as f: f.write(html_str)
    print(f"  ✓ Saved route: {route_name}")

print("Page generator framework defined.")
