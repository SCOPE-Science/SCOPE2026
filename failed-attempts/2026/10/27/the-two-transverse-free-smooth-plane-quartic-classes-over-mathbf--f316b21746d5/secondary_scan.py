"""Independent exhaustive enumeration by direct binomial coefficient expansion.
Uses only Python standard library; agrees with the primary classification certificate.
"""
from itertools import product
from math import comb
import json
from pathlib import Path
exps=[(a,b,4-a-b) for a in range(5) for b in range(5-a)]
pts=[p for p in product((0,1),repeat=3) if p!=(0,0,0)]
lines=[]
for normal in pts:
    linepoints=[p for p in pts if sum(normal[i]*p[i] for i in range(3))%2==0]
    lines.append((linepoints[0],linepoints[1]))

def coefficients(exponent,u,v):
    curr={0:1}
    for i,n in enumerate(exponent):
        nxt={}
        for j in range(n+1):
            if (comb(n,j)*u[i]**(n-j)*v[i]**j)%2:
                for degree,parity in curr.items():
                    nxt[degree+j]=(nxt.get(degree+j,0)+parity)%2
        curr=nxt
    return sum((curr.get(i,0)<<i) for i in range(5))
restrictions=[[coefficients(e,u,v) for e in exps] for u,v in lines]

def trans(q):
    a,b,c,d,e=[q>>i&1 for i in range(5)]
    return (b and (e if d==0 else a^c^e)) or (not b and d and a)

def value_at(exp,p):
    return int(all(not e or p[i] for i,e in enumerate(exp)))

s=[]
for m in range(1,1<<15):
    failed=False
    for row in restrictions:
        q=0
        for j,t in enumerate(row):
            if m>>j&1:q^=t
        if trans(q):failed=True;break
    if failed:continue
    for p in pts:
        val=0;partials=[0,0,0]
        for k,ex in enumerate(exps):
            if m>>k&1:
                val ^= value_at(ex,p)
                for j in range(3):
                    if ex[j]%2:
                        deriv=tuple(ex[t]-(t==j) for t in range(3))
                        partials[j] ^=value_at(deriv,p)
        if not val and not any(partials):failed=True;break
    if not failed:s.append(m)
expected=json.loads(Path(__file__).with_name('classification.json').read_text())['zero_transverse_candidates']
assert s==expected, (s,expected)
print('PASS: independent combinatorial scan of 32767 quartics returns the same 25 rationally smooth transverse-free masks')
