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



$(document).ready(function() {
    $('#lumiere').toggleClick(
	function() {
	    $.get("/applications/lumiere/1/".concat($('#SB').val(),"/",$('#SH').val()));
	    $(this).attr("background-color", "#00CC00");
	    $(this).html("Active");
	},
	function() {
	    $.get("/applications/lumiere/0/40/60");
	    $(this).attr("background-color","#CC0000");
	    $(this).html("Inactive");
	});
});

