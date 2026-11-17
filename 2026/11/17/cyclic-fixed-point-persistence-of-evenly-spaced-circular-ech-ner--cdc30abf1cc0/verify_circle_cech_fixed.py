"""Exact verification of the cyclic fixed-space model for interval nerve complexes.
Uses orbit-saturated face enumeration, independent integer-gap test, and quotient interval enumeration.
"""
from itertools import combinations

def cyclic_intervals(n,k):
    # The empty-set nerve convention is immaterial to the nonempty face test.
    return [sum(1 << ((j+t)%n) for t in range(k+1)) for j in range(n)]

def is_interval_face(S,n,intervals):
    return any((S & I)==S for I in intervals)

def orbit_masks(n,d):
    m=n//d
    return [sum(1 << (i+j*m) for j in range(d)) for i in range(m)]

def gap_face(selected,n,k):
    if not selected:return True
    V=sorted(selected)
    gaps=[(V[(i+1)%len(V)]-V[i])%n or n for i in range(len(V))]
    return max(gaps)>=n-k

def main():
    test_count=0
    total_masks=0
    for n in range(2,25):
        for d in range(2,n+1):
            if n%d:continue
            m=n//d
            orbits=orbit_masks(n,d)
            for k in range(0,n):
                raw=cyclic_intervals(n,k)
                s=k-(d-1)*m
                smaller=cyclic_intervals(m,s) if s>=0 else []
                for subset in range(1,1<<m):
                    union=0
                    verts=[]
                    for i in range(m):
                        if (subset>>i)&1:
                            union |= orbits[i]
                            verts.extend(i+j*m for j in range(d))
                    original=is_interval_face(union,n,raw)
                    independent_gap=gap_face(verts,n,k)
                    target=s>=0 and is_interval_face(subset,m,smaller)
                    assert original==independent_gap==target,(n,d,m,k,subset,original,independent_gap,target)
                    total_masks+=1
                test_count+=1
    # Residual rotation and reflection must agree on the quotient orbit labels.
    dihedral_checks=0
    for n in range(2,25):
        for d in range(2,n+1):
            if n%d: continue
            m=n//d
            OM=orbit_masks(n,d)
            def image(mask,fn):
                return sum(1<<fn(i) for i in range(n) if (mask>>i)&1)
            for a in range(m):
                assert image(OM[a],lambda x:(x+1)%n)==OM[(a+1)%m]
                assert image(OM[a],lambda x:(-x)%n)==OM[(-a)%m]
                dihedral_checks+=2
    print(f'CIRCULAR_ARC_FIXED_FILTRATION_PASS parameters={test_count} orbit_subset_checks={total_masks} dihedral_orbit_checks={dihedral_checks}')
    # Nontrivial example: order 3 subgroup of 18-cycle at k=12 gives N(6,0): six points.
    n,d,k=18,3,12
    m=n//d; s=k-(d-1)*m
    assert (m,s)==(6,0)
    # At k=15, fixed complex N(6,3), two 2-spheres in homotopy.
    assert (15-(d-1)*m)==3
    print('EXAMPLE n=18 d=3 k=12 fixed=N(6,0); k=15 fixed=N(6,3)~two S2')
if __name__=='__main__':main()
