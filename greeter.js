var Role = /** @class */ (function () {
    function Role(role, firstName, lastName) {
        this.role = role;
        this.firstName = firstName;
        this.lastName = lastName;
        this.fullName = role + " " + firstName + " " + lastName;
    }
    return Role;
}());
function hello(person) {
    return "Hello, " + person.fullName + "!";
}
var user = new Role("Student", "CHAU", "Julien");
document.body.textContent = hello(user);
