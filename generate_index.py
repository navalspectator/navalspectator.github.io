import os
from datetime import datetime

OUTPUT_FILE = "index.html"
TITLE = "📄 HTML Mockups Index"
EXCLUDED_FILES = {OUTPUT_FILE}
VALID_EXTENSIONS = {".html"}


def collect_html_files(root="."):
    file_map = {}
    for dirpath, _, filenames in os.walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        rel_dir = "" if rel_dir == "." else rel_dir

        html_files = [
            f for f in filenames
            if os.path.splitext(f)[1] in VALID_EXTENSIONS and f not in EXCLUDED_FILES
        ]
        if html_files:
            file_map[rel_dir] = sorted(html_files)
    return file_map


def generate_html(file_map):
    lines = [
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        f"<title>{TITLE}</title>",
        "<meta charset='UTF-8'>",
        "<style>",
        "body { font-family: Arial, sans-serif; padding: 2rem; background: #f9f9f9; }",
        "h2 { margin-top: 2rem; color: #333; }",
        "ul { list-style-type: none; padding-left: 1rem; }",
        "li { margin: 0.5rem 0; }",
        "a { text-decoration: none; color: #1a0dab; }",
        "a:hover { text-decoration: underline; }",
        "</style>",
        "</head>",
        "<body>",
        f"<h1>{TITLE}</h1>",
        f"<p>Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>",
    ]

    for folder, files in sorted(file_map.items()):
        lines.append(f"<h2>{folder or 'Root'}</h2>")
        lines.append("<ul>")
        for file in files:
            path = os.path.join(folder, file).replace("\\", "/")
            lines.append(f'<li><a href="{path}">{file}</a></li>')
        lines.append("</ul>")

    lines.extend(["</body>", "</html>"])
    return "\n".join(lines)


def main():
    print("📁 Scanning HTML files...")
    file_map = collect_html_files()
    print(f"✅ Found HTML files in {len(file_map)} folders.")
    html_content = generate_html(file_map)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ {OUTPUT_FILE} has been generated.")


if __name__ == "__main__":
    main()