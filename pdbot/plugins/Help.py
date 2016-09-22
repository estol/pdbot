from importlib import import_module

from pdbot import plugins
from pdbot.plugins import BotPlugin


class Help(BotPlugin):

    TRIGGER = "help"

    def exec_plugin(self, command):
        help = "Hi, my name is PDBOT. Currently I respond to:\n"
        classes = plugins.__all__
        for c in classes:
            module = import_module(c)
            class_ = getattr(module, c)
            instance = class_()
            assert isinstance(instance, plugins.BotPlugin)
            help += "{}\n".format(instance.TRIGGER)

        help += "if you mention any of the above, I'll respond... or crash. But one of the two is certain."

        return help
