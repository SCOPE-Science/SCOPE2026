#!/usr/bin/env python3
"""Exact finite checks for rotation quotients of two-subset Kneser independence complexes."""
from itertools import combinations
from math import comb, gcd


def translate(face,n,k):
    return frozenset(tuple(sorted(((a+k)%n,(b+k)%n))) for a,b in face)


def orbit(face,n):
    return frozenset(translate(face,n,k) for k in range(n))


def signed_step(d,n):
    d %= n
    m=(n-1)//2
    assert 1<=d<n
    return d if d<=m else d-n


def triangle_orbits(n):
    unseen=set(combinations(range(n),3))
    reps=[]
    while unseen:
        triple=min(unseen)
        equiv={tuple(sorted((x+k)%n for x in triple)) for k in range(n)}
        assert len(equiv)==n
        unseen.difference_update(equiv)
        reps.append(triple)
    return reps


def original_faces(n):
    families=set()
    for i in range(n):
        star=[tuple(sorted((i,j))) for j in range(n) if j!=i]
        for k in range(1,n):
            for face in combinations(star,k):
                families.add(frozenset(face))
    for i,j,k in combinations(range(n),3):
        families.add(frozenset(((i,j),(i,k),(j,k))))
    return families


def check(n,full=True):
    assert n>=5 and gcd(n,6)==1
    m=(n-1)//2
    orbit_reps=triangle_orbits(n)
    assert len(orbit_reps)==comb(n,3)//n
    orbits={frozenset(tuple(sorted((a+k)%n for a in tr)) for k in range(n)):tr for tr in orbit_reps}
    chosen=[]
    for j in range(1,m+1):
        tri=(0,j,j+1)
        key=frozenset(tuple(sorted((a+k)%n for a in tri)) for k in range(n))
        assert key in orbits and key not in chosen
        chosen.append(key)
    count={-1:0,0:0,1:0}
    for a,b,c in orbit_reps:
        v=sum(signed_step(delta,n) for delta in (b-a,c-b,a-c))
        assert v%n==0 and abs(v)<=n
        count[v//n]+=1
    assert sum(count.values())==len(orbit_reps)
    assert len(chosen)==m
    for j in range(1,m):
        assert signed_step(j,n)+signed_step(1,n)+signed_step(-j-1,n)==0
    assert signed_step(m,n)+signed_step(1,n)+signed_step(-m-1,n)==n
    rank=(n-1)*(n-5)//6
    assert len(orbit_reps)-m==rank
    assert (1+comb(n-1,3))//n==1+rank
    if full:
        faces=original_faces(n)
        assert all(len(orbit(f,n))==n for f in faces)
        counts={k:0 for k in range(1,n)}
        for face in faces: counts[len(face)]+=1
        chi=sum((-1)**(k-1)*v//1 for k,v in counts.items())
        assert chi==1+comb(n-1,3)
        assert sum((-1)**(k-1)*v//n for k,v in counts.items())==1+rank
        print(f'n={n}, faces={len(faces)}, simplex_counts={[counts[k] for k in range(1,n)]}, '
              f'quotient_cells={(1,m,len(orbit_reps))}, cycle_relator_exponents={count}, sphere_rank={rank}')
    else:
        print(f'n={n}, triangle_orbits={len(orbit_reps)}, edge_orbits={m}, '
              f'cycle_relator_exponents={count}, sphere_rank={rank}')

if __name__=='__main__':
    for n in (5,7,11): check(n,True)
    for n in (13,17,19,25,35): check(n,False)
    print('ALL_ROTATION_QUOTIENT_CHECKS_OK')
