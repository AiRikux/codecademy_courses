// This is a constant for Kelvin
const kelvin = 0;

// this is a constant for Celcius by minus 273 from Kelvin
const celcius = kelvin - 273

// this is a constant for farenheit
let fahrenheit = celcius * (9/5) + 32
// round down farenheit
fahrenheit = Math.floor(fahrenheit)

console.log(`The temperature is ${fahrenheit} degrees Fahrenheit`)

// convert celcius to newton temp
let newton = celcius * (33/100)
// round down newton
newton = Math.floor(newton)

console.log(`The temperature is ${newton} degrees Newton`)
