"""Reproducible numerics for block-doubling ray of E_kappa(z)=exp(z)+kappa, kappa=-ln2.
Conjugate to f(z)=(1/2)exp(z) via T(z)=z+ln2.

Produces:
 - ray points g(t) for log-spaced t (pullback method), tail-independence check
 - forward-orbit itinerary shadowing vs address
 - escape diagnosis of candidate landing point
"""
import cmath, math, json

kappa = -math.log(2)

def F(t):
    return math.exp(t) - 1.0

def build_address(n):
    a = []
    k = 0
    while len(a) < n:
        blk = 2 ** k
        a.extend([0] * blk)
        if len(a) >= n:
            break
        a.extend([1] * blk)
        k += 1
    return a[:n]

def ray_point(s, t, T_target=15.0):
    cur = t
    N = 0
    while cur < T_target:
        cur = F(cur)
        N += 1
    w = complex(cur, 2 * math.pi * s[N])
    for k in range(N, 0, -1):
        w = cmath.log(w - kappa) + 2j * math.pi * s[k - 1]
    return w, N

def strip(y):
    return int(math.floor((y + math.pi) / (2 * math.pi)))

def Ek(z):
    return cmath.exp(z) + kappa

if __name__ == "__main__":
    a = build_address(300000)
    out = {"ray_points": [], "tail_check": [], "shadowing": {}, "escape": {}}
    for t in [0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001, 5e-4, 2e-4, 1e-4, 5e-5]:
        w, N = ray_point(a, t)
        out["ray_points"].append({"t": t, "N": N, "re": w.real, "im": w.imag})
    for T in [8.0, 12.0, 15.0, 20.0]:
        w, N = ray_point(a, 0.002, T)
        out["tail_check"].append({"T": T, "N": N, "re": w.real, "im": w.imag})
    p = complex(out["ray_points"][5]["re"], out["ray_points"][5]["im"])
    z = p
    matched = 0
    for n in range(200):
        k = strip(z.imag)
        if k != a[n]:
            break
        matched += 1
        z = Ek(z)
        if abs(z) > 50:
            out["shadowing"]["stopped_at"] = n + 1
            out["shadowing"]["modulus"] = abs(z)
            break
    out["shadowing"]["matched"] = matched
    # escape diagnosis in extended precision via mpmath if available
    try:
        from mpmath import mp, mpf, log, exp, cos, sin, sqrt
        mp.dps = 50
        kk = -log(2)
        r, i = mpf(repr(p.real)), mpf(repr(p.imag))
        esc = None
        for n in range(300):
            er = exp(r) if r < 100 else None
            if er is None:
                esc = {"step": n, "re": str(r)}
                break
            r, i = er * cos(i) + kk, er * sin(i)
        out["escape"] = esc or {"step": None}
    except Exception as e:
        out["escape"] = {"error": str(e)}
    with open("ray_evidence.json", "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1)[:2000])
    print("matched steps:", matched)
