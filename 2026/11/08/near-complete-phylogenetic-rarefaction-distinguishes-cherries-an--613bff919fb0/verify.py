"""Exact small-tree and infinite-family spot checks for rooted PD rarefaction.

Run with Python 3 standard library: python verify.py
The infinite-family theorem is proved algebraically in RESULT.md; checking
finitely many instances does not replace that proof.
"""
from functools import lru_cache
from fractions import Fraction
from itertools import combinations
from math import comb

LEAF = 'x'

@lru_cache(None)
def shapes(n):
    if n == 1:
        return (LEAF,)
    ans = []
    for a in range(1, n//2+1):
        b = n-a
        for x in shapes(a):
            for y in shapes(b):
                if a==b and repr(x)>repr(y):
                    continue
                ans.append((x,y))
    return tuple(ans)

def subtree_counts(t):
    if t == LEAF:
        return 1,0,0
    a,b=t
    na,ca,pa=subtree_counts(a)
    nb,cb,pb=subtree_counts(b)
    return na+nb,ca+cb+(na==1 and nb==1),pa+pb+(na+nb==3)

def descendants(t, first=0):
    if t == LEAF:
        return first+1,[frozenset([first])]
    a,b=t
    k,aa=descendants(a,first)
    end,bb=descendants(b,k)
    return end,aa+bb+[frozenset(range(first,end))]

def observed_var(t,r):
    n,edges=descendants(t)
    edges=edges[:-1]  # the root has no incoming edge
    assert n==subtree_counts(t)[0]
    total=2*n-2
    # every non-root node represents one unit-length edge
    assert len(edges)==total
    values=[]
    for removed in combinations(range(n),r):
        R=set(removed)
        lost=sum(x.issubset(R) for x in edges)
        values.append(total-lost)
    m=Fraction(sum(values),len(values))
    return Fraction(sum(x*x for x in values),len(values))-m*m

def predicted_var(n,c,t,r):
    if r==2:
        a=Fraction(c,comb(n,2))
        return a*(1-a)
    if r==3:
        N=comb(n,3)
        s=c*(n-2)
        return Fraction(s+3*t,N)-Fraction((s+t)**2,N**2)
    raise ValueError(r)

def join(blocks):
    blocks=list(blocks)
    while len(blocks)>1:
        blocks[:2]=[(blocks[0],blocks[1])]
    return blocks[0]

def witness(q):
    assert q>=1
    A=join([(LEAF,LEAF) for _ in range(2*q+1)])
    for _ in range(2*q-2):
        A=(LEAF,A)
    B=join([(LEAF,(LEAF,LEAF)) for _ in range(2*q)])
    return A,B

def run():
    count=0
    for n in range(4,12):
        for t in shapes(n):
            size,c,p=subtree_counts(t)
            assert size==n
            for r in (2,3):
                v=observed_var(t,r)
                assert v==predicted_var(n,c,p,r),(n,t,r,v)
                count+=1
    balanced=((LEAF,LEAF),(LEAF,LEAF))
    comb4=(LEAF,(LEAF,(LEAF,LEAF)))
    assert observed_var(balanced,2)==Fraction(2,9)
    assert observed_var(comb4,2)==Fraction(5,36)
    assert observed_var(balanced,3)==0
    assert observed_var(comb4,3)==Fraction(11,16)
    for q in (1,2,3,5):
        A,B=witness(q)
        n=6*q
        assert subtree_counts(A)==(n,2*q+1,0)
        assert subtree_counts(B)==(n,2*q,2*q)
        for r in (2,3):
            assert observed_var(A,r)==predicted_var(n,2*q+1,0,r)
            assert observed_var(B,r)==predicted_var(n,2*q,2*q,r)
        assert observed_var(A,2)>observed_var(B,2)
        assert observed_var(A,3)<observed_var(B,3)
    print('PASS: exact direct-subset checks:',count)
    print('PASS: sharp four-leaf values and n=6q witness at q=1,2,3,5')

if __name__=='__main__':
    run()
