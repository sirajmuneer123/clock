$( document ).ready(function() {
    console.log( "ready!" );

    $('.start_clock').click(function(e) {
        var button = $(this)
        var type = $(this).attr("data-type") 
        $.ajax({
            type: 'post',
            url: '/employee/start/',
            data: {
                'type': type,
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(data) {
                var res = JSON.parse(data)
                if(res.status == "1"){
                    button.removeClass("btn btn-success")
                    button.addClass("btn btn-danger")
                    button.removeClass("start_clock")
                    button.addClass("stop_clock")
                    if(res.old_type == "1"){
                        $('*[data-type="1"]').val('Start Working')
                        $('*[data-type="1"]').removeClass("btn btn-danger")
                        $('*[data-type="1"]').addClass("btn btn-success")
                    }else if(res.old_type  == "2"){
                        $('*[data-type="2"]').val('Start Breaking')
                        $('*[data-type="2"]').removeClass("btn btn-danger")
                        $('*[data-type="2"]').addClass("btn btn-success")
                    }else if(res.old_type  == "3"){
                        $('*[data-type="3"]').val('Start Meeting')
                        $('*[data-type="3"]').removeClass("btn btn-danger")
                        $('*[data-type="3"]').addClass("btn btn-success")
                    }
                    if(type == "1"){
                        button.val('Stop Working')
                    }else if(type == "2"){
                        button.val('Stop Breaking')
                    }else if(type == "3"){
                        button.val('Stop Meeting')
                    }
                }
                
                
                console.log("yyyyyyyyyy", data)
            }
        });
    })


    $('.stop_clock').click(function(e) {
        var type = $(this).attr("data-type") 
        $.ajax({
            type: 'post',
            url: '/employee/stop/',
            data: {
                'type': type,
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(data) {
                var res = JSON.parse(data)
                if(res.status == "1"){
                    button.removeClass("btn btn-danger")
                    button.addClass("btn btn-success")
                    button.removeClass("stop_clock")
                    button.addClass("start_clock")
                    if(type == '1'){
                        button.val('Start Working')
                    }else if(type == '2'){
                        button.val('Start Breaking')
                    }else if(type == '3'){
                        button.val('Start Meeting')
                    }
                    button.val('')
                }
                console.log("yyyyyyyyyy stop", data)
            }
        });
    })
});
