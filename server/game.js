var players = [];
var grid = [];

exports.createGrid = function (width, height) {
	let tile = 1;
	for(x = 0; x < width; x++){
		row = [];
		for(y = 0; y < height; y++){
			row.push(tile);
			tile++;
		}
		grid.push(row);
	}
	grid.width = width;
	grid.height = height;
	return grid;
};

//Called as soon as a player join, will randomly place the player on the grid
exports.setPlayer = function(){
	players.push(snake);
	rndWidth = Math.floor((Math.random() * grid.width));
	rndHeight = Math.floor((Math.random() * grid.height));
	console.log('player placed on x:' + rndWidth + ' y:' + rndHeight);
	grid[rndHeight][rndWidth] = 'x';
};

exports.Update = function () {
	//console.log('frame updated');
	exports.setPlayer();
};