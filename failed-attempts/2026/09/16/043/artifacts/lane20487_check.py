"""Supporting numerical evidence for lane-20487 (d=2, n=5).
Family F_i(z) = z_i * L_i(z), L = I + 0.3*C, generic integer C.
Checks: (i) isolated zero via min|F| on sphere; (ii) rank DF>=3 via sigma_3;
(iii) kernel dim<=2; (iv) line contact order exactly 2d.
Homogeneity lifts sphere results to conical statements.
"""
import numpy as np

rng = np.random.default_rng(20487)
n = 5
d = 2

C = np.array([[0, 1, 0, 1, 0],
              [1, 0, 1, 0, 0],
              [0, 2, 0, 1, 1],
              [1, 0, 0, 0, 2],
              [0, 1, 1, 0, 0]], dtype=float)
L = np.eye(n) + 0.3 * C
print("det(L) =", np.linalg.det(L))

def F(z):
    return z * (z @ L.T)

def J(z):
    return np.diag(L @ z) + (z[:, None] * L)

def rand_sphere(m):
    z = rng.standard_normal((m, n)) + 1j * rng.standard_normal((m, n))
    z /= np.linalg.norm(z, axis=1, keepdims=True)
    return z

S = rand_sphere(60000)
vals = np.linalg.norm(F(S), axis=1)
print("min|F| on sphere sample    =", float(vals.min()))
print("median|F| on sphere sample =", float(np.median(vals)))

# projected-gradient refinement of min |F|^2 on sphere
worst = S[np.argsort(vals)[:12]].copy()
step = 0.05
h = 1e-6
for it in range(400):
    for k in range(len(worst)):
        z = worst[k]
        g0 = float(np.vdot(F(z), F(z)).real)
        grad = np.zeros(n, dtype=complex)
        for j in range(n):
            dz = np.zeros(n, dtype=complex); dz[j] = h
            gp = float(np.vdot(F(z + dz), F(z + dz)).real)
            dz2 = np.zeros(n, dtype=complex); dz2[j] = 1j * h
            gq = float(np.vdot(F(z + dz2), F(z + dz2)).real)
            grad[j] = ((gp - g0) / h + 1j * (gq - g0) / h) / 2
        z2 = z - step * grad
        z2 /= np.linalg.norm(z2)
        if float(np.vdot(F(z2), F(z2)).real) < g0:
            worst[k] = z2
    step *= 0.999
ref = np.linalg.norm(F(worst), axis=1)
print("refined min|F| (12 worst)  =", float(ref.min()))

# singular values of J
S2 = rand_sphere(20000)
s3min = 1e9; worstp = None; maxker = 0
for k in range(0, len(S2), 2000):
    for z in S2[k:k + 2000]:
        s = np.linalg.svd(J(z), compute_uv=False)
        if s[2] < s3min:
            s3min = float(s[2]); worstp = z.copy()
        maxker = max(maxker, int((s < 1e-9).sum()))
print("min sigma_3(J) on sample   =", s3min)
print("max kernel dim observed    =", maxker)
print("singvals at worst p        =", np.linalg.svd(J(worstp), compute_uv=False))

z = worstp.copy(); best = s3min; step = 0.02
for it in range(2000):
    w = z + step * (rng.standard_normal(n) + 1j * rng.standard_normal(n))
    w /= np.linalg.norm(w)
    s = float(np.linalg.svd(J(w), compute_uv=False)[2])
    if s < best:
        best = s; z = w
    else:
        step *= 0.9995
print("refined min sigma_3        =", best)

# line contact: F(t v) = t^d F(v); slope of log|F| vs log t
v = rand_sphere(8)
ts = np.logspace(-4, -1, 6)
for i in range(3):
    ys = np.array([np.log(float(np.linalg.norm(F(t * v[i])))) for t in ts])
    slope = (ys[-1] - ys[0]) / (np.log(ts[-1]) - np.log(ts[0]))
    print(f"line {i}: slope={slope:.4f} (expect d={d}), contact={2*slope:.4f} (expect {2*d})")
print("done.")
