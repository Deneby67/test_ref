from controllers.base import Base


class Component(Base):
    method = 'test'

    def start(self, a):
        print(a)

