// Create a reasonably complicated Object in JavaScript that contains attributes and methods for the Motelcustomer.  The  customer  attributes  should  include  (and  not be limited  to),  the customer’sname, birth date,  gender,  androompreferences  (as  an  array),  payment method, mailing  address  (as  a  sub-object), phone  number, check-in  and  check-out  datetime  (as  a  sub-object),  and  object  methods  to  determine there age and duration of stay. The JavaScript code should also create a template literal string, or properly formatted html, that describes the customer. In other words, writes a paragraph describing the customer with many of their personal attributes dynamically embedded in the string / html coming from the above object definition.

//Author: Dawson Murray
//Date: March 20 2023

//Customer Info
let customer = {
    name: "",
    birthDate: "",
    gender: "",
    roomPreferences: [],
    paymentMethod: "",

    mailingAddress: {
        street: "",
        city: "",
        province: "",
        postalCode: "",
        country: "",
    },

    phoneNumber: "",

    checkInDate: {
        year: "",
        month: "",
        day: "",
        hour: "",
        minute: "",
    },

    checkOutDate: {
        year: "",
        month: "",
        day: "",
        hour: "",
        minute: "",
    },

    getAge: function() {
        const birthYear = new Date(this.birthDate).getFullYear();
        const currentYear = new Date().getFullYear();
        return currentYear - birthYear;
    },

    getDurationOfStay: function() {
        const checkIn = new Date(
            this.checkInDate.year,
            this.checkInDate.month,
            this.checkInDate.day,
            this.checkInDate.hour,
            this.checkInDate.minute
        );

        const checkOut = new Date(
            this.checkOutDate.year,
            this.checkOutDate.month,
            this.checkOutDate.day,
            this.checkOutDate.hour,
            this.checkOutDate.minute
        );

        const durationInMs = checkOut.getTime() - checkIn.getTime();
        const durationInDays = durationInMs / (1000 * 60 * 60 * 24);
        return durationInDays
    }
};

const customerDescription = `
<p>Customer Name: ${name}</p>
<p>Birth Date: ${birthDate}</p>
<p>Gender: ${gender}</p>
<p>Room Preferences: ${roomPreferences}</p>
<p>Payment Method: ${paymentMethod}</p>
<p>Phone Number: ${phoneNumber}</p>
<p>Address: ${street} ${city} ${province} ${postalCode} ${country}</p>
<p>Check In Date: ${checkInDate}</p>
<p>Check Out Date: ${checkOutDate}</p>`

console.log(customerDescription);