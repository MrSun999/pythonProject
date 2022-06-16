# -- ** -- UTF-8
from collections import Counter
import random


class commonality():

    def anagram(self, first, second):
        return Counter(first) == Counter(second)

    def rdms(self,num):
        rdms = []
        for i in range(2000):
            rdms.append(random.randint(111,9999))
        rds = list(set(rdms))[:num]
        return rds