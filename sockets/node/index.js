const net = require('net')

let socket; 

const server = net.createServer((c) => {
    // 'connection' listener.
    socket = c

    socket.on('readable',() => {
        let chunk = null;
          while ((chunk = socket.read()) !== null) {
            console.log(chunk.toString('utf8'))
          }
      });

      socket.write('oooi')
});

server.on('error', (err) => {
    console.log('error')
    throw err;
});


server.listen(3000, () => {
    console.log('server bound');
});
