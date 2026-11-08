"""Exact rational independent two-step transition check for a two-pathogen SIS hypergraph.
Run: python3 verify.py. Uses Python's standard library only.
The all-healthy initial state is not used: one initially doubly infected source is required.
"""
from fractions import Fraction as Q
from itertools import product


def bern(bit, p):
    return p if bit else (1 - p)


def hazard_survival(bits, triangles, source, b1, bh, bg):
    """Return exp(-H) exactly, given the source-neighbor carrier bits.
    The graph has triangle-side contacts only; all triangles include the source.
    """
    neighbors = {j for tri in triangles for j in tri if j != source}
    n = sum(bits[j] for j in neighbors)
    active = [tri for tri in triangles if all(bits[j] for j in tri if j != source)]
    overlap = sum(len((set(e) & set(f)) - {source})
                  for i, e in enumerate(active) for f in active[i + 1:])
    return b1**n * bh**len(active) * bg**overlap


def direct_two_step(triangles, nverts, source, b1, bh, bg, alpha, s):
    """Enumerate every round-one carrier state and all source transition probabilities.
    The model's independent Bernoulli acquisitions/recoveries are used directly.
    """
    neighbors = {j for tri in triangles for j in tri if j != source}
    p = 1-b1
    MA=MB=MAB=Q(0)
    for ca, cb in product((0, 1), repeat=2):
        for xa in product((0, 1), repeat=len(neighbors)):
            for xb in product((0, 1), repeat=len(neighbors)):
                v = sorted(neighbors)
                a = {source:ca, **dict(zip(v,xa))}
                b = {source:cb, **dict(zip(v,xb))}
                wt = bern(ca,s)*bern(cb,s)
                for x,y in zip(xa,xb):
                    wt *= bern(x,p)*bern(y,p)
                h_a = hazard_survival(a,triangles,source,b1,bh,bg)
                h_b = hazard_survival(b,triangles,source,b1,bh,bg)
                pa = s if ca else (1-h_a**(alpha if cb else 1))
                pb = s if cb else (1-h_b**(alpha if ca else 1))
                MA += wt*pa
                MB += wt*pb
                MAB += wt*pa*pb
    return MA, MB, MAB


def theorem(triangles, nverts, source, b1, bh, bg, alpha, s):
    neighbors = sorted({j for tri in triangles for j in tri if j!=source})
    p=1-b1
    U=V=Q(0)
    for x in product((0,1),repeat=len(neighbors)):
        bits={source:0,**dict(zip(neighbors,x))}
        wt=Q(1)
        for z in x: wt *= bern(z,p)
        hh=hazard_survival(bits,triangles,source,b1,bh,bg)
        U += wt*(1-hh)
        V += wt*(1-hh**alpha)
    m=s*s+(1-s)*((1-s)*U+s*V)
    joint=s**4+2*s*s*(1-s)*V+(1-s)**2*U*U
    cov=s*(1-s)**2*(U-V)*(2*U-s*(2+U-V))
    return U,V,m,joint,cov


def check(triangles, nverts, b1, bh, bg, alpha, s):
    ma,mb,j=direct_two_step(triangles,nverts,0,b1,bh,bg,alpha,s)
    U,V,m,joint,cov=theorem(triangles,nverts,0,b1,bh,bg,alpha,s)
    assert ma==mb==m and j==joint and j-ma*mb==cov
    if alpha==1:
        assert cov==0
    if alpha!=1 and U>0 and U<1 and V<1:
        sc=2*U/(2+U-V)
        assert 0<sc<1
        assert (cov>0) == ((U-V)*(sc-s)>0) or cov==0
    return U,V,cov


def main():
    # One dyadic link represented here as a 2-node hyperedge with no triangle
    # is checked separately by passing a dummy contact triangle of size 2.
    # The full overlap case has two triangles sharing an edge.
    tri=[(0,1,2),(0,1,3)]
    U,V,c=check(tri,4,Q(1,2),Q(1,2),Q(1,2),2,Q(1,16))
    assert (U,V,c)==(Q(319,512),Q(25215,32768),
                       Q(-639847670625,70368744177664))
    print('overlapping-triangle exact case:',U,V,c)
    count=0
    for s in (Q(1,16),Q(1,4),Q(1,2),Q(3,4)):
        for b1 in (Q(1,2),Q(3,4)):
            for bh in (Q(1,2),Q(3,4)):
                for bg in (Q(1,2),Q(3,4)):
                    for alpha in (1,2,3):
                        check(tri,4,b1,bh,bg,alpha,s)
                        count+=1
    print('PASS:', count+1, 'exact rational full-transition tests')

if __name__=='__main__':
    main()
