"""Exact four-digit base-12 Kaprekar attractor and basin certificate.

Run: python3 verify.py; standard-library only.
"""
import csv
import io
from collections import Counter, defaultdict
from pathlib import Path

BASE = 12
WIDTH = 4
SIZE = BASE**WIDTH
EXPECTED = {
    3: {"cycle": (6908, 10890, 14212), "hist": (3, 1117, 1128, 1104, 520, 840)},
    6: {"cycle": (7172, 9031, 10626, 12617, 13816, 14344), "hist": (6, 2402, 3080, 5592, 2584, 892, 808, 648)},
}

def digits(x):
    assert 0 <= x < SIZE
    ds=[]
    for _ in range(WIDTH):
        ds.append(x % BASE)
        x //= BASE
    return sorted(ds)

def kap(x):
    ds=digits(x)
    return sum(ds[i] * BASE**i - ds[i] * BASE**(WIDTH-1-i) for i in range(WIDTH))

def gap(x):
    a,b,c,d=digits(x)
    return d-a,c-b

def canonical_pairs():
    return [(u,v) for u in range(1,BASE) for v in range(u+1)]

def image(p):
    u,v=p
    return (BASE**3-1)*u+(BASE**2-BASE)*v

def weight(p):
    u,v=p
    if v==0:
        return (BASE-u)*4*(3*u-1)
    if v==u:
        return (BASE-u)*6
    return (BASE-u)*24*(u-v)

def gap_orbits():
    pairs=canonical_pairs()
    F={p:gap(image(p)) for p in pairs}
    assert len(pairs)==77 and all(q in F for q in F.values())
    record={}
    for start in pairs:
        trail=[]; index={}; p=start
        while p not in record and p not in index:
            index[p]=len(trail)
            trail.append(p)
            p=F[p]
        if p in record:
            end,dist=record[p]
            for x in reversed(trail):
                dist+=1
                record[x]=(end,dist)
        else:
            cut=index[p]
            cyc=tuple(sorted(trail[cut:]))
            for x in trail[cut:]:
                record[x]=(cyc,0)
            dist=0
            for x in reversed(trail[:cut]):
                dist+=1
                record[x]=(cyc,dist)
    return F,record

def calculate_weighted():
    F,R=gap_orbits()
    classes={cyc for cyc,dist in R.values()}
    assert {len(c) for c in classes}=={3,6}
    hist={len(c):Counter() for c in classes}
    table=[]
    for p in canonical_pairs():
        cyc,dist=R[p]
        length=len(cyc)
        w=weight(p)
        hist[length][dist+1]+=w
        if dist==0:
            hist[length][0]+=1
            hist[length][1]-=1
        table.append((p[0],p[1],F[p][0],F[p][1],length,dist,w))
    assert sum(weight(p) for p in canonical_pairs())==SIZE-BASE
    assert sum(sum(v.values()) for v in hist.values())==SIZE-BASE
    for length, obj in EXPECTED.items():
        assert tuple(sorted(image(p) for p in next(c for c in classes if len(c)==length)))==obj['cycle']
        assert tuple(hist[length][i] for i in range(len(obj['hist'])))==obj['hist']
        assert all(i<len(obj['hist']) for i in hist[length])
    return table

def direct_exhaustion():
    # This routine operates on complete integer states, not the weighted gap graph.
    hist=defaultdict(Counter)
    cycles=defaultdict(set)
    for initial in range(SIZE):
        trace=[]
        first={}
        x=initial
        while x not in first:
            first[x]=len(trace)
            trace.append(x)
            x=kap(x)
        cyc=tuple(sorted(trace[first[x]:]))
        h=first[x]
        if len(cyc)==1 and cyc==(0,):
            assert initial in {d*(1+BASE+BASE**2+BASE**3) for d in range(BASE)}
            continue
        assert len(cyc) in EXPECTED
        assert cyc==EXPECTED[len(cyc)]['cycle']
        hist[len(cyc)][h]+=1
        cycles[len(cyc)].add(cyc)
    assert set(cycles)=={3,6}
    for length,obj in EXPECTED.items():
        assert tuple(hist[length][i] for i in range(len(obj['hist'])))==obj['hist']
    assert sum(sum(v.values()) for v in hist.values())==SIZE-BASE
    return hist

def main():
    table=calculate_weighted()
    header=('u','v','next_u','next_v','cycle_length','gap_distance','start_strings')
    s=io.StringIO(newline='')
    w=csv.writer(s,lineterminator='\n')
    w.writerow(header)
    w.writerows(table)
    expected=s.getvalue().encode('utf8')
    path=Path(__file__).with_name('gap_table.csv')
    actual=path.read_bytes()
    assert actual==expected, 'gap certificate differs from recomputed state graph'
    direct_exhaustion()
    print('PASS: 77 reduced states, 20736 padded starting strings, and certificate agree')
    print('Three-cycle: 4712 starts, hitting-time counts 3,1117,1128,1104,520,840')
    print('Six-cycle: 16012 starts, hitting-time counts 6,2402,3080,5592,2584,892,808,648')
    print('Twelve repdigits map to zero; no other attractors; sharp maximal time 7.')

if __name__=='__main__':
    main()
