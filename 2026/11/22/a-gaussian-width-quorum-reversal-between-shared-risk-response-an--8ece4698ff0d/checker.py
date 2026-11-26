"""Exact small-size verification of the independent-composition quorum model."""
from fractions import Fraction as F
from itertools import product
from math import comb


def tail(n, m, p):
    return sum(comb(n, j) * p**j * (1-p)**(n-j) for j in range(m, n+1))


def law(n, p):
    for z in product((0, 1), repeat=n):
        j = sum(z)
        yield z, p**j * (1-p)**(n-j)


def comparison(n, x, strata):
    # Strata entries are (threshold indicator, probability, integrated risk).
    s = sum(p for high, p, r in strata if high)
    mu = sum(r for high, p, r in strata)
    hi = sum(r for high, p, r in strata if high)
    q = s*x
    a = [[F(0) for _ in range(n+1)] for _ in range(2)]
    v = [[F(0) for _ in range(n+1)] for _ in range(2)]
    for z, pz in law(n, x):
        for high, p, r in strata:
            k = high*sum(z)
            a[0][k] += pz*p
            v[0][k] += pz*r
            for draw, pd in law(n, s):
                k = sum(zi*di for zi, di in zip(z, draw))
                a[1][k] += pz*pd*p
                v[1][k] += pz*pd*r
    for aa, vv in zip(a, v):
        assert sum(aa) == 1 and sum(vv) == mu
        assert sum(j*p for j, p in enumerate(aa)) == n*q
    ratio = []
    for m in range(1, n+1):
        assert [sum(aa[m:]) for aa in a] == [s*tail(n,m,x), tail(n,m,q)]
        assert [sum(vv[m:]) for vv in v] == [hi*tail(n,m,x), mu*tail(n,m,q)]
        ratio.append(sum(a[0][m:])/sum(a[1][m:]))
    assert ratio[0] < 1 < ratio[-1]
    assert all(u < v for u,v in zip(ratio,ratio[1:]))
    return a, v


if __name__ == '__main__':
    ntests = 0
    for n in range(2, 7):
        for x in (F(1,5), F(1,2), F(2,3)):
            for s in (F(1,4), F(1,2), F(3,4)):
                tau = 1-s
                a,v = comparison(n, x, [(0,tau,tau*tau/2),(1,s,(1-tau*tau)/2)])
                ntests += n
                if (n,x,tau)==(6,F(1,2),F(1,2)):
                    assert sum(a[0][2:])-sum(a[1][2:]) == -F(85,4096)
                    assert sum(v[0][2:])-sum(v[1][2:]) == F(827,8192)
            comparison(n,x,[(0,F(2,5),F(2,25)),(1,F(3,5),F(12,25))])
            ntests += n
    # Counterexample outside the assumptions: risk 3/4 for odd and 1/4 for
    # even type parity; each indicator is individually independent of risk.
    a_shared = a_ind = w_shared = w_ind = F(0)
    for z,pz in law(2,F(1,2)):
        high = sum(z) % 2
        r = F(3,4) if high else F(1,4)
        a_shared += pz*(high*sum(z)==2)
        w_shared += pz*r*(high*sum(z)==2)
        for d,pd in law(2,F(1,2)):
            reached = sum(zi*di for zi,di in zip(z,d)) == 2
            a_ind += pz*pd*reached
            w_ind += pz*pd*r*reached
    assert (a_shared,a_ind,w_shared,w_ind) == (0,F(1,16),0,F(1,64))
    print(ntests,'exact quorum comparisons; witness -85/4096, +827/8192; parity counterexample confirmed')
