import boto3


class CloudProcessor:
    def __init__(self):
        self.polly_client = boto3.client('polly', region_name="us-east-1")
        self.s3_client = boto3.client('s3')

    def text_to_speech(self, text, output_format='mp3', voice_id='Ruth', language="en-US", engine="generative"):
        response = self.polly_client.synthesize_speech(Text=text, OutputFormat=output_format, VoiceId=voice_id,
                                                       LanguageCode=language, Engine=engine)
        audio_stream = response['AudioStream'].read()
        return audio_stream

    def upload_to_s3(self, file_name, bucket_name, object_name=None):
        if object_name is None:
            object_name = file_name
        self.s3_client.upload_file(file_name, bucket_name, object_name)
        return f'https://{bucket_name}.s3.amazonaws.com/{object_name}'
