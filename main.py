#! /usr/bin/python3

class Dictionary:

    def __init__(self, arrayLength=4) -> None:
        
        # Create an list with None values
        self.array = [None] * arrayLength

    def isDictionaryFull(self):

        # OBJECTIVE: Return boolean variable representing whether or not dictionary is nearly full

        # Create counter
        totalPairs = 0

        # Iterate dictionary
        for pair in self.array:

            # If "pair" is NonEmpty, increment counter
            if pair:
                totalPairs += 1

        # Return true if only 1 new key is needed to make the list full
        return totalPairs >= len(self.array) - 1

    def increaseSize(self):

        # OBJECTIVE: Increase dictionary's size by half

        print("Doubling size!")

        # Initialize dictionary class from within
        oldSize = len(self.array)
        newArray = Dictionary(oldSize * 2)

        # Iterate list
        for idx in range(oldSize):

            # If element at index is a NoneType, skip it
            if self.array[idx]:

                for elem in self.array[idx]:
                    
                    # Get original pair and add it to new list
                    newArray.addPair(elem[0], elem[1])

        # Update variable
        self.array = newArray.array

    def hashStr(self, key):

        # OBJECTIVE: Return key's index based on its hash value and length of array
        return hash(key) % len(self.array)

    def addPair(self, key, value):

        # OBJECTIVE: Add key and value pair to list

        # If list is almost full, increase its size before moving on
        if self.isDictionaryFull():
            self.increaseSize()

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

            # Replace "None" with a list
            self.array[keyIdx] = list()

            # Add values
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