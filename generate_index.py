import os
from datetime import datetime

ROOT_DIR = "/Users/work/Documents/GitHub/Projects"
OUTPUT_FILE = os.path.join(ROOT_DIR, "index.html")
TITLE = "📄 HTML Mockups Index"
VALID_EXTENSIONS = {".html"}


def scan_structure(root):
    structure = {"product": {}, "projects": {}}
    for top_level in structure:
        base_path = os.path.join(root, top_level)
        if not os.path.isdir(base_path):
            continue

        for module in os.listdir(base_path):
            module_path = os.path.join(base_path, module)
            if not os.path.isdir(module_path):
                continue

            html_files = [
                f for f in os.listdir(module_path)
                if os.path.splitext(f)[1] in VALID_EXTENSIONS
            ]
            if html_files:
                structure[top_level][module] = [
                    os.path.splitext(f)[0] for f in sorted(html_files)
                ]
    return structure


def generate_html(data):
    lines = [
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        f"<title>{TITLE}</title>",
        "<meta charset='UTF-8'>",
        "<style>",
        "body { font-family: sans-serif; margin: 0; padding: 0; }",
        "header { background: #333; color: white; padding: 1rem; font-size: 1.5rem; }",
        "nav { background: #eee; padding: 1rem; display: flex; gap: 1rem; }",
        "section { display: none; padding: 2rem; }",
        "section.active { display: block; }",
        "h2 { margin-top: 2rem; }",
        "ul { list-style-type: none; padding-left: 1rem; }",
        "li { margin: 0.5rem 0; }",
        "a { text-decoration: none; color: #0077cc; }",
        "a:hover { text-decoration: underline; }",
        "</style>",
        "<script>",
        "function showSection(id) {",
        "  document.querySelectorAll('section').forEach(sec => sec.classList.remove('active'));",
        "  document.getElementById(id).classList.add('active');",
        "}",
        "</script>",
        "</head>",
        "<body>",
        f"<header>{TITLE}</header>",
        "<nav>",
        "<button onclick=\"showSection('product')\">🧪 Product</button>",
        "<button onclick=\"showSection('projects')\">🛠️ Projects</button>",
        "</nav>",
        f"<p style='padding: 0 2rem;'>Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>",
    ]

    for category in ["product", "projects"]:
        lines.append(f"<section id='{category}'><h1>{category.capitalize()}</h1>")
        for module, files in sorted(data[category].items()):
            lines.append(f"<h2>{module}</h2><ul>")
            for f in files:
                href = f"{category}/{module}/{f}.html"
                lines.append(f'<li><a href="{href}">{f}</a></li>')
            lines.append("</ul>")
        lines.append("</section>")

    lines.append("</body></html>")
    return "\n".join(lines)


def main():
    print("📁 Scanning mockup folders...")
    structure = scan_structure(ROOT_DIR)
    html = generate_html(structure)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Generated index at {OUTPUT_FILE}")


if __name__ == "__main__":
    main()