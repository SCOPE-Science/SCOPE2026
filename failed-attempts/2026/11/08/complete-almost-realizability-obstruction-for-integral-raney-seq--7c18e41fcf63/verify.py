"""Independent finite arithmetic check for the Raney Dold obstruction."""
from math import comb

def raney(P,R,n):
    num=R*comb(P*n+R,n)
    den=P*n+R
    assert num%den==0
    return num//den

def primes(a,b):
    return [x for x in range(a,b) if x>=2 and all(x%d for d in range(2,int(x**0.5)+1))]

checks=0
for P in range(1,8):
    for R in range(1,P+4):
        assert raney(P,R,1)==R
        assert raney(P,R,2)==R*(2*P+R-1)//2
        for ell in primes(17,60):
            if ell<=2*P+R:continue
            a1,a2=raney(P,R,1),raney(P,R,2)
            ax,ay=raney(P,R,ell),raney(P,R,2*ell)
            assert ax%ell==P%ell
            assert ay%ell==(P*(2*P-1))%ell
            assert (ax-a1)%ell==(P-R)%ell
            if R==P:
                assert (ay-ax-a2+a1)%ell==(P*(P-1)//2)%ell
            checks+=1
assert all(raney(1,1,n)==1 for n in range(1,100))
print('Raney exact-binomial and Lucas congruences: PASS')
print('Parameter range: 1 <= P <= 7, 1 <= R <= P+3')
print('Test primes: 17 <= ell < 60, ell > 2P+R')
print('Congruence checks:',checks)
print('Exceptional family (1,1) constant through n=99: PASS')
print('Infinite theorem uses Lucas and Dold; finite checks are supplementary.')
