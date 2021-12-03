$('#send').click(function(){
    if ($("#mail").val() && $("#idea").val()) {
        $('#mail').val("");
        $('#idea').val("");
        $('#alert').show().delay(2000).fadeOut();
    };
});