// Create Variables using var
var favoriteFood = 'pizza'
var numOfSlices = 8

console.log(favoriteFood)
console.log(numOfSlices)

// Create Variables using let
// create initial value
let changeMe = true
// change value
changeMe = false

console.log(changeMe)

// Create Variables using const
const entree = 'Enchiladas'
console.log(entree)
// entree = 'Tacos' - will create error

// Mathematical Assignment Operators
let w = 4;
w = w + 1; // or
w += 1
// similarly
w -= 1
w *= 2
w /= 2

let levelUp = 10;
let powerLevel = 9001;
let multiplyMe = 32;
let quarterMe = 1152;
// Use the mathematical assignments in the space below:
levelUp += 5;
powerLevel -= 100;
multiplyMe *= 11;
quarterMe /= 4;
// These console.log() statements below will help you check the values of the variables.
console.log('The value of levelUp:', levelUp); 
console.log('The value of powerLevel:', powerLevel); 
console.log('The value of multiplyMe:', multiplyMe); 
console.log('The value of quarterMe:', quarterMe);

// Increment and Decrement
let gainedDollar = 3;
let lostDollar = 50;
gainedDollar++;
lostDollar--;

// String Concatenation with Variables
let favoriteAnimal = 'fox'
console.log("My favorite animal:" + favoriteAnimal)

// String Interpolation
const myName = 'Nabilah'
const myCity = 'Melbourne'
console.log(`My name is ${myName}. My favorite city is ${myCity}`)

// Use typeof Operator
let newVariable = 'Playing around with typeof.';
console.log(typeof newVariable)

newVariable = 1
console.log(typeof newVariable)
