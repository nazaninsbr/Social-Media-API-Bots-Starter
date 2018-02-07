console.log("the bot has started working");


var Twit = require('twit');
var config = require('./keys');
var T = new Twit(config)



T.post('statuses/update', { status: 'hello world!' }, function(err, data, response) {
  console.log(data)
})