"""Bounded test: raw sunset lattice sums U_N for resonant T_res at sigma=5/2.

U_N = sum over k,l in Z^2_* with |k|,|l|,|s|<=N (s=k+l != 0) of
  F(k,l) = N(k,l)/D(k,l),
  N = (k.l)(l.s)+(l.s)(s.k)+(s.k)(k.l),  D = |k|^s |l|^s |s|^s, s=5/2.
Fit U_N ~= A*sqrt(N) + B*ln(N) + C; check A stability and bounded residual.
Stdlib only.
"""
import math, time, json

SIG = 2.5

def lattice_pts(N):
    pts = []
    N2 = N * N
    for i in range(-N, N + 1):
        for j in range(-N, N + 1):
            n2 = i * i + j * j
            if 1 <= n2 <= N2:
                pts.append((i, j, n2, math.sqrt(n2)))
    return pts

def compute_U(N):
    pts = lattice_pts(N)
    # norm^sigma lookup by squared norm
    pw = {}
    for (_, _, n2, _) in pts:
        if n2 not in pw:
            pw[n2] = float(n2) ** (SIG / 2.0)
    N2 = N * N
    # half-list for k (use evenness F(-k,-l)=F(k,l)): kx>0 or (kx==0 and ky>0)
    khalf = [p for p in pts if p[0] > 0 or (p[0] == 0 and p[1] > 0)]
    total = 0.0
    for (kx, ky, k2, _) in khalf:
        dk = pw[k2]
        for (lx, ly, l2, _) in pts:
            sx, sy = kx + lx, ky + ly
            s2 = sx * sx + sy * sy
            if s2 < 1 or s2 > N2:
                continue
            ds = float(s2) ** (SIG / 2.0)
            dl = pw[l2]
            kdl = kx * lx + ky * ly
            lds = lx * sx + ly * sy
            sdk = sx * kx + sy * ky
            num = kdl * lds + lds * sdk + sdk * kdl
            total += num / (dk * dl * ds)
    return 2.0 * total, len(pts)

def fit_ABC(data):
    # least squares on [sqrtN, lnN, 1]
    import itertools
    S = [[0.0]*3 for _ in range(3)]
    b = [0.0]*3
    for (N, U) in data:
        r = [math.sqrt(N), math.log(N), 1.0]
        for a in range(3):
            b[a] += r[a]*U
            for c in range(3):
                S[a][c] += r[a]*r[c]
    # solve 3x3 via Cramer
    def det(M):
        return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
                - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
                + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
    d = det(S)
    out = []
    for col in range(3):
        M = [row[:] for row in S]
        for r in range(3):
            M[r][col] = b[r]
        out.append(det(M)/d)
    return out  # A, B, C

if __name__ == "__main__":
    t0 = time.time()
    data = []
    for N in [4, 6, 8, 12, 16, 20, 24]:
        U, n = compute_U(N)
        data.append((N, U))
        print(f"N={N:3d} npts={n:5d} U_N={U:14.6f}  U/sqrtN={U/math.sqrt(N):10.6f}", flush=True)
    A, B, C = fit_ABC(data)
    print(f"fit: A={A:.6f} B={B:.6f} C={C:.6f}")
    for (N, U) in data:
        r = U - (A*math.sqrt(N) + B*math.log(N) + C)
        print(f"  resid N={N:3d}: {r:+.6f}")
    # sequential A estimates (fit on last-3 window) for stability
    for w in [data[-4:], data[-3:]]:
        A2, B2, C2 = fit_ABC(w)
        print(f"  window Ns={[x[0] for x in w]}: A={A2:.6f} B={B2:.6f} C={C2:.6f}")
    print(f"elapsed {time.time()-t0:.1f}s")
    with open("fit_summary.json", "w") as f:
        json.dump({"data": data, "fit": [A, B, C]}, f)
