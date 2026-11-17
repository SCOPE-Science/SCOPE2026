"""Exact spin-1 Petersen ground-envelope verifier; Python standard library only."""
from itertools import product
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
cert=json.loads((ROOT/'certificate.json').read_text(encoding='utf-8'))
E=[(i,(i+1)%5) for i in range(5)]+[(i,5+i) for i in range(5)]+[(5+i,5+(i+2)%5) for i in range(5)]
assert sorted(tuple(sorted(e)) for e in E)==[tuple(e) for e in cert['edges']]
counts=defaultdict(int)
for s in product((-1,0,1),repeat=10):
    e=sum(s[a]*s[b] for a,b in E)
    k=sum(z*z for z in s)
    m=sum(s)
    counts[e,k,m]+=1
assert sum(counts.values())==59049
assert len(counts)==318
mins={}
for (e,k,m),v in counts.items():
    if m<0:continue
    if (k,m) not in mins or mins[k,m][0]>e:mins[k,m]=(e,v)
    elif mins[k,m][0]==e:mins[k,m]=(e,mins[k,m][1]+v)
assert len(mins)==len(cert['sector_bounds'])==36
for r in cert['sector_bounds']:
    k,m,e,c=(r[x] for x in ('u','m','e','count'))
    assert mins[k,m]==(e,c)
assert {(r['u'],r['m']) for r in cert['sector_bounds']}==set(mins)
active=[tuple(r[x] for x in ('e','u','m')) for r in cert['active']]
for r in cert['active']:
    assert mins[r['u'],r['m']]==(r['e'],r['count'])
for r in cert['sector_bounds']:
    weights=[Fraction(x) for x in r['weights']]
    assert len(weights)==7 and all(x>=0 for x in weights)
    assert sum(weights)==1
    assert sum(w*p[1] for w,p in zip(weights,active))==r['u']
    assert sum(w*p[2] for w,p in zip(weights,active))>=r['m']
    assert sum(w*p[0] for w,p in zip(weights,active))<=r['e']
for i,wit in enumerate(cert['witnesses']):
    d=Fraction(wit['delta']);b=Fraction(wit['field_abs'])
    assert b>0
    values=[e+d*k-b*m for e,k,m in active]
    assert values[i]<min(v for j,v in enumerate(values) if j!=i)
for key,d in [('zero_d_3_4',Fraction(3,4)),('zero_d_1',Fraction(1))]:
    energies=defaultdict(int);sectors=[]
    for (e,k,m),v in counts.items():energies[Fraction(e)+d*k]+=v
    base=min(energies)
    assert str(base)==cert['zero_field_boundary'][key]['energy']
    assert energies[base]==cert['zero_field_boundary'][key]['degeneracy']
    sectors=sorted([k,m,e,v] for (e,k,m),v in counts.items() if Fraction(e)+d*k==base)
    assert sectors==cert['zero_field_boundary'][key]['sectors']
print('PASS: 59049 states, 318 energy sectors, 36 nonnegative-magnetization minima, 36 exact dominance certificates, 7 exposed branches, exact coexistence counts.')
