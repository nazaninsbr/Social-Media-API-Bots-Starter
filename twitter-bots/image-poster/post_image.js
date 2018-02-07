console.log("the image bot has started working");


var fs = require('fs');
var Twit = require('twit');
var config = require('./keys');
var T = new Twit(config)


tweetIt();

function tweetIt(){

	var params = {
		encoding: 'base64'
	}
	var fileName = './output.png';
	var b64content = fs.readFileSync(fileName, params);

	T.post('media/upload', {media_data: b64content},uploaded);


	function uploaded(err, data, response){
		var id = data.media_id_string;
		var tweet = {
			status: 'live from node.js',
			media_ids: [id]
		};
		T.post('statuses/update', tweet, tweeted);
	};


	function tweeted(err, data, response){
		if(err){
			console.log("somethign went wrong");
		}
		else{
			console.log("it worked!");
		}
	}
};