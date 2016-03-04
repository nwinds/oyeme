
import random
import datetime # simple time cost calculating tool

# get randomized generator
class TestGen(object):
    """ test case generator """
    def __init__(self, N, itemNum, inversedPercent=2, chrRange=256):
        self.N = N
        self.itemNum = itemNum
        self.inversedPercent = inversedPercent
        self.chrRange = chrRange

    def generate(self):
        lst = []
        for i in range(self.N):
            r = random.randrange(self.itemNum)
            items = [j for j in range(r)]
            random.shuffle(items)
            subDict = {}
            for item in items:  # 1/self.inversedPercent of total items include '_id', lets rock !
                if item % self.inversedPercent == 0:
                    subDict['_id'] = item
                else:
                    subDict[ chr(item % self.chrRange) ] = item
            lst.append(subDict)
        return lst


# test
tg = TestGen(100,90)
lst = tg.generate()
d0 = datetime.datetime.now()

# a matter of algorithm
lst = [ {k: v for k, v in dct.items() if k != '_id' } for dct in lst]

d1 = datetime.datetime.now()
delta = d1 - d0
print('lst(%d*%d) time cost = %s' % (tg.N, tg.itemNum , str(delta))) # in numpy we use npArray.size() to get (x,y,z,... ,n) axis
