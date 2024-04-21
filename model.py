import pafy
import subprocess
import moviepy.editor as mp
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
import nltk
from sumy.summarizers.lsa import LsaSummarizer
from deep_translator import GoogleTranslator
import IPython
import noisereduce as nr
import soundfile as sf
from noisereduce.generate_noise import band_limited_noise
import urllib.request
import io
import json
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from nltk.tokenize import sent_tokenize, word_tokenize
from youtube_transcript_api import YouTubeTranscriptApi

# Youtube link to .webm conversion
def youtube_conversion(url):
    index = url.find('=')

    if index != -1:
        id=url[index + 1:]
    else:
        return None  
    outlis=[]

    tx=YouTubeTranscriptApi.get_transcript(id,languages=['en'])
    for i in tx:
      outtxt=(i['text'])
      outlis.append(outtxt)    
     
    separator=" "
    strr = separator.join(outlis)
    
    return strr


