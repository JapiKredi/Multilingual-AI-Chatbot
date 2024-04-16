from setuptools import find_packages, setup

setup(
    name="Multilingual Assistant Chatbot",
    version="0.0.1",
    author="Jasper Bongers",
    author_email="jasper.bongers@yahoo.com",
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)