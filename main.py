from pdfReader import PDFReader
from cloudProcessor import CloudProcessor
from emailSender import EmailSender
import os

to_email = os.getenv('LOGIN')

if __name__ == "__main__":
    pdf_file_path = 'test/pdf-sample.pdf'
    bucket_name = os.getenv('S3_BUCKET')
    audio_file_name = 'test/output.mp3'

    pdf_reader = PDFReader(pdf_file_path)
    pdf_text = pdf_reader.read_pdf()

    aws_processor = CloudProcessor()
    audio_stream = aws_processor.text_to_speech(text=pdf_text)

    with open(audio_file_name, 'wb') as audio_file:
        audio_file.write(audio_stream)

    audio_url = aws_processor.upload_to_s3(audio_file_name, bucket_name)

    print(f'{audio_url}')

    subject = 'Your Audio File'
    body = f'Your audio file is available at {audio_url}'

    email_sender = EmailSender()
    email_sender.send_email(subject, body, to_email)

    print('Process completed successfully!')
