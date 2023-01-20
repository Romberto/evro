window.addEventListener('load', function(){
    $('.js_valid_num').on('input',function(e){
        let keyup = $(this).val()
        if($.isNumeric(keyup)){
            number = parseInt(keyup)
            if(number < 0 || number>9){
                $(this).val('0')
            }
        }else{
            $(this).val('0')
            e.preventDefault()
        }
    })

    $('.js_drunk').click(function(){
	    if ($(this).is(':checked')) {
		     $('.js_drunk').not(this).prop('checked', false);
	}
    });

    $('.js_damage').click(function(){
	    if ($(this).is(':checked')) {
		     $('.js_damage').not(this).prop('checked', false);
	}
    });

    $('.js_other_damage').click(function(){
	    if ($(this).is(':checked')) {
		     $('.js_other_damage').not(this).prop('checked', false);
	}
    });

    $('.js_polis_men').click(function(){
	    if ($(this).is(':checked')) {
		     $('.js_polis_men').not(this).prop('checked', false);
	}
    });

    $('.js_damage_tc').click(function(){
	    if ($(this).is(':checked')) {
		     $('.js_damage_tc').not(this).prop('checked', false);
	}
    });

    $('.js_damage_b_tc').click(function(){
    if ($(this).is(':checked')) {
         $('.js_damage_b_tc').not(this).prop('checked', false);
	}
    });


    $('.js_case_a').on('click',function(e){
        var count_a = $('.js_case_a:checked').length
        if (count_a > 3){
            e.preventDefault()
        }else{
            $('.js_quantity_case_a').val(count_a)
            $('.quantity_win_a').text(count_a)
        }
    })

    var count_a = $('.js_case_a:checked').length
    $('.js_quantity_case_a').val(count_a)
    $('.quantity_win_a').text(count_a)


    $('.js_case_b').on('click',function(e){
        var count_a = $('.js_case_b:checked').length
        if (count_a > 3){
            e.preventDefault()
        }else{
            $('.js_quantity_case_b').val(count_a)
            $('.quantity_win_b').text(count_a)
        }
    })

    var count_a = $('.js_case_b:checked').length
    $('.js_quantity_case_b').val(count_a)
    $('.quantity_win_b').text(count_a)


    $('.js_transport').click(function(){
	    if ($(this).is(':checked')) {
		     $('.js_transport').not(this).prop('checked', false);
	}
    });

    $('.js_managet').click(function(){
	    if ($(this).is(':checked')) {
		     $('.js_managet').not(this).prop('checked', false);
	}
    });

    $('.js_work_auto').click(function(){
	    if ($(this).is(':checked')) {
		     $('.js_work_auto').not(this).prop('checked', false);
	}
    });

})
