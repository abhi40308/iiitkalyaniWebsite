$(document).ready(function(){       
   var scroll_start = 0;
   var startchange = $('#first-navbar');
   var offset = startchange.offset();

   var temp = $(document).scrollTop();
   if(temp > offset.top){
      $("#startchange").css({
                            'background-color': '#484A4B',
                            'transition': 'background-color 100ms linear'});
          $("#startchange .leaf").css('color', 'white');
          $("#startchange .fa").css('color', 'white');
   }
    // if (startchange.length){
   $(document).scroll(function() { 
      scroll_start = $(this).scrollTop();
      if(scroll_start > offset.top) {
          $("#startchange").css({
                            'background-color': '#484A4B',
                            'transition': 'background-color 100ms linear'});
          $("#startchange .leaf").css('color', 'white');
          $("#startchange .fa").css('color', 'white');
       } else {
          $('#startchange').css('background-color', '#f9f9f9');
          $("#startchange .leaf").css('color', 'grey');
          $("#startchange .fa").css('color', 'grey');
        }
    });
    
});

$(document).ready(function(){ 
    $('#second-nav').singlePageNav({
                offset: $('#second-nav').outerHeight(),
                filter: ':not(.external)',
                updateHash: true,
                beforeStart: function() {
                    console.log('begin scrolling');
                },
                onComplete: function() {
                    console.log('done scrolling');
                }
});
});

$(document).ready(function(){
  // Add smooth scrolling to all links
  $('.scroll-link').on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){
   
        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
});

$(document).ready(function() {
  jQuery.fn.carousel.Constructor.TRANSITION_DURATION = 500  // 2 seconds
});

$(document).ready(function () {
  $("body").click(function(event) {
    if(event.target.id != "first-nav" && event.target.id != "dropdown-content" ){
    $(".navbar-collapse").collapse('hide');
  }
  });
});