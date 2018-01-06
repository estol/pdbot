from plugins import BotPlugin


class SampleBotPlugin(BotPlugin):

    TRIGGER = "hello SamplePlugin"

    def __init__(self):
        self.name = None

    def exec_plugin(self, command):
        return "hello I am {}".format(self.__class__)
