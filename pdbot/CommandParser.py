from profiler_logging import profiler_logging
import plugins as plugins


from importlib import import_module


class CommandParser:

    @profiler_logging
    def parse_command(self, command):
        answer = None
        classes = plugins.__all__
        for c in classes:
            module = import_module(c)
            class_ = getattr(module, c)
            instance = class_()
            assert isinstance(instance, plugins.BotPlugin)
            if isinstance(instance.TRIGGER, list):
                for w in instance.TRIGGER:
                    if w in command:
                        answer = instance.exec_plugin(command)
            else:
                if instance.TRIGGER in command:
                    answer = instance.exec_plugin(command)
        return answer


def main():
    parser = CommandParser()
    print(parser.parse_command("hello SamplePlugin"))


if __name__ == "__main__":
    main()
