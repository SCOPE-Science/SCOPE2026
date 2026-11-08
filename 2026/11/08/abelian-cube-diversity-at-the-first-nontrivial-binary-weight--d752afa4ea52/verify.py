"""Independent direct checks for the mathematical formulas in RESULT.md.

Uses only the Python standard library; exhaustive tests are finite sanity checks,
not a substitute for the mathematical proof.
"""
from itertools import combinations
from math import comb
from fractions import Fraction as Q


def formulas(a, b, c, d):
    n = a + b + c + d + 3
    r = 0
    for t in range(1, n // 3 + 1):
        lo = max(0, a - t + 1, a + b + 2 - 2*t, a + b + c + 3 - 3*t)
        hi = min(a, a + b + 1 - t, a + b + c + 2 - 2*t, n - 3*t)
        r += max(0, hi - lo + 1)
    return r, max(a, b, c, d) // 3


def direct(a, b, c, d):
    w = '0'*a + '1' + '0'*b + '1' + '0'*c + '1' + '0'*d
    found = set()
    for t in range(1, len(w) // 3 + 1):
        for s in range(len(w) - 3*t + 1):
            x, y, z = w[s:s+t], w[s+t:s+2*t], w[s+2*t:s+3*t]
            if x.count('1') == y.count('1') == z.count('1'):
                found.add(w[s:s+3*t])
    return (sum(x.count('1') == 3 for x in found),
            sum(x.count('1') == 0 for x in found))


def aggregate(n):
    allones = sum((n - 3*t + 1)*t**3 for t in range(1, n//3 + 1))
    zeros = sum(
        sum((-1)**(j+1)*comb(4,j)*comb(n-3*t*j,3)
            for j in range(1,5) if n-3*t*j >= 3)
        for t in range(1,(n-3)//3+1))
    return allones, zeros


def integr(x, low, high):
    """Integrate a rational-coefficient quadratic polynomial exactly."""
    A,B,C=x
    def anti(z): return A*z**3/3 + B*z**2/2 + C*z
    return anti(high)-anti(low)


def continuous_region_check():
    # Joint density of three sorted independent uniform points is six.
    prob = 6*(integr((Q(2),Q(0),Q(0)), Q(0), Q(1,3))
             + integr((Q(-1),Q(1),Q(0)),Q(1,3),Q(2,3))
             + integr((Q(2),Q(-4),Q(2)),Q(2,3),Q(1)))
    assert prob == Q(7,9)
    # Independently compare all pairwise interval bounds to two linear tests.
    for n in (9,15,21):
        for x in range(1,n-2):
            for y in range(x+1,n-1):
                for z in range(y+1,n):
                    X,Y,Z=Q(x,n),Q(y,n),Q(z,n)
                    lo=max((Y-X)/2,(Z-X)/3,(Z-Y)/2)
                    hi=min(Y,Z/2,Q(1,3),Z-X,(1-X)/2,1-Y)
                    a = lo < hi
                    b = Z < 3*Y and 3*Y-X < 2
                    assert a == b, (x,y,z,n,lo,hi)
    return prob


def main():
    total = 0
    for n in range(3,27):
        got0=got3=0
        for p1,p2,p3 in combinations(range(n),3):
            g = (p1, p2-p1-1, p3-p2-1, n-1-p3)
            observed=direct(*g)
            predicted=formulas(*g)
            assert observed==predicted,(n,g,observed,predicted)
            got3 += observed[0]; got0 += observed[1]
            total += 1
        exp3,exp0=aggregate(n)
        assert (got3,got0)==(exp3,exp0),(n,(got3,got0),(exp3,exp0))
    assert total == 17550
    prob = continuous_region_check()
    print('DIRECT_CUBE_CLASSIFICATION_AND_AGGREGATES_OK',total)
    print('CONTINUUM_FEASIBILITY_AND_EXACT_ATOM_OK',str(1-prob))
    print('MEAN_COEFFICIENT_OK',str(Q(6,1620)))


if __name__ == '__main__': main()
