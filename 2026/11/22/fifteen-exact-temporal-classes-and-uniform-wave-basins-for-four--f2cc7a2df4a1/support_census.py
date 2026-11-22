#!/usr/bin/env python3
"""Exact support-set certificate for four-state excitation on a clique with private leaves.

Every core/leaf pair has one of 16 local states. Site types with the same
initial state remain identical because the only cross-site input is the
existence of an excited core. Thus one representative per type suffices.
No sampling or finite-n cutoff enters the certificate.
"""
from collections import Counter, defaultdict
from math import comb, factorial
from pathlib import Path
import csv
import subprocess
import sys

Q = 4
TYPE_COUNT = Q * Q

def local_step(pair, excited_core_exists):
    c, leaf = divmod(pair, Q)
    new_c = (c + 1) % Q if c else int(excited_core_exists or leaf == 1)
    new_leaf = (leaf + 1) % Q if leaf else int(c == 1)
    return Q * new_c + new_leaf

def category(mask):
    active = tuple(k for k in range(TYPE_COUNT) if mask & (1 << k))
    assert active
    state = active
    visited = {state: 0}
    for t in range(1, 50):
        excited = any(x // Q == 1 for x in state)
        state = tuple(local_step(x, excited) for x in state)
        if state in visited:
            return visited[state], t - visited[state]
        visited[state] = t
    raise AssertionError('unexpected cycle length or transient')

def build():
    hist = defaultdict(Counter)
    for mask in range(1, 1 << TYPE_COUNT):
        t, period = category(mask)
        assert period in (1, 4), (mask, t, period)
        assert t <= 7, (mask, t, period)
        hist[t, period][mask.bit_count()] += 1
    assert sum(sum(h.values()) for h in hist.values()) == (1 << TYPE_COUNT) - 1
    return dict(hist)

def surjections(n, k):
    return sum((-1) ** j * comb(k, j) * (k - j) ** n for j in range(k + 1))

def census_at_n(hist, n):
    return { (t, p): sum(h.get(k, 0) * surjections(n, k) for k in range(1, TYPE_COUNT+1))
        for (t,p),h in hist.items() }

def write_csv(hist, path):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        wr=csv.writer(f, lineterminator='\n')
        wr.writerow(['entry_time','least_period'] + ['support_'+str(k) for k in range(1,17)])
        for key in sorted(hist):
            wr.writerow(list(key)+[hist[key].get(k,0) for k in range(1,17)])

def read_csv(path):
    with open(path,newline='',encoding='utf-8') as f: r=list(csv.DictReader(f))
    return {(int(row['entry_time']), int(row['least_period'])):
        Counter({k:int(row['support_'+str(k)]) for k in range(1,17) if int(row['support_'+str(k)])}) for row in r}

def check():
    parent=Path(__file__).resolve().parent
    hist=build()
    csv_path=parent/'SUPPORT_COUNTS.csv'
    assert read_csv(csv_path)==hist
    assert sorted(hist)==[(t,p) for t in range(7) for p in (1,4)]+[(7,1)]
    for n in range(2,9):
        a=census_at_n(hist,n)
        assert sum(a.values())==16**n, (n,sum(a.values()))
        surj=surjections(n,4)
        assert sum(v for (t,p),v in a.items() if p==4)==surj*4**n
        assert sum(v for (t,p),v in a.items() if p==1)==(4**n-surj)*4**n
        if n>=3: assert a[(7,1)]>0
        if n>=4: assert a[(0,4)]==surj
    exe=parent/'direct_check'
    if exe.exists():
        out=subprocess.check_output([str(exe)],text=True).splitlines()
        from_direct={}
        for line in out:
            n,t,p,count=map(int,line.split(','))
            from_direct.setdefault(n,{})[t,p]=count
        for n in range(2,6):
            want={key:v for key,v in census_at_n(hist,n).items() if v}
            assert from_direct[n]==want,(n,from_direct[n],want)
        print('INDEPENDENT_DIRECT_CHECK_OK widths=2..5')
    else:
        raise FileNotFoundError('Compile direct_check.cpp to direct_check before verification')
    print('ALL_SUPPORT_SUBSETS_VERIFIED=65535')
    print('PERIODS=1,4 MAX_ENTRY=7')
    print('ALL_TESTS_PASSED')

if __name__=='__main__':
    if len(sys.argv)==2 and sys.argv[1]=='--write':write_csv(build(),Path(__file__).resolve().parent/'SUPPORT_COUNTS.csv')
    else:check()
