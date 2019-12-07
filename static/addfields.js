
$(document).ready(function() {
    var i = 2;

    $('#MenuForm')
        // Add button click handler
        .on('click', '.addDish', function() {
            var $template = $('#dishTemplate'),
                $clone    = $template
                                .clone()
                                .removeClass('invisible')
                                .removeAttr('id')
                                .attr('name','row'+i)
                                .insertBefore($template);

               /* $('div[name="row' + i + '"]').find("select[name ='category']").attr('name','category'+i);
                $('div[name="row' + i + '"]').find("input[name ='dish']").attr('name','dish'+i);
                $('div[name="row' + i + '"]').find("input[name ='country']").attr('name','country'+i);
                $('div[name="row' + i + '"]').find("input[name ='ingredients']").attr('name','ingredients'+i); */
                i++;

        })

        // Remove button click handler
        .on('click', '.removeDish', function() {
            var $row    = $(this).parents('.form-group');
               // $option = $row.find('[name="dishn"]');

            // Remove element containing the option
            $row.remove();

        })

});