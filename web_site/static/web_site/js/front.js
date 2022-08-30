/*global $, document, Chart, LINECHART, data, options, window, setTimeout*/
$(document).ready(function () {

    'use strict';

    // ------------------------------------------------------- //
    // For demo purposes only
    // ------------------------------------------------------ //

    var stylesheet = $('link#theme-stylesheet');
    $( "<link id='new-stylesheet' rel='stylesheet'>" ).insertAfter(stylesheet);
    var alternateColour = $('link#new-stylesheet');

    if ($.cookie("theme_csspath")) {
        alternateColour.attr("href", $.cookie("theme_csspath"));
    }

    $("#colour").change(function () {

        if ($(this).val() !== '') {

            var theme_csspath = 'css/style.' + $(this).val() + '.css';

            alternateColour.attr("href", theme_csspath);

            $.cookie("theme_csspath", theme_csspath, { expires: 365, path: document.URL.substr(0, document.URL.lastIndexOf('/')) });

        }

        return false;
    });


    // ------------------------------------------------------- //
    // Equalixe height
    // ------------------------------------------------------ //
    function equalizeHeight(x, y) {
        var textHeight = $(x).height();
        $(y).css('min-height', textHeight);
    }
    equalizeHeight('.featured-posts .text', '.featured-posts .image');

    $(window).resize(function () {
        equalizeHeight('.featured-posts .text', '.featured-posts .image');
    });


    // ---------------------------------------------- //
    // Preventing URL update on navigation link click
    // ---------------------------------------------- //
    $('.link-scroll').bind('click', function (e) {
        var anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $(anchor.attr('href')).offset().top + 2
        }, 700);
        e.preventDefault();
    });


    // ---------------------------------------------- //
    // FancyBox
    // ---------------------------------------------- //
    $("[data-fancybox]").fancybox();


    // ---------------------------------------------- //
    // Divider Section Parallax Background
    // ---------------------------------------------- //
    $(window).on('scroll', function () {

        var scroll = $(this).scrollTop();

        if ($(window).width() > 1250) {
            $('section.divider').css({
                'background-position': 'left -' + scroll / 8 + 'px'
            });
        } else {
            $('section.divider').css({
                'background-position': 'center bottom'
            });
        }
    });


    // ---------------------------------------------- //
    // Search Bar
    // ---------------------------------------------- //
    $('.search-btn').on('click', function (e) {
        e.preventDefault();
        $('.search-area').fadeIn();
    });
    $('.search-area .close-btn').on('click', function () {
        $('.search-area').fadeOut();
    });



    // ---------------------------------------------- //
    // Navbar Toggle Button
    // ---------------------------------------------- //
    $('.navbar-toggler').on('click', function () {
        $('.navbar-toggler').toggleClass('active');
    });

});


//const imgs = [
    '/static/web_site/img/dishes/g.img_1.jpg',
    '/static/web_site/img/dishes/g.img_3.jpg',
    '/static/web_site/img/dishes/g.img_8.jpg',
    '/static/web_site/img/dishes/g.img_5.jpg',
    '/static/web_site/img/dishes/g.img_6.jpg',
];
const hero = document.querySelector('.hero');

if(hero) {
    let index = 0;
    setInterval(() => {
        hero.style.transition = `300ms linear`;
        hero.style.backgroundImage = `url(${imgs[index]})`;
        index++;
        if(index >= imgs.length) index = 0;
    }, 3000);
}

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
//function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

//function filterFunction() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    div = document.getElementById("myDropdown");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
        if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }
}