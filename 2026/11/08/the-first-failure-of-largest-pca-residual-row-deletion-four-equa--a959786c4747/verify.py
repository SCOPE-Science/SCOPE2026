"""Reproducible supplementary checks for the one-row rank-one residual frontier.

The analytic proof in RESULT.md, not finite random tests, establishes the
universal assertions. Requires Python 3, SymPy and NumPy.
"""
from fractions import Fraction
import numpy as np
import sympy as sp


def exact_witness():
    t = sp.Symbol('t')
    W = sp.Matrix([
        [-sp.Rational(3, 5), sp.Rational(4, 5), 0],
        [-sp.Rational(2, 3), -sp.Rational(2, 3), -sp.Rational(1, 3)],
        [-sp.Rational(2, 3), sp.Rational(1, 3), sp.Rational(2, 3)],
        [-sp.Rational(1, 3), -sp.Rational(2, 3), -sp.Rational(2, 3)],
    ])
    assert all((W.row(j) * W.row(j).T)[0] == 1 for j in range(4))
    C = W.T * W
    assert C == sp.Matrix([[sp.Rational(34, 25), -sp.Rational(8, 225), 0],
                           [-sp.Rational(8, 225), sp.Rational(41, 25), sp.Rational(8, 9)],
                           [0, sp.Rational(8, 9), 1]])
    p = sp.factor((t * sp.eye(3) - C).det())
    assert sp.simplify(p - (2025*t**3-8100*t**2+8989*t-2338)/2025) == 0
    assert p.subs(t, 0) < 0 and p.subs(t, 1) > 0
    assert p.subs(t, 2) < 0 and p.subs(t, 3) > 0
    assert p.subs(t, sp.Rational(9, 4)) == -sp.Rational(3391, 129600)
    cof = (t * sp.eye(3) - C).adjugate()
    s = [sp.factor((W.row(i) * cof * W.row(i).T)[0]) for i in range(4)]
    assert sp.simplify(s[1]-s[0]-(19*t-35)/81) == 0
    assert sp.simplify(s[2]-s[0]-(139*t-299)/2025) == 0
    assert sp.simplify(s[3]-s[0]-1064*(t-1)/2025) == 0
    for diff in s[1:]:
        assert sp.simplify((diff-s[0]).subs(t, sp.Rational(9,4))) > 0
    deleted = [sp.factor((t*sp.eye(3)-(C-W.row(i).T*W.row(i))).det())
               for i in range(4)]
    assert sp.simplify(deleted[0] - (t-1)*(81*t*t-162*t+1)/81) == 0
    assert sp.simplify(deleted[2] - (2025*t**3-6075*t*t+4214*t-324)/2025) == 0
    assert deleted[2].subs(t, sp.Rational(999, 500)) == -sp.Rational(815503, 375000000)
    assert 80*250000 < 249001*81  # (4 sqrt(5)/9)^2 < (499/500)^2
    print('All exact-rational witness, characteristic-polynomial, cofactor, and strict-gap checks passed.')
    return W


def symbolic_three_row_lemma():
    a, b, c, d, t = sp.symbols('a b c d t', real=True)
    G = sp.Matrix([[a,b,c],[b,a,d],[c,d,a]])
    p = sp.factor((t*sp.eye(3)-G).det())
    cof = (t*sp.eye(3)-G).adjugate()
    assert sp.factor(cof[0,0] - ((t-a)**2-d*d)) == 0
    assert sp.factor(cof[1,1] - ((t-a)**2-c*c)) == 0
    assert sp.factor(cof[2,2] - ((t-a)**2-b*b)) == 0
    assert sp.factor(sp.diff(p,t)-sum(cof[i,i] for i in range(3))) == 0
    print('Symbolic three-row eigenprojector principal-minor identities passed.')


def trial_random():
    rng = np.random.default_rng(20261107)
    count = 0
    for d, m_values in [(2,range(3,14)),(3,[3]),(4,[3]),(5,[3]),(9,[3])]:
        for m in m_values:
            for trial in range(175):
                W = rng.standard_normal((m,d))
                W /= np.linalg.norm(W,axis=1)[:,None]
                _, sig, vt = np.linalg.svd(W, full_matrices=False)
                v = vt[0]
                residual = 1.0 - (W@v)**2
                selected = int(np.argmax(residual))
                losses = []
                for i in range(m):
                    subs = np.delete(W,i,axis=0)
                    s = np.linalg.svd(subs,compute_uv=False)
                    losses.append(float(np.sum(s[1:]**2)))
                assert losses[selected] <= min(losses) + 1.0e-9, (d,m,W,residual,losses)
                count += 1
    print(f'{count} deterministic-seed planar/three-row random checks passed (diagnostic only).')


if __name__ == '__main__':
    W = exact_witness()
    symbolic_three_row_lemma()
    trial_random()
    X = np.array(W, dtype=float)
    C = X.T@X
    vals, vecs = np.linalg.eigh(C)
    h = 1 - (X@vecs[:,-1])**2
    losses = [3 - np.linalg.eigvalsh(C-np.outer(X[i],X[i]))[-1] for i in range(4)]
    assert int(np.argmax(h))==0 and losses[2] < losses[0]
    print('Floating diagnostic: top residual index=1, better deletion index=3; LOO losses=',losses)
    print('PASS')
