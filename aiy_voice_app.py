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
# voicemonkey assistant for digital crafts flex 2018 group project

"""A demo of the Google CloudSpeech recognizer."""
import logging
import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
from database.py import *

def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('voice monkey')
    recognizer.expect_phrase('new task')
    recognizer.expect_phrase('goodbye')

    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()

         
    
    while True:
        print('Press the button and speak')
        button.wait_for_press()
        print('Listening...')
        text = recognizer.recognize()
        if not text:
            print('Sorry, I did not hear you.')
        else:
            print('You said "', text, '"')
            if 'voice monkey' in text:
                aiy.audio.say('Hello World!')
            elif 'new task' in text:
                mytask = text.replace('new task', '', 1)
                aiy.audio.say('Task recorded.' + mytask)
                insertTask(mytask)
            elif 'goodbye' in text:
                break


if __name__ == '__main__':
    main()