"""Finite exact-rational checks of the normalized row-profile construction."""
from fractions import Fraction
from itertools import product

def norm_lorentz(x,weights):
    v=sorted((abs(a) for a in x), reverse=True)
    return sum((z*w for z,w in zip(v,weights)), Fraction())

def norm_X(rows,weights):
    return norm_lorentz([sum(map(abs,r)) for r in rows],weights)

def check():
    weights=[Fraction(1,i+1) for i in range(7)]
    m=[2,3,2,4]
    checks=0
    for row in range(4):
        t=[[Fraction(0) for _ in range(k)] for k in m]
        for i in range(m[row]): t[row][i]=Fraction(1,m[row])
        assert norm_X(t,weights)==1
        checks+=1
    for vals in product(range(-2,3), repeat=4):
        ts=[]
        for row,k in enumerate(m):
            ts.append([Fraction(vals[row],k)]*k)
        assert norm_X(ts,weights)==norm_lorentz([Fraction(v) for v in vals],weights)
        checks+=1
    print('FINITE_ROW_PROFILE_IDENTITIES_OK',checks)
if __name__=='__main__':check()
