$.fn.toggleClick = function() {
    var methods = arguments;
    var count = methods.length;
    return this.each(function(i, item){
	var index = 0;
	$(item).on('click', function() {
	    return methods[index++ % count].apply(this, arguments);
	});
    });
};


$(document).ready(function(){
    
    $('#lampe').toggleClick( 
	function() {
	    $.get("/lampe/1");
	    $(this).html("Lampe allumée");
	},
	function() {
	    $.get("/lampe/0");
	    $(this).html("Lampe éteinte");
	}
    );

    $('.couleur').change( function() {
	$.get("/RGB".concat("/",$('#rouge').val(),"/",$('#vert').val(),"/",$('#bleu').val()));
    });

    $("#servo").change( function() {
	$.get("/servo/".concat($('#servo').val()));
    });
});