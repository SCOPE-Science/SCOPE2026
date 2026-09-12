"""Exact Nemethi reduced-root engine (single consistent sign).

chi(x) = -(x, x+K)/2 = -(x^T M x + m^T M x)/2, m = canonical vector
(M m = rhs, rhs_v = -e_v - 2). chi is integer-valued on Z^s.
"""
from fractions import Fraction
import math

# ---------- graphs / linear algebra ----------

def build_star(e0, arms):
    n = 1 + sum(len(a) for a in arms)
    M = [[0]*n for _ in range(n)]
    M[0][0] = e0; i = 1
    for a in arms:
        prev = 0
        for w in a:
            M[i][i] = w; M[prev][i] = M[i][prev] = 1
            prev = i; i += 1
    return M

def solve_lin(A, b):
    n = len(A)
    R = [[Fraction(A[i][j]) for j in range(n)] + [Fraction(b[i])] for i in range(n)]
    for c in range(n):
        piv = next(r for r in range(c, n) if R[r][c] != 0)
        R[c], R[piv] = R[piv], R[c]
        d = R[c][c]; R[c] = [x/d for x in R[c]]
        for r in range(n):
            if r != c and R[r][c] != 0:
                f = R[r][c]
                R[r] = [R[r][j]-f*R[c][j] for j in range(n+1)]
    return [R[i][n] for i in range(n)]

def canon_vec(M):
    return solve_lin(M, [Fraction(-M[i][i]-2) for i in range(len(M))])

def chi_of(M, mc, x):
    """Single consistent Nemethi weight: chi(x) = -(x^T M x + m^T M x)/2."""
    n = len(M)
    q = sum(Fraction(x[i])*M[i][j]*x[j] for i in range(n) for j in range(n))
    l = sum(mc[i]*M[i][j]*x[j] for i in range(n) for j in range(n))
    return (-q - l)/2

def pairing(M, x, v):
    return sum(Fraction(x[j])*M[j][v] for j in range(len(M)))

# ---------- two-sided Laufer fiber minimization ----------

def is_closed(M, x):
    """Two-sided Laufer-closed at all leg vertices: e_v+1 <= (x,E_v) <= 1."""
    n = len(M)
    for v in range(1, n):
        p = pairing(M, x, v)
        if not (Fraction(M[v][v]+1) <= p <= 1):
            return False
    return True

def fiber_min(M, mc, i0):
    """Two-sided global fiber minimization over x_0=i0 (exact).

    Strategy: (1) run the greedy two-sided Laufer walk to a closed point;
    (2) independently minimize each decoupled arm contribution by exact
    bounded dynamic programming around the real minimizer (radius from the
    certified PD lower bound + current gap), and take the best arm states;
    (3) re-run the greedy walk from the assembled point and iterate until
    no arm-DP and no single-coordinate move improves chi. Every returned
    point is two-sided Laufer-closed; per-arm DP boxes certify no better
    point exists in the ellipsoid layer below the current value, and the
    loop terminates because integer chi strictly decreases.
    """
    import math
    n = len(M)
    rhs = rhs_vec(M)
    arms = arm_chains(M)

    def greedy(x):
        x = list(x); guard = 0
        while True:
            moved = False
            for v in range(1, n):
                p = pairing(M, x, v)
                if p >= 2:
                    x[v] += 1; moved = True; guard += 1
                    break
                if p <= M[v][v]:
                    x[v] -= 1; moved = True; guard += 1
                    break
            if not moved:
                return x
            if guard > 1000000:
                raise RuntimeError("laufer runaway")

    def arm_dp_best(arm, fixed_rest_val, cur_arm):
        k = len(arm)
        Qa = [[Fraction(-M[arm[a]][arm[b]]) for b in range(k)] for a in range(k)]
        lam = lam_cert(Qa)
        cur_g2 = arm_g2(M, rhs, arm, i0, cur_arm)
        # real minimizer of the arm contribution
        ca = [Fraction(-rhs[arm[a]], 2) for a in range(k)]
        ca[0] -= i0
        ystar = solve_lin(Qa, [-c for c in ca])
        d = [Fraction(cur_arm[a]) - ystar[a] for a in range(k)]
        gap = sum(d[a]*Qa[a][b]*d[b] for a in range(k) for b in range(k))/2
        if gap < 0:
            gap = Fraction(0)
        R = int(math.sqrt(float(2*gap/lam))) + 2
        bounds = []
        for a in range(k):
            c = float(ystar[a])
            bounds.append((math.floor(c)-R-1, math.ceil(c)+R+1))
        e = [M[v][v] for v in arm]
        r = [rhs[v] for v in arm]
        # chain DP with backpointers
        prev = {}
        L0, H0 = bounds[0]
        for y in range(L0, H0+1):
            prev[y] = (-(e[0]*y*y + 2*i0*y + r[0]*y), None)
        trace = [prev]
        for t in range(1, k):
            cur = {}
            L, H = bounds[t]
            for y in range(L, H+1):
                best = None
                for p, (c, _) in prev.items():
                    v = c - (e[t]*y*y + 2*p*y + r[t]*y)
                    if best is None or v < best[0]:
                        best = (v, p)
                cur[y] = best
            prev = cur
            trace.append(prev)
        yb, (bv, _) = min(prev.items(), key=lambda kv: kv[1][0])
        ys = [yb]
        for t in range(k-1, 0, -1):
            ys.append(trace[t][ys[-1]][1])
        ys.reverse()
        return ys, bv

    x = [0]*n; x[0] = i0
    x = greedy(x)
    for _ in range(50):
        improved = False
        for arm in arms:
            cur_arm = [x[v] for v in arm]
            ys, bv = arm_dp_best(arm, None, cur_arm)
            if bv < arm_g2(M, rhs, arm, i0, cur_arm):
                for a, v in enumerate(arm):
                    x[v] = ys[a]
                x = greedy(x)
                improved = True
        if not improved:
            assert is_closed(M, x)
            return chi_of(M, mc, x), list(x)
    raise RuntimeError("fiber_min polish did not converge")


def weight_seq(M, mc, lo, hi):
    return {i: fiber_min(M, mc, i) for i in range(lo, hi+1)}

# ---------- arm decoupling ----------

def arm_chains(M):
    """Partition leg vertices into chains starting at center neighbors."""
    n = len(M)
    nbr = {i: [j for j in range(n) if j != i and M[i][j] == 1] for i in range(n)}
    arms = []
    for u in nbr[0]:
        chain = [u]; prev = 0
        while True:
            nxt = [w for w in nbr[chain[-1]] if w != prev]
            if not nxt:
                break
            assert len(nxt) == 1, f"leg not a chain at {chain[-1]}"
            prev = chain[-1]; chain.append(nxt[0])
        arms.append(chain)
    assert sorted(sum(arms, [])) == list(range(1, n)), "arms must partition legs"
    return arms

def rhs_vec(M):
    return [Fraction(-M[i][i]-2) for i in range(len(M))]

def arm_g2(M, rhs, arm, i0, y):
    """Doubled arm contribution: G2(y) = -[y^T M_a y + 2 i0 y_1 + rhs_a^T y]."""
    s = 0
    for a, v in enumerate(arm):
        s += M[v][v]*y[a]*y[a] + rhs[v]*y[a]
        for b, w in enumerate(arm):
            if b != a:
                s += y[a]*M[v][w]*y[b]
    s += 2*i0*y[0]
    return -s  # integer (Fraction)

def const2(M, rhs, i0):
    return -(M[0][0]*i0*i0 + rhs[0]*i0)

def total_w2(M, rhs, arms, i0, x):
    t = const2(M, rhs, i0)
    for arm in arms:
        t += arm_g2(M, rhs, arm, i0, [x[v] for v in arm])
    return t

# ---------- certified PD lower bound (exact LDL, Sylvester) ----------

def ldl_ok(Q, lam0):
    n = len(Q)
    A = [[Fraction(Q[i][j]) - (lam0 if i == j else 0) for j in range(n)] for i in range(n)]
    D = [Fraction(0)]*n
    L = [[Fraction(0)]*n for _ in range(n)]
    for j in range(n):
        s = A[j][j] - sum(L[j][k]*L[j][k]*D[k] for k in range(j))
        if s <= 0:
            return False
        D[j] = s; L[j][j] = 1
        for i in range(j+1, n):
            L[i][j] = (A[i][j] - sum(L[i][k]*L[j][k]*D[k] for k in range(j)))/D[j]
    return True

def lam_cert(Q):
    lam = Fraction(1)
    while not ldl_ok(Q, lam):
        lam /= 2
        assert lam >= Fraction(1, 2**25), "PD certification failed"
    return lam

# ---------- per-arm exact optimality certificate (chain DP) ----------

def arm_cert(M, mc, rhs, arm, i0, y0):
    """Prove y0 minimizes the arm contribution over Z^k.

    Real minimizer y* of g_a; gap = g_a(y0)-g_a(y*) = (1/2)(d^T Q_a d), d=y0-y*.
    Any beating y has |y-y*| <= sqrt(2*gap/lam_a); exact chain DP over that
    box decides the minimum. Returns dict certificate.
    """
    k = len(arm)
    Qa = [[Fraction(-M[arm[a]][arm[b]]) for b in range(k)] for a in range(k)]
    ca = [Fraction(-rhs[arm[a]], 2) for a in range(k)]
    ca[0] -= i0
    ystar = solve_lin(Qa, [-c for c in ca])
    d = [Fraction(y0[a]) - ystar[a] for a in range(k)]
    gap = sum(d[a]*Qa[a][b]*d[b] for a in range(k) for b in range(k))/2
    assert gap >= 0
    lam = lam_cert(Qa)
    R = int(math.sqrt(float(2*gap/lam))) + 2
    bounds = []
    for a in range(k):
        c = float(ystar[a])
        bounds.append((math.floor(c)-R-1, math.ceil(c)+R+1))
    # chain DP for min of G2 over box
    e = [M[v][v] for v in arm]
    r = [rhs[v] for v in arm]
    prev = {}
    L0, H0 = bounds[0]
    for y in range(L0, H0+1):
        prev[y] = -(e[0]*y*y + 2*i0*y + r[0]*y)
    for t in range(1, k):
        cur = {}
        L, H = bounds[t]
        for y in range(L, H+1):
            best = None
            for p, c in prev.items():
                v = c - (e[t]*y*y + 2*p*y + r[t]*y)
                if best is None or v < best:
                    best = v
            cur[y] = best
        prev = cur
    dp_min = min(prev.values())
    g2_0 = arm_g2(M, rhs, arm, i0, y0)
    assert dp_min == g2_0, f"arm {arm} i={i0}: DP min {dp_min} != Laufer {g2_0}"
    return {"gap": str(gap), "lam": str(lam), "R": R, "bounds": bounds,
            "dp_min": str(dp_min), "box_size": sum(h-l+1 for l, h in bounds)}

def certify_fiber(M, mc, rhs, arms, i0, xm):
    assert is_closed(M, xm), f"fiber {i0} minimizer not Laufer-closed"
    assert xm[0] == i0
    assert total_w2(M, rhs, arms, i0, xm) == 2*chi_of(M, mc, xm)
    certs = [arm_cert(M, mc, rhs, arm, i0, [xm[v] for v in arm]) for arm in arms]
    return certs

# ---------- rigorous real tail bound (exact Schur complement) ----------

def real_min_quad(M, rhs):
    """Exact real minimum of chi over {x_0=i}: A i^2 + B i + C (Fractions)."""
    n = len(M)
    Q = [[Fraction(-M[i][j]) for j in range(n)] for i in range(n)]
    Qyy = [row[1:] for row in Q[1:]]
    q = [Q[v][0] for v in range(1, n)]
    ry = rhs[1:]
    # y*(i) = -Qyy^{-1}(i q - ry/2) = i*z1 + z2
    z1 = solve_lin(Qyy, [-v for v in q])
    z2 = solve_lin(Qyy, [v/2 for v in ry])
    A = (Q[0][0] + 2*sum(q[a]*z1[a] for a in range(n-1))
         + sum(z1[a]*Qyy[a][b]*z1[b] for a in range(n-1) for b in range(n-1)))/2
    B = (sum(q[a]*z2[a] for a in range(n-1))
         - sum(ry[a]*z1[a] for a in range(n-1))/2
         + sum(z1[a]*Qyy[a][b]*z2[b] for a in range(n-1) for b in range(n-1)))/2 \
        - rhs[0]/2
    C = (sum(z2[a]*Qyy[a][b]*z2[b] for a in range(n-1) for b in range(n-1))
         - sum(ry[a]*z2[a] for a in range(n-1))/2)/2
    assert A > 0
    return A, B, C

def tail_window(A, B, C, N):
    """Integers (LO,HI): realmin(i) > N for all i outside [LO,HI]."""
    iv = -B/(2*A)  # parabola vertex (Fraction)
    f = lambda i: A*i*i + B*i + C
    hi = max(0, int(math.ceil(float(iv)))) + 1
    while f(hi) <= N:
        hi += 1
    lo = min(0, int(math.floor(float(iv)))) - 1
    while f(lo) <= N:
        lo -= 1
    return lo, hi

if __name__ == "__main__":
    for name, M in (("G7", build_star(-1, [[-2],[-3],[-7]])),
                    ("G11", build_star(-2, [[-2],[-2,-2],[-2,-2,-2,-2,-3]]))):
        mc = canon_vec(M); rhs = rhs_vec(M); arms = arm_chains(M)
        A, B, C = real_min_quad(M, rhs)
        lo, hi = tail_window(A, B, C, 4)
        print(f"{name}: realmin(i) = ({A}) i^2 + ({B}) i + ({C}); N=4 window [{lo},{hi}]")
        for i in range(-6, 12):
            w, xm = fiber_min(M, mc, i)
            print(f"  i={i}: w={w} x={xm} closed={is_closed(M, xm)}")
