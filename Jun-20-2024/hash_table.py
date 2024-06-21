hash_map = {}

num_records = 2000

k = 1502

m = 1221
n = 1503

t = 3502


def addToHash(item):
    new_key = item
    while (new_key % num_records) in hash_map.keys():
        new_key += 1

    hash_map[new_key % num_records] = item


addToHash(k)
addToHash(m)
addToHash(n)
addToHash(t)

print(hash_map)
