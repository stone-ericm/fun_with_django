$(document).ready(function(){
$(".create-field").on("submit", ".create-post-form", function(event){
	event.preventDefault()
	var mydata = $(this).serialize()
	$.ajax({
		method: "POST",
		url: "http://localhost:8000/create",
		data: mydata,
		success: function(result){
			console.log(result.title)
			$(".create-fielder").html("");
			var template = $('#new-post').html();
			result.created_at = new Date(result.created_at).toString('MMMM dd, yyyy, h:m tt');
			var renderM = Mustache.render(template, result);
			$('.content').prepend(renderM);

			// $(".content").prepend("<div class='card-panel blue lighten-5'><div><h5><a href='/blogs/edit/"{{ each.slug }}"''>"{{ each.title }}"</a></h5></div><div class=><p>"{{ each.content|linebreaks }}"</p></div></div><div><p><i>Posted by "{{ each.user }}"</i></p></div><div class='timestamp'><p class='timemargin'>"{{ each.created_at }}"</p>{% if each.update_check %}<p>Updated at: {{ each.updated_at }}</p>{%endif%}");
		}
	})
});
$(".create-field").on("submit", ".cancel-form", function(event){
	console.log('CANCELITPLX')
	event.preventDefault()
	$(".create-fielder").html("");
});
});