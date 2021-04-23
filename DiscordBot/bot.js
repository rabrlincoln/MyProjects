const Discord = require('discord.js');
const { prefix, token } = require('./auth.json');
const client = new Discord.Client();
var hangmanWord = "";
var firstCalledId;
var i =0;
var x=0;
let hiddenWord = [];
client.once('ready', () => {
	console.log('Ready!');
});

client.on('message', message => {
  if (message.channel.type === "dm") {
    message.channel.messages.fetch({limit: 2}).then(res => {
      let recent = res.first();
      let past = res.last();
      if (past.content == "Please choose a word for hangman" && past.author.bot && !recent.author.bot) {
        hangmanWord = recent.content;
				message.channel.send(`Your word is ${hangmanWord}`);
      }
    })
  }
	const args = message.content.slice(prefix.length).trim().split(/ +/);
	const command = args.shift().toLowerCase();

  if (command === 'hangman'){
	  hangmanWord = "";
		hiddenWord = [];
	  message.channel.send(`I'll dm u, ${message.author}`);
	  cluegiver = message.author;
	  cluegiver.send("Please choose a word for hangman");
	  firstCalledId = message.channel.id ;
		i = 0;
  }
	else if (command === "exithangman") {
		if (message.channel.id === firstCalledId) {
			message.channel.send('The game has been cancelled');
			cluegiver.send('The game was cancelled');
			hangmanWord = "";
			hiddenWord = [];
			i = 2;
		}
		else {
			message.channel.send("Please exit in the channel where '!hangman' was called");
		}
	}

	if (hangmanWord.length && i == 0) {
		i = 1;
		client.channels.cache.get(firstCalledId).send("The game will now begin, guess single letters or the full word");

		for (var j = 0; j< hangmanWord.length; j++) {
			hiddenWord.push("+");
		}
		console.log(hiddenWord.join(""));
		client.channels.cache.get(firstCalledId).send(hiddenWord.join(""));
	}
	if (message.channel.id === firstCalledId) {
		if (i == 1) {
			if (message.content.length == 1 && !message.author.bot){
				if(hangmanWord.includes(message.content)) {
					for (var n = 0; n< hangmanWord.length; n++) {
						if (hangmanWord.charAt(n) == message.content) {
							hiddenWord[n] = hangmanWord.charAt(n);
						}
					}
					message.channel.send(hiddenWord.join(""));
					if (!hiddenWord.includes("+")) {
						message.channel.send("YOU WONNNNN!!!");
						hangmanWord = "";
						hiddenWord = [];
						i = 2;
					}
				}
				else {
					x++;
					message.channel.send("nah thats wrong");
					message.channel.send({
	  				files: [{
	    				attachment: `./hangmanPics/hangman${x}.png`,
	    				name: `hangman${x}.png`
						}]
					})
					message.channel.send(hiddenWord.join(""));
					if (x == 8) {
						message.channel.send(`you lost, the word was ${hangmanWord}`);
						hangmanWord = "";
						hiddenWord = [];
						i = 2;
					}
				}
			}
			if (message.content.length == hangmanWord.length && !message.author.bot) {
				if(message.content == hangmanWord) {
						message.channel.send("YOU WONNNNN!!!");
						hangmanWord = "";
						hiddenWord = [];
						i = 2;
				}
				else {
						x++;
						message.channel.send("nah thats not the word");
						message.channel.send({
		  				files: [{
		    				attachment: `./hangmanPics/hangman${x}.png`,
		    				name: `hangman${x}.png`
							}]
						})
						message.channel.send(hiddenWord.join(""));
				}
			}
		}
	}
});

client.login(token);
