#!/usr/bin/env python3
"""Weighted-fiber sample checks using independent face enumeration and modular ranks."""
import itertools
from math import prod
from check_double_star import rankmod

def run(p,q,sizes,primes=(2,101)):
    m=p+q+2
    assert len(sizes)==m and all(s>=2 for s in sizes)
    offsets=[0]
    for s in sizes:offsets.append(offsets[-1]+s)
    bad={(i,p+q) for i in range(p)}|{(p+i,p+q+1) for i in range(q)}|{(p+q,p+q+1)}
    dd={-1:{()}}
    for r in range(1,m+1):
        for inds in itertools.combinations(range(m),r):
            if any(a in inds and b in inds for a,b in bad):continue
            for cs in itertools.product(*(range(sizes[i]) for i in inds)):
                ff=tuple(offsets[i]+c for i,c in zip(inds,cs))
                dd.setdefault(r-1,set()).add(ff)
    f=[sorted(dd.get(d,set())) for d in range(-1,m)]
    def b(prime):
        ranks=[]
        for d in range(m):
            low=f[d]; high=f[d+1]; idx={x:i for i,x in enumerate(low)}
            cols=[{idx[t[:i]+t[i+1:]]:(-1)**i for i in range(len(t))} for t in high]
            ranks.append(rankmod(cols,len(low),prime))
        return {d:len(f[d+1])-ranks[d]-ranks[d+1] for d in range(m-1) if len(f[d+1])-ranks[d]-ranks[d+1]}
    P=prod(s-1 for s in sizes[:p]);Q=prod(s-1 for s in sizes[p:p+q])
    exp={p+q-1:P*Q,p:sizes[-1]*P,q:sizes[-2]*Q}
    if p==q:exp[p]=sizes[-1]*P+sizes[-2]*Q
    for prime in primes:
        got=b(prime)
        assert got==exp,(p,q,sizes,prime,got,exp)
    print(f'weighted p={p} q={q} sizes={sizes}: {exp}; faces={sum(map(len,f))}; PASS')

if __name__=='__main__':
    run(2,2,[2,3,2,4,2,3]);run(2,3,[2,3,2,4,2,3,2]);run(3,2,[2,2,3,2,4,2,3]);print('PASS all weighted samples')
