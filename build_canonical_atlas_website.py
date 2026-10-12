import json

# Load rich adapters
with open('/tmp/canonical_120_adapters_rich.json') as f:
    adapters = json.load(f)

# Family metadata with descriptions
families = {
    1: {
        "code": "F01",
        "name": "Human life quality",
        "desc": "Whole-person functional capacity, longevity, recovery, and domestic environment.",
        "color": "emerald",
        "hex": "#10b981",
        "range": "A001 – A010"
    },
    2: {
        "code": "F02",
        "name": "Psychology & meaning",
        "desc": "Self-model, intimacy, trust, purpose, affect regulation, and social legibility.",
        "color": "teal",
        "hex": "#14b8a6",
        "range": "A011 – A020"
    },
    3: {
        "code": "F03",
        "name": "Biomedical & cellular",
        "desc": "Host reserve, clinical diagnostics, oncology, neurodegeneration, and immunology.",
        "color": "cyan",
        "hex": "#06b6d4",
        "range": "A021 – A030"
    },
    4: {
        "code": "F04",
        "name": "Education, justice & governance",
        "desc": "Child development, judicial sentencing, policing, corrections, and public administration.",
        "color": "blue",
        "hex": "#3b82f6",
        "range": "A031 – A040"
    },
    5: {
        "code": "F05",
        "name": "Culture, beauty & experience",
        "desc": "Aesthetic capital, fashion, luxury provenance, gaming, hospitality, and cultural markets.",
        "color": "indigo",
        "hex": "#6366f1",
        "range": "A041 – A050"
    },
    6: {
        "code": "F06",
        "name": "Money, markets & organizations",
        "desc": "Banking liquidity, credit underwriting, insurance, sovereign wealth, and venture creation.",
        "color": "amber",
        "hex": "#f59e0b",
        "range": "A051 – A060"
    },
    7: {
        "code": "F07",
        "name": "Technology & information",
        "desc": "Artificial intelligence, software systems, cybersecurity, data infra, and digital identity.",
        "color": "sky",
        "hex": "#0284c7",
        "range": "A061 – A070"
    },
    8: {
        "code": "F08",
        "name": "Earth, infrastructure & ecology",
        "desc": "Energy grids, water, agrivoltaics, supply chains, circular materials, and climate resilience.",
        "color": "lime",
        "hex": "#84cc16",
        "range": "A071 – A080"
    },
    9: {
        "code": "F09",
        "name": "Physical, microscopic & formal",
        "desc": "Molecular biology, nanotechnology, chemical kinetics, electromagnetism, and pure mathematics.",
        "color": "purple",
        "hex": "#a855f7",
        "range": "A081 – A090"
    },
    10: {
        "code": "F10",
        "name": "Frontier, illicit & cosmic",
        "desc": "Causal inference, informal markets, orbital space economy, and astrobiology.",
        "color": "rose",
        "hex": "#f43f5e",
        "range": "A091 – A100"
    },
    11: {
        "code": "F11",
        "name": "Conscious agency & responsibility",
        "desc": "Self-model topology, causal attribution, consent, addiction, and human-AI co-agency.",
        "color": "fuchsia",
        "hex": "#d946ef",
        "range": "A101 – A110"
    },
    12: {
        "code": "F12",
        "name": "Evolution, emergence & coexistence closure",
        "desc": "Morphogenesis, emergence, dependency trees, cosmological structure, and cross-substrate closure.",
        "color": "violet",
        "hex": "#8b5cf6",
        "range": "A111 – A120"
    }
}

adapters_json_str = json.dumps(adapters)
families_json_str = json.dumps(families)

with open('template_atlas.html') as f:
    template = f.read()

output = template.replace('__ADAPTERS_JSON__', adapters_json_str).replace('__FAMILIES_JSON__', families_json_str)

with open('index.html', 'w') as f:
    f.write(output)

with open('RUFINOVENTURES.html', 'w') as f:
    f.write(output)

print("Website generated successfully in index.html and RUFINOVENTURES.html!")
