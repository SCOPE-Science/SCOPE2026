"""Phase-1d: exact horn-necessity identities (set equalities) + randomized
Boolean-combination small-or-cosmall check. Stdlib only."""
import random
from twisted_checks import Fq, MODS, verify_irred, sumset, twprod, scale
from phase1b_checks import ev
import itertools

def load(p, l):
    m = MODS[(p, l)]; assert verify_irred(p, l, m)
    return Fq(p, l, m)

def check_identities(p, l):
    F = load(p, l); z, o = F.z, F.o
    Nexp = (F.q - 1) // (p - 1)
    T = [a for a in F.els if a != z and F.pow(a, Nexp) == o]
    def trace(a):
        s = z; x = a
        for _ in range(l): s = F.add(s, x); x = F.frob(x)
        return s
    V = [a for a in F.els if trace(a) == z]
    sT = {F.frob(a) for a in T}
    print("p=%d l=%d: sig(T)==T: %s | T.sigT==T: %s | V+V==V: %s | sig(V)==V: %s" % (
        p, l, sT == set(T), twprod(F, T) == set(T), sumset(F, V) == set(V),
        {F.frob(a) for a in V} == set(V)))
    assert sT == set(T) and twprod(F, T) == set(T)
    assert sumset(F, V) == set(V) and {F.frob(a) for a in V} == set(V)

def bool_check(p, l, D=2, trials=400, seed=529):
    # random Boolean combos of random Fp-slice atoms: small-or-cosmall?
    rng = random.Random(seed)
    F = load(p, l); z = F.z; q = F.q
    mons = [(a, b) for a in range(D + 1) for b in range(D + 1 - a)]
    atoms = []
    for _ in range(60):
        coeff = tuple(rng.randrange(p) for _ in mons)
        if all(c == 0 for c in coeff): continue
        atoms.append({x for x in F.els if ev(F, x, F.frob(x), mons, coeff) == z})
    B = D * p * 2  # allow union bound over 2 atoms
    bad = 0
    for _ in range(trials):
        A1, A2 = rng.choice(atoms), rng.choice(atoms)
        op = rng.randrange(6)
        if op == 0: S = A1 | A2
        elif op == 1: S = A1 & A2
        elif op == 2: S = A1 - A2
        elif op == 3: S = A1 ^ A2
        elif op == 4: S = (A1 | A2) - (A1 & A2)
        else: S = set(F.els) - (A1 | A2)
        n = len(S)
        if not (n <= B or n >= q - B):
            bad += 1
            if bad <= 3: print("   VIOL n=%d (B=%d q=%d)" % (n, B, q))
    print("p=%d l=%d: bool trials=%d BAD=%d (bound B=%d, q=%d)" % (p, l, trials, bad, B, q))
    return bad

def main():
    for (p, l) in [(2, 2), (3, 2), (5, 2), (2, 3), (3, 3)]:
        check_identities(p, l)
    tot = 0
    for (p, l) in [(3, 2), (5, 2), (3, 3)]:
        tot += bool_check(p, l)
    print("VERIFY_OK" if tot == 0 else "VERIFY_FAIL")

if __name__ == "__main__":
    main()
