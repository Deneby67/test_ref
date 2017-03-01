from controllers.base import Base


class Two(Base):
    method = 'two'

    def start(self, *args, **kwargs):
        print(self.service.test_parent_property)
