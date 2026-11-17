"""Exact rational checks for leave-one-out randomized block least squares.

Requires Python 3 and SymPy. Run: python verify.py
All symbolic claims are proved in RESULT.md; this executable checks finite instances.
"""
from itertools import product
from sympy import Matrix, eye, zeros, Rational, simplify


def build(n, t):
    rho = Rational(t*t - 1, t*t + 1)
    sigma = Rational(2*t, t*t + 1)
    a = eye(n)
    a[0, 1], a[1, 1] = rho, sigma
    residual_projectors = []
    volumes = []
    for omitted in range(n):
        columns = [i for i in range(n) if i != omitted]
        b = a[:, columns]
        gram = b.T*b
        residual_projectors.append(eye(n) - b*gram.inv()*b.T)
        volumes.append(gram.det())
    return rho, a, residual_projectors, volumes


def expected_operator(probs, projectors, n):
    ans = zeros(n)
    for prob, proj in zip(probs, projectors):
        ans += prob*proj
    return ans


def test():
    tests = 0
    for n in (3, 4, 5, 6):
        for t in (2, 3, 4, 5, 7):
            rho, a, projs, volumes = build(n, t)
            s = Rational(2*t, t*t+1)
            w1 = Matrix([s, -rho]+[0]*(n-2))
            w2 = Matrix([0, 1]+[0]*(n-2))
            normals = [w1, w2]+[eye(n)[:,i] for i in range(2,n)]
            for k in range(n):
                assert projs[k] == normals[k]*normals[k].T
                assert projs[k]*projs[k] == projs[k]
                assert volumes[k] == (1 if k < 2 else 1-rho*rho)
                tests += 3
            dopt = 2+(n-2)*(1+rho)
            optimal = [1/dopt]*2+[(1+rho)/dopt]*(n-2)
            dvol = 2+(n-2)*(1-rho*rho)
            volume = [v/dvol for v in volumes]
            assert sum(optimal) == sum(volume) == 1
            for probs, predicted in ((optimal,(1+rho)/dopt),
                                     (volume,(1+rho)/dvol)):
                e = expected_operator(probs,projs,n)
                eigs = list(e.eigenvals())
                assert max(eigs) == predicted
                tests += 1
            assert (1+rho)/dopt < (1+rho)/dvol
            tests += 1
            for probs, den in ((optimal,dopt),(volume,dvol)):
                q = probs[0]
                beta = q*(1+rho*rho)
                # Exact power-law check from the transition distribution on normals.
                weights = [Rational(1), Rational(0)]
                for k in range(1,8):
                    weights = [q*(weights[0]+rho*rho*weights[1]),
                               q*(rho*rho*weights[0]+weights[1])]
                    assert simplify(sum(weights)-beta**k) == 0
                    tests += 1
                if n <= 4 and t <= 4:
                    for k in (1,2,3):
                        total = Rational(0)
                        for sequence in product(range(n),repeat=k):
                            v = w1
                            prob = Rational(1)
                            for i in sequence:
                                v = projs[i]*v
                                prob *= probs[i]
                            total += prob*(v.T*v)[0]
                        assert simplify(total-beta**k) == 0
                        tests += 1
    print(f'VERIFY_OK exact projector, determinant, spectral, and finite-time identities: {tests} checks')


if __name__ == '__main__':
    test()
