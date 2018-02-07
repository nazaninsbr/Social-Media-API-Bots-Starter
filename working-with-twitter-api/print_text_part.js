console.log("the bot has started working");


var Twit = require('twit');
var config = require('./keys');
var T = new Twit(config)


var params = {
	q: 'rainbow',
	count: 4
};

T.get('search/tweets', params, gotData);


function gotData(err, data, response){
	var tweet = data.statuses;
	for(var i = 0; i < tweet.length; i++){
		console.log(tweet[i].text);
	}
};