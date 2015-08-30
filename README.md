# yowsup-queue
This Project provides a interface to yowsup2. You can Send/Receive Whatsapp-Messages with any language of your choice. 

###Installation:

Install & Configure the yowsup2 CLI Demo. Use yowsup-cli to register a Number. 
Install or use a Beanstalkd Server. 

###Configuration:

rename "config.sample.ini" to "config.ini" and put your credentials into it.

###Usage:

Run the Project with:
```
python3 run.py 
```

You will get the Messages from Whatsapp into the Queue "whatsapp-receive".

Put the messages you want to send into the "whatsapp-send" Queue. The Format of the Messages is JSON:

Example Messages:


Simple Message to a receiver:

```
	{"type":"simple","body":"This is a Test-Message!","address":"+12345678"}
```

###Known Issues:

Sometimes the keys are not synced. You will get Errors like this: 
```
	Exception: No such signedprekeyrecord!
```
Fix it using:
```
	rm -r ~/.yowsup/
	(deleted the yowsup database)
```

