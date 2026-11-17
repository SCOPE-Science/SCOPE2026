"""Direct Kirchhoff-circuit diagnostics for a continuous parallel-arm network.

No external scientific claim or independent certification is asserted.
Run: python3 check_resistance.py
Dependencies: numpy.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss


def analytic_pair(lengths, i, x, j, y):
    a = lengths[i]
    b = lengths[j]
    h = 1.0 / sum(1.0 / v for v in lengths)
    if i == j:
        z = abs(x - y)
        return z - (a - h) * z * z / (a * a)
    return x * (a - x) / a + y * (b - y) / b + h * (x / a - y / b) ** 2


def circuit_pair(lengths, i, x, j, y):
    # Independently assemble all conducting segments between their true nodes;
    # solve the unit-injection Kirchhoff equations with A as ground.
    nodes = {"A": 0, "B": 1}
    segs = []
    marks = {}
    for k, a in enumerate(lengths):
        stops = [(0.0, 0), (float(a), 1)]
        for label, edge, pos in [("X", i, x), ("Y", j, y)]:
            if k == edge:
                nodes[label] = len(nodes)
                stops.append((float(pos), nodes[label]))
        stops.sort()
        for (u, nu), (v, nv) in zip(stops, stops[1:]):
            assert v > u and nu != nv
            segs.append((nu, nv, v-u))
    m = len(nodes)
    mat = np.zeros((m, m))
    for u, v, length in segs:
        conductance = 1.0 / length
        mat[u, u] += conductance
        mat[v, v] += conductance
        mat[u, v] -= conductance
        mat[v, u] -= conductance
    charge = np.zeros(m)
    charge[nodes["X"]] = 1.0
    charge[nodes["Y"]] = -1.0
    voltage = np.linalg.solve(mat[1:, 1:], charge[1:])
    voltage = np.r_[0.0, voltage]
    return voltage[nodes["X"]] - voltage[nodes["Y"]]


def exact_mean(lengths):
    L = sum(lengths)
    h = 1.0 / sum(1.0 / v for v in lengths)
    return (h + 2.0 * sum(v*v for v in lengths) / L -
            sum(v**3 for v in lengths) / (L*L)) / 6.0


def integrated_pair_formula(lengths):
    L = sum(lengths)
    h = 1.0 / sum(1.0/v for v in lengths)
    # Independent algebraic integration of resistance kernel on every ordered
    # pair of edge rectangles.
    numerator = 0.
    for i, a in enumerate(lengths):
        numerator += (a**3 + h*a*a) / 6.
        for j, b in enumerate(lengths):
            if i != j:
                numerator += a*b*(a+b+h)/6.
    return numerator / L**2


def quadrature_mean(lengths, n=28):
    L = sum(lengths)
    gauss, weights = leggauss(n)
    gauss = (gauss+1.)/2.
    weights = weights/2.
    total = 0.
    for i, a in enumerate(lengths):
        for j, b in enumerate(lengths):
            if i != j:
                # Analytic-pair expression independently summed numerically.
                for t, w1 in zip(gauss, weights):
                    for s, w2 in zip(gauss, weights):
                        total += a*b*w1*w2*analytic_pair(lengths, i,a*t,j,b*s)
            else:
                # Split the square into its two smooth triangular halves.
                for t, w1 in zip(gauss, weights):
                    for s, w2 in zip(gauss, weights):
                        total += 2*a*a*w1*w2*t*analytic_pair(lengths,i,a*t,i,a*t*s)
    return total/L**2


def main():
    rng = np.random.default_rng(24731)
    triples = [(.3,.3,.3),(.2,.3,.5),(.02,.13,.85),(.5,.6,.7),(.1,.2,.3,.4)]
    for l in triples:
        for _ in range(80):
            i,j = rng.integers(0,len(l),2)
            x = l[i]*rng.uniform(.04,.96)
            y = l[j]*rng.uniform(.04,.96)
            if i == j and abs(x-y)<1e-9: continue
            a=analytic_pair(l,i,x,j,y)
            b=circuit_pair(l,i,x,j,y)
            assert np.isclose(a,b,atol=2e-12,rtol=2e-12),(l,i,j,a,b)
        f=exact_mean(l)
        g=integrated_pair_formula(l)
        q=quadrature_mean(l,n=12)
        assert abs(f-g)<2e-12,(l,f,g)
        assert abs(f-q)<2e-10,(l,f,q)
        print('lengths',l,'direct mean',f,'integral check',q)
    for j in range(2,101):
        l=(j/101,1-j/101)
        assert abs(exact_mean(l)-sum(l)/6)<1e-12
    for _ in range(40000):
        l=rng.dirichlet([.4,.4,.4])
        f=exact_mean(l)
        assert f >= 1/9-1e-12 and f<1/6+1e-12
    print('DIRECT_CIRCUITS_AND_EXACT_MEAN_OK')
    print('THREE_PATH_SHARP_BOUNDS_AND_TWO_PATH_INVARIANCE_OK')

if __name__ == '__main__':
    main()
