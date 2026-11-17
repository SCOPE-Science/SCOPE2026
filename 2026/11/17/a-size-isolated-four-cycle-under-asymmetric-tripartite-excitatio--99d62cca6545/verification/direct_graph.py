#!/usr/bin/env python3
"""Independent full-vertex test for the heterogeneous tripartite excitation theorem."""
from itertools import product
from collections import Counter
from pathlib import Path
import csv


def direct(size, init):
    a, b, c = size
    marks = ([0]*a)+([1]*b)+([2]*c)
    seen = {}
    state = tuple(init)
    t = 0
    while state not in seen:
        seen[state] = t
        excited = [sum(state[v] == 1 for v, x in enumerate(marks) if x == i)
                   for i in range(3)]
        next_state = []
        for vertex, color in enumerate(state):
            shore = marks[vertex]
            neighbors_excited = sum(excited[j] for j in range(3) if j != shore)
            if color == 0:
                next_state.append(1 if neighbors_excited >= (1, 1, 2)[shore] else 0)
            elif color == 1:
                next_state.append(2)
            else:
                next_state.append(0)
        state = tuple(next_state)
        t += 1
        assert t < 65
    return seen[state], t - seen[state]


def signature(size, colors):
    a, b, c = size
    t = 0
    out = []
    for n in (a,b,c):
        v = colors[t:t+n]
        out.extend(min(2, v.count(col)) for col in range(3))
        t += n
    return tuple(out)


def check():
    source = Path(__file__).resolve().parents[1]/'certificates'/'all_signatures.csv'
    with source.open(newline='', encoding='utf-8') as f:
        r = list(csv.reader(f))
    lookup = {tuple(map(int, row[:9])):tuple(map(int,row[9:])) for row in r[1:]}
    assert len(lookup)==17576
    all_checks = 0
    by_size = {}
    for total in range(3,9):
        for a in range(1,total-1):
            for b in range(1,total-a):
                c=total-a-b
                if c<1:continue
                sizes=(a,b,c)
                hist=Counter()
                for init in product(range(3),repeat=total):
                    actual=direct(sizes,init)
                    expected=lookup[signature(sizes,init)]
                    assert actual==expected,(sizes,init,actual,expected)
                    hist[actual]+=1
                    all_checks+=1
                assert sum(hist.values())==3**total
                assert hist.get((0,4),0)==(8 if a==2 and b==2 else 0), (sizes,hist)
                assert max(t for t,p in hist) <=7
                by_size[sizes]={'hist':dict(sorted(hist.items())), 'states':3**total}
    # A direct sharpness witness: K_{1,2,2}, five vertices.
    witness=(0,0,1,1,2)
    assert direct((1,2,2),witness)==(7,1),direct((1,2,2),witness)
    print('INDEPENDENT_VERTEX_STATES',all_checks)
    print('GRAPHS',len(by_size))
    for sizes in ((1,1,1),(1,2,1),(2,2,1),(2,2,2),(3,2,1),(2,3,1),(2,2,3)):
        print('SIZE',sizes,'PERIODIC', {p:sum(v for (t,period),v in by_size[sizes]['hist'].items() if t==0 and period==p) for p in (1,3,4)},'MAX_ENTRY',max(t for t,p in by_size[sizes]['hist']))
    print('PASS')

if __name__=='__main__':check()
