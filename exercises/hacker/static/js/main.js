$(document).ready(function(){
	// $(".create-button").on('click', function(event){
	// 	var postTemplate = "<div class='card-panel blue lighten-5'><div><h5><a href='/blogs/edit/{{ slug }}'>{{ title }}</a></h5></div><div class=><p>{{ content|linebreaks }}</p></div></div><div><p><i>Posted by {{ user }}</i></p></div><div class='timestamp'><p class='timemargin'>{{ created_at }}</p>{% if update_check %}<p>Updated at: {{ updated_at }}</p>{%endif%}</div>"
	// 	function addPost(post){
	// 		$('.content').append(Mustache.render(postTemplate, post));
	// 	}
	// 	var url = "http://localhost:8000/posts/view-all"
	// 	$.get(url, function(posts){
	// 		$.each(JSON.parse(posts), function(i, post){
	// 			addPost(post);
	// 		})
	// 	})
	// })
	$(".create-button").on("click", function(event){
		var createTemplate = "<div>{{{forms.as_p}}}</div>"
		console.log(1)
		var url = "http://localhost:8000/create"
		// function createField(){
		$.ajax({
			method: "GET",
			url: "http://localhost:8000/create",
			success: function(result){
				console.log(result)
			$('.create-field').html(Mustache.render(result));
			},
			error: function(){console.log('you suck')
			}
		})	
		}
		
	)
})