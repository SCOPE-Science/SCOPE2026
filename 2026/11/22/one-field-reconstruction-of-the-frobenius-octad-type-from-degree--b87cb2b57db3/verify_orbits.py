"""Exact E8 exceptional-curve one-field flag census; Python standard library."""
from itertools import combinations
from collections import Counter

EXPECTED = {
 (1,1,1,1,1,1,1,1): (240,6720,15120,60480),
 (2,1,1,1,1,1,1): (126,2072,3780,11592),
 (2,2,1,1,1,1): (60,544,804,2080),
 (2,2,2,1,1): (26,144,168,432),
 (2,2,2,2): (8,32,72,96),
 (3,1,1,1,1,1): (72,720,1080,2214),
 (3,2,1,1,1): (30,140,180,330),
 (3,2,2,1): (12,40,24,70),
 (3,3,1,1): (12,12,36,36),
 (3,3,2): (6,8,0,12),
 (4,1,1,1,1): (40,240,290,400),
 (4,2,1,1): (14,36,42,68),
 (4,2,2): (4,8,14,8),
 (4,3,1): (4,0,8,10),
 (4,4): (0,0,4,0),
 (5,1,1,1): (20,60,60,40),
 (5,2,1): (6,12,0,12),
 (5,3): (2,0,0,4),
 (6,1,1): (8,6,12,0),
 (6,2): (2,2,0,0),
 (7,1): (2,0,0,0),
 (8,): (0,0,0,0),
}

def partitions(n, bound=8):
    if not n:
        yield ()
    else:
        for a in range(min(n,bound),0,-1):
            for rest in partitions(n-a,a):
                yield (a,)+rest

def build_curves():
    out=[]
    out += [(0,)+tuple(-int(i==j) for i in range(8)) for j in range(8)]
    out += [(1,)+tuple(int(i in ss) for i in range(8)) for ss in combinations(range(8),2)]
    out += [(2,)+tuple(int(i in ss) for i in range(8)) for ss in combinations(range(8),5)]
    out += [(3,)+tuple(0 if i==b else 2 if i==a else 1 for i in range(8)) for a in range(8) for b in range(8) if a!=b]
    out += [(4,)+tuple(2 if i in ss else 1 for i in range(8)) for ss in combinations(range(8),3)]
    out += [(5,)+tuple(1 if i in ss else 2 for i in range(8)) for ss in combinations(range(8),2)]
    out += [(6,)+tuple(3 if i==j else 2 for i in range(8)) for j in range(8)]
    assert len(out)==len(set(out))==240
    assert all(3*d-sum(m)==1 and d*d-sum(t*t for t in m)==-1 for d,*m in out)
    return out

def intersection(a,b):
    return a[0]*b[0]-sum(x*y for x,y in zip(a[1:],b[1:]))

def cycle_perm(parts):
    p=[]; start=0
    for n in parts:
        p.extend(list(range(start+1,start+n))+[start]);start+=n
    assert sorted(p)==list(range(8))
    return p

def count_all():
    curves=build_curves(); pos={v:k for k,v in enumerate(curves)}
    intr={(i,j):intersection(curves[i],curves[j]) for i in range(240) for j in range(i+1,240)}
    assert Counter(intr.values())=={0:6720,1:15120,2:6720,3:120}
    counts={}
    for part in partitions(8):
        p=cycle_perm(part); inv=[p.index(i) for i in range(8)]
        f=[pos[(a[0],)+tuple(a[1+k] for k in inv)] for a in curves]
        assert sorted(f)==list(range(240))
        cycles=[]; done=set()
        for i in range(240):
            if i in done: continue
            cyc=[]; x=i
            while x not in done:
                done.add(x);cyc.append(x);x=f[x]
            assert x==i
            cycles.append(tuple(cyc))
        fixed=[c[0] for c in cycles if len(c)==1]
        pairs=[c for c in cycles if len(c)==2]
        triples=[c for c in cycles if len(c)==3]
        skew=lambda v:all(intr[tuple(sorted(ab))]==0 for ab in combinations(v,2))
        t=sum(map(skew,triples))
        t+=sum(skew((a,)+c) for a in fixed for c in pairs)
        t+=sum(map(skew,combinations(fixed,3)))
        g0=g1=0
        for (i,j),w in intr.items():
            if tuple(sorted((f[i],f[j])))==(i,j):
                g0+=(w==0);g1+=(w==1)
        counts[part]=(len(fixed),g0,g1,t)
    assert counts==EXPECTED,(counts,EXPECTED)
    assert len(set(v[:3] for v in counts.values()))==21
    assert len(set(counts.values()))==22
    assert {p for p,v in counts.items() if v[:3]==(2,0,0)}=={(5,3),(7,1)}
    for part in [(5,3),(7,1)]:
        p=cycle_perm(part);inv=[p.index(i) for i in range(8)]
        f=[pos[(a[0],)+tuple(a[1+k] for k in inv)] for a in curves]
        all_pairs=Counter(w for (i,j),w in intr.items() if tuple(sorted((f[i],f[j])))==(i,j))
        assert all_pairs=={3:1},(part,all_pairs)
    print('PASS: 240 classes; intersection multiplicities; 22 partitions; full flag table; unique triple separation')

if __name__=='__main__':count_all()
