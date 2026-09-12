"""Numeric extraction of 3x2 Kasteleyn characteristic polynomial P(z,w)=det K(z,w).
K entries are Laurent monomials; get coefficients by 2D DFT on torus. Pure numpy."""
import itertools, json, math
import numpy as np

MX, MY = 3, 2
def idx(m, n):
    return (m % MX) * MY + (n % MY)

def Kmat(z, w, H, V):
    N = MX * MY
    K = np.zeros((N, N), dtype=complex)
    for m in range(MX):
        for n in range(MY):
            r = idx(m, n)
            c = idx(m + 1, n)
            ph = z if m == MX - 1 else 1.0
            K[r, c] += H[m, n] * ph
            c = idx(m - 1, n)
            ph = 1 / z if m == 0 else 1.0
            K[r, c] += -H[(m - 1) % MX, n] * ph
            c = idx(m, n + 1)
            ph = w if n == MY - 1 else 1.0
            K[r, c] += V[m, n] * ph * 1j
            c = idx(m, n - 1)
            ph = 1 / w if n == 0 else 1.0
            K[r, c] += -V[m, (n - 1) % MY] * ph * 1j
    return K

def laurent_coeffs(H, V, G=32, tol=1e-8):
    th = 2*np.pi*np.arange(G)/G
    Z = np.exp(1j*th); W = np.exp(1j*th)
    F = np.zeros((G, G), dtype=complex)
    for i in range(G):
        for j in range(G):
            F[i, j] = np.linalg.det(Kmat(Z[i], W[j], H, V))
    # F[i,j] = sum_{a,b} c[a,b] exp(2 pi i (a i + b j)/G); inverse DFT:
    C = np.fft.ifft2(F) * G * G  # C[a mod G, b mod G]
    terms = {}
    for a in range(G):
        for b in range(G):
            v = C[a, b]
            if abs(v) > tol * max(1.0, abs(F).max()):
                ea = a if a <= 6 else a - G
                eb = b if b <= 6 else b - G
                if abs(ea) <= 6 and abs(eb) <= 6:
                    terms[(ea, eb)] = v
                else:
                    terms[(ea, eb)] = v  # aliasing flag
    return terms, F

def newton_interior(pts):
    P = sorted(set(pts))
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower, upper = [], []
    for p in P:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(P):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    hull = lower[:-1] + upper[:-1]
    A = 0
    for i in range(len(hull)):
        x1, y1 = hull[i]; x2, y2 = hull[(i+1) % len(hull)]
        A += x1*y2 - x2*y1
    A = abs(A)/2
    B = 0
    for i in range(len(hull)):
        x1, y1 = hull[i]; x2, y2 = hull[(i+1) % len(hull)]
        B += math.gcd(abs(x2-x1), abs(y2-y1))
    I = int(round(A - B/2 + 1))
    return hull, A, B, I

rng = np.random.default_rng(1422)
H_gen = {(m,n): float(0.5+rng.random()*2.0) for m in range(MX) for n in range(MY)}
V_gen = {(m,n): float(0.5+rng.random()*2.0) for m in range(MX) for n in range(MY)}
H_uni = {(m,n): 1.0 for m in range(MX) for n in range(MY)}
V_uni = {(m,n): 1.0 for m in range(MX) for n in range(MY)}

out = {"weights_generic": {"H": {str(k): v for k,v in H_gen.items()},
                            "V": {str(k): v for k,v in V_gen.items()}}}
for tag, H, V in [("uniform", H_uni, V_uni), ("generic", H_gen, V_gen)]:
    terms, F = laurent_coeffs(H, V)
    hull, A, B, I = newton_interior(list(terms.keys()))
    # z-roots of P(z,1): 1D DFT
    G = 32
    th = 2*np.pi*np.arange(G)/G
    f1 = np.array([np.linalg.det(Kmat(np.exp(1j*t), 1.0, H, V)) for t in th])
    c1 = np.fft.ifft(f1)*G
    # polynomial q(u)=sum_{a} c1[a] u^{a+6}, u=z
    coeff = np.zeros(13, dtype=complex)
    for a in range(G):
        ea = a if a < G/2 else a - G
        if abs(ea) <= 6:
            coeff[ea+6] += c1[a]
    poly = coeff[::-1]  # highest first for u^12..u^0
    # strip leading zeros
    nz = np.argmax(np.abs(poly) > 1e-9)
    proots = np.roots(poly[nz:])
    seps = [abs(a-b) for a,b in itertools.combinations(proots, 2)]
    out[tag] = {
        "monomials": {str(k): [float(v.real), float(v.imag)] for k,v in terms.items()},
        "n_terms": len(terms),
        "hull": hull, "area": A, "boundary_pts": B, "interior_pts_genus": I,
        "max_abs_on_torus": float(np.max(np.abs(F))),
        "min_abs_on_torus": float(np.min(np.abs(F))),
        "zpoly_degree": int(12-nz),
        "z_roots": [[float(x.real), float(x.imag)] for x in proots],
        "min_root_separation": float(min(seps)) if seps else 0.0,
    }

with open("output/artifacts/check_32_result.json", "w") as f:
    json.dump(out, f, indent=1)
for tag in ["uniform", "generic"]:
    d = out[tag]
    print(tag, "n_terms=", d["n_terms"], "hull=", d["hull"], "area=", d["area"],
          "B=", d["boundary_pts"], "genus=", d["interior_pts_genus"],
          "min|P|=", round(d["min_abs_on_torus"],4), "max|P|=", round(d["max_abs_on_torus"],2),
          "deg=", d["zpoly_degree"], "minsep=", round(d["min_root_separation"],4))
print("generic monomials:", sorted(out["generic"]["monomials"].keys()))
print("uniform monomials:", sorted(out["uniform"]["monomials"].keys()))
