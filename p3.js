$(document).ready(function() {
	$('.nav-btn').on('click', function(event) {
		event.preventDefault();
		
		$('.sidebar').slideToggle('fast');

		window.onresize = function(){
			if ($(window).width() >= 768) {
				$('.sidebar').show();
			} else {
				$('.sidebar').hide();
			}
		};
	});
});