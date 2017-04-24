module.exports = {

	createGrid: function (width, height) {
		grid = [];
		tile = 1;
		for(x = 0; x < width; x++){
			row = [];
			for(y = 0; y < height; y++){
				row.push(tile);
				tile++;
			}
			grid.push(row);
		}
		return grid;
	},

	Update: function () {
		//console.log('frame updated');
	}
};
