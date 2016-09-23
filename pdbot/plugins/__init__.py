import pkgutil


class BotPlugin(object):

    TRIGGER = None

    def exec_plugin(self, command):
        pass


__all__ = []
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    __all__.append(module_name)
    module = loader.find_module(module_name).load_module(module_name)
    exec('%s = module' % module_name)