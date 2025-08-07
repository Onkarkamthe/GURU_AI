from setuptools import setup, find_packages

setup(
    name='guru_assistant',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'speechrecognition',
        'pyttsx3',
        'pyaudio',
        'pocketsphinx',
        'python-dotenv',
        'nltk',
    ],
)