#!/usr/bin/env python3
"""
Comprehensive verification test suite for RUFINOVENTURES.html & GitHub Pages free hosting architecture.
"""

import os
import re
import urllib.request
import json
import subprocess

def run_tests():
    base_dir = "/Users/thehighlandboy/Downloads/RUFINOVENTURES"
    html_file = os.path.join(base_dir, "RUFINOVENTURES.html")
    index_file = os.path.join(base_dir, "index.html")
    cname_file = os.path.join(base_dir, "CNAME")
    nojekyll_file = os.path.join(base_dir, ".nojekyll")
    error_file = os.path.join(base_dir, "404.html")
    robots_file = os.path.join(base_dir, "robots.txt")
    sitemap_file = os.path.join(base_dir, "sitemap.xml")
    readme_file = os.path.join(base_dir, "README.md")
    guide_file = os.path.join(base_dir, "DEPLOYMENT_GUIDE.md")

    assert os.path.exists(html_file), f"File {html_file} does not exist"
    
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"[TEST 1] File Size Check: {len(content)} bytes")
    assert len(content) > 10000, "HTML file too small!"

    print("[TEST 2] Checking Required Titles & Branding...")
    assert "THE PHOTOSYNTHESIS PROJECT" in content, "Missing Photosynthesis Project title"
    assert "THE RUFINO SYNTHESIS" in content, "Missing Rufino Synthesis title"
    assert "2026-27 SUPER EL NIÑO" in content or "2026–2027 SUPER EL NIÑO" in content, "Missing Super El Nino designation"
    assert "jeffersonrrufino@gmail.com" in content, "Missing contact email jeffersonrrufino@gmail.com"

    print("[TEST 3] Checking Panes and Anchor Links...")
    expected_panes = [
        "hero",
        "pane-telemetry",
        "pane-solar",
        "pane-photosynthesis",
        "pane-agrivoltaics",
        "pane-rufino-synthesis",
        "pane-water",
        "pane-origins",
        "pane-medical",
        "pane-coalition",
        "pane-media",
        "pane-nations",
        "pane-doctrine",
        "pane-calculator",
        "pane-contact"
    ]
    for pane in expected_panes:
        pattern = f'id="{pane}"'
        assert pattern in content, f"Missing section id='{pane}'"
        print(f"  ✓ Found pane: {pane}")

    # Check anchor link resolution
    anchors = set(re.findall(r'href=[\"\']#([^\"\']+)[\"\']', content))
    dom_ids = set(re.findall(r'id=[\"\']([^\"\']+)[\"\']', content))
    missing_anchors = anchors - dom_ids
    assert len(missing_anchors) == 0, f"Dead anchor links found: {missing_anchors}"
    print(f"  ✓ All {len(anchors)} internal anchor links resolve correctly to valid DOM IDs")

    print("[TEST 4] Verifying 54 Sovereign Nations in Data...")
    nations_match = re.search(r'const NATIONS_DATA = (\[.*?\]);', content, re.DOTALL)
    assert nations_match, "Could not find NATIONS_DATA in JS"
    
    nations_js = nations_match.group(1)
    ranks = re.findall(r'rank:\s*(\d+)', nations_js)
    names = re.findall(r'name:\s*"([^"]+)"', nations_js)
    print(f"  Total nations detected: {len(ranks)} ranks, {len(names)} names")
    assert len(ranks) == 54, f"Expected 54 nations, got {len(ranks)}"
    assert len(names) == 54, f"Expected 54 names, got {len(names)}"
    
    critical_countries = ["Philippines", "Indonesia", "Peru", "Kenya", "India (Peninsular Belt)", "Somalia", "Ethiopia", "Vietnam (Mekong Delta)", "Kiribati", "Tuvalu"]
    for c in critical_countries:
        assert c in names, f"Critical country '{c}' missing from dataset"
        print(f"  ✓ Country verified: {c}")

    print("[TEST 5] Verifying Background Images on Every Pane...")
    img_urls = re.findall(r'src="(https://images\.unsplash\.com/[^"]+)"', content)
    print(f"  Found {len(img_urls)} Unsplash image sources:")
    for url in img_urls:
        print(f"    - {url[:70]}...")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            req.get_method = lambda: 'HEAD'
            res = urllib.request.urlopen(req, timeout=10)
            assert res.status == 200, f"Image URL returned {res.status}: {url}"
            print(f"      ✓ 200 OK")
        except Exception as e:
            raise AssertionError(f"Failed to fetch image {url}: {e}")
    assert len(img_urls) >= 8, f"Expected at least 8 contextual pane images, found {len(img_urls)}"

    print("[TEST 6] Checking Interactive Features & DOM Bindings...")
    assert "recalculateModel()" in content, "Missing recalculateModel function"
    assert "exportCalculatorReport()" in content, "Missing exportCalculatorReport function"
    assert "filterNations(" in content, "Missing filterNations function"
    assert "searchNations()" in content, "Missing searchNations function"
    assert "copyEmailToClipboard()" in content, "Missing copyEmailToClipboard function"
    assert "openModal(" in content, "Missing openModal function"
    assert "updateUtcClock()" in content, "Missing updateUtcClock function"

    # Verify all document.getElementById bindings exist in DOM
    get_elem_ids = set(re.findall(r'document\.getElementById\([\'\"]([^\'\"]+)[\'\"]\)', content))
    missing_get_elems = get_elem_ids - dom_ids
    assert len(missing_get_elems) == 0, f"JS document.getElementById calls missing DOM targets: {missing_get_elems}"
    print(f"  ✓ All {len(get_elem_ids)} document.getElementById targets verified in DOM")

    print("[TEST 7] Checking Contact Email Handlers...")
    mailto_matches = re.findall(r'mailto:jeffersonrrufino@gmail\.com[^\"]*', content)
    print(f"  Found {len(mailto_matches)} mailto links targeting jeffersonrrufino@gmail.com")
    assert len(mailto_matches) >= 3, "Expected multiple direct mailto links"

    print("[TEST 8] Verifying Free Hosting & GitHub Pages Infrastructure...")
    # 1. index.html checks
    assert os.path.exists(index_file), "index.html missing at workspace root!"
    with open(index_file, "r", encoding="utf-8") as f:
        index_content = f.read()
    assert index_content == content, "index.html must match RUFINOVENTURES.html exactly"
    assert 'rel="canonical" href="https://rufinoventures.com/"' in index_content, "Missing canonical tag for rufinoventures.com"
    assert 'og:title' in index_content, "Missing Open Graph og:title tag"
    assert 'twitter:card' in index_content, "Missing Twitter card tag"
    print("  ✓ index.html validated as primary GitHub Pages entry point (synchronized with RUFINOVENTURES.html)")

    # 2. CNAME check
    assert os.path.exists(cname_file), "CNAME file missing at workspace root!"
    with open(cname_file, "r", encoding="utf-8") as f:
        cname_content = f.read().strip()
    assert cname_content == "rufinoventures.com", f"CNAME must be 'rufinoventures.com', found '{cname_content}'"
    print(f"  ✓ CNAME validated: {cname_content}")

    # 3. .nojekyll check
    assert os.path.exists(nojekyll_file), ".nojekyll file missing at workspace root!"
    print("  ✓ .nojekyll validated (GitHub Pages Jekyll engine bypassed)")

    # 4. 404.html check
    assert os.path.exists(error_file), "404.html missing at workspace root!"
    with open(error_file, "r", encoding="utf-8") as f:
        err_content = f.read()
    assert "404" in err_content, "404.html missing 404 indication"
    assert "jeffersonrrufino@gmail.com" in err_content, "404.html missing contact email"
    assert "/" in err_content, "404.html missing return link to root"
    print(f"  ✓ 404.html validated ({len(err_content)} bytes)")

    # 5. robots.txt and sitemap.xml check
    assert os.path.exists(robots_file), "robots.txt missing!"
    with open(robots_file, "r", encoding="utf-8") as f:
        robots_content = f.read()
    assert "User-agent:" in robots_content and "sitemap.xml" in robots_content, "Invalid robots.txt"
    print("  ✓ robots.txt validated")

    assert os.path.exists(sitemap_file), "sitemap.xml missing!"
    with open(sitemap_file, "r", encoding="utf-8") as f:
        sitemap_content = f.read()
    assert "https://rufinoventures.com/" in sitemap_content, "Invalid sitemap.xml"
    print("  ✓ sitemap.xml validated")

    # 6. README.md check
    assert os.path.exists(readme_file), "README.md missing!"
    with open(readme_file, "r", encoding="utf-8") as f:
        readme_content = f.read()
    assert "https://rufinoventures.com" in readme_content, "README.md missing live URL"
    assert "jeffersonrrufino@gmail.com" in readme_content, "README.md missing contact email"
    print(f"  ✓ README.md validated ({len(readme_content)} bytes)")

    # 7. DEPLOYMENT_GUIDE.md check
    assert os.path.exists(guide_file), "DEPLOYMENT_GUIDE.md missing!"
    with open(guide_file, "r", encoding="utf-8") as f:
        guide_content = f.read()
    assert len(guide_content) > 1000, "DEPLOYMENT_GUIDE.md too short!"
    assert "GitHub Pages" in guide_content, "Guide missing GitHub Pages instructions"
    assert "Enforce HTTPS" in guide_content or "SSL" in guide_content, "Guide missing SSL instructions"
    assert "185.199.108.153" in guide_content, "Guide missing GitHub Pages IP DNS records"
    assert "jeffersonrrufino@gmail.com" in guide_content, "Guide missing contact email"
    assert ".nojekyll" in guide_content, "Guide missing .nojekyll explanation"
    assert "404.html" in guide_content, "Guide missing 404.html explanation"
    print(f"  ✓ DEPLOYMENT_GUIDE.md validated ({len(guide_content)} bytes)")

    # 8. Zero external server requirement / 100% static check
    assert not re.search(r'<(?:form|button)[^>]*action=[\"\'](?!mailto:)[^\"\']*[\"\']', index_content), "Form action requires external server!"
    print("  ✓ 100% static client-side architecture verified (zero backend server required)")

    print("[TEST 9] Checking Git Staging Safety & Security Protection...")
    status_proc = subprocess.run(["git", "status", "--porcelain"], cwd=base_dir, capture_output=True, text=True)
    untracked_lines = status_proc.stdout.splitlines()
    forbidden_tokens = ["BPI", "UNIONBANK", ".mp4", ".m4a", ".zip", "iamfp", "sentry", "jefferson_existence", "drift"]
    for line in untracked_lines:
        for token in forbidden_tokens:
            assert token.lower() not in line.lower(), f"Security violation: confidential or heavy file '{line}' would be staged!"
    print(f"  ✓ Git staging verified safe: 0 sensitive or heavy files exposed across {len(untracked_lines)} staged candidates")

    print("\nALL 9 COMPREHENSIVE VERIFICATION SUITES PASSED SUCCESSFULLY! ✓✓✓")

if __name__ == "__main__":
    run_tests()
