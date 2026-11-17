#!/usr/bin/env python3
"""Exact finite checks for fixed-cell joins of complete-graph Hom complexes.
Uses only the Python standard library. Does not claim to prove infinite scope.
"""
import itertools
import math

def perms(n): return list(itertools.permutations(range(n)))
def compose(p,q): return tuple(p[q[i]] for i in range(len(p)))
def action_data(n, target):
    group=perms(n); index={g:i for i,g in enumerate(group)}
    if target=='natural_regular':
        pts=list(range(n))+[(g,) for g in group]
        target_action=[]
        for h in group:
            target_action.append(tuple((h[x] if isinstance(x,int) else n+index[compose(h,x[0])]) for x in pts))
    elif target=='two_ordered_pairs':
        pairs=[(i,j) for i in range(n) for j in range(n) if i!=j]
        pts=[(k,p) for k in range(2) for p in pairs]
        loc={p:i for i,p in enumerate(pts)}
        target_action=[tuple(loc[k,(h[i],h[j])] for k,(i,j) in pts) for h in group]
    else: raise ValueError(target)
    return group, pts, target_action

def orbits(acts,n):
    unseen=set(range(n)); ans=[]
    while unseen:
        a=min(unseen); orb=tuple(sorted({act[a] for act in acts}))
        assert set(orb)<=unseen
        unseen.difference_update(orb); ans.append(orb)
    return ans

def equivariant_options(group, acts, nsrc, orbit):
    y=orbit[0]
    # For each source label fixed by the stabilizer, construct the unique
    # orbit-to-source equivariant map with that image of y.
    stab=[k for k,act in enumerate(acts) if act[y]==y]
    options=[]
    for x in range(nsrc):
        if any(group[k][x]!=x for k in stab): continue
        f={}
        for k,act in enumerate(acts):
            if act[y] in f: assert f[act[y]]==group[k][x]
            f[act[y]]=group[k][x]
        assert set(f)==set(orbit)
        options.append(tuple(f[z] for z in orbit))
    return options

def predicted_supports(orbits,opts,n):
    states=[]
    for choices in itertools.product(*([[None]+list(op) for op in opts])):
        if all(c is None for c in choices): continue
        x=[-1]*n
        for orbit,choice in zip(orbits,choices):
            if choice is not None:
                for color,src in zip(orbit,choice): x[color]=src
        states.append(tuple(x))
    return set(states)

def brute_supports(group, acts, nsrc, ncolors):
    # Exhaust all multihomomorphism supports. Every color is either unused or
    # assigned to exactly one source vertex, by K_m disjointness.
    ans=set()
    for x in itertools.product(range(-1,nsrc), repeat=ncolors):
        if set(x[xx] for xx in range(ncolors) if x[xx]>=0)!=set(range(nsrc)):
            continue
        if all(x[acts[k][i]]==(-1 if x[i]==-1 else group[k][x[i]]) for k in range(len(group)) for i in range(ncolors)):
            ans.add(x)
    return ans

def test(n,mode,brute):
    group,pts,acts=action_data(n,mode)
    oo=orbits(acts,len(pts))
    opts=[equivariant_options(group,acts,n,o) for o in oo]
    expected=predicted_supports(oo,opts,len(pts))
    counts=[len(t) for t in opts]
    assert len(expected)==math.prod(x+1 for x in counts)-1
    assert all(set(x)>=set(range(n))|{-1} or set(x)==set(range(n)) for x in expected)
    if brute:
        actual=brute_supports(group,acts,n,len(pts))
        assert actual==expected,(len(actual),len(expected))
    print('GROUP=',f'S_{n}', 'TARGET=',mode, 'TARGET_SIZE=',len(pts),
          'ORBIT_SIZES=',[len(t) for t in oo], 'OPTIONS=',counts,
          'NONEMPTY_INVARIANT_CELLS=',len(expected),
          'BRUTE=',('MATCH' if brute else 'ORBIT_DIRECT_CHECK'))
    if all(x>1 for x in counts):
        print('REDUCED_INTEGRAL_HOMOLOGY=',f'Z^{math.prod(x-1 for x in counts)} in degree {len(counts)-1}')
    else: print('FIXED_SPACE_CONTRACTIBLE')
    return len(expected)

if __name__=='__main__':
    test(3,'natural_regular',True)
    test(4,'two_ordered_pairs',False)
    print('NONABELIAN_HOM_TRANSITIVE_ORBIT_CHECKS_PASS')
