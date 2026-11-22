"""Exact finite matching checks for interval-intersection graph component/edge moments.

No third-party dependencies. Exhaustive matching enumeration at sizes 2..7
checks finite formulas; analytic arguments establish asymptotic assertions.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def pairings(vertices):
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for i in range(1, len(vertices)):
        b = vertices[i]
        rest = vertices[1:i] + vertices[i+1:]
        for tail in pairings(rest):
            yield ((a, b),) + tail


def formulas(n):
    assert n >= 2
    p = {k: Fraction(comb(n, k), comb(2*n, 2*k))
         for k in range(1, n)}
    s = sum(p.values(), Fraction())
    mixed = sum((p[k] * Fraction(comb(k, j), comb(2*k, 2*j))
                 for k in range(2, n) for j in range(1, k)), Fraction())
    mean_c = 1 + s
    var_c = s + 2*mixed - s*s
    mean_e = Fraction(n*(n-1), 3)
    var_e = Fraction(n*(n-1)*(2*n+1), 45)
    cov = -Fraction(2, 3)*sum((k*(n-k)*p[k] for k in p), Fraction())
    return mean_c, mean_e, var_c, var_e, cov


def exhaustive(n):
    count = sum_c = sum_e = sum_cc = sum_ee = sum_ce = 0
    for pairing in pairings(tuple(range(2*n))):
        cuts = sum(all((a < 2*k) == (b < 2*k) for a,b in pairing)
                   for k in range(1, n))
        c = 1 + cuts
        e = sum(max(a, x) < min(b, y)
                for (a,b),(x,y) in combinations(pairing,2))
        count += 1
        sum_c += c
        sum_e += e
        sum_cc += c*c
        sum_ee += e*e
        sum_ce += c*e
    mc, me = Fraction(sum_c,count), Fraction(sum_e,count)
    vc = Fraction(sum_cc,count) - mc*mc
    ve = Fraction(sum_ee,count) - me*me
    cv = Fraction(sum_ce,count) - mc*me
    expected = formulas(n)
    observed = (mc,me,vc,ve,cv)
    assert expected == observed, (n,expected,observed)
    return count,cv,vc,ve


def main():
    for n in range(2,8):
        total,cov,var_c,var_e = exhaustive(n)
        assert cov < 0 and var_c > 0 and var_e > 0
        print(f'n={n} matchings={total} covariance={cov} '
              f'var_components={var_c} var_edges={var_e}')
    for n in (10,20,50,100,300):
        mc,me,vc,ve,cov = formulas(n)
        assert cov < 0
        print(f'n={n} n_times_variance_components={float(n*vc):.8f} '
              f'covariance={float(cov):.8f}')
    print('All exact finite checks passed')


if __name__=='__main__':
    main()
