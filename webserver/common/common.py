import re


class fun():

    def getDigitStr(self,str):
        num = re.sub(r'\D',"",str)
        return num