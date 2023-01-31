// Load the SDK
var AWS = require('aws-sdk');
AWS.config.update({ region: "eu-west-3" });

// Initialize the S3 service object
var s3 = new AWS.S3({apiVersion: '2006-03-01'});

var params = {
    Bucket: "test-transcribe-paris",
    Key: "angele-trou-story.mp3"
};

s3.getObject(params, function(error, data) {
    if (error != null) {
        console.log("Failed to retrieve an object: " + error);
      } else {
        console.log("Loaded " + data.ContentLength + " bytes");
      }
}); 