#!/usr/bin/env python3
"""Difference-support conflict test plus independent fiber capacity certificate."""
import itertools, json
from pathlib import Path
C=json.loads(Path(__file__).with_name('codebooks.json').read_text())
for n in range(2,8):
    allwords=[''.join(w) for w in itertools.product('012',repeat=n)
              if all(w[i]!=w[i+1] for i in range(n-1))]
    assert len(allwords)==3*2**(n-1)
    chosen=C[str(n)]
    assert all(w in allwords for w in chosen)
    intervals=[frozenset((i,i+1)) for i in range(n-1)]
    unions=[i|j for i in intervals for j in intervals]
    for u,v in itertools.combinations(chosen,2):
        support={i for i in range(n) if u[i]!=v[i]}
        assert all(not support.issubset(k) for k in unions),(u,v)
    if n<=4:
        assert len(chosen)==1
        assert any(len(k)==n for k in unions) or n<4
    else:
        groups={}
        for w in allwords:
            groups.setdefault(w[2:-2],[]).append(w)
        assert len(groups)==3*2**(n-5)
        assert set(w[2:-2] for w in chosen)==set(groups)
        assert all(len(v)==16 for v in groups.values())
        for fiber in groups.values():
            assert all(set(i for i in range(n) if u[i]!=v[i]).issubset({0,1,n-2,n-1})
                       for u,v in itertools.combinations(fiber,2))
    print('n=',n,'source=',len(allwords),'size=',len(chosen),'upper=',1 if n<=4 else len(groups))
# General-q five-symbol family: w^(a)_i=a+i (mod q), for all a in Z_q.
for q in range(2,12):
    words=[tuple((a+i)%q for i in range(5)) for a in range(q)]
    assert all(all(w[i]!=w[i+1] for i in range(4)) for w in words)
    assert all(sum(x!=y for x,y in zip(u,v))==5
               for u,v in itertools.combinations(words,2))
print('ALTERNATE_OK')
