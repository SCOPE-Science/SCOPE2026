"""Cyclic Paley/QR census + Fourier/Gram certificates, v<=31. stdlib+numpy only."""
import json, math, itertools
import numpy as np

# ---------- basic combinatorial machinery (exact integers) ----------
def units(v):
    return [a for a in range(v) if math.gcd(a, v) == 1]

def mul(a, b, v):
    return (a * b) % v

def subgroup_generated(gens, v):
    seen = {1 % v}
    stack = [1 % v]
    G = set(gens)
    while stack:
        x = stack.pop()
        for g in list(G) + [x]:
            pass
        for g in gens:
            for y in (mul(x, g, v), mul(g, x, v)):
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
    # closure under inverses
    changed = True
    while changed:
        changed = False
        cur = list(seen)
        for x in cur:
            for y in cur:
                z = mul(x, y, v)
                if z not in seen:
                    seen.add(z); changed = True
    return sorted(seen)

def all_subgroups(U, v):
    """All subgroups of U (abelian, rank<=3 in scope): closures of 0-3 element subsets."""
    subs = set()
    subs.add((1 % v,))
    cand = list(U)
    pools = [()] + [(g,) for g in cand]
    pools += list(itertools.combinations(cand, 2))
    pools += list(itertools.combinations(cand, 3))
    for t in pools:
        H = tuple(subgroup_generated(list(t), v))
        if all(h in U for h in H):
            subs.add(H)
    return sorted(subs)

def cosets(H, U, v):
    Hset = set(H); reps = []; used = set()
    for u in U:
        if u in used:
            continue
        c = sorted(mul(u, h, v) for h in H)
        reps.append(c)
        used.update(c)
    return reps

def diff_counts(v, D):
    c = [0] * v
    for x in D:
        for y in D:
            c[(x - y) % v] += 1
    return c

def classify(v, D):
    """Return dict(kind,k,lam,mu) if D is a (partial) difference set, else None.
    kind: 'DS' (c_g const for all g!=0), 'PDS' (two values on D / complement), 'complete' (D = all nonzero)."""
    D = sorted(set(D))
    k = len(D)
    if v in D or 0 in D or k == 0 or k >= v:
        return None
    c = diff_counts(v, D)
    if c[0] != k:
        return None
    Ds = set(D)
    on = {c[g] for g in range(1, v) if g in Ds}
    off = {c[g] for g in range(1, v) if g not in Ds}
    if len(on) == 1 and len(off) == 0:
        return dict(kind='complete', k=k, lam=on.pop(), mu=None)
    if len(on) == 1 and len(off) == 1:
        lam, mu = on.pop(), off.pop()
        if lam == mu:
            return dict(kind='DS', k=k, lam=lam, mu=mu)
        return dict(kind='PDS', k=k, lam=lam, mu=mu)
    return None

def qr_set(q):
    return sorted({(x * x) % q for x in range(1, q)})

# ---------- exhaustive low-order cyclotomic union census ----------
def census(v):
    U = units(v)
    found = []
    seen_sets = set()
    for H in all_subgroups(U, v):
        cs = cosets(H, U, v)
        m = len(cs)
        idx = range(m)
        if m <= 10:
            subsets = []
            for r in range(m + 1):
                for combo in itertools.combinations(idx, r):
                    S = set()
                    for j in combo:
                        S.update(cs[j])
                    subsets.append(sorted(S))
        else:
            # restricted: single cosets, complements, full unit set (covers Paley e=2 etc.)
            subsets = [sorted(c) for c in cs]
            subsets += [sorted(set(U) - set(c)) for c in cs]
            subsets.append(sorted(U))
        for S in subsets:
            for add0 in (False, True):
                D = ([0] + S) if add0 else S
                key = tuple(sorted(D))
                if key in seen_sets:
                    continue
                seen_sets.add(key)
                cl = classify(v, D)
                if cl is not None:
                    cl = dict(cl)
                    cl['v'] = v
                    cl['D'] = sorted(D)
                    cl['H'] = list(H)
                    cl['ncyc'] = m
                    cl['symmetric'] = all(((-d) % v) in set(D) for d in D)
                    found.append(cl)
    return found

# ---------- certificates ----------
def fourier_vals(v, D):
    j = np.arange(len(D))
    Dm = np.array(D, dtype=float)
    out = []
    for a in range(v):
        out.append(np.sum(np.exp(2j * np.pi * a * Dm / v)))
    return np.array(out)

def certify_ds(q, D, k, lam):
    """Skew-Hadamard / DS Fourier + complex harmonic ETF Gram replay."""
    S = fourier_vals(q, D)
    mag2 = np.abs(S[1:]) ** 2
    target = k - lam
    err_fourier = float(np.max(np.abs(mag2 - target)))
    # nonreal check (skew case): min |Im(S)| over a!=0
    min_imag = float(np.min(np.abs(S[1:].imag)))
    d = len(D)
    w = np.exp(2j * np.pi / q)
    Dm = np.array(D)
    G = np.zeros((q, q), dtype=complex)
    for j in range(q):
        G[j, :] = np.sum(np.exp(2j * np.pi * np.outer(np.ones(q), Dm) * 0 + 0))  # placeholder
    # vectorized Gram: G[j,l] = mean over t in D of w^((j-l) t)
    pw = np.array([[w ** ((j - l) * t) for t in Dm] for j in range(q) for l in range(q)],
                  dtype=complex).reshape(q, q, d).mean(axis=2)
    G = pw
    coh = float(np.max(np.abs(G - np.eye(q))[np.eye(q) == 0].reshape(q, q - 1)))
    ev = np.linalg.eigvalsh((G + G.conj().T) / 2)
    evr = np.sort(ev.real)
    n, dd = q, d
    exp_nz = n / dd
    top = evr[dd - dd:]  # not used; split directly:
    small = evr[:n - dd]
    large = evr[n - dd:]
    return dict(
        fourier_target=target, fourier_maxerr=err_fourier, min_imag=min_imag,
        coherence=coh, coh_formula=float(math.sqrt(target) / k),
        gram_eig_small_max=float(np.max(np.abs(small))),
        gram_eig_large_min=float(np.min(large)), gram_eig_large_max=float(np.max(large)),
        gram_eig_nonzero_expected=exp_nz,
        gram_eigvals=[float(x) for x in evr],
    )

def certify_conference(q, D):
    """Exact integer C^2=qI + real-lines Gram spectrum replay."""
    Dset = set(D)
    def chi(a):
        a %= q
        if a == 0:
            return 0
        return -1 if a in Dset else 1
    # Note: with D = QR, chi = Legendre symbol: +1 on QR. Use +chi convention:
    n = q + 1
    C = np.zeros((n, n), dtype=int)
    for j in range(1, n):
        C[0, j] = C[j, 0] = 1
    for i in range(1, n):
        for j in range(1, n):
            a = (j - i) % q
            if a == 0:
                C[i, j] = 0
            else:
                C[i, j] = 1 if a in Dset else -1
    P = C @ C.T
    exact_ok = bool(np.array_equal(P, q * np.eye(n, dtype=int)))
    maxdev = int(np.max(np.abs(P - q * np.eye(n, dtype=int))))
    # Fourier two-value check: (2S_a+1)^2 == q for all a!=0
    S = fourier_vals(q, D)
    qv = (2 * S[1:] + 1) ** 2
    err_q = float(np.max(np.abs(qv - q)))
    signs = np.sign((2 * S[1:] + 1).real)
    both = bool(np.any(signs > 0) and np.any(signs < 0))
    # lines Gram
    G = np.eye(n) + C.astype(float) / math.sqrt(q)
    coh = float(np.max(np.abs(G - np.eye(n)).reshape(-1)))
    ev = np.linalg.eigvalsh(G)
    d = (q + 1) // 2
    evs = np.sort(ev)
    return dict(
        conf_exact=exact_ok, conf_maxdev=maxdev,
        fourier_q_maxerr=err_q, both_signs=both,
        coherence=coh, coh_formula=1.0 / math.sqrt(q),
        gram_eigvals=[float(x) for x in evs],
        gram_small_max=float(np.max(np.abs(evs[:n - d]))),
        gram_large_min=float(np.min(evs[n - d:])), gram_large_max=float(np.max(evs[n - d:])),
    )

def main():
    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    div3 = [q for q in primes if q % 4 == 3]
    div1 = [q for q in primes if q % 4 == 1]
    ds_rows, pds_rows = [], []
    for q in div3:
        D = qr_set(q)
        c = diff_counts(q, D)
        k = len(D)
        lam = c[1]
        assert all(x == lam for x in c[1:]), (q, c)
        cert = certify_ds(q, D, k, lam)
        ds_rows.append(dict(q=q, k=k, lam=lam, D=D, cert=cert))
    for q in div1:
        D = qr_set(q)
        c = diff_counts(q, D)
        k = len(D)
        lam = c[D[0]]
        mu = next(c[g] for g in range(1, q) if g not in set(D))
        assert all((c[g] == lam) if g in set(D) else (c[g] == mu) for g in range(1, q)), (q, c)
        cert = certify_conference(q, D)
        pds_rows.append(dict(q=q, k=k, lam=lam, mu=mu, D=D, cert=cert))
    # full census v=3..31
    cens = {}
    for v in range(3, 32):
        cens[str(v)] = census(v)
    results = dict(ds_prime_rows=ds_rows, pds_prime_rows=pds_rows, census=cens)
    with open('output/artifacts/results.json', 'w') as f:
        json.dump(results, f, indent=1)
    # table.csv (headline constructions)
    lines = ['family,q,v,k,lambda,mu,d,N,coherence,gerzon,gap']
    for r in ds_rows:
        q = r['q']; d = (q - 1) // 2; N = q
        mu = math.sqrt(q + 1) / (q - 1)
        lines.append(f"complexETF,{q},{q},{r['k']},{r['lam']},,{d},{N},{mu:.8f},{d*d},{d*d-N}")
    for r in pds_rows:
        q = r['q']; d = (q + 1) // 2; N = q + 1
        mu = 1 / math.sqrt(q)
        lines.append(f"realLines,{q},{q},{r['k']},{r['lam']},{r['mu']},{d},{N},{mu:.8f},{d*(d+1)//2},{d*(d+1)//2-N}")
    with open('output/artifacts/table.csv', 'w') as f:
        f.write('\n'.join(lines) + '\n')
    # console summary with pass/fail
    ok = True
    for r in ds_rows:
        c = r['cert']
        good = (c['fourier_maxerr'] < 1e-9 and c['gram_eig_small_max'] < 1e-9
                and abs(c['gram_eig_large_min'] - c['gram_eig_nonzero_expected']) < 1e-9
                and abs(c['coherence'] - c['coh_formula']) < 1e-12)
        ok &= good
        print(f"DS q={r['q']}: ferr={c['fourier_maxerr']:.2e} coherr={abs(c['coherence']-c['coh_formula']):.2e} "
              f"eig0={c['gram_eig_small_max']:.2e} eignz=[{c['gram_eig_large_min']:.6f},{c['gram_eig_large_max']:.6f}] "
              f"minImag={c['min_imag']:.3f} {'PASS' if good else 'FAIL'}")
    for r in pds_rows:
        c = r['cert']
        good = (c['conf_exact'] and c['fourier_q_maxerr'] < 1e-9 and c['both_signs']
                and c['gram_small_max'] < 1e-9 and abs(c['gram_large_min'] - 2) < 1e-9
                and abs(c['coherence'] - c['coh_formula']) < 1e-12)
        ok &= good
        print(f"PDS q={r['q']}: exact={c['conf_exact']} qerr={c['fourier_q_maxerr']:.2e} both={c['both_signs']} "
              f"eig0={c['gram_small_max']:.2e} eignz=[{c['gram_large_min']:.6f},{c['gram_large_max']:.6f}] "
              f"coh={c['coherence']:.6f} {'PASS' if good else 'FAIL'}")
    print('CENSUS sizes:', {v: len(cens[str(v)]) for v in range(3, 32)})
    print('ALL_PASS' if ok else 'SOME_FAIL')

if __name__ == '__main__':
    main()
