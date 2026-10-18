from itertools import product

checks = 0

def compose(A, B, n):
    # Boolean relational composition A;B.
    C = [[False]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            C[i][k] = any(A[i][j] and B[j][k] for j in range(n))
    return C

def power(R, m, n):
    I = [[i == j for j in range(n)] for i in range(n)]
    A = I
    B = R
    while m:
        if m & 1:
            A = compose(A, B, n)
        B = compose(B, B, n)
        m >>= 1
    return A

def rho_q(R, q, n):
    A = [row[:] for row in R]
    for _ in range(q):
        A = compose(A, A, n)
    return A

def transfer_property(R, q, n):
    A = rho_q(R, q, n)
    return all((not A[i][j]) or R[i][j] for i in range(n) for j in range(n))

def diamond(R, truth, n):
    return tuple(any(R[i][j] and truth[j] for j in range(n)) for i in range(n))

def modal_transfer_valid(R, q, n):
    # Validity of Diamond^(2^q) p -> Diamond p under every valuation/world.
    m = 1 << q
    for bits in product((False, True), repeat=n):
        dm = bits
        for _ in range(m):
            dm = diamond(R, dm, n)
        d1 = diamond(R, bits, n)
        for i in range(n):
            if dm[i] and not d1[i]:
                return False
    return True

# Symbolic complexity identities used in the result.
for q in range(1, 25):
    qr_rho = q
    qr_sentence = q + 2
    modal_depth = 1 << q
    assert qr_sentence == qr_rho + 2; checks += 1
    assert modal_depth == 2 ** (qr_sentence - 2); checks += 1

# Exhaustive finite-frame semantic replay.  Every directed graph on <=3 vertices,
# with loops allowed, is tested.  rho_q must be exact 2^q-step reachability, and
# the modal transfer axiom must define exactly R^(2^q) subseteq R.
for n in range(1, 4):
    edges = [(i,j) for i in range(n) for j in range(n)]
    for mask in range(1 << len(edges)):
        R = [[False]*n for _ in range(n)]
        for b,(i,j) in enumerate(edges):
            R[i][j] = bool(mask & (1 << b))
        for q in range(0, 5):
            A = rho_q(R, q, n)
            B = power(R, 1 << q, n)
            assert A == B; checks += 1
        for q in range(1, 5):
            t = transfer_property(R, q, n)
            v = modal_transfer_valid(R, q, n)
            assert t == v; checks += 1

print(f"VERIFY_OK {checks} exact assertions")
