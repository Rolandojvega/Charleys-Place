
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