"""Independently compare three forms of the K_{3,b} period-three mass polynomial."""
from collections import Counter
from itertools import product
from math import comb

def add(P,Q):
    ans=Counter(P)
    for k,v in Q.items():ans[k]+=v
    return +ans

def multiply(P,Q):
    R=Counter()
    for i,a in P.items():
        for j,b in Q.items():R[i+j]+=a*b
    return {k:v for k,v in R.items() if v}

def positive_composition_polynomial(b):
    out=Counter()
    for r in range(1,b-1):
        for s in range(1,b-r):
            t=b-r-s
            P={0:1}
            for width in (r,s,t):P=multiply(P,{i:1 for i in range(width)})
            m=6*comb(b,r)*comb(b-r,s)
            for k,v in P.items():out[k]+=m*v
    return +out

def rhs_numerator(b):
    # 6*(3^b-3(2+z)^b+3(1+2z)^b-(3z)^b)
    out=Counter({0:6*3**b,b:-6*3**b})
    for k in range(b+1):
        out[k]+=18*comb(b,k)*(2**k-2**(b-k))
    return {k:v for k,v in out.items() if v}

def main():
    for b in range(3,31):
        P=positive_composition_polynomial(b)
        L=multiply(P,{0:1,1:-3,2:3,3:-1})
        assert dict(L)==dict(rhs_numerator(b)),(b,L,rhs_numerator(b))
        assert len(P)==b-2 and all(P[k]>0 and P[k]==P[b-3-k] for k in range(b-2))
        assert sum(P.values())==6*b*(b-1)*(b-2)*3**(b-3)
        assert P[0]==6*(3**b-3*2**b+3)
        # The predicted two activity classes have disjoint, sharp energy intervals.
        energies={4*b+k for k in P}|{6*b+k for k in P}
        assert energies==set(range(4*b,5*b-2))|set(range(6*b,7*b-2))
        if b in (3,4,5,8,12,20,30):
            print(f'PASS b={b}; Q(1)={sum(P.values())}; endpoint coefficient={P[0]}; support=({4*b}..{5*b-3}) union ({6*b}..{7*b-3})')
    print('ALL POLYNOMIAL CHECKS PASSED FOR b=3..30')

if __name__=='__main__':main()
