"""Exact supplementary checks for a three-shore defect hard-core gas."""
from fractions import Fraction
from math import comb

def formulas(n,k,z):
    t=1+z
    Z=3*t**n-2+k*z*z*(3+z)
    A=z*t**(n-1)+z*z*(2+z)
    B=z*z*(1+z)
    F=t*Z-(t**(n-1)+z*(2+z))**2
    assert B*Z-A*A == z*z*F
    return Z,A,B,F

def enumerate_sets(n,k,z):
    # Cross-shore edges persist except within k aligned triples.
    size=3*n
    forbidden=[0]*size
    for i in range(size):
        shore,idx=divmod(i,n)
        for j in range(i+1,size):
            other,idx2=divmod(j,n)
            edge= shore!=other and not(idx==idx2 and idx<k)
            if edge:
                forbidden[i]|=1<<j
                forbidden[j]|=1<<i
    Z=A=B=Fraction(0)
    for mask in range(1<<size):
        if any(mask>>i&1 and (mask & forbidden[i]) for i in range(size)):
            continue
        w=z**mask.bit_count()
        Z+=w
        a=bool(mask&1)
        b=bool(mask&(1<<n))
        if a:A+=w
        if a and b:B+=w
    return Z,A,B

def coefficients(n,k):
    # Exact binomial expansion of covariance sign polynomial F(z).
    c=[]
    C=lambda a,b:comb(a,b) if 0<=b<=a else 0
    for j in range(2*n-1):
        c.append(-C(2*n-2,j)+C(n+1,j)+2*C(n-1,j)
                 +(k-1)*C(4,j)+(2-3*k)*C(2,j)
                 +(2*k-2)*C(1,j)-(j==0))
    return c

def run():
    checks=0
    for n in range(3,6):
        for k in (1,n):
            for z in (Fraction(1,2),Fraction(2),Fraction(3,2)):
                got=enumerate_sets(n,k,z)
                expected=formulas(n,k,z)[:3]
                assert got==expected,(n,k,z,got,expected)
                checks+=3
    # Symbolic coefficients and Descartes variations over a wide exact range.
    for n in range(3,71):
        for k in range(1,n+1):
            cs=coefficients(n,k)
            assert cs[0]==0 and cs[1]==n-1
            signs=[1 if t>0 else -1 for t in cs[1:] if t]
            changes=sum(s!=t for s,t in zip(signs,signs[1:]))
            assert changes==(0 if n==3 else 1),(n,k,changes)
            if n>=4:assert cs[-1]==-1
            # Integer value of F versus coefficient polynomial.
            for z in [1,2]:
                signpoly=sum(a*z**i for i,a in enumerate(cs))
                F=formulas(n,k,z)[3]
                assert signpoly==F,(n,k,z)
                checks+=1
            checks+=3
    print('THREE_SHORE_DEFECT_CHECKS_PASSED',checks)
if __name__=='__main__':run()
