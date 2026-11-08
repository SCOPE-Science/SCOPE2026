"""Exact rational absorption probabilities for asynchronous majority on K_2 join independent set."""
from fractions import Fraction
from functools import lru_cache
from math import ceil


def derived(s, x, y, j):
    r = (s - 1 + 1)//2  # ceil((s-1)/2)
    def same_one(z):
        if z >= r:
            return Fraction(1)
        return Fraction((s-r+2)*(s-r+1), (s-z+2)*(s-z+1))
    if x == y == 1:
        return same_one(j)
    if x == y == 0:
        return 1 - same_one(s-j)
    if 2*j > s:
        return Fraction(1)
    if 2*j < s:
        return Fraction(0)
    return Fraction(1,2)


def markov(s):
    @lru_cache(None)
    def p(x,y,j):
        if x == y == 0 and j == 0: return Fraction(0)
        if x == y == 1 and j == s: return Fraction(1)
        # Excluding null picks, select among precisely the opinion-changing vertices.
        moves=[]
        for hub,own,other in [(0,x,y),(1,y,x)]:
            ones = other+j
            zeros = 1-other+s-j
            new = 1 if ones>zeros else 0 if zeros>ones else own
            if new!=own:
                moves.append(((new,y,j) if hub==0 else (x,new,j), 1))
        if x == y == 1 and j < s:
            moves.append(((x,y,j+1),s-j))
        if x == y == 0 and j > 0:
            moves.append(((x,y,j-1),j))
        if not moves:
            raise AssertionError(('nonconsensus stable',s,x,y,j))
        t=sum(weight for _,weight in moves)
        return sum(Fraction(weight,t)*p(*state) for state,weight in moves)
    for x in (0,1):
      for y in (0,1):
       for j in range(s+1):
        got=p(x,y,j); expect=derived(s,x,y,j)
        assert got==expect,(s,x,y,j,got,expect)
    return p(1,1,0)

if __name__=='__main__':
    for s in list(range(1,31))+[40,49,50,99,100]:
        result=markov(s)
        if s <= 12 or s in (30,50,99,100):print(f's={s}: P(two one-hubs win against all zero leaves)={result}')
    print('PASS: 35 full rational count-state kernels, including all hub opinions and leaf counts.')
