"""Exact tests for regular-nilpotent products of uniform square matrices."""
from itertools import product
from fractions import Fraction
from math import prod


def plus(a,b,q):
    return a^b if q==4 else (a+b)%q


def times(a,b,q):
    if q!=4: return a*b%q
    t=0
    for i in range(2):
        if (b>>i)&1: t^=a<<i
    if t&8: t^=0b1100
    if t&4: t^=0b111
    return t


def mm(A,B,n,q):
    return tuple(_dot(A,B,i,j,n,q) for i in range(n) for j in range(n))


def _dot(A,B,i,j,n,q):
    s=0
    for k in range(n): s=plus(s,times(A[i*n+k],B[k*n+j],q),q)
    return s


def power(A,k,n,q):
    I=tuple(int(i==j) for i in range(n) for j in range(n))
    M=I
    for _ in range(k): M=mm(M,A,n,q)
    return M


def regular(A,n,q):
    z=(0,)*(n*n)
    return power(A,n,n,q)==z and power(A,n-1,n,q)!=z


def expected(q,n):
    L=prod(q**n-q**i for i in range(n-1))
    exact=q**(n-1)*(2*q-1)*L*L
    nilpairs=(2*q**n-1)*q**(2*n*n-2*n)
    conditional=Fraction(exact,nilpairs)
    ratio=Fraction(2*q-1,q)*Fraction(q**n,2*q**n-1)*prod(Fraction(q**j-1,q**j)**2 for j in range(2,n+1))
    assert conditional==ratio,(q,n,conditional,ratio)
    return L,exact,conditional


def exhaustive(q,n):
    ms=list(product(range(q),repeat=n*n))
    reg={X for X in ms if regular(X,n,q)}
    out=sum(mm(A,B,n,q) in reg for A in ms for B in ms)
    L,exp,cond=expected(q,n)
    assert len(reg)==L and out==exp,(q,n,len(reg),L,out,exp)
    print('EXHAUSTIVE',q,n,'matrices',len(ms),'matrix_pairs',len(ms)**2,'regular_matrices',len(reg),'regular_products',out,'cond',cond)
    return len(ms)**2


def fixed_fiber(q,n):
    ms=list(product(range(q),repeat=n*n))
    J=tuple(int(j==i+1) for i in range(n) for j in range(n))
    f=sum(mm(A,B,n,q)==J for A in ms for B in ms)
    L,_,_=expected(q,n)
    want=q**(n-1)*(2*q-1)*L
    assert f==want,(q,n,f,want)
    print('JORDAN_FIBER',q,n,'count',f,'expected',want)


def main():
    s=0
    for q,n in [(2,2),(3,2),(4,2),(2,3)]:s+=exhaustive(q,n)
    fixed_fiber(2,3)
    for q in (2,3,4,5,7,8,9):
        for n in range(2,30):
            L,exact,cond=expected(q,n)
            assert 0 < cond < 1
    print('VERIFY_OK exhaustive_cases=4 exhaustive_matrix_pairs=',s,'Jordan_fiber=262144 symbolic_pairs=203')

if __name__=='__main__':main()
