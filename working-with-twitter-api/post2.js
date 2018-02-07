console.log("the bot has started working");


var Twit = require('twit');
var config = require('./keys');
var T = new Twit(config)

var tweet = {
	status: '#rainbow #cool'
}

T.post('statuses/update', tweet, tweeted);


function tweeted(err, data, response){
	if(err){
		console.log("somethign went wrong");
	}
	else{
		console.log("it worked!");
	}
};