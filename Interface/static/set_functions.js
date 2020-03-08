
		function get_option_id( input_reference, list_reference) {
			var val = $(input_reference).val();
			console.log(val)
			console.log(val.replace(/ /g,''))
			var id = $('#'+list_reference+' option[value2='+ val.replace(/ /g,'')+']').attr('id');
			return id;
		}

		$('#brand').focusout(function(argument) {
			var id = get_option_id(this, 'brandSeacrhList'); 
			$('#brandSeacrhList').attr('data-id', id)
		})

		$('#type').focusout(function(argument) {
			var id = get_option_id(this, 'typeSeacrhList'); 
			$('#typeSeacrhList').attr('data-id', id)
		})

		$('#color').focusout(function(argument) {
			var id = get_option_id(this, 'colorSeacrhList'); 
			$('#colorSeacrhList').attr('data-id', id)
		})
		
		$('#car').focusout(function(argument) {
			var id = get_option_id(this, 'carSeacrhList'); 
			$('#carSeacrhList').attr('data-id', id)
			$('#car_to_move').html($(this).val())
		})

		$('#move_to').focusout(function(argument) {

			$('#action').html($(this).val())
		})

		$('#ref_car').focusout(function(argument) {
			var id = get_option_id(this, 'ref_carSeacrhList'); 
			$('#ref_carSeacrhList').attr('data-id', id)
			$('#move_to_ref_car').html($(this).val())
		})

