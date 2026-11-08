#!/usr/bin/env python3
"""Independent finite test for shifted geometric sum-incidence forest thresholds.
Finite tests are supplementary to the proof for all b,c.
"""

def cycle_in_three_sums(base, shift):
    sums=[1+shift,base+shift,base*base+shift]
    m=sums[-1]
    parent=list(range(2*(m+1)))
    rank=[0]*len(parent)
    def root(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    for val in sums:
        for left in range(val+1):
            a=root(left)
            b=root(m+1+val-left)
            if a==b:
                return True
            if rank[a]<rank[b]:a,b=b,a
            parent[b]=a
            rank[a]+=(rank[a]==rank[b])
    return False

def cycle_witness(base,shift):
    d=base-1
    a=shift+1
    first=shift+base
    second=shift+base*base
    edges=[(first,0,first)]
    edges.append((a,0,a))
    for j in range(base):
        l=a-j*d
        r=(j+1)*d
        edges.append((l,r,first))
        if j<base-1:
            edges.append((a-(j+1)*d,r,a))
    edges.append((first,base*d,second))
    assert len(edges)==2*base+2
    assert all(x>=0 and y>=0 and x+y==s for x,y,s in edges)
    # All vertices have degree two; the construction forms one cycle
    L={};R={}
    for x,y,s in edges:
        L[x]=L.get(x,0)+1
        R[y]=R.get(y,0)+1
    assert len(L)==len(R)==base+1 and all(v==2 for v in L.values()) and all(v==2 for v in R.values())

checks=0
for base in range(2,16):
    threshold=base*(base-2)
    for shift in range(threshold+5):
        observed=cycle_in_three_sums(base,shift)
        expected=shift>=threshold
        assert observed==expected,(base,shift,observed,expected)
        if expected:
            cycle_witness(base,shift)
        checks+=1
print('SHIFTED_GEOMETRIC_FOREST_VERIFY_OK',checks,'cases, bases 2..15')
