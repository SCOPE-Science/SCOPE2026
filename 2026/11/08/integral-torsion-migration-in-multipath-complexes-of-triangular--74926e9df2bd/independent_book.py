#!/usr/bin/env python3
"""Independent exhaustive multipath enumeration and boundary-rank tests.
Builds candidates from combinations, rather than from the Morse verifier's recursive union-find.
"""
from itertools import combinations
from collections import Counter

def edges(m):
    e=[(0,1),(1,0)]
    for j in range(2,m+2):e.extend([(0,j),(j,0),(1,j),(j,1)])
    return e

def is_multipath(arcs):
    incoming=set();outgoing=set();successor={}
    for a,b in arcs:
        if a in outgoing or b in incoming:return False
        outgoing.add(a);incoming.add(b);successor[a]=b
    for x in successor:
        seen=set();y=x
        while y in successor:
            if y in seen:return False
            seen.add(y);y=successor[y]
    return True

def faces(m):
    arc=edges(m);out=[[] for _ in range(5)]
    out[0].append(0)
    for k in range(1,5):
        for seq in combinations(range(len(arc)),k):
            if is_multipath([arc[i] for i in seq]):out[k].append(sum(1<<i for i in seq))
    return out

def rank(columns,p):
    piv={};r=0
    for column in columns:
        v={i:c%p for i,c in column.items() if c%p}
        while v:
            i=min(v)
            if i not in piv:
                a=v[i];z=pow(a,-1,p)
                piv[i]={j:c*z%p for j,c in v.items() if c*z%p}
                r+=1;break
            a=v[i]
            for j,c in piv[i].items():
                val=(v.get(j,0)-a*c)%p
                if val:v[j]=val
                else:v.pop(j,None)
    return r

EXPECTED={
 3:{2:(0,1,8,0),3:(0,0,7,0),5:(0,0,7,0)},
 4:{2:(0,0,18,1),3:(0,0,17,0),5:(0,0,17,0)},
 5:{2:(0,0,23,32),3:(0,0,22,31),5:(0,0,22,31)},
 6:{2:(0,0,38,169),3:(0,0,38,169),5:(0,0,38,169)},
}

def main():
 for m in sorted(EXPECTED):
    f=faces(m)
    assert sum(map(len,f))=={3:141,4:355,5:773,6:1503}[m]
    assert f[0]==[0]
    for p,expect in EXPECTED[m].items():
        ranks={0:0,5:0}
        for k in range(1,5):
            row_index={u:i for i,u in enumerate(f[k-1])}
            cols=[]
            for u in f[k]:
                bits=[j for j in range(u.bit_length()) if u>>j&1]
                cols.append({row_index[u^(1<<j)]:((1 if v%2==0 else -1)%p) for v,j in enumerate(bits)})
            ranks[k]=rank(cols,p)
        betti=tuple(len(f[k+1])-ranks[k+1]-ranks[k+2] for k in range(4))
        assert betti==expect,(m,p,betti,expect)
        print(f'm={m} F_{p} reduced_betti={betti} faces={sum(map(len,f))}')
 print('INDEPENDENT_CHECK_OK')
if __name__=='__main__':main()
