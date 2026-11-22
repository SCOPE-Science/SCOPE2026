"""Independent exhaustive computation of ternary hare images (Python 3, stdlib)."""
from itertools import product
from collections import defaultdict
from math import comb

def hare(w):
    if not w:
        return ''
    high=max(w)
    parts=w.split(high)
    return ''.join(hare(s) for s in parts)+high*(len(parts)-1)

def criterion(w):
    c=len(w)-len(w.rstrip('2'))
    u=w[:len(w)-c]
    if '2' in u:
        return False
    return sum(u[i:i+2]=='10' for i in range(len(u)-1))<=c

for n in range(11):
    seen=set(); seen_by_content=defaultdict(set)
    for p in product('012',repeat=n):
        w=''.join(p)
        t=hare(w)
        seen.add(t)
        content=(w.count('0'),w.count('1'),w.count('2'))
        seen_by_content[content].add(t)
    lang={''.join(p) for p in product('012',repeat=n) if criterion(''.join(p))}
    assert seen==lang, (n,'language',seen^lang)
    for (a,b,c), targets in seen_by_content.items():
        expected=sum(comb(a,d)*comb(b,d) for d in range(min(a,b,c)+1))
        assert len(targets)==expected,(n,a,b,c,len(targets),expected)
    print('n=%2d images=%4d Parikh_classes=%2d PASS'%(n,len(seen),len(seen_by_content)))
print('PASS all ternary source words and candidate output words through length 10')
