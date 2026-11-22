#!/usr/bin/env python3
"""Independent finite checks of a three-generator semigroup gap-run theorem.
Nothing in this program certifies the universal theorem on its own.
"""
from collections import Counter

def predicted(a):
    k,r=divmod(a,5)
    if a<8: raise ValueError('a must be at least 8')
    b=Counter()
    b[1]=4*k+(2 if r==0 else 0 if r==1 else 3)
    b[2]=k+1+(r==3)
    for g in range(3,a):
        if (a-1-g)%5==0: b[g]=1
    return +b

def direct(a):
    # The row-filling argument establishes that this range contains the conductor.
    end=a*(a+5)
    reachable=bytearray(end+1)
    reachable[0]=1
    for n in range(end+1):
        if reachable[n]:
            for d in (a,a+3,a+5):
                if n+d<=end: reachable[n+d]=1
    assert all(reachable[n] for n in range(end-a,end+1)), (a,'insufficient range')
    b=Counter(); n=0
    while n<=end:
        if reachable[n]: n+=1; continue
        z=n
        while n<=end and not reachable[n]: n+=1
        b[n-z]+=1
    return +b

def exact_offsets(m):
    return {3*u+5*v for u in range(m+1) for v in range(m-u+1)}

def expected_offsets(m):
    if m==0:return {0}
    if m==1:return {0,3,5}
    return {0,3,5,6,5*m-2,5*m}|set(range(8,5*m-3))

def by_row(a):
    k,r=divmod(a,5)
    if k==1: return None
    rows=[]
    for m in range(k+5):
        g=[]
        if m==0:g=[(1,a-1)]
        elif m==1:g=[(1,2),(4,1),(6,a-6)]
        elif 2<=m<=k:
            g=[(1,2),(4,1),(7,1),(5*m-3,1),(5*m-1,1)]
            tail=(a-5*m-1)
            if tail>0:g.append((5*m+1,tail))
        elif m==k+1:
            g=[(1,2),(4,1),(7,1)]
            if r>=3:g.append((5*k+2,1))
        elif m==k+2:
            if r==1:g=[(1,1),(7,1)]
            elif r==3:g=[(1,1),(4,1),(7,1)]
            else:g=[(2,1),(4,1),(7,1)]
        elif m==k+3:
            if r==1:g=[]
            elif r==3:g=[(4,1)]
            else:g=[(7,1)]
        z=set()
        for t,l in g:
            for i in range(t,t+l):z.add(i)
        rows.append(z)
    return rows

def test():
    for m in range(70):
        assert exact_offsets(m)==expected_offsets(m),('offset',m)
    for a in range(8,301):
        got=direct(a)
        want=predicted(a)
        assert got==want,(a,got,want)
        rows=by_row(a)
        if rows:
            k,r=divmod(a,5)
            for m in range(k+5):
                # Independent offset representation criterion using cached offset sets.
                cand=[exact_offsets(j) for j in range(max(0,m-1),m+1)]
                observed={t for t in range(a) if all((m-j)*a+t not in cand[j-max(0,m-1)] for j in range(max(0,m-1),m+1))}
                assert observed==rows[m],('row',a,m,observed^rows[m])
    print('PASS: offsets m=0..69, all independent membership histograms a=8..300, row tables a=10..300')
if __name__=='__main__':test()
