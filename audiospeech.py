import speech_recognition as sr
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import speech_recognition as sr
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

#import nltk
#nltk.download('punkt')

def transcribe_audio(path):
    """
    This function takes an audio file path and returns the transcript.
    """
    r = sr.Recognizer()
    with sr.AudioFile(path) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
    return text

def summarize_text(text):
    """
    This function takes a text and returns a summarized version of it.
    """
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentences_count=3)  # specify the number of sentences in the summary
    return " ".join([str(sentence) for sentence in summary])

def main():
    audio_path = r"C:\Users\vaishali\Downloads\ttsMP3.com_VoiceText_2024-6-4_17-56-12.aiff"  # replace with your audio file path
    transcript = transcribe_audio(audio_path)
    print("Transcript:")
    print(transcript)
    summary = summarize_text(transcript)
    print("\nSummary:")
    print(summary)

if __name__ == "__main__":
    main()
