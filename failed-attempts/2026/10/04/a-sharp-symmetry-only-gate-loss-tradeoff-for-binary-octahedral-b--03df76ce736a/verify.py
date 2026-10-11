from fractions import Fraction

# Exact character arithmetic in Z[sqrt(2)] for the binary octahedral group.
# A pair (a,b) represents a + b*sqrt(2).

SIZES = [1, 1, 8, 6, 12, 8, 6, 6]

CHARS = {
    "r1": [(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0)],
    "r2": [(1,0),(1,0),(1,0),(1,0),(-1,0),(1,0),(-1,0),(-1,0)],
    "r3": [(2,0),(2,0),(-1,0),(2,0),(0,0),(-1,0),(0,0),(0,0)],
    "r4": [(2,0),(-2,0),(-1,0),(0,0),(0,0),(1,0),(0,1),(0,-1)],
    "r5": [(2,0),(-2,0),(-1,0),(0,0),(0,0),(1,0),(0,-1),(0,1)],
    "r6": [(3,0),(3,0),(0,0),(-1,0),(-1,0),(0,0),(1,0),(1,0)],
    "r7": [(3,0),(3,0),(0,0),(-1,0),(1,0),(0,0),(-1,0),(-1,0)],
    "r8": [(4,0),(-4,0),(1,0),(0,0),(0,0),(-1,0),(0,0),(0,0)],
}

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def sub(x, y):
    return (x[0] - y[0], x[1] - y[1])

def mul(x, y):
    return (x[0]*y[0] + 2*x[1]*y[1], x[0]*y[1] + x[1]*y[0])

def scale(x, n):
    return (x[0]*n, x[1]*n)

def inner(f, g):
    s = (0, 0)
    for w, x, y in zip(SIZES, f, g):
        s = add(s, scale(mul(x, y), w))
    return (Fraction(s[0], 48), Fraction(s[1], 48))

def tensor(f, g):
    return [mul(x, y) for x, y in zip(f, g)]

def char_sum(*terms):
    out = [(0,0)] * 8
    for f in terms:
        out = [add(x,y) for x,y in zip(out,f)]
    return out

def decomp(f):
    out = {}
    for name, chi in CHARS.items():
        c = inner(f, chi)
        assert c[1] == 0
        assert c[0].denominator == 1
        if c[0]:
            out[name] = int(c[0])
    return out

# Orthogonality of the published irreducible character table.
for a, ca in CHARS.items():
    for b, cb in CHARS.items():
        expected = (Fraction(1 if a == b else 0), Fraction(0))
        assert inner(ca, cb) == expected

# The physical representation r4 is two-dimensional with determinant one.
# Therefore chi_Sym^k = chi_r4 * chi_Sym^(k-1) - chi_Sym^(k-2).
sym = [CHARS["r1"], CHARS["r4"]]
for k in range(2, 5):
    sym.append([
        sub(mul(CHARS["r4"][i], sym[k-1][i]), sym[k-2][i])
        for i in range(8)
    ])

expected_sym = {
    0: {"r1":1},
    1: {"r4":1},
    2: {"r6":1},
    3: {"r8":1},
    4: {"r3":1, "r7":1},
}
for k, expected in expected_sym.items():
    assert decomp(sym[k]) == expected, (k, decomp(sym[k]))

# r4 has real character, so r4* has the same symmetric-power characters.
def error_sector(k, l):
    return tensor(sym[k], sym[l])

expected_error = {
    (0,0): {"r1":1},
    (0,1): {"r4":1},
    (0,2): {"r6":1},
    (0,3): {"r8":1},
    (0,4): {"r3":1, "r7":1},
    (1,1): {"r1":1, "r6":1},
    (1,2): {"r4":1, "r8":1},
    (1,3): {"r3":1, "r6":1, "r7":1},
    (2,2): {"r1":1, "r3":1, "r6":1, "r7":1},
}
for kl, expected in expected_error.items():
    assert decomp(error_sector(*kl)) == expected, (kl, decomp(error_sector(*kl)))

# Traceless logical-operator representations.
end0 = {
    "r1+r1": {"r1":3},
    "r1+r2": {"r1":1, "r2":2},
    "r2+r2": {"r1":3},
    "r3": {"r2":1, "r3":1},
    "r4": {"r6":1},
    "r5": {"r6":1},
}

# Direct checks for irreducible tensor products.
assert decomp(tensor(CHARS["r3"], CHARS["r3"])) == {"r1":1, "r2":1, "r3":1}
assert decomp(tensor(CHARS["r4"], CHARS["r4"])) == {"r1":1, "r6":1}
assert decomp(tensor(CHARS["r5"], CHARS["r5"])) == {"r1":1, "r6":1}

# r5 = r2 tensor r4.
assert tensor(CHARS["r2"], CHARS["r4"]) == CHARS["r5"]

def first_overlap(target, max_degree=4):
    target_irreps = set(target)
    # Exclude total degree zero: E_(0,0) is the literal identity operator.
    for total in range(1, max_degree + 1):
        for k in range(total + 1):
            l = total - k
            d = decomp(error_sector(k,l))
            if target_irreps.intersection(d):
                return total
    return None

depths = [first_overlap(end0[name]) for name in
          ["r1+r1","r1+r2","r2+r2","r3","r4","r5"]]
assert depths == [2,2,2,4,2,2], depths

print("symmetric_powers", {k: decomp(sym[k]) for k in range(5)})
print("depths", depths)
print("VERIFY_OK")
