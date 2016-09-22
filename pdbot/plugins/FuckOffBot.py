from pdbot.plugins import BotPlugin

class FuckOffBot(BotPlugin):

    TRIGGER = "?"

    def exec_plugin(self, command):
        return "I may be a bot, but don't as me stupid questions like \"{}\" !!!".format(command)
