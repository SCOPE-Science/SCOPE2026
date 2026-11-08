"""Exact rational verification of finite-round synchronous pull on K_{a,b}.

Run: python3 verify_pull.py. No external dependencies.
"""
from fractions import Fraction as F
from math import comb
from functools import lru_cache


def two_round_probability(a, b):
    """Start informed in the a-vertex part; a,b positive integers."""
    if a == 1:
        return F(1)
    return sum((F(comb(b,j), a**b * b**(a-1))
                * j**(a-1) * F(a-1,a)**(b-j))
               for j in range(b+1))

@lru_cache(None)
def transition(a, b, i, j):
    """Exact one-round law for (informed in A, informed in B)."""
    assert 1 <= a and 1 <= b and 0 <= i <= a and 0 <= j <= b
    dist = {}
    for h in range(a-i+1):
        ph = F(comb(a-i,h)) * F(j,b)**h * F(b-j,b)**(a-i-h)
        for k in range(b-j+1):
            pk = F(comb(b-j,k)) * F(i,a)**k * F(a-i,a)**(b-j-k)
            if ph * pk:
                dist[i+h, j+k] = ph * pk
    assert sum(dist.values()) == 1
    return dist


def distribution(a, b, source_a, rounds):
    distribution = {(1,0):F(1)} if source_a else {(0,1):F(1)}
    for _ in range(rounds):
        new = {}
        for (i,j),mass in distribution.items():
            for (h,k),prob in transition(a,b,i,j).items():
                new[h,k] = new.get((h,k), F(0)) + mass*prob
        distribution = new
        assert sum(distribution.values()) == 1
    return distribution


def check():
    checks=0
    # Independent formula agrees with Markov recurrence on all smaller pairs.
    for s in range(3,12):
        for a in range(1, s//2+1):
            b=s-a
            if a >= b:
                continue
            x=two_round_probability(a,b)
            y=two_round_probability(b,a)
            if s <= 10:
                assert x>y,(a,b,x,y)
                checks+=1
            elif (a,b)==(5,6):
                assert x<y
                checks+=1
            else:
                assert x>y
                checks+=1
            if s<=8 or (a,b)==(5,6):
                assert distribution(a,b,True,2).get((a,b),F(0))==x
                assert distribution(a,b,False,2).get((a,b),F(0))==y
                checks+=2

    # Critical counterexample and exact, irreducible certificates.
    a,b=5,6
    two_a=distribution(a,b,True,2).get((a,b),F(0))
    two_b=distribution(a,b,False,2).get((a,b),F(0))
    three_a=distribution(a,b,True,3).get((a,b),F(0))
    three_b=distribution(a,b,False,3).get((a,b),F(0))
    assert two_a==F(37053,97656250)
    assert two_b==F(480389,1259712000)
    assert three_a==F(207876362387783,4449462890625000)
    assert three_b==F(188835022260049,6122200320000000)
    assert two_a-two_b==F(-947518181,492075000000000)
    assert three_a-three_b==F(949127700048257234999,59787112500000000000000)
    checks+=6
    print('CERTIFICATE t2 A,B:',two_a,two_b)
    print('CERTIFICATE t3 A,B:',three_a,three_b)
    print('STRICT CROSSING differences:',two_a-two_b,three_a-three_b)
    print('VERIFY_OK',checks,'exact checks')

if __name__=='__main__':
    check()
