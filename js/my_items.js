var datasorce

$(document).ready(function() {
	 $( "#names" ).autocomplete({
         source: "/?get=types",
         minLength: 2,
         select: function( event, ui ) {
             log( ui.item ?
                 "Selected: " + ui.item.value + " aka " + ui.item.id :
                 "Nothing selected, input was " + this.value );
         }
     });
});