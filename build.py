import re
import os

source_file = r"F:\RGU-001\RGU-Curriculum design 2027-27\RGU-Rough Plan\rathinam-global-university.html"
target_file = r"F:\RGU-001\RGU-Curriculum design 2027-27\RGU-WEB Proposal 1.0\index.html"

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CSS variables
css_replacements = {
    "--navy: #080e20;": "--navy: #ffffff;",
    "--navy2: #0d1730;": "--navy2: #f4f7f6;",
    "--navy3: #142040;": "--navy3: #e2e8e4;",
    "--gold: #c9a227;": "--gold: #005A9C;", # Blue
    "--gold-light: #f0c43f;": "--gold-light: #0073CF;", # Lighter blue
    "--gold-pale: #f5e6b0;": "--gold-pale: #e6f0fa;", # Pale blue
    "--teal: #00c4d4;": "--teal: #00A859;", # Green
    "--teal-dark: #007a8a;": "--teal-dark: #008040;", # Dark green
    "--text: #ede8df;": "--text: #1a1a1a;", # Dark text for light theme
    "--text-muted: #8a94aa;": "--text-muted: #555555;",
    "--text-dim: #4a5370;": "--text-dim: #777777;",
    "--border: rgba(201,162,39,0.18);": "--border: rgba(0, 90, 156, 0.15);",
    "--border-light: rgba(255,255,255,0.07);": "--border-light: rgba(0,0,0,0.05);",
    "--card-bg: rgba(13,23,48,0.85);": "--card-bg: #ffffff;",
    "background: var(--navy);": "background: var(--navy); color: var(--text);",
    "background: rgba(8,14,32,0.92);": "background: rgba(255,255,255,0.95);",
}

for old, new in css_replacements.items():
    content = content.replace(old, new)

# Update background textures for light theme
content = content.replace("opacity='0.03'", "opacity='0.01'")
content = content.replace("rgba(201,162,39,0.04)", "rgba(0, 90, 156, 0.04)")
content = content.replace("rgba(201,162,39,0.08)", "rgba(0, 90, 156, 0.08)")
content = content.replace("rgba(255,255,255,0.02)", "rgba(0,0,0,0.02)")
content = content.replace("rgba(255,255,255,0.04)", "rgba(0,0,0,0.03)")
content = content.replace("rgba(255,255,255,0.05)", "rgba(0,0,0,0.04)")
content = content.replace("rgba(255,255,255,0.06)", "rgba(0,0,0,0.05)")
content = content.replace("rgba(255,255,255,0.07)", "rgba(0,0,0,0.05)")
content = content.replace("rgba(0,196,212,0.12)", "rgba(0, 168, 89, 0.12)")
content = content.replace("rgba(0,196,212,0.15)", "rgba(0, 168, 89, 0.15)")
content = content.replace("rgba(0,196,212,0.05)", "rgba(0, 168, 89, 0.05)")
content = content.replace("rgba(0,196,212,0.06)", "rgba(0, 168, 89, 0.06)")
content = content.replace("rgba(0,196,212,0.08)", "rgba(0, 168, 89, 0.08)")
content = content.replace("rgba(0,196,212,0.1)", "rgba(0, 168, 89, 0.1)")
content = content.replace("rgba(0,196,212,0.2)", "rgba(0, 168, 89, 0.2)")

content = content.replace("linear-gradient(135deg, var(--gold), var(--gold-light))", "linear-gradient(135deg, var(--gold), var(--teal))")
content = content.replace("background: linear-gradient(180deg, var(--navy) 0%, #080e20 100%);", "background: linear-gradient(180deg, #ffffff 0%, #f4f7f6 100%);")
content = content.replace("background: linear-gradient(135deg, var(--navy2) 0%, var(--navy3) 100%);", "background: linear-gradient(135deg, #f4f7f6 0%, #e2e8e4 100%);")

# Box shadow enhancements to look professional
content = content.replace("border: 1px solid var(--border-light);", "border: 1px solid var(--border-light); box-shadow: 0 4px 12px rgba(0,0,0,0.03);")
content = content.replace("border: 1px solid var(--border);", "border: 1px solid var(--border); box-shadow: 0 4px 12px rgba(0,0,0,0.03);")

# Update Logo
logo_html = '<img src="logo-Final.png" alt="Rathinam Global Logo" style="height: 50px;">'
content = re.sub(r'<div class="nav-logo-mark">RG</div>\s*<div>\s*<div class="nav-logo-text">Rathinam Global</div>\s*<div class="nav-logo-sub">Deemed to be University</div>\s*</div>', logo_html, content)

# Include campus image in hero section
hero_image_css = """
  .hero-img-container {
    margin-top: 3rem;
    max-width: 900px;
    width: 100%;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    animation: fadeUp 0.8s 0.5s ease both;
    position: relative;
    border: 1px solid var(--border);
  }
  .hero-img-container img {
    width: 100%;
    height: auto;
    display: block;
  }
"""
content = content.replace("</style>", hero_image_css + "</style>")

hero_img_html = """
  <div class="hero-img-container">
    <img src="campus-image.jpg" alt="Rathinam Research Hub" />
  </div>
"""
content = content.replace('<div class="hero-actions">', hero_img_html + '\n  <div class="hero-actions">')

# Update button text color for light theme (primary buttons now blue)
content = content.replace("color: var(--navy);", "color: #ffffff;") 
content = content.replace(".prog-new { position: absolute; top: 12px; right: 12px; font-size: 9px; background: var(--gold); color: var(--navy);", ".prog-new { position: absolute; top: 12px; right: 12px; font-size: 9px; background: var(--gold); color: #ffffff;")

# Footer Update
footer_old = "<div>Programmes designed and intelligenced by <a href=\"https://www.linkedin.com/in/profanjitraja/\" target=\"_blank\">Prof. Anjit Raja R</a></div>"
footer_new = "<div>2026-2027 @ Programmes designed and Intelligence by <a href=\"https://www.linkedin.com/in/profanjitraja/\" target=\"_blank\">Prof. Anjit Raja R</a></div>"
content = content.replace(footer_old, footer_new)

# Update button outlines 
content = content.replace("background: rgba(201,162,39,0.07);", "background: rgba(0, 90, 156, 0.07);")

# Update footer background
content = content.replace("<footer>\n  <div class=\"container\">\n    <div class=\"footer-grid\">", "<footer style=\"background: #002244; color: #fff;\">\n  <div class=\"container\">\n    <div class=\"footer-grid\">")
content = content.replace(".footer-brand p { font-size: 13px; color: var(--text-muted);", ".footer-brand p { font-size: 13px; color: #a0aab5;")
content = content.replace(".footer-col h5 { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: var(--gold);", ".footer-col h5 { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: var(--teal);")
content = content.replace(".footer-col a { display: block; font-size: 13px; color: var(--text-muted);", ".footer-col a { display: block; font-size: 13px; color: #a0aab5;")
content = content.replace(".footer-bottom { border-top: 1px solid var(--border-light); padding-top: 1.5rem; display: flex; justify-content: space-between; align-items: center; font-size: 12px; color: var(--text-dim); }", ".footer-bottom { border-top: 1px solid rgba(255,255,255,0.1); padding-top: 1.5rem; display: flex; justify-content: space-between; align-items: center; font-size: 12px; color: #a0aab5; }")

# Write to new file
os.makedirs(os.path.dirname(target_file), exist_ok=True)
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Redesign complete.")
