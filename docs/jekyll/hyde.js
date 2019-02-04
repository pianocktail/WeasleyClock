
window.addEventListener ('load', function(){

    let ul = document.querySelector ('header.sidebar li ul');  if (!ul)  return
    let toc = Array.prototype.slice.call(document.querySelectorAll ('.sidebar.menu > li > a, .sidebar.menu > dt > a')) .map (
        function(each) {
            let item = '<li>' + each.outerHTML + '</li>'

            let next = each.nextElementSibling
            if (next && next.tagName == 'LABEL')
                item = item.replace (/>[^<]+<\/a>/, '>'+next.innerHTML+'</a>')

            if (each.hash) {
                let target = document.querySelector (each.hash)
                if (target && target.attributes.label )
                    item = item.replace (/>[^<]+<\/a>/, '>'+ target.attributes.label.value +'</a>')
            }

            return item
        }
    )
    let link = ul.parentElement.querySelector('a')
    if (path(link) != path(location)) {
        link.innerHTML = (link.dataset.shorty || link.innerHTML) +
            '<span onclick="_2top()"> &#9656; ' + ul.dataset.shorty + '</span>'
    }
    if (toc.length) {
        ul.innerHTML = toc.join('\n')
        if (ul.scrollIntoViewIfNeeded)
            ul.scrollIntoViewIfNeeded()
        else
            ul.scrollIntoView() // IE
    }
    else {
        if (ul.children.length == 0)  ul.style.display = 'none'
    }

    let selected = document.querySelector ('header.sidebar a[href="'+ (
        location.pathname.replace(/\/$/,'')
        // path(location)
    ) +'"]');  
    if (selected)  selected.classList.add ('selected')

    document.dispatchEvent(newEvent('sidebar-ready'))
})

function newEvent(eventName) {
    try {
        return new Event(eventName)
    } catch (err) { // IE
        const event = document.createEvent('Event');
        event.initEvent(eventName, false, false);
        return event
    }
}

function path (link) {
    return link.pathname.replace('.html','').replace(/\/$/,'')
}

if (window.matchMedia ('screen and (max-width: 400px)').matches)  window.onload = function() {

    let menu = document.querySelector ('header.sidebar')
    let content = document.querySelector('section#content')
    let menuButton = document.querySelector ('header.menubar > a')

    let toggle = true
    menuButton.onclick = function(){
        content.style.display = toggle ? 'none' : 'block'
        menu.style.display = toggle ? 'block' : 'none'
        toggle = !toggle
        event.preventDefault()
    }
    menu.onclick = function(){
        content.style.display = 'block'
        menu.style.display = 'none'
    }
}

function _2top(){
    event.preventDefault()
    window.scrollTo (0,0)
}

Array.prototype.slice.call(document.querySelectorAll('pre.highlight')).forEach (function(pre) {
	let a = document.createElement('a')
    a.className = 'copy'
    a.title = 'Copy to Clipboard'
	pre.insertBefore (a, pre.firstChild)
})

new Clipboard ('pre.highlight .copy', {
    target: function(a) { return a.parentElement }
}).on('success', function(e) {
    window.getSelection().removeAllRanges()
    e.trigger.parentElement.style.background = '#fe7'
    setTimeout (function() {e.trigger.parentElement.style.background='', 111})
})


