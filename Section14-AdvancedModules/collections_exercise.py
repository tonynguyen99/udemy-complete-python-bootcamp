from collections import Counter

mylist = [1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3]

print(Counter(mylist))

print(Counter('aaaaabbbssdgysgdhsassdasaaabb'))

from collections import defaultdict

d = {'a':10}
print(d['a'])

d = defaultdict(lambda: 0)

d['correct'] = 100

print(d['wrong key'])

mytuple = (10, 20, 30)
print(mytuple[0])

from collections import namedtuple

Dog = namedtuple('Dog',['age','breed','name'])
sammy = Dog(age=5,breed='Husky',name='Sam')
print(sammy)
print(sammy.age)