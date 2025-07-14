//factory function
function createCircle(radius) {
    return {
        radius,
        draw: function() {
            console.log('draw');
        }
    };

}
const circle = createCircle(1);

//constructor function
function Circle(radius) {
    this.radius = radius;
    this.draw = function() {
        console.log('draw');
    }
}
const another = new Circle(1);

//Object-oriented Programming in JavaScript: Made Super Simple | Mosh
    //22:00 minutes in