#!/usr/bin/env python3
"""Exact support-class certificate and independent labelled-graph check."""
from collections import defaultdict, Counter
from itertools import product
from math import comb
from pathlib import Path
import csv

SUPPORTS=tuple(tuple(j for j in range(3) if mask>>j&1) for mask in range(1,8))

def gh(c,i):
    eC=(1 in c); eI=(1 in i)
    return (tuple((t+1)%3 if t else int(eC or eI) for t in c),
            tuple((t+1)%3 if t else int(eC) for t in i))

def eventual(x, transition):
    seen={}; time=0
    while x not in seen:
        seen[x]=time
        x=transition(x)
        time+=1
        assert time<100
    return seen[x],time-seen[x]

# Complete finite certificate: every initially occupied phase is a tagged representative.
M=defaultdict(lambda: [[0]*3 for _ in range(3)])
status={}
for C in SUPPORTS:
    for I in SUPPORTS:
        value=eventual((C,I),lambda x: gh(*x))
        M[value][len(C)-1][len(I)-1]+=1
        status[(C,I)]=value
assert set(M)=={(0,1),(1,1),(2,1),(3,1),(4,1),(0,3),(1,3),(2,3),(3,3)}
assert sum(sum(map(sum,m)) for m in M.values())==49
assert M[(1,3)]==M[(2,3)]==M[(3,3)]

# A direct graph update implementation, independent of the compressed module rule.
def direct_step(state,a,b):
    n=a+b; excited=[v for v in range(n) if state[v]==1]
    result=[]
    for v in range(n):
        if state[v]: result.append((state[v]+1)%3); continue
        # Every vertex of the clique connects to all others;
        # every independent vertex connects to the entire clique.
        adj = (range(n) if v<a else range(a))
        result.append(int(any(u!=v and u in excited for u in adj)))
    return tuple(result)

def surj(n,k):
    return sum((-1)**j * comb(k,j) * (k-j)**n for j in range(k+1))

def closed(a,b):
    A,B,C,D=2**a,3**a,2**b,3**b
    V=(A-2)*(D-2*C+1)
    return {
      (0,1):1, (1,1):A*C-1, (2,1):A*C-2*C+D,
      (3,1):A*C-3*C+D+1, (4,1):D-C-1,
      (0,3):B*D-3*A*D+3*A*C-6*C+3*D-3*A+6,
      (1,3):V,(2,3):V,(3,3):V,
    }

for a in range(1,7):
  for b in range(1,7):
    if a+b>10:continue
    expected=closed(a,b)
    calculated={key:sum(matrix[k-1][l-1]*surj(a,k)*surj(b,l) for k in range(1,4) for l in range(1,4)) for key,matrix in M.items()}
    assert calculated==expected,(a,b,calculated,expected)
    assert sum(expected.values())==3**(a+b)
    counts=Counter(eventual(x,lambda z:direct_step(z,a,b)) for x in product(range(3),repeat=a+b))
    assert all(counts[key]==expected[key] for key in M),(a,b,counts,expected)

with (Path(__file__).parent/'support_table.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow(['clique_support\\independent_support']+[''.join(map(str,I)) for I in SUPPORTS])
    for C in SUPPORTS:
        w.writerow([''.join(map(str,C))]+[f'{status[(C,I)][0]}/{status[(C,I)][1]}' for I in SUPPORTS])
print('ALL 49 TAGGED SUPPORT CASES: VERIFIED')
for key in sorted(M): print('CLASS',key,'3x3 SUPPORT-SIZE MATRIX',M[key])
print('DIRECT LABELLED CONFIGURATION PAIRS:',[(a,b) for a in range(1,7) for b in range(1,7) if a+b<=10])
print('NUMBER OF LABELLED CONFIGURATIONS:',sum(3**(a+b) for a in range(1,7) for b in range(1,7) if a+b<=10))
print('PARAMETER FORMULAS AND ALL HISTOGRAMS: VERIFIED')
