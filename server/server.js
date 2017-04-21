const net = require('net');
const game = require('./game');
const port = 35246;

//Create Server
console.log('creating server...');
const server = net.createServer();

//On discovering new client, create a new socket and attach event handlers to it
server.on('connection', function (socket) {
	console.log('found new snake!');
});

//Create the level
cosole.log('creating level...');
const grid = game.createGrid(10,10);
console.log(grid);

//Start Listening on server
server.listen(port, function () {
	console.log('server now listening for clients on port ' + port);
});
