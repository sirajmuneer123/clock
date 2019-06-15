$( document ).ready(function() {
    var timeoutID;
 
    function setup() {
        this.addEventListener("mousemove", resetTimer, false);
        this.addEventListener("mousedown", resetTimer, false);
        this.addEventListener("keypress", resetTimer, false);
        this.addEventListener("DOMMouseScroll", resetTimer, false);
        this.addEventListener("mousewheel", resetTimer, false);
        this.addEventListener("touchmove", resetTimer, false);
        this.addEventListener("MSPointerMove", resetTimer, false);
    
        startTimer();
    }
    setup();
    
    function startTimer() {
        // wait 2 seconds before calling goInactive
        timeoutID = window.setTimeout(goInactive, 60000*10);
    }
    
    function resetTimer(e) {
        window.clearTimeout(timeoutID);
    
        goActive();
    }
    var time_status = false
    function goInactive() {
        // do something
        time_status = true
        console.log("idleleeeee", timeoutID)
        $.ajax({
            type: 'post',
            url: '/employee/idle-time/',
            data: {
                'status': 'start',
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(data) {
                 console.log("idle start response", data)
            }
        })
    }
    
    function goActive() {
        // do something
        if(time_status){
            console.log("idleleeeeeactive", timeoutID)
            $.ajax({
                type: 'post',
                url: '/employee/idle-time/',
                data: {
                    'status': 'stop',
                    'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
                },
                success: function(data) {
                    console.log("idle stop response", data)
                }
            })
            time_status = false 
        }
         
        startTimer();
    }
})