"""Standalone exact checks of the path-network outbreak-detection theorem.

Run with Python 3.10+: python verify.py
All enumerations below are finite diagnostics, not an infinite proof.
"""
from fractions import Fraction
from itertools import combinations
from math import ceil


def objective(n, sensors, p):
    """Closed-form probability that a uniform epidemic origin reaches a sentinel."""
    sensors = tuple(sorted(sensors))
    assert 1 <= len(sensors) <= n
    assert len(set(sensors)) == len(sensors)
    def b(g):
        return sum((p**j for j in range(1, g + 1)), Fraction(0))
    def h(g):
        return 2*b(g) - g*p**(g+1)
    score = (len(sensors) + b(sensors[0]-1) + b(n-sensors[-1])
             + sum((h(sensors[i+1]-sensors[i]-1)
                    for i in range(len(sensors)-1)), Fraction(0)))
    return score / n


def path_percolation(n, sensors, p):
    """Different formula: enumerate all edge sets and initial origins."""
    count = Fraction(0)
    for mask in range(1 << (n-1)):
        chance = p**mask.bit_count() * (1-p)**(n-1-mask.bit_count())
        for source in range(1, n+1):
            hit = False
            for observed in sensors:
                lo = min(source, observed)
                hi = max(source, observed)
                if all(mask & (1 << (edge-1)) for edge in range(lo, hi)):
                    hit = True
                    break
            if hit:
                count += chance / n
    return count


def greedy_gaps(n, k, p):
    """Construct optimal gaps from ranked marginal rewards, not node enumeration."""
    gaps = [0]*(k+1)  # boundary left, k-1 interiors, boundary right
    def marginal(j, length):
        t = length+1
        if j in (0,k):
            return p**t
        return p**t * (1+t*(1-p))
    for _ in range(n-k):
        options = [(marginal(j, gaps[j]), -j, j) for j in range(k+1)]
        j = max(options)[2]
        gaps[j] += 1
    sensors = [1+gaps[0]]
    for g in gaps[1:-1]:
        sensors.append(sensors[-1] + g+1)
    assert n-sensors[-1] == gaps[-1]
    return tuple(sensors)


def endpoints_admissible(n, k, p):
    if k == n:
        return True
    assert 2 <= k < n
    q = ceil(Fraction(n-k,k-1))
    return q == 1 or p**(q-1)*(1+q*(1-p)) >= 1


def run():
    checks = 0
    probabilities = [Fraction(1,5), Fraction(1,4), Fraction(1,2),
                     Fraction(3,4), Fraction(9,10)]
    for n in range(3,10):
        for k in range(2,n):
            for p in probabilities:
                vals = [(objective(n,s,p),s)
                        for s in combinations(range(1,n+1),k)]
                peak = max(v for v,s in vals)
                optimum = [s for v,s in vals if v == peak]
                assert objective(n, greedy_gaps(n,k,p),p) == peak
                checks += 1
                eq = endpoints_admissible(n,k,p)
                observed = any(s[0] == 1 and s[-1] == n for s in optimum)
                assert eq == observed
                checks += 1
                if eq and p**(ceil(Fraction(n-k,k-1))-1) * (1+ceil(Fraction(n-k,k-1))*(1-p)) > 1:
                    assert all(s[0] == 1 and s[-1] == n for s in optimum)
                    checks += 1
                for value, s in vals:
                    if n <= 7:
                        assert value == path_percolation(n,s,p)
                        checks += 1
                    # Marginals directly constructed from the closed form.
                    assert Fraction(0) < value <= 1
                    checks += 1
    # Threshold ties for q=2: p_2=1/2.
    vals = [(objective(4,s,Fraction(1,2)),s) for s in combinations(range(1,5),2)]
    peak = max(v for v,s in vals)
    assert (1,4) in [s for v,s in vals if v == peak]
    assert (1,3) in [s for v,s in vals if v == peak]
    checks += 2
    # Sharp illustrative placement switch.
    assert objective(10,(2,5,9),Fraction(1,2)) == Fraction(109,160)
    assert objective(10,(1,5,10),Fraction(1,2)) == Fraction(101,160)
    assert objective(10,(1,5,10),Fraction(9,10)) == Fraction(486897,500000)
    assert objective(10,(2,5,9),Fraction(9,10)) == Fraction(96717,100000)
    checks += 4
    # Polynomial root and large-q limit diagnostics (not proofs).
    roots=[]
    for q in range(2,301):
        def f(p):return p**(q-1)*(1+q*(1-p))-1
        left,right=0.00001,1-1/q**2
        for _ in range(85):
            mid=(left+right)/2
            if f(mid)<0:left=mid
            else:right=mid
        r=(left+right)/2
        assert 0<r<1-1/q**2
        roots.append(r)
        checks+=1
    assert all(a<b for a,b in zip(roots,roots[1:]))
    assert abs(300*300*(1-roots[-1])-2)<0.025
    checks+=2
    print('PASS:',checks,'assertions/diagnostics')


if __name__ == '__main__':
    run()
