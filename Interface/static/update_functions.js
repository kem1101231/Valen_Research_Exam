
	    $('#save_car').on('click', function (argument) {

	            $.ajax({
	                type: 'POST',
	                url:'/add/car',
	                data:{
	                    'brand_input': $('#brandSeacrhList').attr('data-id'),
	                    'type_input': $('#typeSeacrhList').attr('data-id'),
	                    'color_input': $('#colorSeacrhList').attr('data-id'),
	                    'model_input': $('#car_model').val(),
	                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),

	                },

	                    success:function(response) {

	                    	table_data = $('#data_table').html()

	                    	new_car = response['new_car']

	                    	new_line = "<tr>"
	                    	new_line += "<td>"+new_car['name']+"</td>"
	                    	new_line += "<td>"+new_car['brand']+"</td>"
	                    	new_line += "<td>"+new_car['type']+"</td>"
	                    	new_line += "<td>"+new_car['color']+"</td>"
	                    	new_line += "</tr>"

	                    	table_data += new_line

	                    	$('#data_table').html(table_data)
	       
	                    	set_all_to_default();

	                    	alert("New Car Added")

	                    }

	            });
	    })

	    $('#move_car_btn').on('click', function () {

	            $.ajax({
	                type: 'POST',
	                url:'/move/car',
	                data:{
	                    'car_to_move': $('#carSeacrhList').attr('data-id'),
	                    'position': $('#move_to').val(),
	                    'move_to': $('#ref_carSeacrhList').attr('data-id'),
	                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),

	                },

	                    success:function(response) {
	                    	alert("Car list updated");
	                    	location.reload();
	                    }

	            });
	    })
	    
	    function set_all_to_default() {
	    	$('#brand').val('')
	    	$('#type').val('')
	    	$('#color').val('')
	    	$('#car_model').val('')
	    	$('#brand_g').val('')
	    	$('#type_g').val('')
	    	$('#color_g').val('')
	    }
