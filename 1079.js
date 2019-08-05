var input = require('fs').readFileSync('./dev/stdin', 'utf8');
var lines = input.split('\n');

let n = lines.shift();

for(let i = 0; i < n; i++) {
	let valores = lines.shift().split(" ");

	let floats = valores.map(valor => parseFloat(valor));
	let soma = (floats[0] * 2) + (floats[1] * 3) + (floats[2] * 5);
	let media = soma / 10;
	
 	console.log(media.toFixed(1));
}
