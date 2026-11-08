"""Separate finite-local-enumerator check; enumerates every 2-cycle edge reversal pair, not using a closed petal classification.
Run: python local_poly_checker.py (Python standard library only)."""
from collections import Counter

def sgn(t):return (t>0)-(t<0)

def local_distributions(D, B):
    counter=Counter()
    for a in range(-B,B+1):
        for b in range(-B,B+1):
            a2=a-sgn(a)+sgn(b-a)-D
            b2=b-sgn(b)+sgn(a-b)-D
            if (sgn(a2),sgn(b2),sgn(a2-b2)) == (-sgn(a),-sgn(b),-sgn(a-b)):
                counter[sgn(a)+sgn(b)]+=1
    return counter

def coefficient_power(base, r, target):
    poly={0:1}
    for _ in range(r):
        next_poly=Counter()
        for d, n1 in poly.items():
            for t, n2 in base.items():
                next_poly[d+t] += n1*n2
        poly=next_poly
    return poly.get(target,0)

if __name__=='__main__':
    for r in range(1,15):
        total=0
        branches={}
        B=2*r+3
        for D in range(-2*r,2*r+1):
            p=local_distributions(D,B)
            c=coefficient_power(p,r,D)
            if c:branches[D]=c
            total+=c
        expected = 19 if r==1 else 3**r+2*(6*r-2)**r
        required = {-2:4,-1:4,0:3,1:4,2:4} if r==1 else {-2*r:(6*r-2)**r,0:3**r,2*r:(6*r-2)**r}
        assert total==expected and branches==required, (r,total,expected,branches)
        print(f'r={r} total={total} hub_branches={branches} PASS')
    print('LOCAL_POLYNOMIAL_PASS')
