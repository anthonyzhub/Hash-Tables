#! /usr/bin/python3

class Dictionary:

    def __init__(self, arrayLength=4) -> None:
        
        # Create an array with None values
        self.array = [None] * arrayLength

    def hashStr(self, key):

        # OBJECTIVE: Return key's index based on its hash value and length of array
        return hash(key) % len(self.array)

    def addPair(self, key, value):

        # OBJECTIVE: Add key and value pair to list

        # Get key's potential index
        keyIdx = self.hashStr(key)

        # Check if element at keyIdx exist
        if self.array[keyIdx]:

            # Iterate list
            keyExist = False
            for elem in self.array[keyIdx]:

                # If "key" was found, update value
                if elem[0] == key:
                    elem[1] = value
                    keyExist = True
                    break

            # If key doesn't exist, add a new pair to list
            if keyExist == False:
                self.array[keyIdx].append([key, value])

        # Execute if index inside list is empty
        else:

            self.array[keyIdx] = list()
            self.array[keyIdx].append([key, value])

    def getValue(self, key):

        # OBJECTIVE: Return key's value if it exist

        # Get key's potential index
        keyIdx = self.hashStr(key)

        # Check if element at keyIdx exist
        if self.array[keyIdx]:

            # Iterate list
            for elem in self.array[keyIdx]:

                # If key was found, exit function
                if elem[0] == key:
                    return elem[1]

            # If for-loop couldn't find key, raise error
            raise KeyError()

        # In case key doesn't exist
        else:

            raise KeyError()
if __name__ == "__main__":
    
    dictionaryClass = Dictionary()

    # Add pairs to dictionary
    dictionaryClass.addPair("Apple", 1)
    dictionaryClass.addPair("Banana", 1)
    dictionaryClass.addPair("Cherry", 3)

    # Get pairs from dictionary
    print(dictionaryClass.getValue("Apple"))
    print(dictionaryClass.getValue("Banana"))
    print(dictionaryClass.getValue("Cherry"))
    print(dictionaryClass.getValue("Date"))