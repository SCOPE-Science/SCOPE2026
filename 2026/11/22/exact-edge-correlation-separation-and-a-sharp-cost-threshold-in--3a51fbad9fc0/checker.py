"""Exact finite-state verification of edge-labelled donation games on C4.

Run: python checker.py (requires SymPy >= 1.12).
This program reconstructs the entire transition law from stated game rules;
it does not use simulations to establish the claimed sign inequalities.
"""

from fractions import Fraction
from itertools import permutations
from sympy import Matrix, Rational, Poly, cancel, factor, symbols, simplify, count_roots, nroots

EDGES = ((0, 1), (1, 2), (2, 3), (3, 0))
N = 4


def transitions(mask, edge_benefits, cost, intensity):
    payoff = [0] * N
    for (i, j), b in zip(EDGES, edge_benefits):
        si, sj = (mask >> i) & 1, (mask >> j) & 1
        payoff[i] += b * sj - cost * si
        payoff[j] += b * si - cost * sj
    fitness = [1 + intensity * z for z in payoff]
    probabilities = {}
    for dead in range(N):
        left, right = (dead - 1) % N, (dead + 1) % N
        d = fitness[left] + fitness[right]
        for parent in (left, right):
            target = (mask & ~(1 << dead)) | (((mask >> parent) & 1) << dead)
            probabilities[target] = probabilities.get(target, 0) + fitness[parent] / (N * d)
    return probabilities


def orbits_for_benefits(edge_benefits):
    edge_map = {tuple(sorted(e)): b for e, b in zip(EDGES, edge_benefits)}
    preserving = [p for p in permutations(range(N))
                  if all(edge_map.get(tuple(sorted((p[i], p[j])))) == b
                         for (i, j), b in zip(EDGES, edge_benefits))]
    def permute_mask(mask, p):
        return sum(((mask >> i) & 1) << p[i] for i in range(N))
    unseen = set(range(1 << N))
    result = []
    while unseen:
        mask = min(unseen)
        orbit = tuple(sorted(set(permute_mask(mask, p) for p in preserving)))
        result.append(orbit)
        unseen.difference_update(orbit)
    index = {m: i for i, o in enumerate(result) for m in o}
    return result, index


def fixation_quotient(edge_benefits, cost, intensity):
    orbits, index = orbits_for_benefits(edge_benefits)
    transient = [i for i, o in enumerate(orbits) if o[0] not in (0, 15)]
    row_of = {o: j for j, o in enumerate(transient)}
    Q = Matrix.zeros(len(transient))
    rhs = Matrix.zeros(len(transient), 1)
    for i in transient:
        aggregation = {}
        for target, prob in transitions(orbits[i][0], edge_benefits, cost, intensity).items():
            j = index[target]
            aggregation[j] = aggregation.get(j, 0) + prob
        for j, prob in aggregation.items():
            if j == index[15]:
                rhs[row_of[i]] += prob
            elif j in row_of:
                Q[row_of[i], row_of[j]] += prob
    f = (Matrix.eye(len(transient)) - Q).inv() * rhs
    return factor(sum(f[row_of[index[1 << i]]] for i in range(N)) / N)


def fixation_full_exact(edge_benefits, cost, intensity):
    transient = list(range(1, 15))
    Q = Matrix.zeros(14)
    rhs = Matrix.zeros(14, 1)
    for i, mask in enumerate(transient):
        for target, prob in transitions(mask, edge_benefits, cost, intensity).items():
            if target == 15:
                rhs[i] += prob
            elif target != 0:
                Q[i, target - 1] += prob
    f = (Matrix.eye(14) - Q).inv() * rhs
    return factor(sum(f[(1 << i) - 1] for i in range(N)) / N)


def check():
    x, y, c, t = symbols('x y c t')
    clustered0 = fixation_quotient([x, x, y, y], Rational(0), Rational(1))
    alternating0 = fixation_quotient([x, y, x, y], Rational(0), Rational(1))
    D = (51*x**4 + 190*x**3*y + 288*x**3 + 286*x**2*y**2 +
         864*x**2*y + 614*x**2 + 190*x*y**3 + 864*x*y**2 +
         1268*x*y + 576*x + 51*y**4 + 288*y**3 + 614*y**2 +
         576*y + 192)
    numerator = (x-y)**2 * (3*x**2+7*x*y+11*x+3*y**2+11*y+9)
    assert simplify(alternating0 - Rational(1, 4)) == 0
    assert simplify(clustered0 - Rational(1, 4) - numerator/(2*D)) == 0
    print('PASS: unrestricted benefit and selection contrast identity, alternating neutrality')

    clustered = fixation_quotient([5, 5, 1, 1], c, Rational(1, 4))
    alternating = fixation_quotient([5, 1, 5, 1], c, Rational(1, 4))
    K = 12*c**6-648*c**5+13237*c**4-130826*c**3+660641*c**2-1624004*c+1537200
    Dc = (18*c**9-1347*c**8+42753*c**7-759242*c**6+8345254*c**5-
          59029779*c**4+269178291*c**3-763949868*c**2+1225277200*c-845827200)
    Npoly = (30*c**9-2157*c**8+64435*c**7-1046362*c**6+10109558*c**5-
             59511289*c**4+208484029*c**3-398421956*c**2+323640240*c-15004800)
    Qpoly = 6*c**6-366*c**5+7630*c**4-73129*c**3+345210*c**2-766635*c+656460
    assert simplify(clustered-(c-10)*(c-7)*(c-2)*K/Dc) == 0
    assert simplify(alternating-(c-10)*(c-2)*(2*c-7)/((c-7)*(c-5)*(3*c-16))) == 0
    assert simplify(clustered-Rational(1,4)-Npoly/(4*Dc)) == 0
    assert simplify(alternating-Rational(1,4)-c*(5*c**2-72*c+199)/(4*(c-7)*(c-5)*(3*c-16))) == 0
    assert simplify(clustered-alternating-2*(c-20)*(c-10)*(c-4)*(c-2)*Qpoly/((c-7)*(c-5)*(3*c-16)*Dc)) == 0
    transform = lambda p,degree: Poly(cancel((1+t)**degree*p.subs(c,2*t/(1+t))), t)
    Ncoeff = list(reversed(transform(Npoly,9).all_coeffs()))
    Dcoeff = list(reversed(transform(-Dc,9).all_coeffs()))
    Qcoeff = list(reversed(transform(Qpoly,6).all_coeffs()))
    assert Ncoeff[0]<0 and all(z>0 for z in Ncoeff[1:])
    assert all(z>0 for z in Dcoeff)
    assert all(z>0 for z in Qcoeff)
    quadratic = 5*c**2-72*c+199
    assert quadratic.subs(c, 2) == 75 and quadratic.diff(c).subs(c, 2) < 0
    assert Npoly.subs(c,0)<0 and Npoly.subs(c,2)>0
    print('PASS: fixed-parameter exact identities and all positive-coefficient sign certificates')
    print('c_star:', [z for z in nroots(Npoly, maxsteps=250) if abs(complex(z).imag)<1e-10 and 0<float(complex(z).real)<2])

    test_c=Rational(1,100)
    clustered_v=clustered.subs(c,test_c)
    alternate_v=alternating.subs(c,test_c)
    assert clustered_v == Rational(3914160121776143533946622,15437973229592093026196383)
    assert alternate_v == Rational(46254366,185678399)
    assert clustered_v>Rational(1,4)>alternate_v
    for w in (Rational(1,4), Rational(1,5)):
        for cc in (Rational(0), Rational(1,100)):
            assert fixation_full_exact([5,5,1,1],cc,w) == fixation_quotient([5,5,1,1],cc,w)
            assert fixation_full_exact([5,1,5,1],cc,w) == fixation_quotient([5,1,5,1],cc,w)
    print('PASS: 14-state unquotiented independent exact reconstruction; positive-cost witness', clustered_v,alternate_v)

if __name__=='__main__':
    check()
