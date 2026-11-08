"""Exact exhaustive census for three-by-three terminal-agent proposal histories.

Only Python standard library. Run: python reachability_verify.py
"""
from itertools import permutations, product
from collections import Counter
from fractions import Fraction

P = tuple(permutations(range(3)))
ENC = {p:i for i,p in enumerate(P)}
FULL = P
SUB = []
for missing in range(6):
    if missing < 3:
        men = tuple(i for i in range(3) if i != missing)
        SUB.append(tuple(tuple(dict(zip(men, ps)).get(i, -1) for i in range(3))
                         for ps in permutations(range(3), 2)))
    else:
        women = tuple(j for j in range(3) if j != missing-3)
        SUB.append(tuple(tuple(a) for a in product((-1,)+women, repeat=3)
                         if sorted(x for x in a if x >= 0) == list(women)))
        # Above list comprises exactly two matched men and one unmatched man.

def acceptable_stable(a, missing, rank_m, rank_w):
    inv = [-1]*3
    for i,w in enumerate(a):
        if w>=0:
            if inv[w]!=-1 or i==missing or w+3==missing: return False
            inv[w]=i
    if 0<=missing<3 and a[missing]!=-1: return False
    for i in range(3):
        if i==missing: continue
        mi = a[i]
        for j in range(3):
            if j+3==missing: continue
            if rank_m[i][j]<(3 if mi<0 else rank_m[i][mi]):
                if rank_w[j][i]<(3 if inv[j]<0 else rank_w[j][inv[j]]):
                    return False
    return True

def final_after_entry(missing, initial, pm, pw, rm, rw):
    a = list(initial)
    if missing < 3:
        wpartner = [-1]*3
        for i,w in enumerate(a):
            if w>=0: wpartner[w]=i
        man = missing
        for _ in range(10):
            displaced = None
            for w in pm[man]:
                prior = wpartner[w]
                if prior < 0 or rw[w][man]<rw[w][prior]:
                    a[man]=w
                    wpartner[w]=man
                    if prior < 0: return tuple(a)
                    a[prior]=-1
                    displaced=prior
                    break
            if displaced is None: return tuple(a)
            man=displaced
    else:
        woman = missing-3
        for _ in range(10):
            displaced = None
            for man in pw[woman]:
                prior = a[man]
                if prior < 0 or rm[man][woman]<rm[man][prior]:
                    a[man]=woman
                    if prior < 0: return tuple(a)
                    displaced=prior
                    break
            if displaced is None: return tuple(a)
            woman=displaced
    raise AssertionError('Unexpectedly long proposal chain')

def orbit_of_cyclic_example():
    men = ((0,1,2),(1,2,0),(2,0,1))
    women = ((1,2,0),(2,0,1),(0,1,2))
    orbit = set()
    for new_m in P:
        for new_w in P:
            m2=[None]*3; w2=[None]*3
            for old in range(3):
                m2[new_m[old]]=tuple(new_w[j] for j in men[old])
                w2[new_w[old]]=tuple(new_m[i] for i in women[old])
            orbit.add(tuple(ENC[p] for p in m2+w2))
    assert len(orbit)==12, len(orbit)
    return orbit

def census():
    orbit = orbit_of_cyclic_example()
    distro = Counter(); bad = set()
    for codes in product(range(6), repeat=6):
        pm = tuple(P[c] for c in codes[:3]); pw = tuple(P[c] for c in codes[3:])
        rm = tuple(tuple(p.index(j) for j in range(3)) for p in pm)
        rw = tuple(tuple(p.index(i) for i in range(3)) for p in pw)
        stable = tuple(a for a in FULL if acceptable_stable(a,-1,rm,rw))
        reached = set()
        for missing in range(6):
            partial_stable = tuple(a for a in SUB[missing] if acceptable_stable(a, missing, rm, rw))
            assert 1 <= len(partial_stable) <= 2
            for a in partial_stable:
                end=final_after_entry(missing,a,pm,pw,rm,rw)
                assert acceptable_stable(end,-1,rm,rw),(codes,missing,a,end,pm,pw)
                reached.add(end)
        assert reached <= set(stable)
        distro[len(stable),len(reached)]+=1
        if len(stable)!=len(reached): bad.add(codes)
    expected = {(1,1):34080,(2,2):11484,(3,2):12,(3,3):1080}
    assert distro == expected,(distro, expected)
    assert bad==orbit,(len(bad),len(orbit),bad-orbit,orbit-bad)
    print('Exact distribution:', sorted(distro.items()))
    print('Unreachable-profile count:',len(bad),'out of',6**6,'=',Fraction(len(bad),6**6))
    print('Bad profiles form exactly the 12-element relabeling orbit of the cyclic market.')
if __name__=='__main__': census()
