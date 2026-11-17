"""Exact rational checks for the cross-polytope skeleton distance profile.

The general theorem is proved in RESULT.md; finite checks here test the
pointwise sparse-sphere distance identity, sharp witnesses, and thresholds.
Only Python's standard library is required.
"""
from fractions import Fraction as F
from itertools import combinations, product
from random import Random


def l1(v):
    return sum(map(abs, v), F(0))


def sparse_sphere(n, s, denom):
    """All points of the signed rational grid on the sparse l1 unit sphere."""
    points = set()
    def compositions(total, count):
        if count == 1:
            yield (total,)
            return
        for z in range(1, total-count+2):
            for tail in compositions(total-z, count-1):
                yield (z,)+tail
    for count in range(1, min(s, denom)+1):
        for indices in combinations(range(n), count):
            for mass in compositions(denom, count):
                for signs in product((-1, 1), repeat=count):
                    vec = [F(0)]*n
                    for i, m, sign in zip(indices, mass, signs):
                        vec[i] = F(sign*m, denom)
                    points.add(tuple(vec))
    return points


def point_distance_formula(y, s):
    t = l1(y)
    T = sum(sorted(map(abs, y), reverse=True)[:s], F(0))
    return t-T+abs(T-1)


def defect_formula(n, s, lam):
    r = F(s, n)
    return max(F(0), 1-lam, 2*(1-r*(1+lam)))


def max_distance_witness(n,s,lam):
    r=F(s,n)
    if 2*s < n:
        y = tuple([F(1, n)*(1+lam)]*n)
    else:
        y = tuple([F(0)]*n)
    return y


def main():
    rng = Random(729133)
    count = 0
    gridchecks = 0
    for n in range(2,6):
        for s in range(1,n+1):
            # Exact exhaustive distance minimization on rational signed grids.
            A = sparse_sphere(n,s,4)
            for _ in range(70):
                y = tuple(F(rng.randrange(-8,9),4) for _ in range(n))
                expected = point_distance_formula(y,s)
                direct = min(l1(tuple(y[i]-a[i] for i in range(n))) for a in A)
                assert expected == direct, (n,s,y,expected,direct)
                gridchecks += 1
            for lam in [F(0),F(1,4),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(2),F(3),F(7)]:
                defect = defect_formula(n,s,lam)
                # Independent exact max over parameter t of the piecewise-linear distance.
                Tvals={F(0),F(1)+lam, F(n,s)}
                Tvals={t for t in Tvals if F(0)<=t<=1+lam}
                maximum = max((t-F(s,n)*t+abs(F(s,n)*t-1) for t in Tvals))
                assert defect == max(F(0),maximum-lam)
                y=max_distance_witness(n,s,lam)
                # The explicit origin/uniform witness reaches the positive defect.
                if defect > 0:
                    assert point_distance_formula(y,s)-lam == defect
                # Check exact necessary and sufficient lambda threshold.
                threshold=max(F(1),F(n,s)-1)
                assert (defect==0)==(lam>=threshold)
                count+=1
    print(f'VERIFY_OK {gridchecks} exhaustive-grid point-distance tests; {count} profile/threshold tests')

if __name__=='__main__':
    main()
