from pdbot import profiler_logging
import pdbot.plugins as plugins


from importlib import import_module


class CommandParser:


    @profiler_logging
    def parse_command(self, command):
        answer = "Sorry, I don't even feel like I should know how to respond to that.\nTry @pdbot help"
        classes = plugins.__all__
        for c in classes:
            module = import_module(c)
            class_ = getattr(module, c)
            instance = class_()
            assert isinstance(instance, plugins.BotPlugin)
            if instance.TRIGGER in command:
                answer = instance.exec_plugin(command)


        return answer



def main():
    parser = CommandParser()
    print(parser.parse_command("hello SamplePlugin"))



if __name__ == "__main__":
    main()
