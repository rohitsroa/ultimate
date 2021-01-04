function w3_open() {
    document.getElementById("mySidebar").style.width = "200px";
}
function w3_close() {
    document.getElementById("mySidebar").style.width = "0px";
}
function xanimation(x) {
    x.classList.toggle("change");
}
function opennav() {
    var mobNav = document.getElementById("mobNav");

    if (mobNav.className.indexOf("w3-show") == -1) {
        mobNav.className += " w3-show";
    } else {
        mobNav.className = mobNav.className.replace(" w3-show", "");
    }
}

var navbar = document.getElementById("nav");
var sticky = navbar.offsetTop;
function stickyNav() {
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky");
        navbar.classList.remove("w3-margin-top")
    } else {
        navbar.classList.remove("sticky");
        navbar.classList.add("w3-margin-top")
    }
    scrollFunction();
}

/*  window.onscroll = function () {
     scrollFunction();
 } */

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("topbtn").style.display = "block";
    } else {
        document.getElementById("topbtn").style.display = "none";
    }
}
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
