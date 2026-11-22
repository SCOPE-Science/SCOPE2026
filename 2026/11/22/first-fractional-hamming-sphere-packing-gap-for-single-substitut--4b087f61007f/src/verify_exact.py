#!/usr/bin/env python3
"""Exact independent check of the integer witnesses and rational LP certificates."""
import json
from fractions import Fraction
from itertools import product, combinations
from pathlib import Path

def dyck_words(n):
    out=[]
    for steps in product((0,1),repeat=2*n):
        height=0
        for b in steps:
            height += (2*b-1)
            if height<0:break
        else:
            if height==0:
                out.append(sum(b<<i for i,b in enumerate(steps)))
    return sorted(out)

def outputs(w,n):
    return {w}|{w^(1<<j) for j in range(2*n)}

P=Path(__file__).resolve().parent.parent
obj=json.loads((P/'certificates.json').read_text(encoding='utf-8'))
assert obj['schema_version']==1
assert len(obj['instances'])==6
for entry in obj['instances']:
    n=entry['semilength']
    source=dyck_words(n)
    assert len(source)==entry['word_count']
    code=entry['optimal_code_bitmasks']
    assert len(code)==entry['integer_optimum']==len(set(code))
    assert all(w in source for w in code)
    assert all((a^b).bit_count()>=4 for a,b in combinations(code,2))
    seen=set()
    for w in code:
        o=outputs(w,n)
        assert seen.isdisjoint(o)
        seen|=o
    p={int(w):Fraction(v) for w,v in entry['fractional_primal']}
    d={int(w):Fraction(v) for w,v in entry['fractional_dual']}
    assert all(v>=0 for v in p.values()) and all(v>=0 for v in d.values())
    assert set(p)<=set(source)
    allouts=set().union(*(outputs(w,n) for w in source))
    assert set(d)<=allouts
    assert all(sum(d.get(y,0) for y in outputs(w,n))>=1 for w in source)
    assert all(sum(p.get(w,0) for w in source if y in outputs(w,n))<=1 for y in allouts)
    objp=sum(p.values());objd=sum(d.values())
    assert objp==objd==Fraction(entry['fractional_optimum'])
    print(f'EXACT_CERT_OK n={n} source={len(source)} integer_witness={len(code)} fractional={objp}')
assert [x['integer_optimum'] for x in obj['instances']]==[1,1,2,4,10,22]
assert [Fraction(x['fractional_optimum']) for x in obj['instances']]==[1,1,2,4,10,26]
print('EXACT_ALL_OK')
