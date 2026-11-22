#!/usr/bin/env python3
"""Independent finite checks of leaf-injection generator criterion on finite out-forests.
All edges run from the smaller-index parent toward the larger-index child.
"""
from itertools import product
from math import factorial, ceil, log2


def all_forests(n):
    # Each vertex j either begins a new root or picks one smaller parent.
    return product(*(tuple([-1] + list(range(j))) for j in range(n)))


def child_lists(parents):
    out=[[] for _ in parents]
    for j,p in enumerate(parents):
        if p>=0: out[p].append(j)
    return out


def modal_signatures(children, colors):
    """Depth-h ordinary modal observations; same signature means no formula separates."""
    h=[0]*len(children)
    for v in reversed(range(len(children))):
        h[v]=0 if not children[v] else 1+max(h[c] for c in children[v])
    s=[(c,) for c in colors]
    levels=[len(set(s))]
    for _ in range(max(h)):
        s=[(colors[v],frozenset(s[c] for c in children[v])) for v in range(len(s))]
        levels.append(len(set(s)))
    return s,h,levels


def full_modal_boolean_algebra(children, colors, alphabet_bits):
    """Independently construct smallest Boolean / diamond-closed family of truth sets."""
    n=len(children); mask=(1<<n)-1
    family={0,mask}
    for bit in range(alphabet_bits):
        family.add(sum(1<<i for i,c in enumerate(colors) if (c>>bit)&1))
    while True:
        start=len(family); a=list(family)
        for x in a:
            family.add(mask^x)
            family.add(sum(1<<v for v,vs in enumerate(children) if any((x>>j)&1 for j in vs)))
        a=list(family)
        for x in a:
            for y in a:
                family.add(x&y)
        if len(family)==start: return len(family)==(1<<n)


def check():
    instances=0; direct=0; depth_cases=0
    for n in range(1,8):
        for parents in all_forests(n):
            cs=child_lists(parents)
            leaves=[i for i,c in enumerate(cs) if not c]
            for bits in ((0,1,2) if n<=5 else (0,1)):
                if bits==2 and n==5: # n=5 4^5*120 stays affordable
                    pass
                q=1<<bits
                successes=0
                for col in product(range(q),repeat=n):
                    inject=len(set(col[i] for i in leaves))==len(leaves)
                    sig,h,levels=modal_signatures(cs,col)
                    distinct=len(set(sig))==n
                    assert inject==distinct,(n,parents,col,inject,distinct)
                    if distinct:
                        successes+=1
                        assert len(levels)-1==max(h)
                    if n<=5 and bits<=1:
                        direct+=1
                        assert full_modal_boolean_algebra(cs,col,bits)==inject,(parents,col,bits)
                    instances+=1
                falling=1
                for j in range(len(leaves)): falling*=max(0,q-j) if j<q else 0
                assert successes==falling*q**(n-len(leaves)),(n,parents,q,successes,falling)
            depth_cases+=1
    # Sharp depth: identical atom colours on directed paths; root and child
    # indistinguishable at depth h-1, but distinct at depth h.
    for h in range(1,31):
        cs=[([i+1] if i<h else []) for i in range(h+1)]
        col=(0,)*(h+1)
        a=[(0,) for _ in col]
        for d in range(h):
            if d==h-1: assert a[0]==a[1]
            a=[(0,frozenset(a[c] for c in cs[v])) for v in range(h+1)]
        assert a[0]!=a[1]
    print(f'VERIFY_OK coloring_cases={instances} direct_boolean_closures={direct} forest_cases={depth_cases} sharp_paths=30')

if __name__=='__main__': check()
