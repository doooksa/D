$(document).ready(function() {
    $('.header_burger').click(function(event) {
        $('.header_burger,.header_menu').toggleClass('active');
        $('body').toggleClass('lock');
    });

    $('.search-box').click(function(event) {
        $(this).toggleClass('active');
        
    });   


    $('.slider').slick({
        dots: true,
        speed: 1000,
        autoplay: true,
    });

});

let sbox=$('search-box')
$(document).mouseup(function(e){
    if (!sbox.is(e.target) && sbox.has(e.target).length ===0)
    {$('.search-box').removeClass('active')}
})


