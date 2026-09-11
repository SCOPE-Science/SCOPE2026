"""Independent stdlib-only verification of the target disproof (lane-1009).

Replays (i) transplant-mean identity tildeV_0 = log(sqrt2/2),
(ii) transplanted Fourier tail ck = (-1)^{k+1}/(2k),
(iii) divergent Szego ledger S(M) = (1/4) H_M -> infinity,
(iv) O(n)-term least-squares fit showing the missing n*logcap term.
Uses only the `math` module. Run: python3 verify.py  -> prints VERIFY_OK
"""
import math

LOGCAP = math.log(math.sqrt(2.0) / 2.0)  # = -0.5*log2


def theta_of_phi(phi):
    s = math.sqrt(2.0) / 2.0
    return 2.0 * math.asin(s * math.sin(phi / 2.0))


def tildeV(phi):
    c = math.cos(theta_of_phi(phi))
    if c <= 0.0:
        c = 5e-17  # clamp: floating-point overshoot at phi ~= pi only
    return 0.5 * math.log(2.0 * c)


def simpson(f, a, b, n):
    assert n % 2 == 0
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        w = 4.0 if i % 2 == 1 else 2.0
        s += w * f(a + i * h)
    return s * h / 3.0


def cusp_quad(f):
    # split [0, pi] with refinement near the log cusp at pi
    return (simpson(f, 0.0, math.pi - 0.05, 2000)
            + simpson(f, math.pi - 0.05, math.pi - 2e-6, 4000))


def mean_check():
    m = cusp_quad(lambda ph: tildeV(ph)) / math.pi
    print("transplant mean:", m, " logcap:", LOGCAP, " diff:", m - LOGCAP)
    assert abs(m - LOGCAP) < 5e-4, "transplant-mean identity failed"


def ck(k):
    return cusp_quad(lambda ph: tildeV(ph) * math.cos(k * ph)) / math.pi


def tail_check():
    ok = True
    for k in [1, 2, 3, 4, 8, 16]:
        c = ck(k)
        pred = ((-1.0) ** (k + 1)) / (2.0 * k)
        print("k=%d numeric=%.6f predicted=%.6f diff=%.2e" % (k, c, pred, c - pred))
        if abs(c - pred) > 5e-4:
            ok = False
    assert ok, "Fourier tail identity failed"


def szego_check(M=2000):
    s = sum(k * ((((-1.0) ** (k + 1)) / (2.0 * k)) ** 2) for k in range(1, M + 1))
    HM = sum(1.0 / k for k in range(1, M + 1))
    print("Szego partial S(%d)=" % M, s, " (1/4)H_M=", 0.25 * HM)
    assert abs(s - 0.25 * HM) < 1e-12
    assert s > 1.5, "Szego sum should exceed 1.5 (diverging), refuting O(1) claim"


def on_term_demo():
    N = 8
    moms = [0.0] * N
    for k in range(N):
        f = lambda th, k=k: math.sqrt(2.0) * math.sqrt(math.cos(th)) * math.cos(k * th)
        moms[k] = (simpson(f, -1.57079632679 + 1e-9, 0.0, 1200)
                   + simpson(f, 0.0, 1.57079632679 - 1e-9, 1200)) / (2 * math.pi)

    def logdet(n):
        A = [[moms[abs(j - k)] for k in range(n)] for j in range(n)]
        L = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                s = A[i][j] - sum(L[i][t] * L[j][t] for t in range(j))
                if i == j:
                    assert s > 0
                    L[i][j] = math.sqrt(s)
                else:
                    L[i][j] = s / L[j][j]
        return 2.0 * sum(math.log(L[i][i]) for i in range(n))

    ns = list(range(2, 9))
    Y = [logdet(n) - n * n * LOGCAP for n in ns]
    SX = [float(n) for n in ns]
    SL = [math.log(n) for n in ns]

    def solve3(A, b):
        M = [row[:] + [bb] for row, bb in zip(A, b)]
        for c in range(3):
            p = max(range(c, 3), key=lambda r: abs(M[r][c]))
            M[c], M[p] = M[p], M[c]
            for r in range(3):
                if r != c:
                    f = M[r][c] / M[c][c]
                    for cc in range(c, 4):
                        M[r][cc] -= f * M[c][cc]
        return [M[i][3] / M[i][i] for i in range(3)]

    m7 = len(ns)
    A = [[sum(SX[i] * SX[i] for i in range(m7)), sum(SX[i] * SL[i] for i in range(m7)), sum(SX[i] for i in range(m7))],
         [sum(SX[i] * SL[i] for i in range(m7)), sum(SL[i] * SL[i] for i in range(m7)), sum(SL[i] for i in range(m7))],
         [sum(SX[i] for i in range(m7)), sum(SL[i] for i in range(m7)), float(m7)]]
    b = [sum(SX[i] * Y[i] for i in range(m7)), sum(SL[i] * Y[i] for i in range(m7)), sum(Y)]
    a, bb, cc = solve3(A, b)
    print("fit a(n coeff)=", a, " expected logcap=", LOGCAP)
    print("fit b(log coeff)=", bb, " target says -0.125")
    assert abs(a - LOGCAP) < 0.01, "O(n) term mismatch"
    assert abs(bb - 0.0) < 0.15, "log-coefficient near 0, not -1/8"


if __name__ == "__main__":
    mean_check()
    tail_check()
    szego_check()
    on_term_demo()
    print("VERIFY_OK")
