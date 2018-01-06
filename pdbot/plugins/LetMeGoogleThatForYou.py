from plugins import BotPlugin
import re


class LetMeGoogleThatForYou(BotPlugin):

    TRIGGER = "google"

    def exec_plugin(self, command):
        pattern = re.compile(r'google\s*(.+)$')
        match = re.match(pattern, command)
        if match:
            query = match.group(1).replace(' ', '+')
            return "Let me google that for you: https://google.com/#q={}".format(query)
