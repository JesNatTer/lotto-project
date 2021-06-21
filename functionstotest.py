class TestFunctions:
    def lotto(self, entry1, randomset1):
        count = 0
        entry = entry1
        randomset = randomset1
        for x in range(3):
            if entry[x] == randomset[x]:
                count += 1
        return count
