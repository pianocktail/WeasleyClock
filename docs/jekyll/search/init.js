$(document).ready (function() {

    const input = $('#tipue_search_input')
    const results = $('#search-results')[0]
    const content = $('#content')[0]

    let toggle = true, revisit = false
    $('#search-icon').click (function(){
        $('#search')[0].style.display = toggle ? 'block' : 'none'
        if (toggle) {
            
            input.val (localStorage.recentSearch) 
            input.focus().select()

            if (revisit) {
                results.style.display = 'block'
                content.style.display='none'
            }
        } else {
            results.style.display = 'none'
            content.style.display='block'
        }
        toggle = !toggle
    })

    $('#search') .on ("submit", function(event) {
        revisit = localStorage.recentSearch = input.val()
        results.style.display='block'
        content.style.display='none'
        event.preventDefault()
    })
    input.tipuesearch({ showURL: false })

})
