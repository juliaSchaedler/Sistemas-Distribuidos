const http = require('http');
const url = require('url');

const serverUrl = 'http://127.0.0.1:8088/index.html'; // URL do servidor e arquivo solicitado

const options = {
    hostname: url.parse(serverUrl).hostname,
    port: url.parse(serverUrl).port,
    path: url.parse(serverUrl).pathname,
    method: 'GET'
};

const req = http.request(options, (res) => {
    let data = '';

    res.on('data', (chunk) => {
        data += chunk;
    });

    res.on('end', () => {
        console.log(data); // Exibe o conteúdo da página HTML retornada pelo servidor
    });
});

req.on('error', (e) => {
    console.error(`Erro na requisição: ${e.message}`);
});

req.end();
