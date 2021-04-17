import re
from .settings import load_setting

class Message:
    def __init__(self, msg_text, msg_from=None, source=None):
        self.msg_text = re.sub(r'\s+', ' ',msg_text.strip())
        self.msg_from = msg_from
        self.msg_source = source

        command_pfx = load_setting('command_prefix').strip()
        self.is_command=self.msg_text.startswith(command_pfx)
        if self.is_command:
            self.command = self.msg_text[len(command_pfx):].split()
        else:
            self.command = []

        if len(self.command) > 0:
            self.command[0] = self.command[0].lower()

if __name__ == "__main__":
    msg = Message('!qb hello world!')
    print(msg.command)