class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance



obj1 = Singleton()
print('Object 1 Memory Location is ', obj1)
obj1.data = 100

