
$(document).ready(function(){
	$(".create-button").on("click", function(event){
		$.ajax({
			method: "GET",
			url: "http://localhost:8000/create",
			success: function(result){
				// make json dict where result = value, form = key
				var jeff = new Object();
				jeff.form = result;
				jeff.csrftoken = $.cookie('csrftoken');
				var template = $('#create').html();
				var renderM = Mustache.render(template, jeff);
				$('.create-field').html(renderM);
				my_validator();
			},
			error: function(){console.log('you suck')
			}
		})	
	});
})