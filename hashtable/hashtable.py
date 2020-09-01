class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = MIN_CAPACITY
        self.table = [None] * capacity
        self.num_of_items = 0
        self.head = None


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        num_of_slots = len(self.table)
        return num_of_slots


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        
        return self.num_of_items / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        ### FNV-1
        seed = 0
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037
        hash = offset_basis + seed
        for char in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(char)
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here 
        ## DJB2
        h = 5381
        for c in key[1:]:
            h = (h << 5) + h + ord(c)
        return h



    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        ## Your code here
        indx = self.hash_index(key)
        # self.table[indx] = value
        # new_node = HashTableEntry(key, value)

        ### Day 2

        # if self.get_load_factor() > 0.7:
        #     self.resize(self.capacity)

        if self.table[indx] == None:
            self.table[indx] = HashTableEntry(key, value)
            self.num_of_items += 1
        else: 
            cur = self.table[indx]
            while True:
                if cur.key == key:
                    cur.value = value
                    return 
                if cur.next == None: break
                cur = cur.next
            cur.next = HashTableEntry(key, value)



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # # Your code here
        indx = self.hash_index(key)
        # if self.table[indx] != None:
        #     self.table[indx] = None
        # if not self.table[indx]:
        #     return "Key not found"

        ### Day 2
        cur = self.table[indx]
        prev = cur
        if cur is None:
            return None
        # special case: delete the head
        if cur.key == key:
            old_head = self.table[indx]
            self.table[indx] = cur.next
            return old_head
        # general case
        prev = cur
        cur = cur.next
        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                return cur
            prev = cur
            cur = cur.next
        return None
            
        


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # # Your code here
        # indx = self.table[self.hash_index(key)]
        # if indx:        
        #     return indx
        # else:
        #     return None
        ind = self.hash_index(key)
        cur = self.table[ind]
        
        while cur:
            if cur.key == key:
                return cur.value
            else:
                cur = cur.next
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
 
        Implement this.
        """
        # Your code here
        
        self.capacity  = new_capacity
        self.table = [None] * self.capacity
       



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
