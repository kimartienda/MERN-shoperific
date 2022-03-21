// removed the "const" should be one declaration only.
let fullname = "Steve Rogers";
	console.log(fullname);




// change the parameter from "userAge" to "age" since userAge is not existing variable.
	let age = 40;
	console.log(age);




// added double quotes for "Thor" and "Natasha" because both are strings.
	let friends = ["Tony","Bruce","Thor","Natasha","Clint","Nick"];
	console.log(friends);




// removed ";" and replaced to "," in the value of key fullName and added " since the pair is missing.
// removed ";" and replaced to "," in the value of key age.
// added ";" after the closing bracket.
	let profile = {

		username: "captain_america",
		fullName: "Steve Rogers",
		age: 40,
		isActive: false,

	};
	console.log(profile);



// changed the variable name from fullname to avengerName and use camelCase.
	let avengerName = "Tony Stark";
	console.log(avengerName);

// removed const largestOcean = "Pacific Ocean"; since const cannot be redeclared.
	const largestOcean = "Atlantic Ocean";
	console.log(largestOcean);



// Create a getSum() function

function getSum(x,y) {
	return `${x + y}`
};

let sample1 = getSum (100, 500);
console.log(sample1);