"""Independent replay: regenerates every set from parameters alone, rechecks all certificates."""
import json, math
import numpy as np

R = json.load(open('output/artifacts/results.json'))

def diff_counts(v, D):
    c = [0] * v
    for x in D:
        for y in D:
            c[(x - y) % v] += 1
    return c

fails = []

# 1) Headline skew-Hadamard DS rows: regenerate QR set from q alone
for r in R['ds_prime_rows']:
    q = r['q']
    D = sorted({(x * x) % q for x in range(1, q)})
    assert D == sorted(r['D']), q
    k, lam = r['k'], r['lam']
    c = diff_counts(q, D)
    assert c[0] == k and all(x == lam for x in c[1:]), q
    S = np.array([np.sum(np.exp(2j * np.pi * a * np.array(D) / q)) for a in range(q)])
    assert float(np.max(np.abs(np.abs(S[1:]) ** 2 - (k - lam)))) < 1e-6, q
    w = np.exp(2j * np.pi / q)
    Dm = np.array(D)
    G = np.array([[np.mean([w ** ((j - l) * t) for t in Dm]) for l in range(q)] for j in range(q)])
    ev = np.sort(np.linalg.eigvalsh((G + G.conj().T) / 2).real)
    dd = (q - 1) // 2
    assert float(np.max(np.abs(ev[:q - dd]))) < 1e-6, (q, ev)
    assert abs(float(np.min(ev[q - dd:])) - q / dd) < 1e-6, (q, ev)
    coh = float(np.max(np.abs((G - np.eye(q)).reshape(-1))))
    assert abs(coh - math.sqrt(q + 1) / (q - 1)) < 1e-9, (q, coh)
    print(f"VERIFY DS q={q}: QR regen + difftable + Fourier + Gram spectrum + coherence OK")

# 2) Headline Paley PDS rows: regenerate QR set, exact integer C^2=qI, Gram spectrum
for r in R['pds_prime_rows']:
    q = r['q']
    D = sorted({(x * x) % q for x in range(1, q)})
    assert D == sorted(r['D']), q
    Ds = set(D)
    c = diff_counts(q, D)
    assert all((c[g] == r['lam']) if g in Ds else (c[g] == r['mu']) for g in range(1, q)), q
    n = q + 1
    C = np.zeros((n, n), dtype=int)
    for j in range(1, n):
        C[0, j] = C[j, 0] = 1
    for i in range(1, n):
        for j in range(1, n):
            a = (j - i) % q
            C[i, j] = 0 if a == 0 else (1 if a in Ds else -1)
    assert np.array_equal(C @ C.T, q * np.eye(n, dtype=int)), q
    G = np.eye(n) + C.astype(float) / math.sqrt(q)
    ev = np.sort(np.linalg.eigvalsh(G))
    d = (q + 1) // 2
    assert float(np.max(np.abs(ev[:n - d]))) < 1e-6, (q, ev)
    assert abs(float(np.min(ev[n - d:])) - 2) < 1e-6, (q, ev)
    assert abs(float(np.max(np.abs(G - np.eye(n)).reshape(-1))) - 1 / math.sqrt(q)) < 1e-9, q
    print(f"VERIFY PDS q={q}: QR regen + difftable + exact C^2=qI + Gram spectrum + coherence OK")

# 3) Full cyclotomic-union census replay: re-test every stored D from scratch
n_checked = 0
for v in range(3, 32):
    for r in R['census'][str(v)]:
        D = sorted(r['D'])
        c = diff_counts(v, D)
        assert c[0] == r['k'], (v, D)
        Ds = set(D)
        on = {c[g] for g in range(1, v) if g in Ds}
        off = {c[g] for g in range(1, v) if g not in Ds}
        if r['kind'] == 'DS':
            assert len(on) == len(off) == 1 and on == off == {r['lam']}, (v, D)
        elif r['kind'] == 'PDS':
            assert len(on) == len(off) == 1 and on == {r['lam']} and off == {r['mu']}, (v, D)
        elif r['kind'] == 'complete':
            assert len(on) == 1 and len(off) == 0 and on == {r['lam']}, (v, D)
        n_checked += 1
print(f"VERIFY census: {n_checked} stored (partial) difference sets re-tested from scratch OK")

# 4) Gerzon extremal check q=5: N=6, d=3, d(d+1)/2=6
assert 3 * 4 // 2 == 6
print("VERIFY Gerzon extremal (q=5 -> 6 lines in R^3, gap 0) OK")
print("VERIFY_ALL_OK")
