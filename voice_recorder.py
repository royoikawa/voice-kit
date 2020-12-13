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

import argparse
import time
import threading
import cloudspeech_demo
import mcs_api
import shutdown
import datetime
import files
import upload_file
import os


from aiy.board import Board
from aiy.voice.audio import AudioFormat, play_wav, record_file, Recorder

def record():
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', '-f', default='recording.wav')
    args = parser.parse_args()

    with Board() as board:
        #print('Press button to start recording.')
        #board.button.wait_for_press()

        done = threading.Event()
        done.set
        #board.button.when_pressed = done.set
        def wait():
            start = time.monotonic()
            while not done.is_set():
                duration = time.monotonic() - start
                print('Recording: %.02f seconds [Press button to stop]' % duration)
                #time.sleep(0.5)
                #cloudspeech_demo.speech()
                i = cloudspeech_demo.startOrder()
                if i=='yes':
                    print('happy')
                    findWords = cloudspeech_demo.speech()
                    print(findWords)
                    mcs_api.post_mcs_word(findWords)
                #elif i=='over':
                    #break;
                elif mcs_api.get_mcs_start()=='off':
                    break;
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
        print(pid)
        d = "UploadFiles/"+d+"-"+pid[1]
        record_file(AudioFormat.CD, filename=d, wait=wait, filetype='wav')
        if (mcs_api.get_mcs_start()=="off"):
            upload_file.main(is_update_file_function=bool(True), update_drive_service_folder_name='Uploaded Files', update_drive_service_name=None, update_file_path=os.getcwd() + '/UploadFiles/')
        #print('Press button to play recorded sound.')
        #board.button.wait_for_press()

        #print('Playing...')
        #play_wav(args.filename)
        print('Done.')

def shut():
    shutdown.button_shut()
    
def main():
    #thread_shut = threading.Thread(target=shut, name='ts')
    #thread_shut.start()
    #cloudspeech_demo.say_good()
    while True:
        #cloudspeech_demo.say_start()
        status = mcs_api.get_mcs_start()
        if status=="start":
            record()
        elif status=="end":
            print('end')
            mcs_api.post_mcs_done()
            #cloudspeech_demo.say_shut()
            break;
    #os.system('sudo shutdown -P now')
    
    
    
if __name__ == '__main__':
    main()