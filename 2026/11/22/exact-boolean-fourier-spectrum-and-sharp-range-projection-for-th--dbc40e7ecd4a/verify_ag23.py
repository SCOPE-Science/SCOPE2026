"""Independent exact-integer checks for the Boolean Fourier spectrum of AG(2,3) bases.

Run: python3 verify_ag23.py
No external dependencies. This is finite verification of a separately given proof.
"""
from collections import Counter
from itertools import combinations
from math import comb

V = tuple((i, j) for i in range(3) for j in range(3))
N = 1 << len(V)
FULL = N - 1
checks = 0

def ensure(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def bits(indices):
    return sum(1 << i for i in indices)

def parity_dot(a, b):
    return -1 if (a & b).bit_count() % 2 else 1

def kr(r, weight):
    return sum((-1)**j * comb(weight, j) * comb(9-weight, r-j)
               for j in range(max(0, r-9+weight), min(r,weight)+1))

# Construction 1: independent affine triples are those whose vector sum is nonzero.
triples = [tuple(c) for c in combinations(range(9), 3)]
line_masks = set()
base_masks = set()
for t in triples:
    x = sum(V[i][0] for i in t) % 3
    y = sum(V[i][1] for i in t) % 3
    (line_masks if (x, y) == (0, 0) else base_masks).add(bits(t))
ensure(len(line_masks) == 12, 'line count')
ensure(len(base_masks) == 72, 'basis count')
ensure(len(line_masks | base_masks) == 84, 'partition of triples')

# Construction 2: independently generate all affine lines from directions.
by_direction = set()
for dx, dy in [(1, 0), (0, 1), (1, 1), (1, 2)]:
    for ax, ay in V:
        line = [V.index(((ax+t*dx) % 3, (ay+t*dy) % 3)) for t in range(3)]
        by_direction.add(bits(line))
ensure(by_direction == line_masks, 'independent line generation')
for a,b in combinations(range(9),2):
    ensure(sum(bool((1<<a)&L) and bool((1<<b)&L) for L in line_masks)==1,
           'unique Steiner line through two points')

# Direct signed-base enumeration, independent of the closed-form proof.
lam = []
for S in range(N):
    direct = sum(parity_dot(S,B) for B in base_masks)
    L = sum(parity_dot(S,ell) for ell in line_masks)
    k = S.bit_count()
    ensure(direct == kr(3, k) - L, f'Krawtchouk-line subtraction {S}')
    inside = sum((S & ell) == ell for ell in line_masks)
    ensure(L == 12 - 8*k + 4*comb(k,2) - 8*inside,
           f'Steiner incidence formula {S}')
    if k <= 4:
        explicit = {0:72, 1:24, 2:0, 3:-8, 4:-8}[k] + 8*inside
    else:
        complement = FULL ^ S
        ck = 9 - k
        cinside = sum((complement & ell) == ell for ell in line_masks)
        explicit = -({0:72, 1:24, 2:0, 3:-8, 4:-8}[ck] + 8*cinside)
    ensure(direct == explicit, f'closed form {S}')
    lam.append(direct)

spect = Counter(lam)
ensure(spect == {-72:1,-24:9,-8:126,0:240,8:126,24:9,72:1}, 'full spectrum')
ensure(sum(v != 0 for v in lam) == 272, 'rank')
ensure(sum(v == 0 for v in lam) == 240, 'nullity')
ensure(sum(v > 0 for v in lam) == 136, 'positive inertia')
ensure(sum(v < 0 for v in lam) == 136, 'negative inertia')
ensure(set(abs(v) for v in lam if v) == {8,24,72}, 'positive singular levels')
ensure(all(v%8 == 0 for v in lam), 'dyadic divisibility')

# Projection P has Fourier symbol 1 at nonzero multipliers and 0 otherwise.
mask_nonzero = [int(v != 0) for v in lam]
unnormalized_kernel = mask_nonzero[:]
for j in range(9):
    step = 1 << j
    for u in range(N):
        if not u & step:
            a,b = unnormalized_kernel[u], unnormalized_kernel[u+step]
            unnormalized_kernel[u], unnormalized_kernel[u+step] = a+b,a-b

# Distinct geometric closed formula for the projection kernel via line sums.
for x in range(N):
    t = x.bit_count()
    SX = 9 - 2*t
    L = sum(parity_dot(x, ell) for ell in line_masks)
    formula = (1 + (-1)**t) * (sum(kr(r,t) for r in range(5)) - (SX+1)*L)
    ensure(unnormalized_kernel[x] == formula, f'projection analytic {x}')

# At 4 points the kernel distinguishes the 72 sets containing a line from 54 caps.
for x in range(N):
    t = x.bit_count()
    inside = sum((x & ell) == ell for ell in line_masks)
    complement = FULL ^ x
    cin = sum((complement & ell) == ell for ell in line_masks)
    if t==0: expected=272
    elif t==4: expected=16 if inside==1 else -16
    elif t==6: expected=32 if cin==1 else 0
    elif t==8: expected=-48
    else: expected=0
    ensure(unnormalized_kernel[x] == expected, f'kernel geometry {x}')

kernel_hist = Counter(unnormalized_kernel)
ensure(kernel_hist == {-48:9,-16:54,0:364,16:72,32:12,272:1},'kernel multiplicities')
ensure(sum(abs(q) for q in unnormalized_kernel) == 3104, 'endpoint norm numerator')
ensure(3104//32 == 97 and 3104%32 == 0, 'endpoint norm 97/16')
ensure(sum(q*q for q in unnormalized_kernel) == N*272, 'projection Plancherel')

# Apply kernel to an independent Fourier character and check projection identity.
for S in range(N):
    test = sum(unnormalized_kernel[x] * parity_dot(S,x) for x in range(N))
    ensure(test == N*mask_nonzero[S], f'projection Fourier symbol {S}')

print(f'PASS: {checks} exact checks, 72 bases, 12 lines, rank 272/nullity 240;')
print('signed spectrum:',sorted(spect.items()))
print('projection kernel unnormalized:',sorted(kernel_hist.items()))
print('sharp endpoint projection norm: 97/16; smallest surviving |eigenvalue|: 8')
