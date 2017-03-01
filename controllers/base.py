class Base(object):
    method = None

    def __init__(self, service):
        self.service = service

    def __call__(self, *args, **kwargs):
        self.start(*args, **kwargs)

    def start(self, *args, **kwargs):
        raise NotImplementedError
