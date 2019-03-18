#!/usr/bin/python

eng2sp = dict()
print eng2sp
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}

print eng2sp
print len(eng2sp)
print len(eng2sp['three'])
print 'one' in eng2sp
print 'uno' in eng2sp
print '\n'

vals = eng2sp.values()
print vals
print 'uno' in vals
print '\n'

print eng2sp.get('two')
print eng2sp.get('four')
print eng2sp.get('four', 0)
print '\n'

def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d

h = histogram('parrot')
print h

def print_hist(h):
	for c in h:
		print c, h[c]

h = histogram('parrot')
print_hist(h)	
print '\n'


def reverse_lookup(d, v):
	j = []
	count = 0
	for k in d:
		if d[k] == v:
			return k
	raise ValueError	
		
h = histogram('parrot')
k = reverse_lookup(h, 2)
print k		
print'\n'


def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse
	
hist = histogram('parrot')
print hist
inverse = invert_dict(hist)
print inverse
print '\n'


been_called = False
def example2():
	been_called = True

example2()
print been_called


been_called = False
def example2():
	global been_called
	been_called = True

example2()
print been_called		
print '\n'

t1 = 'a'
print type(t1)

t2 = 'a',
print type(t2)

t3 = ['a', 'b', 'c']
print type(t3)

t4 = 'a', 'b', 'c'
print type(t4)

print t4
print t4[1]
print t4[1:3] #slice function

t = ('A',) + t4[1:]
print t
print'\n'



addr = 'monty@python.org'
uname, domain = addr.split('@')
print uname
print domain

t = divmod(7, 3)
print t

quot, rem = divmod(7, 3)
print quot
print rem
print '\n'


x = 2, 3, 9, 38
def min_max(n):
	return min(x), max(x)
	
minimum, maximum = min_max(x)
print minimum
print maximum
print'\n'

def printall(*args): # gather with *
	print args
	
printall('test', 'hello', 'major')	

t = (7, 3)
print divmod(*t) # scatter with *
print'\n'

list1 =  'abc'
list2 = [0,1,2]
print zip(list1, list2)
print zip('Anne', 'Elk')


t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
	print number, letter
	
for index, element in enumerate('abc'):
	print index, element
	
print'\n'

d = {'a':0, 'b':1, 'c':2}
t = d.items()
print t		 

d = dict(zip('abc', range(3)))
print d

d = {'uno':1, 'dos':2, 'tres':3}

for key, val in d.items():
	print val, key
print '\n'

print (0, 1, 2) < (0, 3, 4)
print (0, 1, 2000000) < (0, 3, 4)

wordz = ['good', 'better', 'best', 'running riot']

def sort_by_length(words):
	t = []
	for word in words:
		t.append((len(word), word))
	t.sort(reverse=True)
	res = []
	for length, word in t:
		res.append(word)
	return res
	
print sort_by_length(wordz)	