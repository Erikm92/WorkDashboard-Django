


$('.editable').each(function(){

    var label = $(this)
    label.after("<input type='text' style='display:none'/>")
    var edittext = $(this).next()
    edittext[0].name = this.id.replace('lbl','txt')
    edittext.val(label.html())
    label.click(function(){

        $(this).hide()
        $(this).next().show()

    });

    edittext.focusout(function(){
        $(this).hide()
        $(this).prev().html($(this).val())
        $(this).prev().show()

    });


});




