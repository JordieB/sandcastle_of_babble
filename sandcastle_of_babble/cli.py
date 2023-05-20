import sys
import click
from sandcastle_of_babble.pdf_to_audio import PDFToAudio


@click.command()
@click.option('--pdf', default='novel.pdf', help='The path to the PDF file.')
@click.option('--mp3', default='combined.mp3',
              help='The path to the output MP3 file.')
def main(pdf: str, mp3: str):
    """
    Main function that creates a PDFToAudio object and converts a PDF to audio.

    Parameters:
    pdf (str): Path to the input PDF file.
    mp3 (str): Path to the output MP3 file.
    """

    converter = PDFToAudio(pdf, mp3)
    converter.generate_audio_files()
    converter.concatenate_audio_files()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
