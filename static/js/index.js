$(document).ready(function() {
    $(window).on('load', function() {
        setTimeout(function() {
            var msnry = new Masonry('.grid');
            msnry.layout();
        }, 100);
    });
})