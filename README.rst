====================
Sandcastle of Babble
====================


.. image:: https://img.shields.io/pypi/v/sandcastle_of_babble.svg
        :target: https://pypi.python.org/pypi/sandcastle_of_babble

.. image:: https://img.shields.io/travis/JordieB/sandcastle_of_babble.svg
        :target: https://travis-ci.com/JordieB/sandcastle_of_babble

.. image:: https://readthedocs.org/projects/sandcastle-of-babble/badge/?version=latest
        :target: https://sandcastle-of-babble.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


"SandcastleOfBabble: Turning Pages into Prattle" is an innovative Python application that transforms the written text of PDF documents into engaging audio content. By seamlessly combining powerful libraries like PyPDF2, pyttsx3, and pydub, SandcastleOfBabble enlivens the often monotonous task of reading through pages, turning them into delightful auditory prattle. Whether you're wanting to consume a novel while on the move or convert educational materials for easier understanding, SandcastleOfBabble offers a convenient solution. It's time to let your books babble!


* Free software: MIT license
* Documentation: https://sandcastle-of-babble.readthedocs.io.


Usage
-----

To use SandcastleOfBabble, follow these steps:

1. Install system dependencies by running the following command in the project directory:

.. code-block:: bash

    ./install_dependencies.sh

This will install the necessary system-level package `python3-pyaudio`.

2. Set up the Python environment and install project dependencies using Poetry. Run the following command:

.. code-block:: bash

    poetry install

This will create a virtual environment and install the required Python packages.

3. Once the dependencies are installed, you can run SandcastleOfBabble by navigating to the project directory and executing the following command:

.. code-block:: bash

    python -m sandcastle_of_babble.cli --pdf /path/to/your/pdf --mp3 /path/to/output/mp3

Replace `/path/to/your/pdf` with the path to the PDF file you wish to convert, and `/path/to/output/mp3` with the desired output path for the resulting MP3 file.

Running Tests
-------------

To run tests, navigate to the project directory and run the following command:

.. code-block:: bash

    pytest

This will execute all tests within the `tests` directory.

Features
--------

* Converts text from PDF files into MP3 audio
* Provides command-line interface for ease of use
* Handles errors gracefully and provides informative feedback to the user

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage






