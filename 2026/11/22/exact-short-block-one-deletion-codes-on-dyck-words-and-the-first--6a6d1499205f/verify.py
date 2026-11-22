#!/usr/bin/env python3
"""Exact-arithmetic checker of six finite Dyck deletion-code certificates."""
import json
from fractions import Fraction
from pathlib import Path

EXPECTED_INTEGER = (1, 1, 2, 4, 9, 24)
EXPECTED_FRACTIONAL = (Fraction(1), Fraction(1), Fraction(2), Fraction(4), Fraction(29,3), Fraction(3269,131))

def dyck(n):
    def go(word, ups, downs):
        if ups == n and downs == n:
            yield word
        if ups < n:
            yield from go(word+'1', ups+1, downs)
        if downs < ups:
            yield from go(word+'0', ups, downs+1)
    return set(go('', 0, 0))

def descendants(word):
    return {word[:i]+word[i+1:] for i in range(len(word))}

cert = json.loads((Path(__file__).resolve().parent/'certificates.json').read_text(encoding='utf-8'))
assert set(cert) == {str(i) for i in range(1,7)}
for n in range(1,7):
    data=cert[str(n)]
    universe=dyck(n)
    outputs=set().union(*(descendants(word) for word in universe))
    C=data['code']
    assert len(C)==len(set(C))==EXPECTED_INTEGER[n-1] and set(C)<=universe
    seen=set()
    for x in C:
        assert not (seen & descendants(x)), ('duplicate read',n,x)
        seen.update(descendants(x))
    primal={x:Fraction(val) for x,val in data['fractional_primal'].items()}
    dual={y:Fraction(val) for y,val in data['fractional_dual'].items()}
    assert set(primal)<=universe and set(dual)<=outputs
    assert all(val>0 for val in primal.values()) and all(val>0 for val in dual.values())
    assert all(sum((primal.get(w,Fraction(0)) for w in universe if y in descendants(w)),Fraction(0))<=1 for y in outputs)
    assert all(sum((dual.get(y,Fraction(0)) for y in descendants(w)),Fraction(0))>=1 for w in universe)
    ptotal=sum(primal.values(),Fraction(0))
    dtotal=sum(dual.values(),Fraction(0))
    assert ptotal==dtotal==EXPECTED_FRACTIONAL[n-1]
    assert EXPECTED_INTEGER[n-1]==ptotal.numerator//ptotal.denominator
    print('verified semilength',n,'Dyck',len(universe),'outputs',len(outputs),'code',len(C),'LP',ptotal)
assert EXPECTED_FRACTIONAL[4] > EXPECTED_INTEGER[4]
assert all(EXPECTED_FRACTIONAL[i] == EXPECTED_INTEGER[i] for i in range(4))
print('EXACT_DYCK_CERTIFICATES_OK')
