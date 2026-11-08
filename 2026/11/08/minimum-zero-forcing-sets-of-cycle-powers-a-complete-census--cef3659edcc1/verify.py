"""Reproduce the zero-forcing minimum-set classification on cycle powers.
Pure Python standard library. All checks use exact finite integer/set operations.
These finite tests support, but do not replace, the unrestricted proof.
"""
from collections import Counter
from itertools import combinations


def graph(n,k):
    assert n >= 2*k+1 and k>=1
    return [frozenset((v+d)%n for d in range(-k,k+1) if d) for v in range(n)]


def closure(nbrs, blue):
    blue=set(blue)
    history=[]
    while True:
        forcing=set()
        for v in blue:
            whites=nbrs[v]-blue
            if len(whites)==1:
                forcing.update(whites)
        if not forcing:
            break
        history.append(len(forcing))
        blue.update(forcing)
    return frozenset(blue), history


def predicted(n,k):
    if n==2*k+1: return n
    if n==2*k+2: return n*k
    return n*(2*k-1)


def families(n,k):
    nb=graph(n,k)
    reps=Counter()
    for v in range(n):
        for w in nb[v]:
            B=frozenset((nb[v]-{w})|{v})
            assert len(B)==2*k
            reps[B]+=1
    return reps


def exhaustive():
    tested=0
    for n in range(3,14):
        for k in range(1,(n-1)//2+1):
            # test all k with n>=2k+1 and nontrivial n; budget ~2^15
            nbrs=graph(n,k)
            good=set()
            for B in combinations(range(n), 2*k):
                out,_=closure(nbrs, B)
                if len(out)==n:
                    good.add(frozenset(B))
            reps=families(n,k)
            assert set(reps)==good,(n,k,'classification',len(reps),len(good))
            assert len(good)==predicted(n,k),(n,k,len(good),predicted(n,k))
            if n>=2*k+3:
                assert Counter(reps.values())==Counter({1:2*n*(k-1),2:n}) if k>1 else Counter({2:n})
            if n==2*k+2:
                assert set(reps.values())=={2}
            if n==2*k+1:
                assert set(reps.values())=={2*k}
            tested+=1
    print('ALL_MINIMUM_SETS_EXHAUSTIVE_OK',tested)


def larger_representations():
    for n in range(3,41):
        for k in range(1,(n-1)//2+1):
            if n*k>500: continue
            rep=families(n,k)
            assert len(rep)==predicted(n,k),(n,k)
            for B in rep:
                colored,stages=closure(graph(n,k),B)
                assert len(colored)==n,(n,k,B)
    print('ALL_REPRESENTED_SETS_FORCE_OK through n=40')

def dihedral_orbits():
    # Separate independent check of the claimed k orbit types, with actual dihedral permutations.
    cases=0
    for n in range(7,26):
        for k in range(2,(n-3)//2+1):
            unseen=set(families(n,k))
            orbit_sizes=[]
            while unseen:
                sample=next(iter(unseen))
                orbit={frozenset((a*v+t)%n for v in sample) for a in (-1,1) for t in range(n)}
                assert orbit<=unseen,(n,k,'orbit closure')
                unseen-=orbit
                orbit_sizes.append(len(orbit))
            assert sorted(orbit_sizes)==[n]+[2*n]*(k-1),(n,k,orbit_sizes)
            cases+=1
    print('DIHEDRAL_ORBITS_EXACT_OK',cases)

if __name__=='__main__':
    exhaustive()
    larger_representations()
    dihedral_orbits()
    print('VERIFY_OK')
