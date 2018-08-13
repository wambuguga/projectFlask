class Dog:
        kind = 'canine'

        def __init__(self, name):
                                self.name = name


d = Dog('Fido')
e = Dog('Buddy')


x = d.kind
y = e.kind
z = d.name
a = e.name

print(x)
print(y)
print(z)
print(a)
