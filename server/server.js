const net = require('net');
const port = 35246;

const server = net.createServer();

server.on('connection', function (socket) {
	console.log('found new client!');
});

server.listen(port, function () {
	console.log('server now listening for clients on port ' + port);
});