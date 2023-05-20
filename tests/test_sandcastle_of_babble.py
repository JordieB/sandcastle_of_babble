import os
import shutil
import pytest
from unittest.mock import patch, MagicMock
from sandcastle_of_babble.cli import main as main_cli
from sandcastle_of_babble.pdf_to_audio import PDFToAudio

# Provide a valid PDF file and check if the output MP3 file is correctly created
def test_valid_file():
    # Use the absolute path to the test PDF file
    test_pdf_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                 'test.pdf'))
    test_mp3_path = 'test.mp3'

    # Use a known good file and make sure to clean up afterwards
    converter = PDFToAudio(test_pdf_path, test_mp3_path)
    try:
        converter.generate_audio_files()
        converter.concatenate_audio_files()

        assert os.path.exists('test.mp3')
    finally:
        os.remove('test.mp3')
        shutil.rmtree('audio_files', ignore_errors=True)


# Provide an invalid PDF file path and check if the program handles the error
# gracefully
def test_invalid_file_path():
    converter = PDFToAudio('invalid_path.pdf', 'dummy.mp3')

    with pytest.raises(FileNotFoundError):
        converter.generate_audio_files()


# Mock the PyPDF2.PdfFileReader and pyttsx3.init calls to return predefined
# values and check if the program logic is executed as expected.
def test_mocked_file_reader_and_speaker():
    with patch('sandcastle_of_babble.PyPDF2.PdfFileReader') as mock_reader, \
         patch('sandcastle_of_babble.pyttsx3.init') as mock_speaker:
        mock_reader.return_value.getNumPages.return_value = 1
        mock_speaker.return_value = MagicMock()

        converter = PDFToAudio('dummy.pdf', 'dummy.mp3')
        converter.generate_audio_files()

        mock_reader.assert_called_once_with('dummy.pdf')
        mock_speaker.assert_called_once()


# Test the main function with different command line arguments
# and check if they are correctly passed to the PDFToAudio class.
def test_cli_arguments():
    with patch('sandcastle_of_babble.PyPDF2.PdfFileReader') as mock_reader, \
         patch('sandcastle_of_babble.pyttsx3.init') as mock_speaker, \
         patch('sandcastle_of_babble.AudioSegment.from_mp3') as mock_from_mp3, \
         patch('sandcastle_of_babble.os.listdir') as mock_listdir:
        mock_reader.return_value.getNumPages.return_value = 1
        mock_speaker.return_value = MagicMock()
        mock_from_mp3.return_value = MagicMock()
        mock_listdir.return_value = ['dummy.mp3']

        runner = CliRunner()
        result = runner.invoke(main_cli, ['--pdf', 'dummy.pdf', '--mp3',
                                          'dummy.mp3'])
        
        assert 'dummy.pdf' in result.output
        assert 'dummy.mp3' in result.output

        mock_reader.assert_called_once_with('dummy.pdf')
        mock_speaker.assert_called_once()
        mock_from_mp3.assert_called_once_with('audio_files/audio_0.mp3')
