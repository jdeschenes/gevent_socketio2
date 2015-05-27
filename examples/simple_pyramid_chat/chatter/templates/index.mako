<html>
  <head>
    <title>Chatter!</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js" type="text/javascript"></script>
    <script src="https://cdn.socket.io/socket.io-1.3.5.js"></script>
    <script src="/static/chatter.js" type="text/javascript"></script>
    <link rel="stylesheet" type="text/css" href="/static/styles.css" />
  </head>
  <body>
  <div id="container">
    <h1>Chat Log</h1>
    <div id="chatlog"></div><br />
    <form id="chat_form">
      <input type="text" id="chatbox"></input>
      <button type="submit" id="submit">Send</button>
    </form>
    <button id='join'>join</button>
  </div>
  </body>
</html>
