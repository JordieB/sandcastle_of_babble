import os
from typing import List, Optional
import PyPDF2
from pydub import AudioSegment

from sandcastle_of_babble.tts import Speaker


class PDFToAudio:
    """
    A class that converts PDF files to audio using a TTS converter.
    """

    def __init__(self, pdf_path: str, output_path: str):
        """
        Initializes PDFToAudio with paths for PDF and output files.

        Parameters:
        pdf_path (str): Path to the input PDF file.
        output_path (str): Path to the output MP3 file.
        """
        self.pdf_path = pdf_path
        self.output_path = output_path
        self.speaker = Speaker()

    def generate_audio_files(self, start_page: Optional[int] = None,
                             end_page: Optional[int] = None):
        """
        Reads the PDF file, extracts text, converts each page to audio.

        Stores the audio files in the 'audio_files' directory.

        Parameters:
        start_page (int, optional): The starting page number for conversion.
        end_page (int, optional): The ending page number for conversion.
        """
        if not os.path.exists('audio_files'):
            os.makedirs('audio_files')

        with open(self.pdf_path, 'rb') as pdf_file:
            read_pdf = PyPDF2.PdfReader(pdf_file)

            total_pages = len(read_pdf.pages)

            start_page = 0 if start_page is None else start_page
            end_page = total_pages if end_page is None else end_page

            for page_number in range(start_page, end_page):
                page = read_pdf.pages[page_number]
                text = page.extract_text()
                print(f"Processing page {page_number + 1}/{total_pages}")

                audio_output = self.speaker.say(text)
                self.speaker.save_audio(
                    audio_output, f'audio_{page_number}.wav')

    def concatenate_audio_files(self):
        """
        Concatenates the audio files generated by generate_audio_files into
        a single MP3 file using pydub.
        """
        audio_files = sorted(os.listdir('audio_files'))
        combined = AudioSegment.empty()

        for audio_file in audio_files:
            audio_path = os.path.join('audio_files', audio_file)
            audio = AudioSegment.from_wav(audio_path)
            combined += audio

        combined.export(self.output_path, format='mp3')
