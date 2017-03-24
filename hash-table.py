class KeyValue:
	def __init__(self,key,value):
		self.key=key
		self.value=value
	def __str__(self):
		return self.key+":"+str(self.value)


class HashTable:
	SIZE=10
	def __init__(self):
		i=0
		self.list=[]
		while i<self.SIZE:
			self.list.append([])
			i=i+1

	def getValue(self,key):
		h = self.hash (key)
		bucket = self.list[h]
		for kv in bucket:
			if kv.key==key:
				return kv.value
	def setValue(self,key,value):
		h = self.hash(key)
		# should search first so we don't put key in twice, but for now ignore
		self.list[h].append(KeyValue(key,value))
	def hash(self,key):
		i=0
		total=0
		while i<len(key):
			total = total+ord(key[i])
			i=i+1
		return total % self.SIZE

htable= HashTable()
htable.setValue("wolber","359-4787")
htable.setValue("reblow","akfj-askf")
print htable.getValue("wolber")
print htable.getValue("reblow")


class HashMap(object):
    def __init__(self):
        self.hashmap = [[] for i in range(256)]

    def insert(self, key, value):
        hash_key = hash(key) % len(self.hashmap)
        key_exists = False
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key,value))

    def retrieve(self, key):
        hash_key = hash(key) % len(self.hashmap)
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            return v
        raise KeyError


H = HashMap()
H.insert(23, 'dog')
H.insert(45, 'god')
print(H.retrieve(45))
