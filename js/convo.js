var botui = new BotUI('api-bot');
//socket opening for connection with server
var socket = io.connect('http://127.0.0.1:1024');

//sending message to server 
 socket.emit('new_connection', function(){
 	/*botui.message.add({
 		content:'new content',
 	});*/
 	console.log('new connection');
 });

//receiving message from server
 socket.on('message',function(msg){
 	botui.message.add({
 		content:msg,
 	});
 	botui.action.text({
  action: {
    placeholder: 'Enter your text here'
  }
}).then(function (res) { // will be called when it is submitted.
	socket.send(res.value)
  console.log(res.value); // will print whatever was typed in the field in browser console.
}).then(function (res) {	
	socket.send(res.value);
});
 	console.log('msg is ' + msg);
 });




