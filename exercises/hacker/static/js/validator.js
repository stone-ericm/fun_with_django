console.log('vadiate?????')
var my_validator = function(){
  $(".create-post-form").validate({
    rules: {
      "title": {
      	required: true,
      	maxlength: 40
  	  },
      "content": {
      	required: true,
      	maxlength: 4000
  	  }
    },
    messages: {
      "title": {
      	required: "Enter a title",
      	maxlength: jQuery.validator.format("Exceeded maximum {0} characters")
  	  },
      "content": {
      	required: "Can't be blank",
      	maxlength: jQuery.validator.format("Exceeded maximum {0} characters")
  	  }
    }
  });
};