var input = require('fs').readFileSync('./dev/stdin', 'utf8');
var lines = input.split('\n');

let x = lines.shift();

for(let i = 0; i < x; i++) {
	let n = lines.shift();

	if(n == 0) {
		console.log("NULL");
	} else {
		let output = [];
	
		output.push(n % 2 === 0 ? "EVEN" : "ODD");
		output.push(n > 0 ? "POSITIVE" : "NEGATIVE");
		
		console.log(output.join(" "));
	}
}