// http - serveris, url - tinklalapio adresas, 
// querysting - užklausos parametrai (url dalyje), fs - file system
const http = require('http');
const url = require('url');
const querystring = require('querystring');
const fs = require('fs');

// req – užklausa, res - atsakymas
const server = http.createServer((req, res) => {
  // URL parametras
  const myUrl = url.parse(req.url);
  const pathname = myUrl.pathname;

  // Užklausos parametrai
  const query = querystring.parse(myUrl.query);

  // Užklausas priimti tik iš esamos direktorijos.
  if (pathname === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Serverio direktorija.');
  } else {
    // Pagal prašomą URL rasti kelią į norimą atidarti failą (dabartinėje direktorijoje)
    const filePath = `.${pathname}.html`;

    // Tikrinti, ar failas egzistuoja
    fs.access(filePath, fs.constants.F_OK, (err) => {
      if (err) {
        // 404 - nerasta
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('404 - puslapis nerastas.');
      } else {
        if (!filePath.endsWith('.html')) {
          res.writeHead(404, { 'Content-Type': 'text/plain' });
          res.end('404 - puslapis nerastas.');
        } else
        // Skaityti failą asinchroniniu būdu
        fs.readFile(filePath, 'utf8', (err, data) => {
          if (err) {
            // Jei klaida skaitant failą - 500 (pvz, failas neturi leidimo skaitymui)
            res.writeHead(500, { 'Content-Type': 'text/plain' });
            res.end('500 - puslapio negalima paleisti - serverio klaida.');
          } else {
            // Failas perskaitytas teisingai, 200, išvedamas
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.end(data);
          }
        });
      }
    });
  }
});

// Serverio paleidimas
const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Serveris paleidžiamas: http://localhost:${PORT}/`);
});

