// Load the SDK
var AWS = require('aws-sdk');
AWS.config.update({ region: 'eu-west-3'});

// Initialize the transcribe service object
var transcribeService = new AWS.TranscribeService({apiVersion: '2017-10-26'});

var params = {
    LanguageCode: "fr-FR", // en-US for english audio
    Media: {
        MediaFileUri: "https://test-transcribe-paris.s3.eu-west-3.amazonaws.com/Enregistrement.wav"
    },
    MediaFormat: "wav", // mp3 | mp4 | flac
    TranscriptionJobName: "Example01",
    // MediaSampleRateHertz: , // Between 8000 and 48000
    OutputBucketName: "test-transcribe-paris",
    Settings: {
        ChannelIdentification: false,
        MaxSpeakerLabels: 2,
        ShowSpeakerLabels: true,
        // VocabularyName: ""
    }
};

transcribeService.startTranscriptionJob(params, function(err, data) {
  if (err) console.log(err, err.stack); // an error occurred
  else     console.log(data);           // successful response
}); 