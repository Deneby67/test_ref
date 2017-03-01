from controllers.base import Base


class One(Base):
    method = 'one'

    def start(self, *args, **kwargs):
        self.service.test_parent_method()
        self.service.test_parent_method2()

