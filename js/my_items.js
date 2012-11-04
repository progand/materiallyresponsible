var datasorce

$(document).ready(function() {
	$("#name").kendoAutoComplete({
		minLength : 3,
		dataTextField : "Name",
		dataSource : {
			transport : {
				read : {
					url : "/?get=names",
					dataType : "json",
				}
			}
		}
	});

	$.getJSON("/?get=names", function(json) {
		// $("#list_routines").html("");
		locale = json;
	});

	var dataSource = new kendo.data.DataSource({

		transport : {
			read : function(options) {
				// make AJAX request to the remote service

				$.ajax({
					url : "/?get=names",
					dataType : "json",
					success : function(result) {
						// notify the DataSource that the operation is complete

						options.success(result);
					}
				});
			}
		}
	});

	dataSource.read();
	data = dataSource.data();
});