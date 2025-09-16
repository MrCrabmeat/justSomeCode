//Write an algorithm to allow the user to enter an integer number for the number of paper
//bags, and a second integer (which must be greater than the first) for the number of sweets.
//The program then tells the user whether it is possible to put an odd number of sweets in
//each bag.
let numOfSweets = 0;
let numOfBags = 1;

function amountOfSweets() {
    while (numOfBags > numOfSweets) {
        while ((numOfBags % 2) === (numOfSweets % 2)){
            console.log("Please enter a valid input ");
            NumSweets(numOfSweets);
            NumBags(numOfBags);
            amountOfSweets();}
        console.log("You have too many bags, you pillock. ");
        NumSweets(numOfSweets);
        NumBags(numOfBags);
        amountOfSweets();}

    let NumOfOddSweetsPerBag = numOfSweets / numOfBags;
    if ((NumOfOddSweetsPerBag % 2) === 1) {
        console.log("You can have " + NumOfOddSweetsPerBag + " sweets per bag.")
        }}

function NumSweets() {
    return numOfSweets = prompt("how many sweets? "); }

function NumBags() {
    return numOfBags = prompt("how many bags? "); }

amountOfSweets();