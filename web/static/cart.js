var addToCart = document.getElementsByClassName("btn-gr");

for (var i = 0; i < addToCart.length; i++) {
    var btn = addToCart[i]
    btn.addEventListener('click', function(event) {
        var btnclicked = event.target
        btnclicked.parentElement.remove()
    } )
}