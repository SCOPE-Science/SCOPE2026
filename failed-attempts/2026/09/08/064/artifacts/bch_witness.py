"""Build a certified full-support binary [36,11,12] witness.

Route (classical, self-contained):
  BCH [31,11,11] (narrow-sense, designed distance 11; roots alpha^1..alpha^10
  over GF(32) = GF(2)[x]/(x^5+x^2+1)) -> add overall parity -> [32,11,>=12]
  -> append 4 repeated columns -> [36,11,>=12] (weights can only grow).
All parameters are then MEASURED exactly by enumerating all 2^11 codewords.
Writes witness_36_11_12.json.
Stdlib only.
"""
import json

# ---------- GF(2)[x] as int bitmasks ----------
def g2_mul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r

def g2_deg(a):
    return a.bit_length() - 1

def g2_mod(a, p):
    dp = g2_deg(p)
    while a.bit_length() - 1 >= dp and a:
        a ^= p << (a.bit_length() - 1 - dp)
    return a

P = 0b100101  # x^5 + x^2 + 1, irreducible over GF(2)

def fmul(a, b):
    return g2_mod(g2_mul(a, b), P)

ALPHA = 0b10  # x
# primitivity: order of x mod P divides 31 (prime); x != 1 -> order 31
apow = [1]
for _ in range(31):
    apow.append(fmul(apow[-1], ALPHA))
assert apow[31] == 1 and apow[1] == ALPHA

def coset2(r, mod=31):
    out, x = [], r
    while x not in out:
        out.append(x)
        x = (2 * x) % mod
    return out

# minimal polynomial of ALPHA^r over GF(2): prod_{s in coset} (X - ALPHA^s)
def minpoly(r):
    # polynomial over GF(32) as list of field elements, index = degree
    poly = [1]
    for s in coset2(r):
        a = apow[s % 31]  # ALPHA^s
        # multiply poly by (X + a)
        new = [0] * (len(poly) + 1)
        for i, c in enumerate(poly):
            new[i + 1] ^= c          # X term (additive XOR = field add)
            new[i] ^= fmul(c, a)     # constant term
        poly = new
    # coefficients must lie in GF(2)
    bits = 0
    for i, c in enumerate(poly):
        assert c in (0, 1), (r, i, c)
        if c:
            bits |= (1 << i)
    return bits

m1 = minpoly(1); m3 = minpoly(3); m5 = minpoly(5); m7 = minpoly(7)
print("minpoly degrees:", {x: g2_deg(x) for x in (m1, m3, m5, m7)})
g = g2_mul(g2_mul(m1, m3), g2_mul(m5, m7))
print("generator degree:", g2_deg(g))
assert g2_deg(g) == 20  # -> cyclic [31,11] code

K = 11
rows31 = [(g << i) for i in range(K)]  # 11 cyclic shifts, 31-bit vectors

def rank_of(rows, nbits):
    R = list(rows)
    r = 0
    for b in range(nbits - 1, -1, -1):
        piv = None
        for i in range(r, len(R)):
            if (R[i] >> b) & 1:
                piv = i
                break
        if piv is None:
            continue
        R[r], R[piv] = R[piv], R[r]
        for i in range(len(R)):
            if i != r and ((R[i] >> b) & 1):
                R[i] ^= R[r]
        r += 1
    return r

assert rank_of(rows31, 31) == 11

def enum_dist(rows):
    dist = {}
    codewords = [0] * (1 << K)
    for mask in range(1 << K):
        w = 0
        m = mask
        i = 0
        while m:
            if m & 1:
                w ^= rows[i]
            i += 1
            m >>= 1
        codewords[mask] = w
        wt = bin(w).count("1")
        dist[wt] = dist.get(wt, 0) + 1
    return codewords, dist

cw31, d31 = enum_dist(rows31)
min31 = min(w for w in d31 if w > 0 or True)
print("BCH [31,11] measured min distance:", min(w for w in d31 if w) ,
      "n/distsorted:", sorted(d31.items())[:6])
assert min(w for w in d31 if w) >= 11

# extend with overall parity bit (bit 31): [32,11,>=12]
rows32 = [r | ((bin(r).count("1") & 1) << 31) for r in rows31]
cw32, d32 = enum_dist(rows32)
print("extended [32,11] min:", min(w for w in d32 if w),
      sorted(d32.items())[:8])
assert min(w for w in d32 if w) >= 12

# lengthen: append copies of columns 0..3 as bits 32..35 (weights only grow)
def col(rows, b):
    return [(r >> b) & 1 for r in rows]

copies = [0, 1, 2, 3]
rows36 = list(rows32)
for j, b in enumerate(copies):
    bit = 32 + j
    for i in range(K):
        if (rows32[i] >> b) & 1:
            rows36[i] |= (1 << bit)

assert rank_of(rows36, 36) == 11
cw36, d36 = enum_dist(rows36)
dmin = min(w for w in d36 if w)
print("lengthened [36,11] min:", dmin, "num wt-12:", d36.get(12, 0))
# full support check
supp = 0
for w in cw36:
    supp |= w
assert supp == (1 << 36) - 1, "degenerate coordinate present"

out = {
    "n": 36, "k": 11, "d": dmin,
    "construction": "narrow-sense BCH [31,11,>=11] + overall parity + 4 repeated columns",
    "generator_rows": rows36,
    "weight_enumerator": {str(w): c for w, c in sorted(d36.items())},
    "num_min_weight_words": d36.get(dmin, 0),
    "full_support": True,
}
with open("witness_36_11_12.json", "w") as f:
    json.dump(out, f)
print("wrote witness_36_11_12.json; d =", dmin)
assert dmin >= 12
