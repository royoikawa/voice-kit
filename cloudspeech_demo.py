#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""
import argparse
import locale
import logging
import datetime
from gtts import gTTS
from pydub import AudioSegment
from aiy.voice import audio
from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient
import mcs_api
import files

def say_start():
    say("start")
def say_shut():
    say("shut down")
def say_good():
    say("google is ready")
def say(text):
    tts = gTTS(text, lang='zh-TW') #get the word into gtts inside object
    tts.save('output.mp3') #save the words into output.mp3
    sound = AudioSegment.from_mp3('output.mp3') #read output.mp3
    sound.export('output.wav', format='wav') #save into output.wav
    audio.play_wav('output.wav') #voice kit play the wav

def get_hints(language_code):
    if language_code.startswith('zh-TW'):
        return ('我想搜索文件','會議結束')
    return None

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

def startOrder():
    d = datetime.datetime.now()
    if(d.month<10):
        if(d.day<10):
            d = str(d.year)+"0"+str(d.month)+"0"+str(d.day)
        else:
            d = str(d.year)+"0"+str(d.month)+str(d.day)
    else:
        if(d.day<10):
            d = str(d.year)+str(d.month)+"0"+str(d.day)
        else:
            d = str(d.year)+str(d.month)+str(d.day)
    pid = mcs_api.get_mcs_id()        
    pid = pid.split('*')
    #print(pid)
    d = "UploadFiles/"+d+"-"+pid[1]

    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser(description='Assistant service example.')
    parser.add_argument('--language', default=locale_language())
    args = parser.parse_args()

    logging.info('Initializing for language %s...', args.language)
    hints = get_hints(args.language)
    client = CloudSpeechClient()
    with Board() as board:
        while True:
            #if hints:
              #  logging.info('Say something, e.g. %s.' % ', '.join(hints))
            #else:
             #   logging.info('Say something.')
            text = client.recognize(language_code='zh-TW',
                                    hint_phrases=hints)
            files.to_text(d, text)
            if text is None:
                #logging.info('You said nothing.')
                if mcs_api.get_mcs_start()=='off':
                    break;
            elif '我想搜索文件' in text:
                say("start listening")
                return 'yes';
                break;
            #elif '結束' in text:
                #say("bye")
             #   return 'over';
              #  break;
            #if mcs_api.get_mcs_start()=='off':
                #return 'over';
                #break;
def speech():
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser(description='Assistant service example.')
    parser.add_argument('--language', default=locale_language())
    args = parser.parse_args()

    logging.info('Initializing for language %s...', args.language)
    hints = get_hints(args.language)
    client = CloudSpeechClient()
    with Board() as board:
        while True:
            #if hints:
                #logging.info('Say something, e.g. %s.' % ', '.join(hints))
            #else:
               # logging.info('Say something.')
            text = client.recognize(language_code='zh-TW',
                                    hint_phrases=hints)
            if text is None:
                say("you said nothing")
                #logging.info('You said nothing.')
                continue
            else:
                say('You said: "%s"' % text)
                #logging.info('You said: "%s"' % text)
                text = text.lower()
                return text
                break;
def main():
    speech()
    #say_good()
    #startOrder()
if __name__ == '__main__':
    main()
