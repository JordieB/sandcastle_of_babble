import os
import shutil
import pytest
from unittest.mock import patch, MagicMock
from pydub import AudioSegment
from sandcastle_of_babble.pdf_to_audio import PDFToAudio
from sandcastle_of_babble.tts import Speaker


def test_valid_file():
    """
    Test PDF to audio conversion with a valid PDF file.

    This test case covers the successful scenario where a valid PDF file is 
    converted into an audio file. The existence of the audio file is verified
    after the conversion.
    """
    test_pdf_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'test.pdf')
    )
    test_output_path = 'test.mp3'

    speaker = Speaker()
    converter = PDFToAudio(test_pdf_path, test_output_path)

    try:
        converter.generate_audio_files()
        converter.concatenate_audio_files()

        assert os.path.exists(test_output_path)
    finally:
        if os.path.exists(test_output_path):
            os.remove(test_output_path)
        if os.path.exists('audio_files'):
            shutil.rmtree('audio_files', ignore_errors=True)


def test_invalid_file_path():
    """
    Test PDF to audio conversion with an invalid PDF file path.

    This test case covers the error scenario where an invalid PDF file path 
    is used for conversion. The test verifies that a FileNotFoundError is 
    raised.
    """
    converter = PDFToAudio('invalid_path.pdf', 'dummy.mp3')

    with pytest.raises(FileNotFoundError):
        converter.generate_audio_files()


def test_mocked_file_reader_and_speaker():
    with patch('sandcastle_of_babble.pdf_to_audio.PyPDF2.PdfFileReader') as mock_reader, \
         patch.object(Speaker, 'say') as mock_say, \
         patch.object(Speaker, 'save_audio') as mock_save_audio:

        mock_reader.return_value.getNumPages.return_value = 1
        mock_say.return_value = MagicMock()
        mock_save_audio.return_value = MagicMock()

        converter = PDFToAudio('dummy.pdf', 'dummy.mp3')
        converter.generate_audio_files()

        mock_reader.assert_called_once_with('dummy.pdf')
        mock_say.assert_called_once()
        mock_save_audio.assert_called_once_with(
            mock_say.return_value, 'audio_files/audio_0.wav'
        )


def test_concatenate_audio_files():
    """
    Test audio file concatenation with mocked AudioSegment.

    This test case covers the scenario where the AudioSegment.from_wav is 
    mocked to return a predefined audio segment. The test verifies that the 
    audio concatenation logic executes as expected.
    """
    with patch('sandcastle_of_babble.pdf_to_audio.AudioSegment.from_wav') \
            as mock_from_wav, \
         patch('sandcastle_of_babble.pdf_to_audio.os.listdir') \
            as mock_listdir:

        mock_from_wav.return_value = AudioSegment.empty()
        mock_listdir.return_value = ['audio_0.wav']

        converter = PDFToAudio('dummy.pdf', 'dummy.mp3')
        converter.concatenate_audio_files()

        mock_listdir.assert_called_once_with('audio_files')
        mock_from_wav.assert_called_once_with('audio_files/audio_0.wav')
