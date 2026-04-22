# accessing of lists
a = [10, 20, 30, 40, 50]
print(a[0])
print(a[-1])

# adding elements to a list
a = [10, 20, 30, 40, 50]
a.append(100)
print(a)
a.insert(1, 50)
print(a)

# removing elements from list
a = [10, 20, 30, 40, 50]
a.remove(40)
print(a)
a.pop()
print(a)

# slicing
a = [10, 20, 30, 40, 50]
print(a[0:])
print(a[2:])

t = (10, 20, 30, 40, 50)
print(t)
t1 = tuple((10, 20, 30, 40, 50))
print(t[0])
print(t[-1])
print(t + t1)
print(tuple([t] + [t1]))
print(t * 3)  # error
print(t[0:])
print(t1[1:3])
del t
# print(t)  # error - removed to avoid undefined name

d = {"name": "John", "age": 30, "city": "New York"}
print(d)
d1 = dict(name="John", age=30, city="New York")
print(d1)
print(d["name"])
print(d.get("name"))
print(d.keys())
print(d.values())
print(d1.get("city"))
d1['name'] = 'krishna'

d = {"name": "krishna", "age": 30, "city": "New York"}
print(d)
del d
# print(d) - removed to avoid undefined name

val = d1.pop('age')
print(val)
print(d1)

d1.clear()
print(d1)
