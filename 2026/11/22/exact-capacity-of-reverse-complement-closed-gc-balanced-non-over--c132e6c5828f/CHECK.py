#!/usr/bin/env python3
"""Exact non-overlapping DNA GC-balanced reverse-complement codebook search."""
from itertools import product
from time import perf_counter
ALPHA='ATCG'
COMP=str.maketrans('ATCG','TAGC')
def rc(w):return w.translate(COMP)[::-1]
def nonoverlap(u,v):
    return all(u[-k:]!=v[:k] and v[-k:]!=u[:k] for k in range(1,6))

def solve():
    st=perf_counter()
    words=[''.join(w) for w in product(ALPHA,repeat=6) if sum(x in 'CG' for x in w)==3]
    seen=set(); orbits=[]
    for w in words:
        if w in seen:continue
        r=rc(w);seen.update((w,r))
        if nonoverlap(w,w) and nonoverlap(r,r) and nonoverlap(w,r):
            orbits.append((w,r))
    assert len(words)==1280 and len(orbits)==248
    n=len(orbits); adj=[0]*n; compat_edges=0
    for i in range(n):
        for j in range(i+1,n):
            ok=all(nonoverlap(x,y) for x in orbits[i] for y in orbits[j])
            if ok:
                adj[i]|=1<<j;adj[j]|=1<<i;compat_edges+=1
    assert compat_edges==9048
    # A clique of the compatibility graph is a set of nonoverlapping RC pairs.
    # Greedy coloring provides a valid bound on every remaining induced clique.
    best=0; witness=[]; calls=0; branch=0
    def expand(P, chosen):
        nonlocal best,witness,calls,branch
        calls+=1
        if not P:
            if len(chosen)>best:best=len(chosen);witness=chosen[:]
            return
        rem=P; order=[]; colors=[]; c=0
        while rem:
            c+=1; eligible=rem
            while eligible:
                b=eligible & -eligible
                v=b.bit_length()-1
                order.append(v);colors.append(c)
                rem ^= b
                eligible &= ~(b|adj[v])
        prefix=0
        prefixes=[]
        for v in order:
            prefixes.append(prefix)
            prefix |= 1<<v
        for i in range(len(order)-1,-1,-1):
            if len(chosen)+colors[i]<=best: return
            v=order[i]
            branch+=1
            chosen.append(v)
            expand(adj[v]&prefixes[i],chosen)
            chosen.pop()
    expand((1<<n)-1,[])
    assert best==22
    code=sorted(w for j in witness for w in orbits[j]);assert len(code)==44
    assert {rc(w) for w in code}==set(code)
    assert all(nonoverlap(a,b) for a in code for b in code)
    print(f'word_count={len(words)} rc_orbits={len(orbits)} compatibility_edges={compat_edges}')
    print(f'max_orbits={best} max_codewords={2*best} calls={calls} branches={branch} secs={perf_counter()-st:.2f}')
    print('CODE:', ' '.join(code))
    return code
if __name__=='__main__':solve()

# Compare with the separately supplied witness, not just a constructed optimum.
if __name__ == '__main__':
    from pathlib import Path
    supplied = [line.strip() for line in (Path(__file__).parent / 'WITNESS.txt').read_text(encoding='utf-8').splitlines() if line.strip()]
    assert len(supplied) == 44 and len(set(supplied)) == 44
    assert all(len(w) == 6 and sum(c in 'CG' for c in w) == 3 for w in supplied)
    assert {rc(w) for w in supplied} == set(supplied)
    assert all(nonoverlap(a,b) for a in supplied for b in supplied)
    print('supplied_witness_verified=true')
