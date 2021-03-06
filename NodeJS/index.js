var express = require('express');
var app = express();
var http = require('http').Server(app);
var port = 3100
const fs = require('fs');
var path = require("path");
const axios = require('axios');

const ws_python = 'http://localhost:3200/';
const ws_go = 'http://localhost:3300/';
const ws_php = 'http://localhost:3400/soa-rest/';

http.listen(port, function(){
	console.log('===================');
	console.log('listening on: '+port);
	console.log('-------------------');
	console.log(' ');
});

app.use(express.static(__dirname + '/client'));
app.get('/', function(req, res){ res.sendFile(__dirname + '/index.html'); });

app.get('/ping', function(req, res){
	res.send({status: "ok", statusCode: "200"});
});

//for testing.
app.get('/api/countrylist', function(req, res){
  let filePath = path.join(__dirname, 'countryList.json')
  let jsonList = fs.readFileSync(filePath);
  res.send(JSON.parse(jsonList))
})

//python
app.get('/api/user/list', function(req, res){
  axios.get(ws_python+'/getuserlist', { params: req.query })
    .then( response => {
      data = response.data
      res.send(data)
    })
    .catch(function (error) {
      console.log(error);
      res.send(error);
    })
})

//go(lang)
app.get('/api/movie/list', function(req, res){
  axios.get(ws_go+'/getmovielist', { params: req.query })
    .then( response => {
      data = response.data
      res.send(data)
    })
    .catch(function (error) {
      console.log(error);
      res.send(error);
    })
})

//php
app.get('/api/php/list', function(req, res){
  const params = req.query;
  
  //workaround solution since PHP does not support param in JSON format.
  let apiLink = ws_php+'animal-list';
  if (params.id){
    apiLink = ws_php+'animal-list?id='+params.id
  }

  axios.get(apiLink)
    .then( response => {
      data = response.data
      res.send(data)
    })
    .catch(function (error) {
      console.log(error);
      res.send(error);
    })
})