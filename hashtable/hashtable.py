class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

MIN_CAPACITY = 8

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        if self.capacity < 8:
            self.capacity = 8            
        self.array = [None] * self.capacity
        self.load = 0
        self.loadFactor = self.load / self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # TODO

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # TODO

    def djb2(self, key):
        hash = 5381
        byte_array = key.encode('utf-8')

        for byte in byte_array:
            hash = ((hash * 33) ^ byte) % 0x100000000

        return hash % 8

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        index = self.djb2(key)
        if self.array[index] is not None:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    kvp[1] = value
                    break
                else:
                    self.array[index].append([key, value])
        # Store the value with the given key
        else:
            self.array[index] = []
            self.array[index].append([key, value])


    def delete(self, key):
        index = self.djb2(key)
        # If the key is not found,
        if self.array[index] is None:
            # Prints a warning if the key is not found
            return KeyError()
        else:
            # Remove the value stored with the given key.
            for i in list(range(len(self.array[index]))):
                if self.array[index][i][0] == key:
                    del self.array[index][i][0]


    def get(self, key):
        index = self.djb2(key) % self.capacity
        # Returns None if the key is not found
        if self.array[index] is None:
            return None
        # Retrieve the value stored with the given key
        else:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # TODO



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")