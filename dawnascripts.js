function colourCountry(){
    var name = document.getElementById("inputbox").value;
    var country = document.querySelector('[data-name = ' + name + ']');
    country.style.fill = 'red';
}