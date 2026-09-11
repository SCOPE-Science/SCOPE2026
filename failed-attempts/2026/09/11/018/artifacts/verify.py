"""Verifier for lane-704 TARGET certificate: SHD for phi(x1,x2;y)=G(x1-x2+y) in (R,<,+,e^Z).
Exact symbolic arithmetic only (Laurent polynomials in formal transcendental X=e);
G-membership of a test value v(X) <=> v is a monomial X^n. No floats.
Checks:
 (U) difference-uniqueness: X^j-X^k == X^n-X^m as Laurent polys <=> (j,k)==(n,m).
 (V) VC(phi0)=2: explicit 2-shattering + one pair-forces-full collision instance.
 (R) schema replay on representative finite (A,b) covering all trace classes:
     T=empty | T=singleton | T=multi-same-diff | T=two-distinct-diff,
     verifying trace equality theta(A;d)=phi(A;b) and entailment theta=>phi^b
     on the test universe (existential u ranged over bounded Exps; canonical u
     verified in-range). General proof in output/DRAFT.md.
Prints VERIFY_OK on success.
"""
from itertools import product

def norm(p):
    return {k: v for k, v in p.items() if v != 0}

def add(p, q, s=1):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, 0) + s * v
    return norm(r)

def is_monomial(p):
    return len(p) == 1 and list(p.values())[0] == 1

def exp_poly(n):
    return {n: 1}

def check_U(B=8):
    rng = range(-B, B + 1)
    n = 0
    for j, k, nn, m in product(rng, rng, rng, rng):
        lhs = norm({j: 1, k: -1} if j != k else {})
        rhs = norm({nn: 1, m: -1} if nn != m else {})
        ident = (add(lhs, rhs, -1) == {})
        iff = ((j, k) == (nn, m))
        # zero-difference case: j==k and nn==m both give empty poly; handle:
        if j == k and nn == m:
            iff = True
        assert ident == iff, (j, k, nn, m)
        n += 1
    return n

def G(v):
    return is_monomial(v)

def phi(a1, a2, b):
    return G(add(add(a1, a2, -1), b))

def phi0(a, b):
    return G(add(a, b))

def check_V():
    one, X = {0: 1}, {1: 1}
    B = [one, X]
    W = {(): {0: -10}, (0,): add(exp_poly(2), one, -1), (1,): add(exp_poly(2), X, -1),
         (0, 1): {0: 0}}
    for S, a in W.items():
        got = tuple(phi0(add(a, b), {0: 0}) for b in B)
        want = tuple(i in S for i in (0, 1))
        assert got == want, (S, got)
    # pair-forces-full instance: B3 powers {1,X,X^2}; a hitting first two is a=0
    a = {0: 0}
    assert all(phi0(add(a, e), {0: 0}) for e in [one, X, exp_poly(2)])
    # a=X^2-1 hits 1 (=X^2) but misses X (X^2+X-1 not monomial) and X^2 (X^2+X^2-1)
    a2 = add(exp_poly(2), one, -1)
    assert phi0(add(a2, one), {0: 0}) and not phi0(add(a2, X), {0: 0})
    return True

def exp_range(B=6):
    return [exp_poly(n) for n in range(-B, B + 1)]

def theta_pair(x1, x2, w1, w2, exps):
    d1 = add(w1[0], w1[1], -1)
    d2 = add(w2[0], w2[1], -1)
    delta = add(d1, d2, -1)
    out = False
    for u in exps:
        if G(u) and G(add(u, delta, -1)) and G(add(add(x1, x2, -1), add(u, d1, -1))):
            out = True
            break
    return out

def theta_line(x1, x2, w):
    return add(x1, x2, -1) == add(w[0], w[1], -1)

def theta_single(x1, x2, w):
    return x1 == w[0] and x2 == w[1]

def check_R():
    one, X = {0: 1}, {1: 1}
    E2, E3 = exp_poly(2), exp_poly(3)
    exps = exp_range(6)
    # universe of test points (polys)
    U = [{0: 0}, one, X, E2, E3, {0: -10}, add(E2, one, -1), add(E2, X, -1),
         add(X, one), add(X, one, -1), add(E3, E2, -1), add(E2, E2, -1)]
    U += [exp_poly(n) for n in range(-3, 5)]
    cases = []
    # Case T empty: A pairs, b=1 with differences avoiding G-1... take A={(0,0),(X,0)}, b=1:
    # traces: 0+1=1 in G! adjust: b = X+X (non-monomial): (0,0):0+X+X non-mono; (X,0): X+X+X=3X non-mono
    bE = add(X, X)
    AE = [({0: 0}, {0: 0}), (X, {0: 0}), (E2, X)]
    cases.append(('empty', AE, bE, None))
    # Case T singleton: A={(0,0),(X,0)}, b=0: diffs 0, X; 0+0=0? 0 as poly {0:0} is NOT monomial (empty) -> miss!
    # G=e^Z: 0 not in G. use b=1: diff 0 -> 1 in G hit; diff X -> X+1 non-mono miss. T={0} singleton.
    bS = one
    AS = [({0: 0}, {0: 0}), (X, {0: 0}), (E2, X)]
    cases.append(('singleton', AS, bS, (AS[0],)))
    # Case multi-same-diff: A={(0,0),(X,X),(E2,E2)} all diff 0, b=1: all hit, T={0}.
    AM = [({0: 0}, {0: 0}), (X, X), (E2, E2), (X, {0: 0})]
    cases.append(('multi-same-diff', AM, one, (AM[0],)))
    # Case two-distinct-diff: A={(0,0),(X,0)}, b=0? diffs 0->0 miss, X->X hit: singleton. Use b s.t. two hit:
    # b = 1 - X? not in universe... need d1+b, d2+b monomials with d1!=d2: d1=0,d2=X: b=1 gives 1, X+1. no.
    # b = X^2 - X: d2+b = X^2 hit; d1+b = X^2-X miss. singleton again. For two hits need b with b and X+b monomial:
    # b=X^2-X? no. Take A diffs {X^2-X?...}. Simplest: A={(X^2,0),(X,0)} diffs X^2, X; b=0: both hit (X^2, X monomials).
    AT = [(E2, {0: 0}), (X, {0: 0}), ({0: -10}, {0: 0})]
    cases.append(('two-distinct-diff', AT, {0: 0}, (AT[0], AT[1])))
    for name, A, b, params in cases:
        S = [p for p in A if phi(p[0], p[1], b)]
        T = {tuple(sorted(add(p[0], p[1], -1).items())) for p in S}
        if name == 'empty':
            assert S == [], S
            # theta=perp: empty trace, entails vacuously
            for p in A:
                assert not phi(p[0], p[1], b)
        elif name in ('singleton', 'multi-same-diff'):
            assert len(T) == 1, (name, T)
            w = params[0]
            for p in A:
                assert theta_line(p[0], p[1], w) == phi(p[0], p[1], b), (name, p)
            for x1 in U:
                for x2 in U:
                    if theta_line(x1, x2, w):
                        assert phi(x1, x2, b), (name, 'entail')
        elif name == 'two-distinct-diff':
            assert len(T) == 2, (name, T)
            w1, w2 = params
            d1 = add(w1[0], w1[1], -1)
            assert G(add(d1, b))  # canonical u in G
            cu = add(d1, b)
            assert cu in exps, 'canonical u in range'
            for p in A:
                assert theta_pair(p[0], p[1], w1, w2, exps) == phi(p[0], p[1], b), (name, p)
            for x1 in U:
                for x2 in U:
                    if theta_pair(x1, x2, w1, w2, exps):
                        assert phi(x1, x2, b), (name, 'entail')
    # phi0 corollary replay: same classes in 1 var
    A0 = [{0: 0}, X, E2, {0: -10}]
    b0 = {0: 0}  # hits X, E2 (>=2 hits -> pair schema)
    S0 = [a for a in A0 if phi0(a, b0)]
    assert len(S0) >= 2
    s1, s2 = S0[0], S0[1]
    delta = add(s1, s2, -1)
    for a in U:
        lhs = any(G(u) and G(add(u, delta, -1)) and G(add(a, add(u, s1, -1))) for u in exps)
        assert lhs == phi0(a, b0), a
    return len(cases)

if __name__ == '__main__':
    nU = check_U()
    check_V()
    nC = check_R()
    print(f"U uniqueness: {nU} exponent-quadruples exact OK")
    print("V VC(phi0)=2: 2-shattering + pair-collision OK")
    print(f"R schema replay: {nC} trace classes (empty/singleton/multi-same/two-diff) + phi0 pair case OK")
    print("VERIFY_OK")
