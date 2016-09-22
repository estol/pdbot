from pdbot.plugins import BotPlugin


class IntroduceYourself(BotPlugin):

    TRIGGER = "bot?"

    def exec_plugin(self, command):
        return "Hi, my name is PDBOT v0.0.3, now with plugin support. Please see README.md for more!"
