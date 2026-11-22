"""Independent two-choice subsequence deletion recursion and phase-language test."""
from functools import lru_cache
from itertools import product
from math import comb

@lru_cache(None)
def complements(w,u):
    if not u:
        return {w}
    if not w:
        return set()
    out=set()
    for tail in complements(w[1:],u):
        out.add((w[0],)+tail)
    if w[0]==u[0]:
        out.update(complements(w[1:],u[1:]))
    return out

def language(q,r):
    R=tuple(tuple((x+i)%q for x in range(q)) for i in range(q))
    L=set()
    for h in product(range(q+1),repeat=r):
        if any(h[i]>h[i+1] for i in range(r-1)):
            continue
        L.add(tuple(x for a in h for x in R[a%q]))
    return L

cases=0;total=0
for q in range(2,7):
    for r in range(0,5):
        w=tuple(range(q))*(r+1);u=tuple(range(q))
        got=complements(w,u);want=language(q,r)
        assert got==want,(q,r,len(got),len(want),list(got^want)[:4])
        assert len(got)==comb(r+q,q)-r
        cases+=1;total+=len(got)
    complements.cache_clear()
print(f'RECURSION_VERIFY_OK cases={cases} distinct_outputs={total}')
