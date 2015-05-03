$(document).ready(function(){

    setInterval( function() {
	$.get('/sensor_request', function( data ) {
	    $('#temp').html("Température : " + data.temp);
	    $('#hum').html("Humidité : " + data.hum);
	    $('#lum').html("Luminosité : " + data.lum);
	    $('#US').html("Distance : " + data.dist);
	    $('#slide').html("Slider : " + data.pot);
	    $('#mouv').html("Mouvement : " + data.pir);
	}, "json");
    }, 1000);





});
