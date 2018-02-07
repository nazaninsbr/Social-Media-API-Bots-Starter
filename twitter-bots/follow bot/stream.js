console.log("the follow bot has started working");


var Twit = require('twit');
var config = require('./keys');
var T = new Twit(config)


var stream = T.stream('user');

stream.on('follow', followed);


function followed(eventMsg){
	var name = eventMsg.source.name;
	var screenName = eventMsg.source.screen_name;
	tweetIt('@'+screenName+' do you like ice cream?');
};


function tweetIt(txt){

	var tweet = {
		status: txt
	}

	T.post('statuses/update', tweet, tweeted);


	function tweeted(err, data, response){
		if(err){
			console.log("somethign went wrong");
		}
		else{
			console.log("it worked!");
		}
	}
};