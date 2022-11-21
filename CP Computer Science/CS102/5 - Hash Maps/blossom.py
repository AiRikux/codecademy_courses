class HashMap:
	def __init__(self, size):
		self.array_size = size
		self.array = [None] * self.array_size

	def hash(self, key):
		hash_code = sum(key.encode())
		return hash_code

	def compress(self, hash_code):
		return hash_code % self.array_size

	def assign(self, key, value):
		hash_code = self.hash(key)
		array_index = self.compress(hash_code)
		self.array[array_index] = [key, value]

	def retrieve(self, key):
		hash_code = self.hash(key)
		array_index = self.compress(hash_code)
		payload = self.array[array_index]

		if payload is not None:
			if payload[0] == key:
				return payload[1]

		else:
			return None
