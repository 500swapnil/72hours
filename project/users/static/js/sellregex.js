console.log("This is working");

function regex() {
    var title = document.getElementById('title').value;
    console.log(title);
    var price = document.getElementById('price').value;
    var quantity = document.getElementById('quantity').value;
    var description = document.getElementById('description').value;

    var title_patt = /^[a-zA-Z ]+$/;
    var price_patt = /^[0-9.]+$/;
    var quantity_patt = /^[0-9]+$/;
    var desc_patt = /^[a-zA-Z0-9\s]+$/;

    if (title.length > 50) {
        alert("Title length too long");
        return;
    } else if (title_patt.test(title) == 0) {
        alert("Enter valid title");
        return;
    } else if (parseInt(price) < 0 || price_patt.test(price) == 0) {
        alert("Enter valid price");
        return;
    } else if (parseInt(quantity) < 0 || quantity_patt.test(quantity) == 0) {
        alert("Enter valid quantity");
        return;
    } else if (description.length > 5000 || desc_patt.test(description) == 0) {
        alert("Enter valid description");
        return;
    } else {
        document.getElementById('main-contact-form').action = "mailto:vivek.kaushal@outlook.com";
        // window.location.href = '/selldone';
    }
}