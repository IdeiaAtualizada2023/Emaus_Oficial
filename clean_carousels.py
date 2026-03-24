import re
import os

html_file = r'e:\01_emaus\02. Site\code.html'
photos_dir = r'e:\01_emaus\02. Site\EMAUS _ MIDIA\FOTOS'
videos_dir = r'e:\01_emaus\02. Site\EMAUS _ MIDIA\VIDEOS'

def natural_keys(text):
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', text)]

# Photos
photos = [f for f in os.listdir(photos_dir) if f.lower().endswith(('.jpg', '.png', '.webp'))]
photos.sort(key=natural_keys)

photos_html = ""
for i, photo in enumerate(photos, 1):
    src = f"EMAUS%20_%20MIDIA/FOTOS/{photo.replace(' ', '%20')}"
    slide = f"""            <!-- Slide {i} -->
            <div class="swiper-slide aspect-video relative group bg-stone-950 flex items-center justify-center">
              <img alt="Galeria Foto {i}" class="w-full h-full object-contain" src="{src}"
                loading="lazy" />
            </div>
"""
    photos_html += slide

# Videos
videos = [f for f in os.listdir(videos_dir) if f.lower().endswith(('.mov', '.mp4'))]
videos.sort(key=natural_keys)

videos_html = ""
for i, video in enumerate(videos, 1):
    src = f"EMAUS%20_%20MIDIA/VIDEOS/{video.replace(' ', '%20')}#t=0.001"
    slide = f"""            <!-- Video Slide {i} -->
            <div
              class="swiper-slide aspect-video bg-white rounded-custom p-2 sm:p-4 flex items-center justify-center shadow-sm border border-brand-beige">
              <video class="w-full h-full object-contain rounded bg-stone-950" controls preload="metadata">
                <source src="{src}">
                Seu navegador não suporta o formato de vídeo.
              </video>
            </div>
"""
    videos_html += slide

# Read HTML
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace photos
p_pattern = r'(<div class="swiper photos-swiper[^>]*>[\s\n]*<div class="swiper-wrapper">)[\s\S]*?(</div>[\s\n]*<!-- Add Pagination -->)'
p_replacement = r'\g<1>\n' + photos_html + r'          \g<2>'
content = re.sub(p_pattern, p_replacement, content)

# Replace videos
v_pattern = r'(<div class="swiper videos-swiper[^>]*>[\s\n]*<div class="swiper-wrapper">)[\s\S]*?(</div>[\s\n]*<!-- Add Pagination -->)'
v_replacement = r'\g<1>\n' + videos_html + r'          \g<2>'
content = re.sub(v_pattern, v_replacement, content)

# Write HTML
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated {len(photos)} photos and {len(videos)} videos in HTML.")
