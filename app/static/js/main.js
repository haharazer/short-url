/**
 * Created by han on 15/1/18.
 */

$(document).ready(function(){
    $('#gen-button').click(function(){
            var url = 'http://' + $('#input-url').val();
            $.ajax(
                {
                    data: {'u': url},
                    url: '/short',
                    type: 'POST',
                    dataType: 'text',
                    success: function(resp){
                        $('#res').attr('href', resp).text(resp);
                    },
                    error: function(){
                        alert("error");
                    }
                });
        }
    );
});