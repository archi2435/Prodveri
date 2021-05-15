var cart = {};

$(document).ready(function () {
    CheckCart()
    AddToCart()
    ShowEmptyCart()
    ShowCart()
});

function AddToCart(){
    var form = $('#BuyForm');
    console.log(form);
    form.on('submit', function(e) {
        e.preventDefault();
        var buy_btn = $('#buy-btn');
        var post_name = buy_btn.data("name");
        var post_id = buy_btn.data("id");
        var post_category = buy_btn.data("categoty");
        var post_price = $('input[name=oplata]:checked').val();
    
    
        //var csrf_token = $('#BuyForm [name="csrfmiddlewaretoken"]').val();
        //data["csrfmiddlewaretoken"] = csrf_token;
        
        console.log(post_category);
        console.log(post_id);
        console.log(post_name);
        console.log(post_price);
        
        
        
        if (cart[post_id] != undefined) {
            cart[post_id][2] ++
        }
        else {
            cart[post_id] = [post_name, post_price, 1]
        }
        
        localStorage.setItem('cart', JSON.stringify(cart) )
        CheckCart()
        ShowCart()
    }) 
}

function CheckCart() {
    if (localStorage.getItem('cart') != null) {
        cart = JSON.parse(localStorage.getItem('cart'))
        console.log(cart)
    }
}

function ShowCart(){
    var out = ''
    if (localStorage.getItem('cart') != null) {
        for (var i in cart){
            out += '<li><a class="dropdown-item lead" href="#">' + cart[i][0] + ' ' + cart[i][1] +'₽</a></li>';
        }
    }
    
    $('.basket-items').html(out)
}

function ShowEmptyCart(){
    var out = ''
    if (localStorage.getItem('cart') == null) {
        out += '<li><a class="dropdown-item lead" href="#">Корзина пуста</a></li>'
    }
    $('.basket-items').html(out)
}