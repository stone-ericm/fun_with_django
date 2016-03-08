# Back to JS with AJAX!!!

### Learning Objectives
***Students will be able to...***

* Use ajax calls to talk to api's
* Use Mustache.js to render DOM elements

---
### Context

* All people care about is speed, lets give it to them.

---
### Lesson

#### Part 0 - How we get from client to server and back with AJAX.

![enter image description here](http://i.imgur.com/iqV8Seg.jpg)

This is the overview of how we get a request from a client to a server, and how the server responds with a request, and my example is specific to Django, AJAX, and Mustache.js

Let's go through each part with example code...

####Part 1 - HTML and using JS to detect a click event

First, let's import all the JavaScript libraries we're going to use, which are Mustache.js and jQuery.js, and we'll also import our own `main.js` file.

`index.html`
```
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
<script src="http://cdnjs.cloudflare.com/ajax/libs/mustache.js/0.8.1/mustache.min.js"></script>
<script src="{% static 'js/main.js' %}"></script>

...
    <!-- view todos for user -->
    <h1>Todos: </h1>
    <button id="view-todos-button" type="submit">View todos?</button>
    <ul class='todos'></ul>
...
```
Here's my HTML where I have a button. My button has an ID and a `type`.

I've also created an empty `ul` element in which I'll eventually all my `li` elements that I'll return and render with mustache.js - more on this later!

`main.js`
```
$(document).ready(function(){
    $("#view-todos-button").on('click', function(event){
    //TODO
  })
})
```
With JavaScript, I've set up an event handler on my the HTML element with `ID` of `view-todos-button`.

####Part 2 - AJAX call to server
Let's complete that `main.js` click handler now to make an AJAX call to our server:

`main.js`
```
$(document).ready(function(){
    $("#view-todos-button").on('click', function(event){
        //build a URL
        var url = "http://127.0.0.1:8000/todos/view-all"
        //send a get request to a server
        $.get(url, function(todos){
            //TODO
        });
    })
})
```
You can see here that I set a URL endpoint as a string. Then, I issue a GET request to that URL. I make an anonymous callback function that the `$.get` method will execute when my response returns from the server.

The `//TODO` part is what will execute when I get a response back from the server.

####Part 3 - urls.py

The AJAX call sends a request to Django. This gets routed to the urls.py file, and it looks for the `/todos/view-all` url. Let's make sure that end point is setup.

`urls.py`
```
from .views import ViewAll

...
url(r'^todo/view-all$', ViewAll.as_view(), name='view-all'),
...
```
Here, I've imported my `ViewAll` class based view from views.py. I've setup a URL endpoint that will route all requests to `/todo/view-all` to the `ViewAll` class based view.

####Part 4  and Part 5 - Views.py and JsonResponse

Now, I want to query the database, and send a response.

`views.py`
```
class ViewAll(View):
    def get(self, request, token):
        try:
            todos = Todo.object.all()
            todos = [todo.to_json() for todo in todos ]
            return JsonResponse({'todos':todos})
        except:
            return JsonResponse({'response': 'failed'})
```

`models.py`
```
class Todos(models.Model):
    content = models.TextField()
    finished = models.BooleanField(default=False)

    def to_json(self):
        return {
            'content': self.content,
            'finished': self.finished,
        }
```
In `views.py`, I query the database for all `Todo`'s. I use the `to_json` method that I've defined in `models.py`. Once I've queried them out of the database, I send them back in a dictionary as a `JsonResponse`.

####Part 6 - JavaScript callback
Now that Django has sent us back that data, we execute out callback function.

`main.js`
```
$(document).ready(function(){
    $("#view-todos-button").on('click', function(event){
        //build a URL
        var url = "http://127.0.0.1:8000/todos/view-all"
        //send a get request to a server
        $.get(url, function(todos){
            //for each todo in the list that's returned
            $.each(JSON.parse(todos), function(i, todo){
                //console log the todo
                console.log(todo);
            });
        });
    })
})
```
With the code I've added to `main.js`, I complete the anonymous callback function that's executed when my `$.get` returns. You can see what I do with this function is to iterate across each of the todos that's returned, and I just console.log out each todo at this point.

####Part 7 - Mustache.js to render the todo's to the DOM
Let's change the code within the anonymous callback function so that instead of logging each `todo` to console, we instead render it to the DOM. There's many ways we could do this, but we're going to use Mustache.js in this example.

`main.js`
```
$(document).ready(function(){
    $("#view-todos-button").on('click', function(event){

        //build a template to render to the DOM, and leave room for mustache to inject variables.
        var todoTemplate = "<li>Task: {{content}}, Completed?: {{finished}}</li>"

        //build a function that will use mustache to render data to a template
    function addTodo(todo){
        $('.todos').append(Mustache.render(todoTemplate, todo));
        }

        //build a URL
        var url = "http://127.0.0.1:8000/todos/view-all"
        //send a get request to a server
        $.get(url, function(todos){
            //for each todo in the list that's returned
            $.each(JSON.parse(todos), function(i, todo){
                //call our addTodo mustache functionality
                addTodo(todo);
            });
        });
    })
})
```

Now, we're using mustache.js to render each `todo` to the HTML dom element with the `.todo` selector. This will go back to the `ul` we defined in `index.html` back in part 1, and it will add 1`li` elements to that `ul`.
