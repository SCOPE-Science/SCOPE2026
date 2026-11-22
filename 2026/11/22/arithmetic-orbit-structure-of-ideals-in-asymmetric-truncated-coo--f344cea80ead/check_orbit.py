"""Exhaustive ideal-orbit enumeration for prime finite fields."""
from collections import Counter
from math import gcd
from check_characteristic_ideals import all_subspaces, canonical, mat_transform, apply, multiply_basis, in_span


def actual_orbits(m,n,p):
    d=m+n-2
    nx=[multiply_basis(m,n,'x',j) for j in range(d)]
    ny=[multiply_basis(m,n,'y',j) for j in range(d)]
    gens=[mat_transform(m,n,p,k) for k in ('x_socle','y_socle','x_jet','y_jet','x_scale','y_scale')]
    ideals=set()
    for rows in all_subspaces(d,p):
        if all(in_span(tuple(sum(row[i]*nx[i][j] for i in range(d))%p for j in range(d)),rows,p,d) and
               in_span(tuple(sum(row[i]*ny[i][j] for i in range(d))%p for j in range(d)),rows,p,d) for row in rows):
            ideals.add(rows)
    remaining=set(ideals)
    sizes=[]
    while remaining:
        head=remaining.pop()
        seen={head}
        boundary=[head]
        for rows in boundary:
            for cols in gens:
                target=canonical([apply(row,cols,p) for row in rows],p,d)
                assert target in ideals
                if target not in seen:
                    seen.add(target)
                    boundary.append(target)
                    remaining.discard(target)
        sizes.append(len(seen))
    sizes.append(1) # unit ideal
    return dict(sorted(Counter(sizes).items()))


def predicted_orbits(m,n,q):
    out=Counter({1:m*n-1, q:2})
    for u in range(1,m):
        for v in range(1,n):
            if (u,v) in ((1,n-1),(m-1,1)):
                continue
            g=gcd(gcd(q-1,u),v)
            out[(q-1)//g]+=g
    return dict(sorted(out.items()))

if __name__=='__main__':
    for m,n,p in [(3,4,2),(3,4,3),(3,4,5),(3,5,2),(3,5,3),(4,5,2)]:
        got=actual_orbits(m,n,p)
        want=predicted_orbits(m,n,p)
        print(f'{m},{n},{p}: orbit_size_multiplicities={got}; predicted={want}')
        assert got==want
    print('IDEAL_AUTOMORPHISM_ORBITS_VERIFIED')
