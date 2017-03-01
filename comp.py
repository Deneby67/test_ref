class Base(object):
    method = None

    def __init__(self, service):
        self.service = service

    def __call__(self, *args, **kwargs):
        self.start(*args, **kwargs)

    def start(self, *args, **kwargs):
        raise NotImplementedError


class Component(Base):
    method = 'test'

    def start(self, a):
        print(a)


class One(Base):
    method = 'one'

    def start(self, *args, **kwargs):
        self.service.test_parent_method()
        self.service.test_parent_method2()


class Two(Base):
    method = 'two'

    def start(self, *args, **kwargs):
        print(self.service.test_parent_property)
