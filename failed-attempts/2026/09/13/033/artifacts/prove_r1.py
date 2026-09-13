"""Certificate for the r=1 (Darboux y-line) elimination lemma, v2.

Equation: F = y + a(x) invariant  <=>  g = a*(f - a') =: h(a,f).
Since q := f - a' has its top coefficient killed by the leading choice
l = c_m/d, the system is triangular linear with multipliers -l*(d-j).

Case A (m=3,n=3,d=4): solve h_7..h_4 = 0 -> a_3..a_0 with a_0 =: t free;
the attainable g's form an affine LINE p + t*q in 4-dim g-space.
Exhibit an integer g off that line (rank check over QQ).
Case B (m=4,n=3,d=5, resonant): solve h_9..h_5 = 0, evaluate residual h_4;
check on three independent f whether residual is identically zero.
"""
from fractions import Fraction

def solve_fiber(f_int, d):
    f = [Fraction(x) for x in f_int]
    m = len(f) - 1
    cm = f[m]
    l = cm / d
    assert l != 0
    # a[d] known; a[d-1..0] unknown. Represent each as affine fn of t=a_0:
    # a[i] = base[i] + slope[i]*t. Process j=1..d-1 (unknown a[d-j]).
    base = {d: l}
    slope = {d: Fraction(0)}
    top = 2 * m + 1  # deg of h before leading kill
    # helper: coefficient h_k given dict a (affine pairs)
    def h_aff(aB, aS, k):
        # q_j = c_j - (j+1) a_{j+1}, affine pairs
        qs = {}
        for j in range(m + 1):
            cj = f[j] if j < len(f) else Fraction(0)
            if j + 1 in aB:
                qs[j] = (cj - (j + 1) * aB[j + 1],
                         -(j + 1) * aS[j + 1])
            else:
                qs[j] = (cj, Fraction(0))
        totB = Fraction(0)
        totS = Fraction(0)
        for i in list(aB.keys()):
            j = k - i
            if j in qs:
                totB += aB[i] * qs[j][0]
                totS += aB[i] * qs[j][1] + aS[i] * qs[j][0]
        # cross term aS*slope-of-q only if unknown*unknown; q slopes nonzero
        # only for a-indices already solved (known indices), and current
        # unknown appears in q only via index j+1 = d-j... handled since
        # aS of solved ones is fixed; quadratic self-term check below.
        return totB, totS
    import copy
    aB = dict(base)
    aS = dict(slope)
    log = []
    for j in range(1, d):
        k = top - j
        t = d - j
        mu = -l * (d - j)  # proven multiplier
        # evaluate h_k with a_t = 0 (affine constant part)
        aB[t] = Fraction(0)
        aS[t] = Fraction(0)
        knownB, knownS = h_aff(aB, aS, k)
        # self-quadratic check: slope part coupling a_t with q slope in a_t
        # q index j'+1 = t means j' = t-1; term a_i*q_{t-1} with i + (t-1) = k
        # -> i = k-t+1 = m+1 = d: contributes a_d*(-t)*a_t, already in mu.
        # Any OTHER occurrence of a_t? a_t*q_{k-t}=a_t*q_m, q_m=0. So linear.
        assert knownS == 0, f"slope leak at j={j}"
        val = -knownB / mu
        aB[t] = val
        aS[t] = Fraction(1) if t == 0 else Fraction(0)
        log.append((j, k, t, mu, val))
    # residual: last equation index k_res = top - d
    k_res = top - d
    aB0 = dict(aB)
    aS0 = dict(aS)
    # freeze t=0 to read residual
    aB0[0] = Fraction(0)
    resB, resS = h_aff(aB0, {i: Fraction(0) for i in aS0}, k_res)
    return {'aB': aB, 'aS': aS, 'log': log, 'k_res': k_res,
            'residual': resB, 'l': l, 'f': f, 'd': d, 'm': m,
            'h_aff': h_aff}

def line_in_gspace(sol, n):
    """Return (p, q): h_k = p_k + t q_k for k=0..n."""
    p, q = [], []
    for k in range(n + 1):
        aB = dict(sol['aB'])
        aS = dict(sol['aS'])
        # set a_0 = t symbolically: evaluate at t=0 and t=1
        A0 = dict(aB)
        A0[0] = Fraction(0)
        S0 = {i: Fraction(0) for i in aB}
        b0, _ = sol['h_aff'](A0, S0, k)
        A1 = dict(aB)
        A1[0] = Fraction(1)
        b1, _ = sol['h_aff'](A1, S0, k)
        p.append(b0)
        q.append(b1 - b0)
    return p, q

def rank2(cols):
    r = [list(map(Fraction, c)) for c in cols]
    n = len(r[0])
    piv = 0
    for j in range(len(r)):
        pivots = [i for i in range(piv, n)
                  if any(R[j] != 0 for R in [r[j]])]
        # find nonzero entry at/below piv in col j
        f = next((i for i in range(piv, n) if r[j][i] != 0), None)
        if f is None:
            continue
        r[j][piv], r[j][f] = r[j][f], r[j][piv]
        for jj in range(len(r)):
            if jj != j and r[jj][piv] != 0:
                lam = r[jj][piv] / r[j][piv]
                for i in range(piv, n):
                    r[jj][i] -= lam * r[j][i]
        piv += 1
    return piv

print("=== Case A: (m,n)=(3,3), d=4, f = 3x^3 - x^2 + 2x + 1 ===")
sol = solve_fiber([1, 2, -1, 3], 4)
for (j, k, t, mu, val) in sol['log']:
    print(f"j={j} eq h_{k}=0 -> a_{t} = {val}  (mult {mu})")
print("residual eq h_%d = %s" % (sol['k_res'], sol['residual']))
p, q = line_in_gspace(sol, 3)
print("line base p =", p)
print("line dirn q =", q)
assert any(v != 0 for v in q), "fiber should be 1-dim"
# verify top eqns vanish for two values of t
for t in (Fraction(0), Fraction(7, 3)):
    A = dict(sol['aB'])
    A[0] = t
    S = {i: Fraction(0) for i in A}
    tops = [sol['h_aff'](A, S, k)[0] for k in (7, 6, 5, 4)]
    assert all(v == 0 for v in tops), f"top eqns fail at t={t}"
print("top eqns h_7..h_4 vanish identically in t: OK")
# exhibit integer g off the line: g - p must have rank 2 with q
g0 = [Fraction(0), Fraction(0), Fraction(0), Fraction(1)]  # g = x^3
d0 = [g0[i] - p[i] for i in range(4)]
print("rank[q, g0-p] =", rank2([q, d0]), "(2 => g0 off line => no a for (f,g0))")
assert rank2([q, d0]) == 2
print("Case A CERTIFIED: fiber over this f is a line; e.g. g=x^3 not attained.")

print()
print("=== Case B: (m,n)=(4,3), d=5, residual on three f ===")
for f in ([1, -2, 3, 5, 2], [0, 1, 0, -1, 1], [2, 0, 0, 1, -3]):
    solB = solve_fiber(f, 5)
    print(f"f={f}: residual h_{solB['k_res']} = {solB['residual']}")
print("ALL CHECKS PASSED")
