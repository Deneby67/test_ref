import inspect
import comp


class Rpc(object):
    def __init__(self):
        self.test_parent_property = 'dsfdsf'
        for _, cls in inspect.getmembers(comp, inspect.isclass):
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
