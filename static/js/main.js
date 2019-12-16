
// On Load Scroll Chats
$("#msg-list-div").animate({ scrollTop: $('#msg-list-div').prop("scrollHeight")}, 1000);

// POST New Message
$('#chat-form').on('submit', function(event){
    event.preventDefault();

    $.ajax({
        url : 'post/',
        type : 'POST',
        data : { 'msgbox' : $('#chat-msg').val() },

        success : function(json){
            $('#chat-msg').val('');
            $('#msg-list').append('<li class="replies"><p>' + json.msg + '</p></li>');
            var chatlist = document.getElementById('msg-list-div');
            chatlist.scrollTop = chatlist.scrollHeight;
        }
    });
});

// GET Messages
function getMessages(){
        $.get('/messages/', function(messages){
            $('#msg-list').html(messages);
        });

}
$(function(){
    $('#msg-list-div').on(function(){
        // $("#msg-list-div").animate({ scrollTop: $('#msg-list-div').prop("scroll")}, 2000);
    $('#msg-list-div').animate({
        scrollTop: $('#msg-list-div')[0].scrollHeight}, 2000);
    });

    refreshTimer = setInterval(getMessages, 500);


});

//GET Online User
refreshUsers = setInterval(getUsers, 5000);
function getUsers(){
    $.get('/users/', function(data){
        $('#users-lists').html(data);
        $('#users-lists').prepend($(".onlines"));
    });
}

// TO Overide CSRF Token using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');


function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

// Emoji sugesstion
function emoji_suggest() {
    $(".emoji").remove();
    var y = $('#chat-msg').val().toLowerCase();
    var array = y.split(" ",);
    $.getJSON("/static/js/emojis.json", function(json) {
        get_emoji(json, array)
    });
  }

function get_emoji(data, texts){
    if (data === null) {
        return null;
    }
    else{
        Object.values(data).forEach(element => {
            Object.values(element.keywords).forEach(elements => {
                Object.values(texts).forEach(ele => {
                    if (elements === ele) {
                        create_emoji(element.char)
                    }
                })

            });
        });
    }

}

function create_emoji(data) {
    const root = document.getElementById('emoji-suggestions');
    var h = document.createElement("span");
    h.className = 'emoji'
    var t = document.createTextNode(data);
    h.appendChild(t);
    root.appendChild(h);
  }

$(document).on('click', '.emoji', function(e){
    $('.user-message').val($('.user-message').val() +""+ $(this).text() + " ");
});


// TODO
//Emoji Picker !!
// function emoji_picker(){
//     $(".emoji-picks").remove();
//     $.getJSON("/static/js/emojis.json", function(json) {
//         show_emoji(json)
//     });
// }
//
//
//
// function show_emoji(data){
//     Object.values(data).slice(0,500).forEach(element => {
//         const root = document.getElementById('modal-body');
//         var h = document.createElement("span");
//         h.className = 'emoji-picks'
//         var t = document.createTextNode(element.char);
//         h.appendChild(t);
//         root.appendChild(h);
//         });
// }
//
// $(document).on('click', '.emoji-picks', function(e){
//     $('.user-message').val($('.user-message').val() +""+ $(this).text());
//     $('#myModal').modal('hide');
// });
