$(document).ready(function() {
    $(window).on('load', function() {
        setTimeout(function() {
            var msnry = new Masonry('.grid');
            msnry.layout();
        }, 100);
    });

    var myModal = new bootstrap.Modal(document.getElementById('myModal2'))
    myModal.show();
})