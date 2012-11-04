var autocompleteData = null;

function myAutocompleteRenderer(instance, td, row, col, prop, value,
		cellProperties) {
	Handsontable.AutocompleteCell.renderer.apply(this, arguments);
	td.style.fontStyle = 'italic';
	td.title = 'Type to show the list of options';
}

$(document).ready(function() {
	/*
	 * $("#names").autocomplete({ source : "/?get=types", minLength : 2, select :
	 * function(event, ui) { $("#names").val(ui.value) } });
	 */
	autocompleteData = [];
	$.getJSON("/?get=names", function(data) {
		autocompleteData['names'] = data;
	});
	$.getJSON("/?get=types", function(data) {
		autocompleteData['types'] = data;
	});
	$('#datatable').handsontable({
		colHeaders : true,
		colHeaders : [ "Name", "Type" ],
		startCols : 2,
		startRows : 1,
		minSpareRows : 1,
		autoComplete : [
		{
			match : function(row, col, data) {
				return (col === 0); // if it is first column
			},
			source : function(callback) {
				return autocompleteData['names']
			},
			strict : false
		// allows other values that defined in
		// the source array above
		}, {
			match : function(row, col, data) {
				return (col === 1); // if it is first column
			},
			source : function(callback) {
				return autocompleteData['types']
			},
			strict : false
		// allows other values that defined in
		// the source array above
		} ]
	});
});