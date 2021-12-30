var express = require('express');
var app = express();
var http = require('http').Server(app);
var port = 3100
const fs = require('fs');

http.listen(port, function(){
	console.log('===================');
	console.log('listening on: '+port);
	console.log('-------------------');
	console.log(' ');
});

app.use(express.static(__dirname + '/client/src'));
app.get('/', function(req, res){ res.sendFile(__dirname + '/client/index.html'); });

app.get('/ping', function(req, res){
	res.send({status: "ok", statusCode: "200"});
});

app.get('/api/countrylist', function(req, res){
  let countryList = fs.readFileSync('countryList.json');
  res.send(JSON.parse(countryList))
})