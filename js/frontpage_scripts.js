$(document).ready(function(){       
   var scroll_start = 0;
   var startchange = $('#startchange');
   var offset = startchange.offset();
    if (startchange.length){
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
    }
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
