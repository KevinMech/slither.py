const net = require('net');
const timer = require('timers');
const game = require('./game');
const port = 35246;

//Create Server
console.log('creating server...');
let server = net.createServer();

//Create the level
console.log('creating level...');
let grid = game.createGrid(10, 10);
console.log(grid);
console.log('level created!');

//On discovering new client, create a new socket and attach event handlers to it, and then place the player randomly on the grid
server.on('connection', function (socket) {
	console.log('found new player!');
	socket.write('connected');
	game.setPlayer();
});

//Update Game
timer.setInterval(game.Update, 100);

//Start Listening on server
server.listen(port, function () {
	console.log('server now listening for clients on port ' + port);
});
