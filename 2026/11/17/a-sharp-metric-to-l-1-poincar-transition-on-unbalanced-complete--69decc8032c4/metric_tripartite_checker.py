"""Exact finite diagnostics for the sharp metric Poincare constant of K_(a,a,b).

The analytic argument in RESULT.md proves all integer parameters; these tests
only corroborate the orbit reduction, threshold and metric witnesses.
"""
from fractions import Fraction
from itertools import product


def metric_constant(a,b):
    n=2*a+b
    edges=a*a+2*a*b
    pairs=n*(n-1)//2
    graph=Fraction(edges+2*a*(a-1)+b*(b-1),pairs)
    collapsed=Fraction(a+2*b,n)
    return max(graph,collapsed)


def orbit_ratio(a,b,t):
    # The symmetrized metric has cross distances z=t and w=1.
    # Maximal within-class distances are x=2 min(t,1), y=2.
    t=Fraction(t)
    edges=a*a+2*a*b
    pairs=(2*a+b)*(2*a+b-1)//2
    edge_energy=a*a*t+2*a*b
    pair_energy=edge_energy+2*a*(a-1)*min(t,1)+b*(b-1)
    return Fraction(edges,pairs)*pair_energy/edge_energy


def cut_support_check(a,b):
    # Cut metrics must satisfy the metric bound too; we enumerate all
    # block-cardinality triples rather than all 2^(2a+b) vertex cuts.
    edges=a*a+2*a*b
    n=2*a+b
    pairs=n*(n-1)//2
    target=metric_constant(a,b)
    c=0
    for x,y,z in product(range(a+1),range(a+1),range(b+1)):
        k=x+y+z
        if k in (0,n):
            continue
        numerator=k*(n-k)
        denominator=x*(a-y)+y*(a-x)+(x+y)*(b-z)+(2*a-x-y)*z
        assert denominator>0
        ratio=Fraction(edges,pairs)*Fraction(numerator,denominator)
        assert ratio<=target,(a,b,x,y,z,ratio,target)
        c+=1
    return c


def l1_obstruction_check():
    comparisons=0
    for a in range(3,16):
        for u,v in product(range(a+1),repeat=2):
            W=Fraction(a*(u+v)-2*u*v,a*a)
            U=Fraction(u*(a-u)+v*(a-v),a*(a-1))
            assert W-Fraction(a-1,a)*U==Fraction((u-v)**2,a*a)
            comparisons+=1
        assert Fraction(2*(a-1),a)>1
    return comparisons


def run():
    orbit_cases=0
    cut_cases=0
    for a in range(2,9):
        for b in range(2,28):
            expected=metric_constant(a,b)
            # Exact rational grid and both explicit endpoint metrics.
            assert max(orbit_ratio(a,b,0),orbit_ratio(a,b,1))==expected
            for t in [Fraction(i,12) for i in range(25)]:
                assert orbit_ratio(a,b,t)<=expected,(a,b,t)
                orbit_cases+=1
            if b<4*a-3:
                assert orbit_ratio(a,b,1)>orbit_ratio(a,b,0)
            elif b==4*a-3:
                assert orbit_ratio(a,b,1)==orbit_ratio(a,b,0)
                for t in [Fraction(i,12) for i in range(13)]:
                    assert orbit_ratio(a,b,t)==expected
            else:
                assert orbit_ratio(a,b,0)>orbit_ratio(a,b,1)
            if a<=5 and b<=9:
                cut_cases+=cut_support_check(a,b)
    print(f"TRIPARTITE_CHECK_OK orbit_points={orbit_cases} cut_count_vectors={cut_cases} l1_cut_identities={l1_obstruction_check()}")

if __name__=='__main__':
    run()
