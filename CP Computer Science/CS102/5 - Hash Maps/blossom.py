from linked_list import Node, LinkedList
from blossom_lib import flower_definitions


class HashMap:
	def __init__(self, size):
		self.array_size = size
		self.array = [LinkedList() for i in range(self.array_size)]  # [None*self.array_size]

	def hash(self, key):
		self.hash_code = sum(key.encode())
		return self.hash_code

	def compress(self, hash_code):
		return hash_code % self.array_size

	def assign(self, key, value):
		hash_code = self.hash(key)
		array_index = self.compress(hash_code)
		# remove it and replace with list_at_array.insert()
		# self.array[array_index] = [key, value]

		payload = Node([key, value])
		list_at_array = self.array[array_index]

		for item in list_at_array:
			if item[0] == key:
				# if we find a key item that is the same as the key were trying to assign
				# we replace
				item[1] = value
				return
		list_at_array.insert(payload)

	def retrieve(self, key):
		hash_code = self.hash(key)
		array_index = self.compress(hash_code)

		list_at_index = self.array[array_index]

		# make a marker to see if we found the same key
		found = False
		for item in list_at_index:
			if item[0] == key:
				# if we find a key item that is the same as the key were trying to assign
				return item[1]
			else:
				return None

	# payload = self.array[array_index]

	# if payload is not None:
	#  if payload[0] == key:
	#    return payload[1]

	# else:
	#  return None


# see it in action
# create hashmap with the same length as how many types of flowers there are
blossom = HashMap(len(flower_definitions))
# assign for each flower
for flower in flower_definitions:
	blossom.assign(flower[0], flower[1])
# retrieve something
print(blossom.retrieve('daisy'))
