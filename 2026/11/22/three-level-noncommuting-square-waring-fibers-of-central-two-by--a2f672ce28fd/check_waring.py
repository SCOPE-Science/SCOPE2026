#!/usr/bin/env python3
"""Independent finite-field checks for scalar square-Waring noncommuting fibers.
Only uses the Python standard library. No paper text is bundled."""
from itertools import product
from collections import Counter

class Field:
    def __init__(self, q):
        self.q=q
        self.prime=(q!=9)
        if not self.prime: assert q==9
        self.inv2 = (q+1)//2 if self.prime else 2 # GF(9) has characteristic 3
    def add(self,a,b):
        if self.prime:return (a+b)%self.q
        return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
    def neg(self,a):
        if self.prime:return (-a)%self.q
        return (-a%3)+3*((-(a//3))%3)
    def mul(self,a,b):
        if self.prime:return a*b%self.q
        x,y=a%3,a//3;u,v=b%3,b//3
        return (x*u+2*y*v)%3 + 3*((x*v+y*u)%3)
    def square(self,a):return self.mul(a,a)
    def sub(self,a,b):return self.add(a,self.neg(b))
    def character(self,a):
        if a==0:return 0
        for t in range(1,self.q):
            if self.square(t)==a:return 1
        return -1


def matrices(f, traceless_only):
    elems=range(f.q)
    if traceless_only:
        for a,b,c in product(elems,repeat=3):
            d=f.neg(a)
            if f.sub(f.mul(a,d),f.mul(b,c)):
                yield (a,b,c,d)
    else:
        for a,b,c,d in product(elems, repeat=4):
            if f.sub(f.mul(a,d),f.mul(b,c)):
                yield (a,b,c,d)

def mul(f,A,B):
    a,b,c,d=A;e,g,h,j=B
    return (f.add(f.mul(a,e),f.mul(b,h)),f.add(f.mul(a,g),f.mul(b,j)),
            f.add(f.mul(c,e),f.mul(d,h)),f.add(f.mul(c,g),f.mul(d,j)))

def sq(f,A):return mul(f,A,A)
def target(f,A,B):
    s=tuple(f.add(x,y) for x,y in zip(sq(f,A),sq(f,B)))
    if s[1]==s[2]==0 and s[0]==s[3]:return s[0]
    return None

def check(q,full):
    f=Field(q)
    vec=list(matrices(f,not full))
    sqs=[sq(f,M) for M in vec]
    counts=Counter()
    for i,A in enumerate(vec):
        for j,B in enumerate(vec):
            Q=tuple(f.add(x,y) for x,y in zip(sqs[i],sqs[j]))
            if Q[1] or Q[2] or Q[0]!=Q[3]:continue
            if mul(f,A,B)!=mul(f,B,A):
                assert f.add(A[0],A[3])==0 and f.add(B[0],B[3])==0
                counts[Q[0]]+=1
    for c in range(q):
        chi=f.character(c)
        goal= q*q*(q-1)*(q*q-1) if c==0 else q*(q*q-1)*(q*(q-2)-2*chi)
        assert counts[c]==goal,(q,c,counts[c],goal)
    if not full:
        assert len(vec)==q*q*(q-1)
    print('q',q,'full_matrix_search',full,'noncommuting_fibers',dict(sorted(counts.items())))

if __name__=='__main__':
    for q,full in [(3,True),(5,True),(7,False),(9,False),(11,False)]:check(q,full)
    print('MATRIX_SQUARE_WARING_NONCOMMUTING_OK')
