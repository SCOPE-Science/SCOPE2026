"""Independent direct bit-matrix and full-state temporal checks for a deleted-edge cube.
Uses GF(2) exact XOR linear algebra, no external packages.
"""
from collections import Counter

def rows(d):
    n=1<<d
    return [sum(1<<v for v in range(n) if (i^v).bit_count()==1 and {i,v}!={0,1}) for i in range(n)]

def prod(a,b):
    return [__import__('functools').reduce(int.__xor__, (b[j] for j in range(len(b)) if (r>>j)&1), 0) for r in a]

def rank(a):
    base={}
    for x in a:
        while x:
            k=x.bit_length()-1
            if k not in base:base[k]=x;break
            x^=base[k]
    return len(base)

def identity(n):return [1<<i for i in range(n)]

def plus(a,b):return [x^y for x,y in zip(a,b)]

def iterate_state(x, col):
    z=0
    while x:
        b=x & -x
        z^=col[b.bit_length()-1]
        x-=b
    return z

def expected(d):
    n=1<<d
    if d%2:
        return [2,0], [ (n-4)//2, n-4, n-2], [1,2,4]
    a=n//2-2
    return [2*a,a,0], [0,2,4], [1,3,6]

for d in range(2,8):
    b=rows(d);n=len(b);I=identity(n)
    p=I[:]; ranks=[]
    for t in range(1,9):
        p=prod(p,b)
        ranks.append(rank(p))
    if d%2:
        assert ranks[0]==n-2
        assert all(v==n-2 for v in ranks)
        assert rank(plus(b,I))==n//2+2
        c=plus(b,I);c2=prod(c,c);c3=prod(c2,c);c4=prod(c3,c)
        assert [rank(z) for z in (c,c2,c3,c4)]==[n//2+2,4,3,2]
        assert rank(plus(prod(b,b),I))==4
        assert rank(plus(prod(prod(b,b),prod(b,b)),I))==2
        assert prod(prod(prod(b,b),prod(b,b)),b)==b
    else:
        a=n//2-2
        assert ranks == [n-a,n-2*a]+[4]*6,(d,ranks)
        assert rank(plus(prod(prod(b,b),b),I))==n-2
        p2=prod(b,b)
        p6=prod(prod(p2,p2),p2)
        assert prod(p6,p2)==p2
    print('direct-ranks',d,n,ranks[:5])

for d in range(2,5):
    b=rows(d);n=len(b)
    c=[sum(((b[i]>>j)&1)<<i for i in range(n)) for j in range(n)]
    census=Counter()
    for x in range(1<<n):
        seen={};seq=[];s=x
        while s not in seen:
            seen[s]=len(seq);seq.append(s);s=iterate_state(s,c)
        entry=seen[s];period=len(seq)-entry
        census[entry,period]+=1
    q=2
    if d%2:
        entry={0:1,1:q*q-1}
        period={1:q**((n-4)//2),2:q**(n-4)-q**((n-4)//2),4:q**(n-2)-q**(n-4)}
    else:
        a=n//2-2
        entry={0:1,1:q**a-1,2:q**(2*a)-q**a}
        period={1:1,3:q*q-1,6:q**4-q*q}
    predicted=Counter({(i,j):u*v for i,u in entry.items() for j,v in period.items() if u*v})
    assert census==predicted,(d,census,predicted)
    print('exhaustive',d,'states',1<<n,'classes',sorted(census.items()))
print('DIRECT_CHECKS_PASS')
