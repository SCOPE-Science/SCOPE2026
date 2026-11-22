"""Standalone exact verification of a complete tripartite Potts field envelope.
All arithmetic is integer or rational; tests do not replace the all-size proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, factorial


def triples(n):
    for x in range(n+1):
        for y in range(n-x+1):
            z=n-x-y
            yield (x,y,z), factorial(n)//(factorial(x)*factorial(y)*factorial(z))


def exact_census(a,b,c,h):
    data=defaultdict(int)
    for aa, wa in triples(a):
        for bb,wb in triples(b):
            for cc,wc in triples(c):
                bad=sum(aa[i]*bb[i]+aa[i]*cc[i]+bb[i]*cc[i] for i in range(3))
                occupancy=aa[0]+bb[0]+cc[0]
                data[(bad,occupancy)]+=wa*wb*wc
    emin=min(Fraction(bad)-h*occ for bad,occ in data)
    return emin,{occ:sum(v for (bad,k),v in data.items()
                         if k==occ and Fraction(bad)-h*k==emin)
                 for occ in range(a+b+c+1)
                 if any(k==occ and Fraction(bad)-h*k==emin for bad,k in data)}


def predicted(a,b,c,h):
    N=a+b+c
    branches=[-h*a, Fraction(a*b)-h*(a+b),
              Fraction(a*b+a*c+b*c)-h*N]
    en=min(branches)
    if h==0:
        poly={a:0}  # all proper colorings: their favored counts are a,b,c
        for x in [a,b,c]:poly[x]=poly.get(x,0)+2
    elif h<a:
        poly={a:2}
    elif h==a:
        poly={a:2}
        for k in range(1,b):poly[a+k]=poly.get(a+k,0)+2*comb(b,k)
        for k in range(1,c):poly[a+k]=poly.get(a+k,0)+2*comb(c,k)
        poly[a+b]=poly.get(a+b,0)+2**c
        poly[a+c]=poly.get(a+c,0)+2**b
    elif h<a+b:
        poly={a+b:2**c}
    elif h==a+b:
        poly={a+b+k:comb(c,k)*2**(c-k) for k in range(c+1)}
    else:
        poly={N:1}
    return en,poly


def main():
    cases=[(3,2,1),(4,3,2),(5,4,2),(6,4,3),(7,5,2),(8,6,4)]
    total=0
    for a,b,c in cases:
        hs=[Fraction(0),Fraction(1,2),Fraction(2*a-1,2),
            Fraction(a),Fraction(2*a+1,2),
            Fraction(2*(a+b)-1,2),Fraction(a+b),
            Fraction(2*(a+b)+1,2)]
        for h in hs:
            got=exact_census(a,b,c,h)
            want=predicted(a,b,c,h)
            assert got==want,(a,b,c,h,got,want)
            total+=1
    print('EXACT_TRIPARTITE_CENSUS_PASSED',total)
    print('All displayed energies and labeled occupancy polynomials checked.')

if __name__=='__main__':main()
