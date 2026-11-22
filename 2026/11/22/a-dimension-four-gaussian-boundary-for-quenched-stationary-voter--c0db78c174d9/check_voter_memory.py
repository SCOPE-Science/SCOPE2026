"""Deterministic finite-volume and one-dimensional checks of local-reset voting.

Run: python3 check_voter_memory.py. Uses Python's standard library only.
Finite-volume checks support, but do not prove, the infinite-lattice theorem.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt, cos, pi, isclose

checks = 0

def check(test, label):
    global checks
    if not test:
        raise AssertionError(label)
    checks += 1


def solve(a, b):
    """Exact Gaussian elimination on a nonsingular rational system."""
    n = len(b)
    z = [[F(a[i][j]) for j in range(n)] + [F(b[i])] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if z[i][j] != 0)
        z[j], z[pivot] = z[pivot], z[j]
        u = z[j][j]
        z[j] = [v / u for v in z[j]]
        for i in range(n):
            if i != j:
                u = z[i][j]
                if u:
                    z[i] = [z[i][c] - u * z[j][c] for c in range(n+1)]
    return [z[i][-1] for i in range(n)]


def weighted_initial_mean(initial, rate):
    n = len(initial)
    matrix = [[(rate+1 if x == y else F(0)) -
               (F(1,2) if y == (x-1)%n else 0) -
               (F(1,2) if y == (x+1)%n else 0)
               for y in range(n)] for x in range(n)]
    return solve(matrix, [rate*v for v in initial])


def generator_stationary_mean(initial, rate):
    """Direct stationary distribution of the entire interacting spin chain."""
    n = len(initial)
    states = list(product((-1,1), repeat=n))
    index = {s:i for i,s in enumerate(states)}
    dim = len(states)
    Q = [[F(0) for _ in range(dim)] for _ in range(dim)]
    for i, state in enumerate(states):
        for x in range(n):
            flip = sum(F(1,2) for y in ((x-1)%n,(x+1)%n)
                       if state[y] != state[x])
            if state[x] != initial[x]:
                flip += rate
            if flip:
                other = list(state)
                other[x] = -other[x]
                j = index[tuple(other)]
                Q[i][j] += flip
                Q[i][i] -= flip
    A = [[Q[row][col] for row in range(dim)] for col in range(dim)]
    A[-1] = [F(1)]*dim
    pi_stationary = solve(A,[F(0)]*(dim-1)+[F(1)])
    return [sum(pi_stationary[i]*states[i][x] for i in range(dim))
            for x in range(n)]

for n in (3,4):
    for rate in (F(1,2),F(3,2)):
        kernel = weighted_initial_mean((1,)+(0,)*(n-1),rate)
        check(sum(kernel)==1, 'kernel normalization')
        s2 = sum(v*v for v in kernel)
        s4 = sum(v**4 for v in kernel)
        mean2 = F(0)
        mean4 = F(0)
        for initial in product((-1,1),repeat=n):
            moments = weighted_initial_mean(initial,rate)
            full = generator_stationary_mean(initial,rate)
            for i in range(n):
                check(full[i]==moments[i], 'full generator vs resolvent')
            mean2 += moments[0]**2 / (2**n)
            mean4 += moments[0]**4 / (2**n)
        check(mean2==s2, 'environmental variance')
        check(mean4==3*s2*s2-2*s4, 'Rademacher fourth cumulant')
        check(s2>0 and s4>0, 'strict negative fourth cumulant')
        spectrum = sum((float(rate)/(float(rate)+1-cos(2*pi*j/n)))**2 for j in range(n))/n
        check(isclose(float(s2),spectrum,rel_tol=1e-11,abs_tol=1e-11),
              'Fourier squared resolvent')

for rate in (0.01,0.04,0.1,0.25,0.5,1.0,3.0,10.0):
    lam = rate+1-sqrt(rate*(rate+2))
    k0 = sqrt(rate/(rate+2))
    p_from_series = k0*k0*(1+lam*lam)/(1-lam*lam)
    p_closed = sqrt(rate)*(rate+1)/(rate+2)**1.5
    check(isclose(p_from_series,p_closed,rel_tol=2e-12), 'one-dimensional plateau')
    k4 = k0**4*(1+lam**4)/(1-lam**4)
    fourth_excess = -2*k4/(p_closed*p_closed)
    check(-2 <= fourth_excess < 0, 'fourth cumulant sign and bound')
    check(0 < p_closed < 1, 'plateau admissibility')
    check(0<k0*k0/p_closed<1, 'Lindeberg ratio admissibility')
for rate in (1e-3,1e-4,1e-5):
    p_closed = sqrt(rate)*(rate+1)/(rate+2)**1.5
    check(isclose(p_closed/sqrt(rate),1/(2*sqrt(2)),rel_tol=.002),
          'weak-reset one-dimensional prefactor')
print('PASS: %d deterministic checks (full finite Markov generators, exact fourth cumulant, Fourier and one-dimensional identities)' % checks)
