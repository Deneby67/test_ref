import inspect
import controllers
import pkgutil
import importlib


class Rpc(object):
    def __init__(self):
        self.test_parent_property = 'dsfdsf'
        for module_loader, name, ispkg in pkgutil.iter_modules(controllers.__path__):
            for _, cls in inspect.getmembers(importlib.import_module('controllers' + '.' + name, __package__),
                                             inspect.isclass):
                if cls.method is not None:
                    setattr(self, cls.method, cls(self))

    def test_parent_method(self, a=None):
        if a:
            print(a)
        else:
            print('test_parent_method')

    def test_parent_method2(self):
        self.test_parent_method('test_parent_method2')


a = Rpc()

a.test('test')
a.one()
