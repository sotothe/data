import json

class Data:
    def __init__(self):
        pass

    def __str__(self):
        return f'<< {self.__dict__} >>'

    @classmethod
    def create(cls, **kwargs):
        cls.objects.append(cls(**kwargs))
        cls.save()

    @classmethod
    def find(cls, **kwargs):
        for i in cls.objects:
            if kwargs.items() <= i.__dict__.items():
                return i

    def update(self, **kwargs):
        cls = self.__class__
        data = self.__dict__
        data.update(kwargs)
        cls.objects.remove(self)
        cls.objects.append(cls(**data))
        cls.save()

    def delete(self):
        cls = self.__class__
        cls.objects.remove(self)
        cls.save()

    @classmethod
    def save(cls):
        lst = [i.__dict__ for i in cls.objects]
        with open(f'db/{cls.__name__}.json', 'w') as f:
            json.dump(lst, f, indent=4)

    @classmethod
    def load(cls):
        try:
            with open(f'db/{cls.__name__}.json', 'r') as f:
                lst = json.load(f)
            cls.objects = [cls(**i) for i in lst]
        except:
            pass
