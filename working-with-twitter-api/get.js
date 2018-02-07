console.log("the bot has started working");


var Twit = require('twit');
var config = require('./keys');
var T = new Twit(config)


T.get('search/tweets', { q: 'banana since:2011-07-11', count: 100 }, function(err, data, response) {
  console.log(data)
});