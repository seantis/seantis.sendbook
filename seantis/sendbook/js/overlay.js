$(document).ready(function() {

    $('#document-action-sendbook a').prepOverlay({
        subtype: 'ajax',
        filter: '#content>*',
        formselector: 'form',
        noform: function(el) {return $.plonepopups.noformerrorshow(el, 'close');},
        closeselector: '[name=form.button.cancel]'
    });

});
