#!/usr/bin/env python3
"""
Cepheid API documentation generator that creates styled HTML output.

Generates API.html with formatted API reference, modules, and documentation links
for GitHub Actions artifact deployment.
"""

def generate_html():
    """Generate complete HTML document with Cepheid API reference."""
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cepheid API Reference</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
               max-width: 800px; margin: 0 auto; padding: 40px 20px; line-height: 1.6; color: #333; }
        h1 { color: #1a1a1a; border-bottom: 2px solid #e1e4e8; padding-bottom: 10px; }
        h2 { color: #0366d6; margin-top: 40px; }
        .repo-link { background: #f6f8fa; padding: 20px; border-radius: 6px; margin: 20px 0; }
        .module { background: #f8f9fa; padding: 20px; margin: 20px 0; border-left: 4px solid #0366d6; }
        .module h3 { margin-top: 0; color: #24292e; }
        .module-description { color: #586069; font-style: italic; }
        .module-link { font-weight: bold; color: #0366d6; text-decoration: none; }
        .module-link:hover { text-decoration: underline; }
        footer { margin-top: 40px; padding-top: 20px; border-top: 1px solid #e1e4e8; 
                color: #6a737d; font-size: 0.9em; }
    </style>
</head>
<body>
    <h1>API Reference</h1>
    
    <div class="repo-link">
        <a href="https://github.com/jmcguigs/cepheid" target="_blank">GitHub Repository</a><br>
        <a href="https://hexdocs.pm/cepheid/api-reference.html#modules" target="_blank">Hexdocs API Reference</a>
    </div>

    <h2>Modules</h2>
    
    <div class="module">
        <h3><a href="https://hexdocs.pm/cepheid/Cepheid.html" class="module-link" target="_blank">Cepheid</a></h3>
        <p class="module-description">Documentation for Cepheid.</p>
    </div>

    <div class="module">
        <h3><a href="https://hexdocs.pm/cepheid/Cepheid.Normalization.Magnitude.html" class="module-link" target="_blank">Cepheid.Normalization.Magnitude</a></h3>
        <p class="module-description">Functions for normalizing the magnitude of light curves.</p>
    </div>

    <div class="module">
        <h3><a href="https://hexdocs.pm/cepheid/Cepheid.Periodicity.Pdm.html" class="module-link" target="_blank">Cepheid.Periodicity.Pdm</a></h3>
        <p class="module-description">Functions for Phase Dispersion Minimization (PDM) analysis.</p>
    </div>

    <footer>
        <p>Generated automatically by Cepheid API.py via GitHub Actions</p>
    </footer>
</body>
</html>"""
    
    with open('API.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("API.html generated successfully!")

def main():
    """Main entry point - generates and saves API.html file."""
    generate_html()

if __name__ == "__main__":
    main()
