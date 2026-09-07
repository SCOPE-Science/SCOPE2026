import numpy as np, math, json, csv

def gen_and_dlogs(q, phi):
    n = phi; fac = {}; d = 2
    while d * d <= n:
        while n % d == 0:
            fac[d] = fac.get(d, 0) + 1; n //= d
        d += 1 if d == 2 else 2
    if n > 1: fac[n] = 1
    primes = list(fac)
    for g in range(2, q):
        if math.gcd(g, q) != 1: continue
        if all(pow(g, phi // pr, q) != 1 for pr in primes):
            dlog = {1: 0}; cur = 1
            for k in range(1, phi):
                cur = (cur * g) % q; dlog[cur] = k
            return g, dlog
    raise Exception("no generator for q=%d" % q)

def envelope_for_q(q, p):
    from math import gcd
    phi = q - q // p
    g, dlog = gen_and_dlogs(q, phi)
    units = [u for u in range(q) if gcd(u, q) == 1]
    isunit = np.zeros(q, bool); isunit[units] = True
    js = [j for j in range(phi) if j % p != 0]
    logq = math.log(q); qb = q ** (3 / 16)
    env = np.zeros(q + 1)
    best = (0.0, None)
    chi = np.zeros(q, complex)
    for j in js:
        for u in units:
            chi[u] = np.exp(2j * math.pi * j * dlog[u] / phi)
        for a in range(q):
            wa = np.exp(2j * math.pi * a / q)
            r = np.arange(2 * q) % q
            ext = np.where(isunit[r], chi[r] * (wa ** np.arange(2 * q)), 0.0)
            P = np.zeros(2 * q + 1, complex); P[1:] = np.cumsum(ext)
            iM = np.arange(q)[:, None]; iN = np.arange(1, q + 1)[None, :]
            Amat = np.abs(P[iM + iN + 1] - P[iM + 1])
            env[1:] = np.maximum(env[1:], Amat.max(axis=0))
            i = np.unravel_index(np.argmax(Amat), Amat.shape)
            v = float(Amat[i]); N = int(i[1] + 1)
            R = v / ((N ** 0.5) * qb * logq)
            if R > best[0]:
                best = (R, (j, a, int(i[0]), N, v))
    return {"q": q, "p": p, "phi": phi, "gen": g, "nprim": len(js),
            "maxR": best[0],
            "argmax": dict(zip(["j", "a", "M", "N", "absS"], best[1])),
            "envelope": [float(x) for x in env[1:]]}

def direct_check(q, p, arg):
    # independent code path: pure-python direct summation
    import cmath
    phi = q - q // p
    g, dlog = gen_and_dlogs(q, phi)
    j, a, M, N = arg["j"], arg["a"], arg["M"], arg["N"]
    s = 0j
    for n in range(M + 1, M + N + 1):
        r = n % q
        if math.gcd(r, q) != 1: continue
        s += cmath.exp(2j * math.pi * j * dlog[r] / phi) * cmath.exp(2j * math.pi * a * n / q)
    return abs(s)

results = {}
for (q, p) in [(9, 3), (25, 5), (27, 3), (49, 7)]:
    r = envelope_for_q(q, p)
    dc = direct_check(q, p, r["argmax"])
    r["direct_recompute"] = dc
    r["agreement"] = abs(dc - r["argmax"]["absS"])
    results[str(q)] = r
    print(json.dumps({k: r[k] for k in ["q", "maxR", "argmax", "direct_recompute", "agreement"]}))
    with open("output/artifacts/envelope_q%d.csv" % q, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["N", "envelope_max_absS", "trivial_N", "PV_lemma_bound", "burg_shape_C1"])
        for i, e in enumerate(r["envelope"], start=1):
            pv = min(float(i), (i + q * (1 + math.log(i))) / math.sqrt(q))
            w.writerow([i, e, i, pv, (i ** 0.5) * (q ** (3 / 16)) * math.log(q)])
with open("output/artifacts/summary.json", "w") as f:
    json.dump(results, f, indent=1)
print("DONE")
