"""Standalone exact verification of a random BST boundary/fringe covariance law.
Run: python bst_spine_leaf_checker.py
Uses only the Python 3 standard library.
"""
from fractions import Fraction as Q
from math import factorial
from itertools import permutations

def recurrence(N):
    a=[Q(0)]*(N+1); b=[Q(0)]*(N+1); c=[Q(0)]*(N+1)
    for n in range(1,N+1):
        a[n]=1+sum(a[:n])/n
        b[n]=1 if n==1 else sum(b[k]+b[n-1-k] for k in range(n))/n
        c[n]=1 if n==1 else b[n]+(sum(c[:n])+sum(a[k]*b[n-1-k] for k in range(n)))/n
    return a,b,c

def tree_of_priority(keys):
    # keys are priorities indexed by increasing BST key order; smaller = earlier insertion
    if not keys:return None
    j=min(range(len(keys)),key=lambda i:keys[i])
    return (tree_of_priority(keys[:j]),tree_of_priority(keys[j+1:]))

def stats(T):
    if T is None:return 0,0
    left,right=T
    l,_=stats(left)
    if left is None and right is None:return 1,1
    return 1+l,stats(left)[1]+stats(right)[1]

def check():
    checks=0
    a,b,c=recurrence(300)
    for n in range(1,301):
        h=sum(Q(1,k) for k in range(1,n+1))
        assert a[n]==h
        checks+=1
        assert b[n]==(Q(1) if n==1 else Q(n+1,3))
        checks+=1
        v=c[n]-a[n]*b[n]
        expect=Q(0) if n<=2 else Q((n-2)*(n+1),12*n*(n-1))
        assert v==expect,(n,v,expect)
        checks+=1
        if n>=4:
            assert v-(c[n-1]-a[n-1]*b[n-1])==Q(1,3*n*(n-1)*(n-2))
            checks+=1
    for n in range(1,9):
        sL=sZ=sLZ=0
        for p in permutations(range(n)):
            L,Z=stats(tree_of_priority(p))
            R=sum(p[i]==min(p[:i+1]) for i in range(n))
            peak=sum((i==0 or p[i]>p[i-1]) and (i==n-1 or p[i]>p[i+1]) for i in range(n))
            assert (L,Z)==(R,peak)
            sL+=L;sZ+=Z;sLZ+=L*Z
            checks+=1
        fact=factorial(n)
        cov=Q(sLZ,fact)-Q(sL,fact)*Q(sZ,fact)
        expected=Q(0) if n<=2 else Q((n-2)*(n+1),12*n*(n-1))
        assert cov==expected
        checks+=1
    print(f"PASS: {checks} exact assertions; n<=8 permutation exhaustive, n<=300 rational recurrence")
if __name__=='__main__':check()
