"""Exhaustive verification of the unit-conjugacy orbit theorem for graph cycles.

Run: python3 check_cycle_units.py

All maps are represented as tuples of images of vertices 0,...,n-1.
No external packages are used.
"""
from collections import Counter
from itertools import combinations, product
from math import comb


def endomorphisms(n):
    for a in range(n):
        for positive in combinations(range(n), n // 2):
            pos = set(positive)
            steps = [1 if i in pos else -1 for i in range(n)]
            outputs = [a]
            for d in steps[:-1]:
                outputs.append((outputs[-1] + d) % n)
            assert (outputs[-1] + steps[-1]) % n == a
            yield tuple(outputs)
        yield tuple((a + i) % n for i in range(n))
        yield tuple((a - i) % n for i in range(n))


def dihedral(n):
    return ([tuple((i + k) % n for i in range(n)) for k in range(n)]
            + [tuple((k - i) % n for i in range(n)) for k in range(n)])


def predicted(n):
    m=n//2
    big=comb(n,m)
    h=(comb(m,m//2) if m%2==0
       else comb(m-1,(m-1)//2))
    vertex=4+(2*h if m%2==0 else 0)
    edge=4+(2*h if m%2==0 else 4*h)
    return big,h,vertex,edge


def actual_orbit_histogram(endos,units):
    n=len(units[0]); seen=set(); hist=Counter(); nonsingular=Counter()
    inverses=[]
    for u in units:
        inv=[0]*n
        for x,y in enumerate(u):inv[y]=x
        inverses.append(tuple(inv))
    for f in endos:
        if f in seen:continue
        orb={tuple(u[f[iv[i]]] for i in range(n)) for u,iv in zip(units,inverses)}
        seen.update(orb)
        hist[len(orb)]+=1
        if len(set(f)) != n: nonsingular[len(orb)]+=1
    assert len(seen)==len(endos)
    return hist,nonsingular


def run(n):
    assert n>=4 and n%2==0
    E=list(endomorphisms(n))
    assert len(E)==len(set(E))==n*(comb(n,n//2)+2)
    D=dihedral(n)
    fixed=[]
    for u in D:
        fixed.append(sum(all(f[u[i]] == u[f[i]] for i in range(n)) for f in E))
    B,H,V,W=predicted(n)
    expected=([len(E)]+[2*n if k==n//2 else n for k in range(1,n)]
               + [V if k%2==0 else W for k in range(n)])
    assert fixed==expected,('centralizer',n,fixed,expected)
    orbits_total=(B+n+6+2*H)//2
    assert sum(fixed)==2*n*orbits_total
    assert B%2==0
    if n<=10:
        hist,singular=actual_orbit_histogram(E,D)
        assert sum(hist.values())==orbits_total
        assert singular==Counter({n:2*H,2*n:B//2-H}),(n,singular)
    return {'n':n,'endomorphisms':len(E),'vertex_centralizer':V,
            'edge_centralizer':W,'singular_n_orbits':2*H,
            'singular_2n_orbits':B//2-H,'all_orbits':orbits_total}


def odd_cycle_check(n):
    assert n>=5 and n%2==1
    units=dihedral(n)
    hist,_=actual_orbit_histogram(units,units)
    expected=Counter({1:1,2:(n-1)//2,n:1})
    assert hist==expected,(n,hist,expected)
    return {'n':n,'endomorphisms':len(units),'all_orbits':sum(hist.values())}


def unstructured_check(n):
    # Independent enumeration of ALL n^n self-maps, not using a step-word parametrization.
    full=set()
    for f in product(range(n),repeat=n):
        if all((f[(i+1)%n]-f[i])%n in (1,n-1) for i in range(n)):
            full.add(f)
    assert full==set(endomorphisms(n))


if __name__=='__main__':
    for n in (4,6,8,10,12):
        print(run(n))
    for n in (5,7,9,11):
        print(odd_cycle_check(n))
    for n in (4,6):
        unstructured_check(n)
    print('CYCLE_ENDOMORPHISM_UNIT_COMMUTANT_CHECKS_PASSED')
