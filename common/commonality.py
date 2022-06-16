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

    def iterate_custom(self,list_of_items, custom_func):
        self.list_of_items = list_of_items
        self.custom_func = custom_func
        for item in list_of_items:
            custom_func(item)