"""Exact finite consistency tests of the two-dimensional twisted baker spectral joint law.
Run: python check_twisted_joint.py
Requires Python 3 standard library only. Finite checks supplement the proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb

L=((2,0),(0,1))
R=((0,-2),(1,0))

def mult(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in (0,1)) for j in (0,1)) for i in (0,1))

def mv(A,v):
    return tuple(sum(A[i][k]*v[k] for k in (0,1)) for i in (0,1))

def fstep(v,b):
    x,y=v
    return (1+2*x,y) if b==0 else (1-2*y,x)

def exact_word(word):
    A=((1,0),(0,1)); b=(0,0)
    for c in word:
        J = L if c==0 else R
        b=tuple(a+v for a,v in zip(mv(J,b),(1,0)))
        A=mult(J,A)
    # (I-A)x=b
    a,c=A[0];d,e=A[1]
    P,Q,S,T=1-a,-c,-d,1-e
    det=P*T-Q*S
    assert det
    v=(Fraction(T*b[0]-Q*b[1],det),Fraction(-S*b[0]+P*b[1],det))
    z=v
    for c in word:
        x,y=z
        assert -1 <= x <= 1 and 0 <= y <= 1
        assert (x>=0)==bool(c), (word,v,z)
        z=fstep(z,c)
    assert z==v
    return A

def log2_power(q):
    q=abs(q)
    assert q>0 and q&(q-1)==0
    return q.bit_length()-1

def expected(n):
    ans=Counter()
    for j in range(n):
        g=abs(n-2*j)
        ans[(1,g,0)]+=comb(n-1,j) # complex: class=1
        ans[(0,g,g)]+=comb(n-1,j) # real: class=0; distribution matched via symmetry
    ans[(0,n,n)]-=1 # remove all-left word
    return +ans

checks=0
for n in range(1,12):
    actual=Counter()
    for word in product((0,1), repeat=n):
        if not any(word): continue
        A=exact_word(word) if n<=8 else None
        if A is None:
            A=((1,0),(0,1))
            for c in word: A=mult(R if c else L,A)
        t=sum(word)
        a,b=A[0];c,d=A[1]
        assert (a==d==0) if t%2 else (b==c==0)
        if t%2:
            assert b*c<0
            sing_gap=abs(log2_power(b)-log2_power(c))
            eig_gap=0
        else:
            assert a*d>0
            sing_gap=abs(log2_power(a)-log2_power(d))
            eig_gap=sing_gap
        actual[(t%2,sing_gap,eig_gap)]+=1
        checks+=1
    assert actual==expected(n),(n,actual,expected(n))
    assert sum(actual.values())==2**n-1
    # Marginal no defect except g=n; one difference between real/complex classes.
    for g in range(n%2,n+1,2):
        w=(comb(n,(n-g)//2) if g else comb(n,n//2)//2)
        assert actual.get((1,g,0),0)==w
        assert actual.get((0,g,g),0)==w-(g==n)
print('CHECK_OK',checks,'finite word/periodic geometry/spectrum identities across n=1..11')
