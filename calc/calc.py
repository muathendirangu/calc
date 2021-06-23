"""Main module."""
from functools import reduce
class Calc:
    def add(self,*args):
        return sum(args)
    
    def sub(self,a,b):
        return a - b
    
    def mul(self,*args):
        if not all(args):
            raise ValueError
        return reduce(lambda a,b:a*b,args)
    
    def div(self, a, b):
        if not b:
            return "infinite"
        return a / b
    
    def avg(self, it, ut=None, lt=None):
        if not len(it):
            return 0
        if not ut:
            ut = max(it)
        if not lt:
            lt = min(it)
        _it = [x for x in it if x >= lt and x <= ut]
        if not _it:
            return 0
        return sum(_it)/len(_it)
    
