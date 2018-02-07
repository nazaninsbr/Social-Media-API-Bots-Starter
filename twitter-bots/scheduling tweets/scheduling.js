console.log("the bot has started working");


var Twit = require('twit');
var config = require('./keys');
var T = new Twit(config)


setInterval(tweetIt, 1000*60);


function tweetIt(){

	var r = Math.floor(Math.random()*100)

	var tweet = {
		status: 'here is a random number ' + r
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
}