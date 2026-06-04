import re
import os

file_path = r'c:\Users\pc\Desktop\SBIHM\lp\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix lazy loading: Replace src with data-src and remove data-lazyloaded
# Pattern: <img ... data-lazyloaded="1" ... src="data:image/svg+xml;base64,..." ... data-src="actual_url" ... />
def fix_lazy_img(match):
    tag = match.group(0)
    # Find data-src
    data_src_match = re.search(r'data-src="([^"]+)"', tag)
    if data_src_match:
        actual_url = data_src_match.group(1)
        # Replace the placeholder src with the actual url
        tag = re.sub(r'src="data:image/svg\+xml;base64,[^"]+"', f'src="{actual_url}"', tag)
        # Also handle data-srcset if present
        data_srcset_match = re.search(r'data-srcset="([^"]+)"', tag)
        if data_srcset_match:
            actual_srcset = data_srcset_match.group(1)
            tag = re.sub(r'srcset="[^"]*"', f'srcset="{actual_srcset}"', tag) # Handle existing empty/placeholder srcset
            if 'srcset=' not in tag:
                tag = tag.replace('data-srcset=', 'srcset=')
            else:
                tag = re.sub(r'data-srcset="[^"]+"', '', tag)
        
        # Remove lazyloaded attributes
        tag = tag.replace('data-lazyloaded="1"', '')
        tag = tag.replace('data-src=', 'data-old-src=') # Avoid double processing
    return tag

content = re.sub(r'<img [^>]+>', fix_lazy_img, content)
content = content.replace('data-old-src=', 'data-src=')

# 2. Fix scripts type
content = content.replace('type="litespeed/javascript"', 'type="text/javascript"')

# 3. Fix Hero Banner (adding a fallback style)
# The hero sections have data-id="7e63b8e" and data-id="754b058"
# We'll add a style tag to provide a default background image if the JS fails.
hero_css = """
<style>
/* Hero Banner Fallbacks */
.elementor-element-7e63b8e {
    background-image: url('hero-banner-1.jpg') !important;
    background-position: center center !important;
    background-repeat: no-repeat !important;
    background-size: cover !important;
}
.elementor-element-754b058 {
    background-image: url('hero-banner-1.jpg') !important;
    background-position: center center !important;
    background-repeat: no-repeat !important;
    background-size: cover !important;
}
/* Ensure animations are visible even if JS doesn't trigger them */
.elementor-invisible {
    visibility: visible !important;
    animation: none !important;
}
</style>
"""
if '</head>' in content:
    content = content.replace('</head>', hero_css + '</head>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed lazy loading, script types, and hero banner fallbacks.")
