# ---------------------------------------- Advanced Numbers ----------------------------------------
# print(hex(246))
# print(hex(512))

# print(bin(1234))
# print(bin(128))

# print(pow(2,4))
# print(abs(2))

# print(round(3.1))
# print(round(3.14592, 2))

# ---------------------------------------- Advanced Strings ----------------------------------------
# s = 'hello world'
# print(s.capitalize())
# print(s.upper())
# print(s.lower())
# print(s.count('o'))
# print(s.find('o'))

# print(s.center(20,'z'))
# print('hello\thi')

# s = 'hello'
# print(s.isalnum())
# print(s.isalpha())
# print(s.islower())
# print(s)
# print(s.istitle())
# print(s.isupper())
# print(s.endswith('o'))
# print(s.split('e'))

# s = 'hihihihihihihi'
# print(s.split('i'))
# print(s.partition('i'))

# ---------------------------------------- Advanced Sets ----------------------------------------
# s = set()
# s.add(1)
# s.add(2)
# print(list(s))
# s.clear()

# s = {1,2,3}
# sc = s.copy()
# s.add(4)
# s.difference(sc)

# s1 = {1,2,3}
# s2 = {1,4,5}
# s1.difference_update(s2)
# print(s1)

# s.discard(2)
# print(s)

# s1 = {1,2,3}
# s2 = {1,2,4}
# s1.intersection(s2)
# # make first set equal to that intersection
# s1.intersection_update(s2)

# s1 = {1,2}
# s2 = {1,2,4}
# s3 = {5}
# print(s1.isdisjoint(s2))
# print(s1.isdisjoint(s3))

# s1.issubset(s2)
# s2.issuperset(s1)
# s1.symmetric_difference(s2)

# s1.union(s2)
# s1.update(s2)

# ---------------------------------------- Advanced Dictionaries ----------------------------------------
# d = {'k1':1, 'k2': 2}
# print({x:x**2 for x in range(10)})
# print({k:v**2 for k,v in zip(['a', 'b'], range(2))})

# print(d)
# print(d.values())

# ---------------------------------------- Advanced Lists ----------------------------------------
# l = [1,2,3]
# l.append(4)
# print(l.count(10))
# print(l.count(1))

# x = [1,2,3]
# x.append([4,5])
# print(x)

# x = [1,2,3]
# x.extend([4,5])
# print(x)

# l.index(2)
# l.insert(2, 'inserted')
# print(l)
# ele = l.pop()
# print(ele)

# l.pop(0)
# print(l)
# l.remove('inserted')
# print(l)

# l = [1,2,3,4,3]
# l.remove(3)
# print(l)

# l.reverse()
# print(l)
# l.sort()
# print(l)

# ---------------------------------------- Advanced Python Objects Assessment ----------------------------------------
print(hex(1024))
round(5.23222,2)

s = 'hello how are you Mary, are you feeling okay?'
s.islower()

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
s.count('w')

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

set1.difference(set2)
set1.union(set2)

{x:x**3 for x in range(5)}

list1 = [1,2,3,4]
list1.reverse()
list1

list2 = [3,4,2,5,1]
list2.sort()
list2