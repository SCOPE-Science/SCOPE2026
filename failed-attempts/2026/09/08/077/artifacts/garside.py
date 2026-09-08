"""Classical Garside structure for B_n (n=3,4) on permutations.
Convention: permutations as tuples p with p[i] = image of i (0-based).
Simple element <-> permutation. Product in braid monoid maps to composition:
stacking braid a then b gives perm(a) o perm(b) = tuple compose: (a*b)[i] = b[a[i]].
So compose(p,q)[i] = q[p[i]].
"""
from itertools import permutations

def compose(p, q):
    return tuple(q[p[i]] for i in range(len(p)))

def invert(p):
    n = len(p); q = [0]*n
    for i, v in enumerate(p): q[v] = i
    return tuple(q)

def identity(n): return tuple(range(n))

def inversions(p):
    n = len(p); s = set()
    for i in range(n):
        for j in range(i+1, n):
            if p[i] > p[j]: s.add((i, j))
    return s

def s_perm(n, i):
    """Permutation of Artin generator sigma_{i} (i 0-based): swap i,i+1."""
    p = list(range(n)); p[i], p[i+1] = p[i+1], p[i]; return tuple(p)

def delta_perm(n):
    """Permutation of Delta_n (half-twist): reversal."""
    return tuple(n-1-i for i in range(n))

def left_divides(a, b):
    """a <=_L b for simples iff Inv(a) subset Inv(b)."""
    return inversions(a) <= inversions(b)

def left_gcd(a, b):
    """Meet in left-divisibility (weak order): largest c with c <= a and c <= b.
    Left order = subset of inversion sets; meet = largest biclosed subset of
    Inv(a) cap Inv(b). Search perms with Inv subset of intersection, max size."""
    n = len(a); ia, ib = inversions(a), inversions(b)
    inter = ia & ib
    best = None; bestk = -1
    for p in permutations(range(n)):
        ip = inversions(p)
        if ip <= inter and len(ip) > bestk:
            best = p; bestk = len(ip)
    if best is None: raise ValueError("no gcd")
    return best

def start_set(s):
    """S(s) = {i : sigma_i left-divides s} = left descents = descents of s itself."""
    return {i for i in range(len(s)-1) if s[i] > s[i+1]}

def finish_set(a):
    """F(a) = {i : a right-divisible by sigma_i} = right descents = descents of inverse."""
    q = invert(a)
    return {i for i in range(len(a)-1) if q[i] > q[i+1]}

def left_weighted(a, b):
    return start_set(b) <= finish_set(a)

def right_complement(a, n):
    """d(a) = a^{-1} Delta as simple: perm = compose(invert(a), delta)."""
    return compose(invert(a), delta_perm(n))

def left_complement(a, n):
    """Delta a^{-1}: perm = compose(delta, invert(a))? left complement: c with c*a=Delta."""
    return compose(delta_perm(n), invert(a))

def all_simples(n):
    return list(permutations(range(n)))

def proper_simples(n):
    d = delta_perm(n)
    return [p for p in permutations(range(n)) if p != identity(n) and p != d]

def tau(p, n):
    """Flip automorphism: conjugation by Delta: perm reversal-conjugate."""
    d = delta_perm(n); di = invert(d)
    return compose(compose(d, p), di)

def simple_word(p, n):
    """A positive word (tuple of 0-based gens) representing simple p: bubble-sort style."""
    # greedy: while p != id, find i with p[i]>p[i+1], emit i, swap.
    p = list(p); w = []
    while True:
        done = True
        for i in range(n-1):
            if p[i] > p[i+1]:
                p[i], p[i+1] = p[i+1], p[i]; w.append(i); done = False
                break
        if done: return tuple(w)

def perm_of_word(w, n):
    p = identity(n)
    for i in w: p = compose(p, s_perm(n, i))
    return p

def normalize_pair(a, b, n):
    """Local sliding: (a,b) simples -> (a',b') left-weighted with a*b = a'*b'."""
    # d = gcd(right_complement(a), b); a' = a*d, b' = d^{-1}*b
    d = left_gcd(right_complement(a, n), b)
    ap = compose(a, d)
    bp = compose(invert(d), b)
    return ap, bp

def positive_normal_form(w, n):
    """Left normal form (p, factors) of positive word w via local slidings.
    Returns (delta_power, [simple perms])."""
    if not w: return 0, []
    facs = [s_perm(n, i) for i in w]
    # repeatedly sweep right-to-left until all adjacent pairs left-weighted
    changed = True
    while changed:
        changed = False
        for j in range(len(facs)-2, -1, -1):
            a, b = facs[j], facs[j+1]
            if a == identity(n) or b == identity(n):
                continue
            if not left_weighted(a, b):
                ap, bp = normalize_pair(a, b, n)
                if bp == identity(n):
                    facs[j] = ap; del facs[j+1]
                elif ap == identity(n):
                    facs[j] = bp; del facs[j+1]
                else:
                    facs[j], facs[j+1] = ap, bp
                changed = True
    facs = [f for f in facs if f != identity(n)]
    d = delta_perm(n)
    p = 0
    while facs and facs[0] == d:
        p += 1; facs = facs[1:]
    # also absorb: if first factor == Delta (only possible at front after sliding) handled
    return p, facs
