const fs = require('fs');

const htmlFile = 'e:\\01_emaus\\02. Site\\code.html';
const videosDir = 'e:\\01_emaus\\02. Site\\EMAUS _ MIDIA\\VIDEOS';

const files = fs.readdirSync(videosDir);
const videos = files.filter(f => f.toLowerCase().endsWith('.mov') || f.toLowerCase().endsWith('.mp4'));

// Natural sort
videos.sort((a, b) => {
  return a.localeCompare(b, undefined, { numeric: true, sensitivity: 'base' });
});

let carouselHtml = '';
videos.forEach((video, index) => {
  const i = index + 1;
  const src = `EMAUS%20_%20MIDIA/VIDEOS/${encodeURIComponent(video)}#t=0.001`;
  const ext = video.toLowerCase().split('.').pop();

  carouselHtml += `            <!-- Video Slide ${i} -->
            <div class="swiper-slide aspect-video bg-white rounded-custom p-2 sm:p-4 flex items-center justify-center shadow-sm border border-brand-beige">
              <video class="w-full h-full object-contain rounded bg-stone-950 swiper-no-swiping" controls preload="metadata" playsinline>
                <source src="${src}">
                Seu navegador não suporta o formato de vídeo.
              </video>
            </div>
`;
});

let content = fs.readFileSync(htmlFile, 'utf8');

const regex = /(<div class="swiper videos-swiper[^>]*>[\s\n]*<div class="swiper-wrapper">)[\s\S]*?(<\/div>[\s\n]*<!-- Add Pagination -->)/;
const newContent = content.replace(regex, `$1\n${carouselHtml}          $2`);

fs.writeFileSync(htmlFile, newContent, 'utf8');
console.log(`Updated ${videos.length} videos in HTML with node.`);
