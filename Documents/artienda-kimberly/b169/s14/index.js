/* 
JS - a scripting programming language that enables us to make interactive web pages.

Comments - to add comments: 

// or + / - to create single line comment.

*/
/* create multi line comment.

*/
/* 

	console.log() allows us to show/display data in our console.
	It is part of our browser with which we can use to display data.
*/
console.log("Hello, World!");

// Mini-activity

console.log("Kim");
console.log("Dinakdakan");


/* 

	Variables are containers of data. Save our data within our scripts.
	We use let keyword and the assignment operator (=)


	Syntax:

	let variableName = "data"

*/

let name = "Kimberly Carmel";

console.log(name);

let num = 5;
let num2 = 10;

console.log(num);
console.log(num2);

/*
	When console.logging variables, the name of the variable s will not be shown,
	what will be shown/displated are the contained within the variable.

	You could also check/display the values of multiple variables:

	console.log(variable1, variable2);
*/

console.log(name,num,num2);

// You can declare a blank variable.
// You can create variables without providing an initial value. However, that variable will be assigned as undefined.
// Becauase we dont know the value yet. Can add value later.
let myVariable;
console.log(myVariable)

/*

	Create variables is actually 2 steps:

	1. Declartion - It is the declaration/creation of the variable with either the let or const keyword.
	2. Initilization - Is when we provide an initial value to our variable.

	Declaration Initialization
	let myVar = "inital value"
*/
// you can asugn a value to a variable after it has been declared
myVariable = "new value";
console.log(myVariable);

let bestFinanlFantasy = "Final Fintasy X";
console.log(bestFinanlFantasy);

// you can update the value of the a variable declared using let keyword

bestFinanlFantasy = "Final Fantasy 7";
console.log(bestFinanlFantasy);

// We cannot update with the let keyword
// We cannot create another variable with the same name.
/*
let bestFinanlFantasy = "Final Fantasy 6";
console.log(bestFinanlFantasy);
*/


/*
	Const

	const keyword allows us to create a variable like let, however, the const variable
	cannot be updated. Values in a const variable cannot be changed.
	You cannot create a const variable without initialization.

*/

const pi = 3.1416;
console.log(pi);


// variable declared with const cannot be updated/re-assgined.
// pi = 3.15;
// console.log(pi);

// Declare const variable without initialization
// const plateNum;
// console.log(plateNum);

let name2 = "Edward Cullen";
let role = "Supervisor";

// Mini Activity

role = "Director";

const tin = "12333-1234";

console.log(name2,role,tin);

/*
	Convention in creating variable/constant names:

	To create a let variable, we use the let keyword, 
	To create a const variable we use const.

	variables declared with let, its value can be updated. variables declared with const,
	we cannot change the value.

	let variables and const variables are usually name in small caps.
	Because there are other JS keywords that starts in capital letters.

	If you want to name your variable with multiplae words, we can use camelCase.
	camelCase is a convention in writing by adding the first word in small caps
	and the following words starting with capital letters.

	variable names defines the valuue they contain. Name your variables appropriately.
*/

// Data Types
/*
	In most programming languages, data is differentiated into different types and we can
	do different things about this data. For most programming languages, we have to declare
	the data type of our data before we are able to create the variable and store it.

	However, JS is not strict when it comes to data types.

	There are data types where we need t ouse literals to create them::
	To create string, we use string literals like '' or ""
	To create object, we use object literals like {}
	To create arrays, we can use array literals like []
*/

/*
	Strings

	Strings are a series of alphanumeric characters that create a word, a phrase, a name or anything that is related to  creating a text.

	Strings are not and should not be used for mathematical operations.

	Strings are created with strings literals like single quotes ('') or double (" ")
*/

let country = "Philippines";
let province = "Metro Manila";
console.log(province, country);

/*
	You can actually combine a strings into a single string with the use of the plus sign.

	This is called, concatenation.
*/

// In strings, spaces and commas coun as characters
let address = province + ", " + country;
console.log(address);


// Mini Activity

let city1 = "Manila";
let city2 = "Copenhagen";
let city3 = "Washington D.C.";
let city4 = "Tokyo";
let city5 = "New York";

let country1 = "Philippines";
let country2 = "U.S.A";
let country3 = "South Korea";
let country4 = "Japan";

let capital1 = city1 + ", " + country1;
let capital2 = city3 + ", " + country2;
let capital3 = city4 + ", " + country4;

console.log(capital1);
console.log(capital2);
console.log(capital3);

// Numbers/Integers
// are number data which can be used for mathematical operations.
// to create a number daya, add a numeric character but with no "" or ''

let number1 = 10;
let number2 = 6;
console.log(number1);
console.log(number2);

/*
	Addition Operator

	(+) when used between 2 number types, it will add both numbers
*/
let sum1 = number1 + number2;
console.log(sum1)

let sum2 = 16 + 4;
console.log(sum2);

let numString1 = "30";
let numString2 = "50";
/*
There are numeric strings, they are composed numberic characters but are
considered a string because it is surrounded/created with double quotes ""
*/

let sumString1 = numString1 + numString2;
console.log(sumString1);
/*
When numberic strings are used with addition operators, it will not add but only
combine the strings
*/

// Note: When a number/interger is added with a numeric string, it results to concatenations.
// Force coercion
let sum3 = number1 + numString2;
console.log(sum3) //1050


// Boolean (True or False)
/*
	Usually use for logival operation and if-else-condition.
	When createa variable called a boolean, the variable is usually a YES or NO.

*/

let isAdmin = true;
let isMarried = false;
let isMVP = true;

console.log("Is she married? " + isMarried);
console.log("Is Curry MVP? " + isMVP);
console.log("Is he the current admin? " + isAdmin);

// Arrays
// are special kind of data types. It is used to store multiple values.
// can store different data type, however not a good practice.
// One array = same data type
// Arrays are creayed using array literal or square brackets []

let array1 = ["Goku", "Gohan", "Goten", "Vegeta", "Trunks", "Broly"];
let array2 = ["One Punch Man", "Saitam", true, 5000];

console.log(array1);
console.log(array2);


// Objects
// Objects are another special kind of data types used to mimic real world items/objects.
// to create complex data structure that contain pcs of information.
// Each field in an object is called a property. Each property are separated by comma.
// Each property is a pair of key : value.
// Each data is given more significant because each data/value has key which defines the data.

let hero1 = {
	herName: "Once Punch Man",
	realName: "Saitama",
	income: 5000,
	isActive: true
};

let parokyaNiEdgar = ["Chito", "Buwi", "Darius", "Gab"];
let singer = {
	firstName: "Chito",
	lastName: "Miranda",
	age: false,
	isActive: 46
};
console.log(parokyaNiEdgar);
console.log(singer);

let beatles = ["Ringo", "Paul", "John", "George"];
let person1 = {
	firstName: "Paul",
	lastName: "Martin",
	age: true,
	isActive: 25
};
console.log(beatles);
console.log(person1);


/* Null and Undefined*/
// Null is the explicit absense of data/value. This is done to show that a variable actually contains nothing as 
//opposed to undefined which means the variable has been declared or created but there was no initial value.
	// Null explicit absence value.
	// Undefined there is no value YET.

	// Use cases of Null

	// When doing query or search, there of course might a 0 result.
		let foundResult = null;

// Undefined is a representation that a variable has been create or declared but there is no initial value, so, we cant say what value, thus it is undefined
		let sampleVariable; //declaration with no initial value results to undefined
	
	//For undefined, this is normally 	caused by developers when creating variables that have no data or value associated or initialized with them.
		let person2 = {
			name: "Peter",
			age: 42
		};

		//Access value of object's property we use dot notation:
		// objectName.propertyName

		console.log(person2.name);
		console.log(person2.age);

		//Undefined, because the person2 varialable does exist, however there is no property in the object called isAdmin.
		console.log(person2.isAdmin);

/* Functions */
/*
	Functions in JS, are lines/blocks of code that tell our device/application to perform
	a certain task when callsed or invoked.

	Funcations are reusable pcs of code with instructions/statements which 
	can be used over and over again just so long as we call or use it,

	You can think of functions as programs with a program
*/

	console.log("Good Afternoon, Everyone! Welcome to my application");

	function greet(){
			console.log("Good Afternoon, Everyone! Welcome to my application");

	}
	// function invocation - function invocation is when we call or use our functions.
	greet()
	greet()

// Mini Activity

let favoriteFood = "Xiaolongbao";
console.log(favoriteFood);


let x = 150;
let y = 9;
z = x + y;
console.log(z);

let a = 100;
let b = 90;
c = a * b;
console.log(c);

isActive = true;
console.log("He is active in working out:" + " " + isActive);


favoriteRestaurant = ["Din Tai Fung", "Manam", "Nonos" ,"Sky High Bar", "Wolfgang's Steakhouse"]
console.log(favoriteRestaurant);


favoriteSinger = {
	firstName: "Taylor Alison",
	lastName: "Swift",
	stageName: "Taylor Swift",
	birthDay: "December 13, 1989",
	age: 32,
	bestAlbum: "Lover",
	bestSong: "Teardrops on My Guitar",
	bestMovie: null,
	isActive: true
}
console.log(favoriteSinger);

// Paramters and Arguements

// "name" is called parameter
// Parameter acts as a named variable/container that exists ONLY in the function.

function printName (name){
	console.log(`My name is ${name}`)
};

// console.log(name)

printName("Jake");

function displayNum (number){
	console.log(number)
};

displayNum(3000);
displayNum(3001);

function displayMsg (name) {
	console.log(name)
}

displayMsg("Python is Fun");
// Multiple Parameters and Arguments
function displayFullname (firstName, lastName, age){
	console.log(`${firstName} ${lastName} is ${age}`)
};

	displayFullname("Kim", "Carmel", 25);

// return keyword
	// return keyword is used so that a function may return a value.
	// it also stops the process of the function after the return keyword.
function createFullName (firstName, middleName, lastName) {
	return `${firstName} ${middleName} ${lastName}`
	console.log("I will no longer run because the function's value/result has been returned.")
};

let fullName1 = createFullName("Tom", "Cruise", "Mapother");
console.log(fullName1)