const fs = require('fs');
const path = require('path');

const htmlFile = path.join(__dirname, 'code.html');
const photosDir = path.join(__dirname, 'EMAUS _ MIDIA', 'FOTOS');
const videosDir = path.join(__dirname, 'EMAUS _ MIDIA', 'VIDEOS');

function naturalSort(a, b) {
    return a.localeCompare(b, undefined, { numeric: true, sensitivity: 'base' });
}

// Photos
const photos = fs.readdirSync(photosDir).filter(f => f.match(/\.(jpg|png|webp)$/i)).sort(naturalSort);
let photosHtml = "";
photos.forEach((photo, i) => {
    let src = `EMAUS%20_%20MIDIA/FOTOS/${encodeURIComponent(photo)}`;
    photosHtml += `            <!-- Slide ${i + 1} -->
            <div class="swiper-slide aspect-video relative group bg-stone-950 flex items-center justify-center">
              <img alt="Galeria Foto ${i + 1}" class="w-full h-full object-contain" src="${src}"
                loading="lazy" />
            </div>\n`;
});

// Videos
const videos = fs.readdirSync(videosDir).filter(f => f.match(/\.(mov|mp4)$/i)).sort(naturalSort);
let videosHtml = "";
videos.forEach((video, i) => {
    let src = `EMAUS%20_%20MIDIA/VIDEOS/${encodeURIComponent(video)}#t=0.001`;
    videosHtml += `            <!-- Video Slide ${i + 1} -->
            <div
              class="swiper-slide aspect-video bg-white rounded-custom p-2 sm:p-4 flex items-center justify-center shadow-sm border border-brand-beige">
              <video class="w-full h-full object-contain rounded bg-stone-950" controls preload="metadata">
                <source src="${src}">
                Seu navegador não suporta o formato de vídeo.
              </video>
            </div>\n`;
});

// Replace HTML
let content = fs.readFileSync(htmlFile, 'utf8');

const pPattern = /(<div class="swiper photos-swiper[^>]*>[\s\n]*<div class="swiper-wrapper">)[\s\S]*?(<\/div>[\s\n]*<!-- Add Pagination -->)/;
content = content.replace(pPattern, `$1\n${photosHtml}          $2`);

const vPattern = /(<div class="swiper videos-swiper[^>]*>[\s\n]*<div class="swiper-wrapper">)[\s\S]*?(<\/div>[\s\n]*<!-- Add Pagination -->)/;
content = content.replace(vPattern, `$1\n${videosHtml}          $2`);

fs.writeFileSync(htmlFile, content, 'utf8');
console.log(`Updated ${photos.length} photos and ${videos.length} videos in HTML.`);
