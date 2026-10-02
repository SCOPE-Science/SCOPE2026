"""Lane 260 INDEPENDENT VERIFIER (stdlib only).
Re-derives every truth table from definitions.json primitives, then checks
all metrics with NAIVE algorithms (no FWHT reuse): O(N^2) Walsh, exhaustive
DDT, Mobius ANF + ANF re-evaluation round-trip. Writes verify_log.txt.
Exit nonzero on any failure. Prints VERIFY_OK on success.
"""
import hashlib, json, sys

LOG = []
def log(s):
    LOG.append(s); print(s, flush=True)

TT = json.load(open('output/artifacts/truth_tables.json'))

# ---- 1. re-derive field arithmetic & tables from scratch (independent code path) ----
def mul5(a, b):
    p = 0
    while b:
        if b & 1: p ^= a
        a <<= 1
        if a & 0x20: a ^= 0x25  # x^5+x^2+1
        b >>= 1
    return p & 0x1F

def mul6(a, b):
    p = 0
    while b:
        if b & 1: p ^= a
        a <<= 1
        if a & 0x40: a ^= 0x43  # x^6+x+1
        b >>= 1
    return p & 0x3F

def pw(mul, x, e):
    r = 1
    for _ in range(e):
        r = mul(r, x)
    return r

# field polynomial irreducibility: no root (deg5,6 => check no linear factor)
# + for deg 5: no irreducible quadratic factor; for deg 6: no quadratic/cubic factor.
def poly_mod_mul(a, b):
    r = 0
    while b:
        if b & 1: r ^= a
        a <<= 1; b >>= 1
    return r
def poly_mod(a, m):
    while a.bit_length() >= m.bit_length():
        a ^= m << (a.bit_length() - m.bit_length())
    return a
def has_factor(mod, d):
    # does mod have an irreducible factor of degree d? brute force monic polys
    n = mod.bit_length() - 1
    for c in range(1 << d):
        f = (1 << d) | c
        if poly_mod(mod, f) == 0:
            # check f irreducible (only for d=2,3: no roots / no linear factor)
            roots = [x for x in (0, 1) if poly_mod(f, (1 << 1) | x) == 0]
            if d == 1 or not roots:
                if d == 2 or d == 3 or d == 1:
                    return True, f
    return False, None

M5, M6 = 0x25, 0x43
assert not has_factor(M5, 1)[0], 'x^5+x^2+1 has a root?!'
assert not has_factor(M6, 1)[0], 'x^6+x+1 has a root?!'
assert not has_factor(M5, 2)[0], 'x^5+x^2+1 has quadratic factor'
assert not has_factor(M6, 2)[0], 'x^6+x+1 has quadratic factor'
assert not has_factor(M6, 3)[0], 'x^6+x+1 has cubic factor'
log('field polys irreducible: OK (no linear/quadratic; no cubic for deg6)')

# multiplicative-group sanity: t is primitive? check orders divide 31 / 63
def order(mul, x, grp):
    v, k = x, 1
    while v != 1:
        v = mul(v, x); k += 1
        assert k <= grp
    return k
o5, o6 = order(mul5, 2, 31), order(mul6, 2, 63)
log(f'ord(t)= {o5} in GF32, {o6} in GF64 (divide 31 / 63: {31 % o5 == 0}, {63 % o6 == 0})')

# re-derive power maps by repeated multiplication (no square-multiply path)
E = {}
E['S1'] = [0xC,0x5,0x6,0xB,0x9,0x0,0xA,0xD,0x3,0xE,0xF,0x8,0x4,0x7,0x1,0x2]
E['S2'] = [pw(mul5, x, 3) for x in range(32)]
E['S3'] = [pw(mul5, x, 14) for x in range(32)]
E['S3supp'] = [0 if x == 0 else pw(mul5, x, 30) for x in range(32)]
E['S4'] = [pw(mul6, x, 3) for x in range(64)]
E['S5'] = [0 if x == 0 else pw(mul6, x, 62) for x in range(64)]
def drbg(seed, n):
    a = list(range(n)); ws = []; c = 0
    while len(ws) < n:
        d = hashlib.sha256(seed.encode() + b':' + c.to_bytes(4, 'big')).digest()
        ws += [int.from_bytes(d[i:i+4], 'big') for i in range(0, 32, 4)]
        c += 1
    k = 0
    for i in range(n - 1, 0, -1):
        j = ws[k] % (i + 1); k += 1
        a[i], a[j] = a[j], a[i]
    return a
E['S6'] = drbg('SCOPE-260-n5-v1', 32)
E['S7'] = drbg('SCOPE-260-n6-v1', 64)
E['B'] = [((((v >> 0) & 1) & ((v >> 3) & 1)) ^ (((v >> 1) & 1) & ((v >> 4) & 1)) ^
            (((v >> 2) & 1) & ((v >> 5) & 1))) for v in range(64)]
for k, v in E.items():
    assert v == TT[k], f'truth table mismatch: {k}'
log('truth-table re-derivation from definitions: OK (9/9 byte-equal)')

# printed S6/S7 commitment anchors
log('S6[0:8] = %s sha=%s' % (TT['S6'][:8], hashlib.sha256(bytes(TT['S6'])).hexdigest()[:16]))
log('S7[0:8] = %s sha=%s' % (TT['S7'][:8], hashlib.sha256(bytes(TT['S7'])).hexdigest()[:16]))

# Galois-inverse spot checks: x * x^30 == 1 for x != 0 in GF32; x * x^62 == 1 in GF64
assert all(mul5(x, pw(mul5, x, 30)) == 1 for x in range(1, 32))
assert all(mul6(x, pw(mul6, x, 62)) == 1 for x in range(1, 64))
log('inverse-axiom spot check x*x^(2^n-2)=1: OK (31 + 63 nonzero elements)')

def par(x):
    return bin(x).count('1') & 1

def naive_stats(S, n, name, extra_signed=None):
    N = 1 << n
    assert sorted(S) == list(range(N)) or name == 'S4', f'{name} perm check'
    maxabs = 0; hist = {}; signed = {}
    for b in range(1, N):
        for a in range(N):
            s = 0
            for x in range(N):
                s += 1 if (par(a & x) ^ par(b & S[x])) == 0 else -1
            aa = abs(s)
            if aa > maxabs: maxabs = aa
            hist[aa] = hist.get(aa, 0) + 1
            if extra_signed is not None:
                signed[s] = signed.get(s, 0) + 1
    nl = N // 2 - maxabs // 2
    # Parseval: sum over a of W^2 = N^2 per component
    for b in [1, N - 1]:
        q = sum((sum(1 if (par(a & x) ^ par(b & S[x])) == 0 else -1 for x in range(N))) ** 2 for a in range(N))
        assert q == N * N, (name, b, q)
    delta = 0
    for da in range(1, N):
        c = {}
        for x in range(N):
            k = S[x] ^ S[x ^ da]
            c[k] = c.get(k, 0) + 1
        delta = max(delta, max(c.values()))
    # ANF degree + round-trip per component
    deg = 0
    for b in range(1, N):
        f = [par(b & S[x]) for x in range(N)]
        g = list(f)
        for i in range(n):
            for m in range(N):
                if m & (1 << i): g[m] ^= g[m ^ (1 << i)]
        for m in range(1, N):
            if g[m]: deg = max(deg, bin(m).count('1'))
        # round-trip: evaluate ANF at all points
        for x in range(N):
            v = 0
            for m in range(N):
                if g[m] and (m & x) == m: v ^= 1
            assert v == f[x], (name, b, x)
    log(f'{name}: n={n} perm={name != "S4"} max|W|={maxabs} NL={nl} delta={delta} deg={deg} hist={sorted(hist.items())}')
    if extra_signed is not None:
        log(f'{name} signed spectrum: {sorted(signed.items())}')
    return {'maxAbsW': maxabs, 'NL': nl, 'delta': delta, 'degree': deg}

R = {}
for name, n in [('S1', 4), ('S2', 5), ('S3', 5), ('S3supp', 5), ('S4', 6), ('S5', 6), ('S6', 5), ('S7', 6)]:
    R[name] = naive_stats(TT[name], n, name,
                          extra_signed=True if name in ('S2', 'S3') else None)

# bent: naive Walsh incl. a=0 term, signed
f = TT['B']; N = 64; mags = set(); signed = {}
for a in range(64):
    s = sum(1 if (par(a & v) ^ f[v]) == 0 else -1 for v in range(64))
    mags.add(abs(s)); signed[s] = signed.get(s, 0) + 1
assert mags == {8}, mags
log(f'B: Walsh magnitudes {sorted(mags)} signed={sorted(signed.items())} NL={32 - 4} flat: OK')

# hard assertions = the claim's integers
exp = {'S1': (8, 4, 4, 3), 'S2': (8, 12, 2, 2), 'S3': (8, 12, 2, 3),
       'S3supp': (12, 10, 2, 4), 'S4': (16, 24, 2, 2), 'S5': (16, 24, 4, 5),
       'S6': (16, 8, 10, 4), 'S7': (28, 18, 8, 5)}
for k, (m, nl, dl, dg) in exp.items():
    r = R[k]
    assert (r['maxAbsW'], r['NL'], r['delta'], r['degree']) == (m, nl, dl, dg), (k, r)
log('exact-integer table assertions: OK (8/8 rows)')

# AB certificate: S2 component spectra in {0,+-8} (signed, every component)
assert set(sum([], [])) == set()  # noop guard
for b in range(1, 32):
    vals = set()
    for a in range(32):
        vals.add(sum(1 if (par(a & x) ^ par(b & TT['S2'][x])) == 0 else -1 for x in range(32)))
    assert vals <= {0, 8, -8}, (b, vals)
log('AB certificate S2 (all 31 components signed Walsh in {0,+8,-8}): OK')
# note: S3 (x^14) also has this property; recorded but NOT claimed as AB-theorem instance
s3ab = all(set(sum(1 if (par(a & x) ^ par(b & TT['S3'][x])) == 0 else -1 for x in range(32))
               for a in range(32)) <= {0, 8, -8} for b in range(1, 32))
log(f'S3 x^14 signed-AB-shape (supplementary observation): {s3ab}')

# gap inequalities
assert R['S2']['NL'] - R['S6']['NL'] == 4 >= 2
assert R['S3']['NL'] - R['S6']['NL'] == 4 >= 2
assert R['S3supp']['NL'] - R['S6']['NL'] == 2 >= 2
assert R['S4']['NL'] - R['S7']['NL'] == 6 >= 2
assert R['S5']['NL'] - R['S7']['NL'] == 6 >= 2
assert R['S2']['delta'] < R['S6']['delta']
assert R['S3']['delta'] < R['S6']['delta']
assert R['S4']['delta'] < R['S7']['delta']
assert R['S5']['delta'] < R['S7']['delta']
log('gap inequalities (NL margins 4,4,2 @n=5; 6,6 @n=6; all delta strict): OK')

with open('output/artifacts/table.json', 'w') as fh:
    json.dump({'rows': R, 'bent': {'mags': [8], 'NL': 28}}, fh, indent=1)
with open('output/artifacts/verify_log.txt', 'w') as fh:
    fh.write('\n'.join(LOG) + '\n')
log('VERIFY_OK')
