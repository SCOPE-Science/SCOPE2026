#!/usr/bin/env python3
"""Direct witness verification for three-state excitation on binary hypercubes."""
from pathlib import Path
import itertools

BASE = Path(__file__).resolve().parent.parent
TUPLES = list(itertools.product(range(2), range(3), range(3)))
INDEX = {v: i for i, v in enumerate(TUPLES)}

def quotient_step(x):
    out = []
    for i, (a,b,c) in enumerate(TUPLES):
        adj = []
        for j, (value, end) in enumerate(zip((a,b,c),(1,2,2))):
            for dv in (-1,1):
                if 0 <= value+dv <= end:
                    new = [a,b,c]; new[j] += dv
                    adj.append(INDEX[tuple(new)])
        color = x[i]
        out.append(2 if color == 1 else (int(any(x[k] == 1 for k in adj)) if color == 0 else 0))
    return tuple(out)

def hypercube_step(x,d):
    assert len(x) == (1<<d)
    result=[]
    for v, c in enumerate(x):
        if c==1:result.append(2)
        elif c==2:result.append(0)
        else:result.append(int(any(x[v ^ (1<<j)] == 1 for j in range(d))))
    return tuple(result)

def lift(x,d):
    assert d>=5
    return tuple(x[INDEX[(v&1, (v>>1&1)+(v>>2&1), (v>>3&1)+(v>>4&1))]] for v in range(1<<d))

for p in (7,14):
    words=(BASE/'data'/f'period{p}_trace.txt').read_text().splitlines()
    assert len(words)==p and all(len(w)==18 and set(w)<={'0','1','2'} for w in words)
    trace=[tuple(map(int,w)) for w in words]
    assert len(set(trace))==p
    for i in range(p):
        assert quotient_step(trace[i]) == trace[(i+1)%p]
        # Independent direct five-cube transitions, not quotient-based transitions.
        assert hypercube_step(lift(trace[i],5),5) == lift(trace[(i+1)%p],5)
    # Verify that the 5-cube pattern stays periodic in a six-dimensional cylinder.
    for i in range(p):
        assert hypercube_step(lift(trace[i],6),6)==lift(trace[(i+1)%p],6)
    print(f'period {p}: {p} distinct quotient words, every transition checked on quotient, Q5, Q6')

# Full direct enumeration for smaller hypercubes (2, 4, 8 vertices).
for d in (1,2,3):
    n=1<<d; total=3**n; periods={}; known={}
    for x in range(total):
        if x in known:continue
        seq=[];pos={};y=x
        while y not in pos and y not in known:
            pos[y]=len(seq);seq.append(y)
            a=tuple((y//(3**j))%3 for j in range(n))
            b=hypercube_step(a,d)
            y=sum(z*3**j for j,z in enumerate(b))
        if y in pos:
            start=pos[y];p=len(seq)-start
            periods[p]=periods.get(p,0)+1
            for z in seq[start:]:known[z]=p
            seq=seq[:start]
        for z in reversed(seq): known[z]=known[y]
    assert len(known)==total
    assert 7 not in periods and 14 not in periods
    print(f'Q{d}: all {total} states checked; primitive orbit counts {dict(sorted(periods.items()))}')
print('WITNESS AND SMALL-DIMENSION CHECKS PASSED')
