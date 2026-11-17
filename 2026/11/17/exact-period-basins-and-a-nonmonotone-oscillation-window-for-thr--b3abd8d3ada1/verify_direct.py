"""Independent vertex-level exhaustive check on small complete bipartite graphs."""
from itertools import product
from collections import Counter
from math import comb


def evolve(z, m, n):
    a, b = z[:m], z[m:]
    na = [b.count(c) for c in range(3)]
    nb = [a.count(c) for c in range(3)]
    return tuple((c + int(na[(c+1)%3]>=2))%3 for c in a) + \
           tuple((c + int(nb[(c+1)%3]>=2))%3 for c in b)


def outcome(z, m, n):
    seen = {}
    step = 0
    while z not in seen:
        seen[z] = step
        z = evolve(z, m, n)
        step += 1
        assert step <= 20
    return seen[z], step - seen[z]


def A(n):
    return max(0, 2**n - 2 - 2*n)


def U(n):
    if n < 6:
        return 0
    return 3**n - 3 * (2**n + n * 2**(n-1)) + 3*(n*n+n+1)


def L(n):
    return {1:3, 2:6, 3:6}.get(n, 0)


def census(m, n):
    aa, bb = A(m), m*A(m-1)
    a, b = A(n), n*A(n-1)
    dd, d = m*(m-1) if m>=4 else 0, n*(n-1) if n>=4 else 0
    Cc, c = U(m), U(n)
    period4 = 6*(aa+bb)*(a+b)+3*((aa+bb)*(d+c)+(a+b)*(dd+Cc))
    period3 = Cc*c + Cc*L(n) + L(m)*c
    return {1:3**(m+n)-period3-period4,3:period3,4:period4}


def main():
    for m,n in [(2,4),(3,6),(4,4),(4,5),(5,5),(3,7)]:
        periods = Counter()
        tmax = 0
        for z in product(range(3), repeat=m+n):
            t,p = outcome(z,m,n)
            periods[p] += 1
            tmax = max(tmax,t)
            assert p in (1,3,4) and t <= 3
        expected = census(m,n)
        assert all(periods.get(p,0)==expected[p] for p in expected), (m,n,periods,expected)
        print(f'K_{{{m},{n}}}: {3**(m+n)} vertex configurations; counts {dict(sorted(periods.items()))}; maximal preperiod {tmax}: PASS')
    sample=(1,1,2,2,0,0,2,2)
    assert outcome(sample,4,4) == (0,4)
    assert outcome((0,1,0,0,2,2),2,4) == (3,1)
    print('explicit primitive period-four and sharp three-step examples: PASS')

if __name__ == '__main__':main()
