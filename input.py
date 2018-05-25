class Test(object):
    k = []

    def func(self, name):
        self.k.append(name)
        print(self.k)


a = Test()
a.func('jack')

b = Test()
b.func('jack')



c = Test()
c.func('jack')