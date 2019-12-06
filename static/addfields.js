$(document).ready(function() {
    // The maximum number of options
    var MAX_OPTIONS = 5;

    $('#surveyForm')
        .bootstrapValidator({
            fields: {
                'option[]': {
                    validators: {
                        notEmpty: {
                            message: 'The option required and cannot be empty'
                        },
                        stringLength: {
                            max: 300,
                            message: 'The option must be less than 300 characters long'
                        }
                    }
                }
            }
        })

        // Add button click handler
        .on('click', '.addButton', function() {
            var $template = $('#optionTemplate'),
                $clone    = $template
                                .clone()
                                .removeClass('invisible')
                                .removeAttr('id')
                                .insertBefore($template),
                $option   = $clone.find('[name="option[]"]');

            // Add new field
            $('#surveyForm').bootstrapValidator('addField', $option);
        })

        // Remove button click handler
        .on('click', '.removeButton', function() {
            var $row    = $(this).parents('.form-group'),
                $option = $row.find('[name="option[]"]');

            // Remove element containing the option
            $row.remove();

            // Remove field
            $('#surveyForm').bootstrapValidator('removeField', $option);
        })

        // Called after adding new field
        .on('added.field.bv', function(e, data) {
            // data.field   --> The field name
            // data.element --> The new field element
            // data.options --> The new field options

            if (data.field === 'option[]') {
                if ($('#surveyForm').find(':visible[name="option[]"]').length >= MAX_OPTIONS) {
                    $('#surveyForm').find('.addButton').attr('disabled', 'disabled');
                }
            }
        })

        // Called after removing the field
        .on('removed.field.bv', function(e, data) {
           if (data.field === 'option[]') {
                if ($('#surveyForm').find(':visible[name="option[]"]').length < MAX_OPTIONS) {
                    $('#surveyForm').find('.addButton').removeAttr('disabled');
                }
            }
        });
});

$(document).ready(function() {
    // The maximum number of options
    var MAX_OPTIONS = 10;

    $('#MenuForm')
        .bootstrapValidator({
            fields: {
                'dishn': {
                    validators: {
                        notEmpty: {
                            message: 'The option required and cannot be empty'
                        },
                        stringLength: {
                            max: 300,
                            message: 'The option must be less than 300 characters long'
                        }
                    }
                }
            }
        })

        // Add button click handler
        .on('click', '.addDish', function() {
            var $template = $('#dishTemplate'),
                $clone    = $template
                                .clone()
                                .removeClass('invisible')
                                .removeAttr('id')
                                .insertBefore($template),
                $option   = $clone.find('[name="dishn"]');

            // Add new field
            $('#MenuForm').bootstrapValidator('addField', $option);

            // Add unique row id

        })

        // Remove button click handler
        .on('click', '.removeDish', function() {
            var $row    = $(this).parents('.form-group'),
                $option = $row.find('[name="dishn"]');

            // Remove element containing the option
            $row.remove();

            // Remove field
            $('#MenuForm').bootstrapValidator('removeField', $option);
        })

        // Called after adding new field
        .on('added.field.bv', function(e, data) {
            // data.field   --> The field name
            // data.element --> The new field element
            // data.options --> The new field options

            if (data.field === 'dishn') {
                if ($('#MenuForm').find(':visible[name="dishn"]').length >= MAX_OPTIONS) {
                    $('#MenuForm').find('.addDish').attr('disabled', 'disabled');
                }
            }
        })

        // Called after removing the field
        .on('removed.field.bv', function(e, data) {
           if (data.field === 'dishn') {
                if ($('#MenuForm').find(':visible[name="dishn"]').length < MAX_OPTIONS) {
                    $('#MenuForm').find('.addDish').removeAttr('disabled');
                }
            }
        });
});