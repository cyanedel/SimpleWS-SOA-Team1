var express = require('express');
var app = express();
var http = require('http').Server(app);
var port = 3100
const fs = require('fs');
var path = require("path");
const axios = require('axios');

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

//for testing.
app.get('/api/countrylist', function(req, res){
  let filePath = path.join(__dirname, 'countryList.json')
  let jsonList = fs.readFileSync(filePath);
  res.send(JSON.parse(jsonList))
})

//local data. to be depecrated.
app.get('/api/userlist', function(req, res){
  let filePath = path.join(__dirname, 'userList.json')
  let jsonList = fs.readFileSync(filePath);
  res.send(JSON.parse(jsonList))
})

//get data from python api instead.
app.get('/api/user/list', function(req, res){
  axios.get('http://localhost:3200/getuserlist')
    .then( response => {
      data = response.data
      res.send(data)
    })
    .catch(function (error) {
      console.log(error);
      res.send(error)
    })
})