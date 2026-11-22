"""Independent Diophantine class search and direct Frobenius-stable flag enumeration."""
from itertools import product,combinations
from collections import Counter
from verify_orbits import EXPECTED

def integer_classes():
    curves=[]
    for m in product(range(-1,4),repeat=8):
        s=sum(m);sq=sum(a*a for a in m)
        if (s+1)%3:continue
        d=(s+1)//3
        if 0<=d<=6 and sq==d*d+1:
            curves.append((d,)+m)
    assert len(curves)==len(set(curves))==240
    return sorted(curves)

def calc():
    V=integer_classes(); lookup={v:i for i,v in enumerate(V)}
    adj=[set() for _ in range(240)]
    pair_by_int=[[] for _ in range(4)]
    for i in range(240):
        for j in range(i+1,240):
            z=V[i][0]*V[j][0]-sum(V[i][k]*V[j][k] for k in range(1,9))
            assert z in (0,1,2,3)
            pair_by_int[z].append((i,j))
            if z==0: adj[i].add(j);adj[j].add(i)
    assert [len(x) for x in pair_by_int]==[6720,15120,6720,120]
    tri=[]
    for i in range(240):
        for j in sorted(q for q in adj[i] if q>i):
            tri.extend((i,j,k) for k in adj[i].intersection(adj[j]) if k>j)
    assert len(tri)==60480
    rows={}
    special_pairs={}
    for partition in EXPECTED:
        pi=[];start=0
        for n in partition:
            for t in range(n):pi.append(start+(t+1)%n)
            start+=n
        rev=[pi.index(k) for k in range(8)]
        action=[lookup[(d,)+tuple(m[j] for j in rev)] for d,*m in V]
        assert len(set(action))==240
        one=sum(action[k]==k for k in range(240))
        def stable(flag): return tuple(sorted(action[i] for i in flag))==flag
        zero=sum(stable(p) for p in pair_by_int[0]); onepair=sum(stable(p) for p in pair_by_int[1]); three=sum(stable(t) for t in tri)
        rows[partition]=(one,zero,onepair,three)
        if partition in [(5,3),(7,1)]:
            special_pairs[partition]=tuple(sum(stable(p) for p in pair_by_int[j]) for j in range(4))
    assert rows==EXPECTED
    assert special_pairs=={(5,3):(0,0,0,1),(7,1):(0,0,0,1)}
    for p in [(5,3),(7,1)]:
        assert rows[p][:3]==(2,0,0)
    print('PASS: Diophantine 240-curve enumeration; direct checks on 60480 triples across all 22 cases')

if __name__=='__main__':calc()
