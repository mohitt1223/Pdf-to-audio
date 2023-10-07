# Pdf-to-audio
My Pdf to audio translator website using flask html and mssql

This is a simple tool that allows you to convert PDF documents into audio files while also providing the option to translate the text into different languages. This README.md file provides instructions on how to use the tool and outlines its features.

Table of Contents
# Features
# Requirements
# Installation
# Usage
# Contributing
# License

# Features
> Convert PDF documents to audio files.
> Translate PDF text to different languages.
> Easy-to-use command-line interface.
> Multilingual support for translation.

# Requirements

Before you can use this tool, you'll need the following prerequisites:
> Python 3.7 or higher
> An active internet connection for translation (if required)
> The following Python libraries:
  > 'PyPDF2' for PDF processing
  > googletrans for translation
  >gTTS (Google Text-to-Speech) for audio conversion
You can install the necessary Python libraries using pip:

  pip install PyPDF2 googletrans gTTS

# Installation

Clone or download this repository to your local machine.

  git clone https://github.com/om237/Pdf-to-audio.git

  cd Pdf-to-audio

1} Make sure you have met the requirements mentioned above.
2} You are now ready to use the tool.

# Usage
To convert a PDF document to an audio file and optionally translate the text, follow these steps:

1] Open your command-line interface.

2] Navigate to the directory where you have cloned/downloaded this repository.

3] Run the following command:
   python main.py

  The tool will process the PDF, translate the text (if required), and save the audio file in the specified format and location.

# Contributing

  Contributions are welcome! If you'd like to improve this tool, fix bugs, or add new features, please open an issue or create a pull request.

# License
  This tool is licensed under the MIT License. Feel free to use, modify, and distribute it as per the terms of the license.

  You can create a new README.md file in the root directory of the "Pdf-to-audio" project on GitHub and paste this content into it. Make sure to customize the       content as needed and update any specific project details.
