"""Reproduce exact rational graph energies and small-period Floquet checks.

Requires Python 3, numpy, scipy. Numerical observations are corroboration,
not an infinite-time proof of the expansion in the accompanying theorem.
"""
from fractions import Fraction as F
from math import log
import numpy as np
from scipy.linalg import expm


def rational_integrals(phases, durations):
    """Return centered-primitive covariance integrals, exactly as Fractions."""
    n = len(phases[0]); assert sum(durations) == 1
    mean = [sum(durations[s]*phases[s][i] for s in range(len(phases)))
            for i in range(n)]
    slopes = [[phases[s][i]-mean[i] for i in range(n)]
              for s in range(len(phases))]
    starts = []; cur = [F(0)]*n
    for s, dur in enumerate(durations):
        starts.append(cur[:])
        cur = [cur[i]+dur*slopes[s][i] for i in range(n)]
    assert all(x == 0 for x in cur)
    center = [sum(durations[s]*starts[s][i] + durations[s]**2*slopes[s][i]/2
                  for s in range(len(phases))) for i in range(n)]
    covariance = [[F(0) for _ in range(n)] for _ in range(n)]
    for s, dur in enumerate(durations):
        a = [starts[s][i]-center[i] for i in range(n)]
        b = slopes[s]
        for i in range(n):
            for j in range(n):
                covariance[i][j] += (a[i]*a[j]*dur
                    +(a[i]*b[j]+a[j]*b[i])*dur**2/2
                    +b[i]*b[j]*dur**3/3)
    return covariance


def graph_energy(L, u, v, C):
    n = len(L)
    return sum(u[i]*L[i][j]*v[j]*(C[i][i]+C[j][j]-2*C[i][j])/2
               for i in range(n) for j in range(n) if i != j)


def no_commutator_energy(L, u, v, C):
    # For the examples L has Perron root zero and L v=0, u^T L=0.
    n = len(L)
    return -sum(u[i]*L[i][j]*v[j]*C[i][j]
                for i in range(n) for j in range(n))


def floquet_rate(L, phases, durations, T):
    n = len(L); P = np.eye(n)
    for r, dur in zip(phases, durations):
        A = np.array([[float(L[i][j])+(float(r[i]) if i==j else 0)
                        for j in range(n)] for i in range(n)])
        P = expm(float(dur)*T*A) @ P
    e = np.linalg.eigvals(P)
    return log(max(abs(x) for x in e))/T


def run_case(name, L, phases, durations, u, v, expected=None):
    n = len(L)
    assert all(sum(L[i][j] for i in range(n)) == 0 for j in range(n))
    assert all(sum(L[i][j]*v[j] for j in range(n)) == 0 for i in range(n))
    assert all(sum(u[i]*L[i][j] for i in range(n)) == 0 for j in range(n))
    assert sum(u[i]*v[i] for i in range(n)) == 1
    assert all(sum(durations[s]*phases[s][i] for s in range(len(phases))) == 0
               for i in range(n))
    C = rational_integrals(phases, durations)
    E = graph_energy(L, u, v, C)
    E2 = no_commutator_energy(L, u, v, C)
    assert E > 0 and E == E2, (E, E2)
    if expected is not None: assert E == expected, (E,expected)
    print(f'{name}: coefficient={E} exact_identity=PASS')
    for T in (0.025, 0.0125, 0.00625):
        observed = floquet_rate(L, phases, durations, T)/T**2
        assert abs(observed-float(E)) <= 0.03*float(E), (T,observed,float(E))
        print(f'  T={T:.3f} Lambda/T^2={observed:.11f}')
    return E


if __name__ == '__main__':
    L1 = [[F(-1),F(0),F(1)], [F(1),F(-1),F(0)],
          [F(0),F(1),F(-1)]]
    phases1 = [(F(1),F(-1),F(0)), (F(-1),F(1),F(0))]
    run_case('three-patch directed cycle two-phase',L1,phases1,
             [F(1,2),F(1,2)],[F(1,3)]*3,[F(1)]*3,F(1,48))

    L2 = [[F(-2),F(0),F(3)], [F(2),F(-4),F(0)],
          [F(0),F(4),F(-3)]]
    phases2 = [(F(1),F(-2),F(0)),(F(0),F(1),F(2)),
               (F(-1),F(1),F(-2))]
    run_case('nonreversible asymmetric three-phase',L2,phases2,
             [F(1,3)]*3,[F(1)]*3,[F(6,13),F(3,13),F(4,13)])
    print('FAST_PERIOD_GRAPH_ENERGY_CHECK_OK exact_cases=2 numeric_horizons=6')
