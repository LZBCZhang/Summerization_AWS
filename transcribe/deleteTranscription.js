// Load the SDK
var AWS = require('aws-sdk');
AWS.config.update({ region: 'us-east-2'});

// Initialize the transcribe service object
var transcribeService = new AWS.TranscribeService({apiVersion: '2017-10-26'});

var params = {
    TranscriptionJobName: "Example01"
  };
  transcribeService.deleteTranscriptionJob(params, function(err, data) {
    if (err) console.log(err, err.stack); // an error occurred
    else     console.log(data);           // successful response
  });