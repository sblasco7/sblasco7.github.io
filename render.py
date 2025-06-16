from jinja2 import Environment, FileSystemLoader
import os

# where your templates live
env = Environment(loader=FileSystemLoader("_layouts"))

# pages to render
pages = [
    ("index.html", {"title": "main structure"}),
    ("cv.html", {"title": "main structure"}),
]

out_dir = "docs"  # GitHub Pages will serve this

os.makedirs(out_dir, exist_ok=True)
for tpl_name, ctx in pages:
    tpl = env.get_template(tpl_name)
    rendered = tpl.render(**ctx)
    with open(os.path.join(out_dir, tpl_name), "w", encoding="utf-8") as f:
        f.write(rendered)
print("Rendered", len(pages), "pages →", out_dir)