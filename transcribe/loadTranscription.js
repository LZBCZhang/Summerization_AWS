// Load the SDK
var AWS = require('aws-sdk');
AWS.config.update({ region: 'us-east-2'});

// Initialize the transcribe service object
var transcribeService = new AWS.TranscribeService({apiVersion: '2017-10-26'});

var name = {
    TranscriptionJobName: "Example01"
};

transcribeService.getTranscriptionJob(name, function(err, data) {
    if (err) console.log(err, err.stack); // an error occurred
    else     console.log(data);           // successful response
  });