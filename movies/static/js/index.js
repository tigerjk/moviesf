$(document).ready(function () {
	{% if data %}
	var data = {{ data|safe }};
	$tableBody = $('#movie_table').find('tbody');
	$.each(data, function() {
		$row = $('<tr>');
		$.each(this, function(key, value) {
			$col = $('<td>');
			$col.text(key+":"+value);
			$row.append($col);
		});

	});	
	$tableBody.append($row);
	{% endif %}
});
