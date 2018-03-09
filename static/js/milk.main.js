$(document).ready(function() {
    function updateButtonStatus() {
        $.get('/status').done(function(data) {
            $('#status-text').text(data)

            status_map = {'yes': '#7bf702',
                          'no': 'red',
                          'a bit': 'orange'}

            $('#status-circle').attr('fill', status_map[data])
        });
    }

    $('#yes-button').click(function(){
        $.post('/set_yes')
        updateButtonStatus()
        //~ $('#moo-sound')[0].play();
    })

    $('#no-button').click(function(){
        $.post('/set_no')
        updateButtonStatus()
        //~ $('#moo-sound')[0].play();
    })

    $('#almost-button').click(function(){
        $.post('/set_almost')
        updateButtonStatus()
        //~ $('#moo-sound')[0].play();
    })

    function mainUpdateLoop() {
        updateButtonStatus()
        setTimeout(mainUpdateLoop, 1000)
    }
    mainUpdateLoop()
});
