const fs = require('fs');
const path = require('path');
const htmlPath = path.join(__dirname, 'code.html');

let htmlContent = fs.readFileSync(htmlPath, 'utf8');
htmlContent = htmlContent.replace(/preload="metadata"/g, 'preload="none"');
fs.writeFileSync(htmlPath, htmlContent, 'utf8');
