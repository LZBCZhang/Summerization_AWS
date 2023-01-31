// Load the SDK
var AWS = require('aws-sdk');
AWS.config.update({ region: "eu-west-3" });

// Initialize the S3 service object
var s3 = new AWS.S3({apiVersion: '2006-03-01'});

var fs = require('fs');
var path = require('path');

var uploadParams = {
    Bucket: "test-bucket-api-0001", 
    Key: '', 
    Body: ''
};
var file = "test.txt";

var fileStream = fs.createReadStream(file);
fileStream.on('error', function(err) {
  console.log('File Error', err);
});

uploadParams.Body = fileStream;
uploadParams.Key = path.basename(file);

s3.upload (uploadParams, function (err, data) {
  if (err) {
    console.log("Error", err);
  } if (data) {
    console.log("Upload Success", data.Location);
  }
});