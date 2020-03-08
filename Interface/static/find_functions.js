
		function get_data(input_name, url_input, searchList) {

	            $.ajax({
	                type: 'POST',
	                url:url_input,
	                data:{
	                    'input_data': $(input_name).val(),
	                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),

	                },

	                    success:function(response) {

	                       var list  = response['data_result']
	                       var html_to_add = ''

	                       
	                       for(var line in list){
	                       		
	                       		var id_val = list[line]['id']
	                       		var name_val = list[line]['name']
	                       		
	                       		html_to_add += '<option id="'+id_val+'" value ="'+name_val+'" value2 ="'+name_val.replace(/ /g,'')+'"/>'
	                       }

	                       $('#'+searchList).html(html_to_add)
	                    }

	            });

		}

		$('#brand').keypress(function(e){
			get_data(this, '/find/brand', 'brandSeacrhList')
	    });

		$('#type').keypress(function(e){
			get_data(this, '/find/type', 'typeSeacrhList')
	    });

		$('#color').keypress(function(e){
			get_data(this, '/find/color', 'colorSeacrhList')
	    });
		
		$('#car').keypress(function(e){
			get_data(this, '/find/car', 'carSeacrhList')
	    });
		
		$('#ref_car').keypress(function(e){
			get_data(this, '/find/car', 'ref_carSeacrhList')
	    });

		$('#brand_g').keypress(function(e){
			get_data(this, '/find/brand', 'brand_gSeacrhList')
	    });

		$('#type_g').keypress(function(e){
			get_data(this, '/find/type', 'type_gSeacrhList')
	    });

		$('#color_g').keypress(function(e){
			get_data(this, '/find/color', 'color_gSeacrhList')
	    });
