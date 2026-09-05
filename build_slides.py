import os, glob

workspace = os.path.dirname(os.path.abspath(__file__))
slides_dir = os.path.join(workspace, 'slides')
index_path = os.path.join(workspace, 'index.html')

slides_html = []
slide_files = sorted(glob.glob(os.path.join(slides_dir, 'slide_*.html')))

for sf in slide_files:
    fname = os.path.basename(sf)
    with open(sf, 'r', encoding='utf-8') as f:
        content = f.read().strip()
        slides_html.append(f'<!-- ==================== {fname.upper()} ==================== -->\n{content}')

all_slides_content = '\n\n'.join(slides_html)

full_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chuyên Đề: Cấu Trúc Dữ Liệu Chuyên Biệt (Trie & Union-Find)</title>
    
    <!-- Reveal.js CSS (White Theme) -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/theme/white.min.css" id="theme">
    
    <!-- Code Highlight CSS (Light Theme: Atom One Light) -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/plugin/highlight/atom-one-light.min.css">
    
    <!-- Google Fonts (Be Vietnam Pro cho Tiếng Việt) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Fira+Code:wght@400;600&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- FontAwesome CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- Custom CSS for Clean White Theme (NO SHADOWS) -->
    <style>
        :root {{
            --bg-color: #ffffff;
            --text-color: #0f172a;
            --accent-cyan: #0284c7;
            --accent-blue: #2563eb;
            --accent-violet: #7c3aed;
            --accent-pink: #e11d48;
            --accent-emerald: #059669;
            --accent-gold: #d97706;
            --card-bg: #f8fafc;
            --card-border: #cbd5e1;
        }}

        *, *::before, *::after {{
            box-sizing: border-box !important;
            box-shadow: none !important;
            text-shadow: none !important;
        }}

        body {{
            font-family: 'Be Vietnam Pro', 'Inter', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
        }}

        .reveal {{
            font-family: 'Be Vietnam Pro', 'Inter', sans-serif;
            color: var(--text-color);
        }}

        .reveal .slides section {{
            padding: 10px 20px !important;
        }}

        .reveal h1, .reveal h2, .reveal h3, .reveal h4 {{
            font-family: 'Be Vietnam Pro', sans-serif;
            text-transform: none;
            letter-spacing: 0px !important;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 6px;
        }}

        .reveal h1 {{ font-size: 1.35em; }}
        .reveal h3 {{ font-size: 0.85em; }}
        .reveal h4 {{ font-size: 0.55em; }}

        /* Clean Solid Cards - NO SHADOW */
        .glass-card {{
            background: #f8fafc;
            border: 1px solid var(--card-border);
            border-radius: 10px;
            padding: 10px 12px;
            box-shadow: none !important;
            transition: border-color 0.2s ease;
        }}

        .glass-card:hover {{
            border-color: var(--accent-cyan);
        }}

        /* Gradient Text (High Contrast on Light Theme) */
        .text-gradient {{
            background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .text-gradient-purple {{
            background: linear-gradient(135deg, #7c3aed 0%, #0284c7 100%);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .text-gradient-gold {{
            background: linear-gradient(135deg, #d97706 0%, #dc2626 100%);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        /* Badges - Light Theme Crisp */
        .badge {{
            display: inline-block;
            padding: 3px 10px;
            border-radius: 14px;
            font-size: 0.36em;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            background: #e0f2fe;
            color: #0369a1;
            border: 1px solid #bae6fd;
            margin-bottom: 4px;
        }}

        .badge-purple {{
            background: #f3e8ff;
            color: #6b21a8;
            border-color: #e9d5ff;
        }}

        .badge-gold {{
            background: #fef3c7;
            color: #92400e;
            border-color: #fde68a;
        }}

        /* Grid Layouts */
        .grid-2 {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            align-items: center;
        }}

        .grid-3 {{
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 10px;
        }}

        /* Callout Box - High Contrast Light Theme with Absolute Vertical Centering */
        .callout {{
            border-left: 4px solid var(--accent-cyan);
            background: #f0f9ff;
            padding: 6px 12px;
            border-radius: 0 6px 6px 0;
            text-align: left;
            margin: 6px 0 0 0;
            font-size: 0.35em;
            color: #0f172a;
            display: flex !important;
            align-items: center !important;
            justify-content: flex-start !important;
            line-height: 1.3 !important;
        }}

        .callout-warning {{
            border-left-color: var(--accent-pink);
            background: #fff1f2;
            color: #881337;
        }}

        .callout-success {{
            border-left-color: var(--accent-emerald);
            background: #ecfdf5;
            color: #065f46;
        }}

        /* Custom Tables - Clean Light Border */
        .reveal table {{
            font-size: 0.35em;
            margin: 0 auto;
            border-collapse: separate;
            border-spacing: 0;
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid #cbd5e1;
            width: 100%;
        }}

        .reveal table th {{
            background: #e2e8f0;
            color: #0f172a;
            padding: 6px 10px;
            border-bottom: 2px solid #cbd5e1;
            font-weight: 700;
        }}

        .reveal table td {{
            padding: 5px 10px;
            border-bottom: 1px solid #e2e8f0;
            background: #ffffff;
            color: #1e293b;
        }}

        .reveal table tr:last-child td {{
            border-bottom: none;
        }}

        /* Code Blocks - Light Theme - NO SHADOW */
        .reveal pre {{
            border-radius: 8px;
            border: 1px solid #cbd5e1;
            font-size: 0.45em;
            width: 100%;
            margin: 6px 0;
        }}

        .reveal pre code {{
            font-family: 'Fira Code', monospace;
            padding: 10px;
            max-height: 380px;
            background: #f8fafc !important;
            color: #0f172a !important;
        }}

        /* Node Diagrams Styling - Clean Light Circles */
        .node-circle {{
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: #ffffff;
            border: 2px solid var(--accent-cyan);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 0.55em;
            color: #0f172a;
            margin: 0 auto;
        }}

        .node-circle.is-end {{
            background: #f3e8ff;
            border-color: #7c3aed;
            color: #6b21a8;
        }}

        /* Bullet lists */
        .reveal ul {{
            font-size: 0.35em;
            line-height: 1.45;
            color: #334155;
        }}

        .reveal li {{
            margin-bottom: 4px;
        }}
    </style>
</head>
<body>

    <div class="reveal">
        <div class="slides">

{all_slides_content}

        </div>
    </div>

    <!-- Reveal.js JS -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/plugin/notes/notes.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/plugin/highlight/highlight.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/plugin/math/math.min.js"></script>

    <script>
        Reveal.initialize({{
            width: 1280,
            height: 720,
            margin: 0.04,
            minScale: 0.2,
            maxScale: 1.5,
            controls: true,
            progress: true,
            center: true,
            hash: true,
            transition: 'slide',
            plugins: [ RevealHighlight, RevealNotes, RevealMath.KaTeX ]
        }});
    </script>
</body>
</html>
"""

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f"Successfully rebuilt White Theme {index_path} from {len(slide_files)} split slide files!")
