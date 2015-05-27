$(document).ready(function () {
    // connect to the websocket
    var socket = io.connect('');

    $(window).bind("beforeunload", function () {
        socket.disconnect();
    });

    // Listen for the event "chat" and add the content to the log
    socket.on("message", function (e) {
        $("#chatlog").append(e + "<br />");
    });

    socket.on("user_disconnect", function () {
        $("#chatlog").append("user disconnected" + "<br />");
    });

    socket.on("user_connect", function () {
        $("#chatlog").append("user connected" + "<br />");
    });

    // Execute whenever the form is submitted
    $("#chat_form").submit(function (e) {
        // don't allow the form to submit
        e.preventDefault();

        var val = $("#chatbox").val();

        // send out the "chat" event with the textbox as the only argument
        socket.emit("message", val);

        $("#chatbox").val("");
    });

    $("#join").click(function (e) {
        socket.emit('join', 'test')
    })
});