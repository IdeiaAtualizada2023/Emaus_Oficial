import re
import os

html_file = r'e:\01_emaus\02. Site\code.html'
videos_dir = r'e:\01_emaus\02. Site\EMAUS _ MIDIA\VIDEOS'

# get all video files
videos = []
for f in os.listdir(videos_dir):
    if f.lower().endswith(('.mov', '.mp4')):
        videos.append(f)

# natural sort
import re
def natural_keys(text):
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', text)]

videos.sort(key=natural_keys)

carousel_html = ""
for i, video in enumerate(videos, 1):
    src = f"EMAUS%20_%20MIDIA/VIDEOS/{video.replace(' ', '%20')}"
    # type attribute
    v_type = "video/mp4" if video.lower().endswith('.mp4') else "video/quicktime"
    
    slide = f"""            <!-- Video Slide {i} -->
            <div class="swiper-slide aspect-[9/16] md:aspect-[4/5] bg-stone-950 flex items-center justify-center overflow-hidden rounded-custom relative group">
              <video class="w-full h-full object-cover object-[center_top]" controls preload="none">
                <source src="{src}" type="{v_type}">
                Seu navegador não suporta o formato de vídeo.
              </video>
            </div>
"""
    carousel_html += slide

# Read HTML
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace between <div class="swiper-wrapper"> for videos-swiper
# Find <div class="swiper videos-swiper...
pattern = r'(<div class="swiper videos-swiper[^>]*>[\s\n]*<div class="swiper-wrapper">)[\s\S]*?(</div>[\s\n]*<!-- Add Pagination -->)'
replacement = r'\1\n' + carousel_html + r'          \2'
new_content = re.sub(pattern, replacement, content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Updated {len(videos)} videos in HTML.")
