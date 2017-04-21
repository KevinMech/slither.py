const net = require('net');
const timer = require('timers');
const game = require('./game');
const port = 35246;

//Create Server
console.log('creating server...');
let server = net.createServer();

//On discovering new client, create a new socket and attach event handlers to it
server.on('connection', function (socket) {
	console.log('found new snake!');
});

//Create the level
console.log('creating level...');
let grid = game.createGrid(10, 10);
console.log(grid);

//Update Game
timer.setInterval(game.Update, 100);

//Start Listening on server
server.listen(port, function () {
	console.log('server now listening for clients on port ' + port);
});

