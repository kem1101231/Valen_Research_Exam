
		$('#reference_type').on('input', function (argument) {
			
			var display_div

			switch($(this).val()){
				case 'Type':
					display_div = $('#type_div');
					break
				case 'Brand':
					display_div = $('#brand_div');
					break
				case 'Color':
					display_div = $('#color_div');
					break
			}

			hide_all_except(display_div)

		})

		function group_cars() {

	            $.ajax({
	                type: 'POST',
	                url:'/find/car/by_group',
	                data:{
	                    'reference_type': $('#reference_type').val(),
	                    'reference_input':$('#reference').val(),
	                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),

	                },

	                    success:function(response) {

	                       var list  = response['cars']
	                       var html_to_add = ''

	                       
	                       for(var line in list){

	                       		    html_to_add += "<tr>"
			                    	html_to_add += "<td>"+list[line]['name']+"</td>"
			                    	html_to_add += "<td>"+list[line]['brand']+"</td>"
			                    	html_to_add += "<td>"+list[line]['type']+"</td>"
			                    	html_to_add += "<td>"+list[line]['color']+"</td>"
			                    	html_to_add += "</tr>"

	                       }

	                       $('#data_group_table').html(html_to_add)
	                    }

	            });
		}

		$('#brand_g').on('input',function(argument) {
			var id = get_option_id(this, 'brand_gSeacrhList'); 
			$('#reference').val(id)
			group_cars()

		})

		$('#type_g').on('input',function(argument) {
			var id = get_option_id(this, 'type_gSeacrhList'); 
			$('#reference').val(id)
			group_cars()
		})

		$('#color_g').on('input',function(argument) {
			var id = get_option_id(this, 'color_gSeacrhList'); 
			$('#reference').val(id)
			group_cars()
		})

		$('#group_car_btn').on('click', function (argument) {
			hide_all_except($('#type_div'))

		})
	    
	    function hide_all_except(except_dom) {
	    	set_all_to_default()
	    	$('#brand_div').attr('style', 'display:none');
	    	$('#type_div').attr('style', 'display:none');
	    	$('#color_div').attr('style', 'display:none');

	    	$(except_dom).removeAttr('style');
	    }
