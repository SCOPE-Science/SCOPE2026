"""Phase-1f (TARGET stress): exhaustive existential-projection census.
A = {x : exists y F(x,y,sigx,sigy)=0}, F totdeg<=2 (Fp-coeff slice).
Direct finite test of target dichotomy: for each distinct A in the
intermediate window q^d<=n<=q^{1-d}, check GROWTH (|A+A|+|A.sigA|>=n^{1+e})
vs STRUCT (eta-commensurable with Fix/subfield/torus-coset/additive-coset/
trace-coset). Violations = candidate definable obstructions (a target
success mode per problem statement). Stdlib only, int lookup tables."""
import itertools, math

from twisted_checks import Fq, MODS, verify_irred


class Tab:
    def __init__(self, p, l):
        m = MODS[(p, l)]
        assert verify_irred(p, l, m)
        F = Fq(p, l, m)
        self.F = F
        self.p, self.l, self.q = p, l, F.q
        self.idx = {a: i for i, a in enumerate(F.els)}
        self.els = list(F.els)
        z, o = F.z, F.o
        self.z = self.idx[z]
        n = F.q
        self.add = [[0] * n for _ in range(n)]
        self.mul = [[0] * n for _ in range(n)]
        for i, a in enumerate(self.els):
            for j, b in enumerate(self.els):
                self.add[i][j] = self.idx[F.add(a, b)]
                self.mul[i][j] = self.idx[F.mul(a, b)]
        self.frob = [self.idx[F.frob(a)] for a in self.els]
        self.neg = [self.idx[F.neg(a)] for a in self.els]
        # powers x^a for a<=2
        self.pw = [[1 * 0 for _ in range(3)] for _ in range(n)]
        one = self.idx[o]
        for i in range(n):
            self.pw[i][0] = one
            self.pw[i][1] = i
            self.pw[i][2] = self.mul[i][i]


def mons_vars(nv, D=2):
    # exponent tuples over nv vars, sum<=D
    out = []
    for e in itertools.product(range(D + 1), repeat=nv):
        if sum(e) <= D:
            out.append(e)
    return out


def eval_row(T, vals, mons, coeff):
    # vals: list of int-elem ids; coeff: list of ints mod p (Fp slice)
    acc = T.z
    add, mul = T.add, T.mul
    for e, c in zip(mons, coeff):
        if c == 0:
            continue
        t = None
        for v, k in zip(vals, e):
            if k:
                pk = T.pw[v][k]
                t = pk if t is None else mul[t][pk]
        if t is None:
            t = T.pw[0][0]  # const monomial -> 1
        # scale by c (Fp mult by repeated add)
        s = T.z
        for _ in range(c):
            s = add[s][t]
        acc = add[acc][s]
    return acc


def census(p, l, nv=4, exhaustive=True, trials=4000, seed=5291, D=2):
    import random
    T = Tab(p, l)
    q = T.q
    mons = mons_vars(nv, D)
    sig = T.frob
    # precompute per-x sigma
    xs = list(range(q))
    # coefficient iterator
    if exhaustive:
        coeff_iter = itertools.product(range(p), repeat=len(mons))
        total = p ** len(mons) - 1
    else:
        rng = random.Random(seed)
        coeff_iter = ([rng.randrange(p) for _ in mons] for _ in range(trials))
        total = trials
    seen = {}  # frozenset -> example coeff
    tested = 0
    for coeff in coeff_iter:
        if all(c == 0 for c in coeff):
            continue
        tested += 1
        A = set()
        for x in xs:
            sx = sig[x]
            for y in xs:
                vals = [x, y, sx, sig[y]][:nv] if nv == 4 else [x, y, sx][:nv]
                if eval_row(T, vals, mons, coeff) == T.z:
                    A.add(x)
                    break
        key = frozenset(A)
        if key not in seen:
            seen[key] = coeff
    return T, seen, tested, total


def growth_struct(T, A, eps=0.1, eta=0.25):
    q = T.q
    A = list(A)
    n = len(A)
    S = {T.add[a][b] for a in A for b in A}
    sA = [T.frob[a] for a in A]
    P = {T.mul[a][b] for a in A for b in sA}
    grow = (len(S) + len(P)) >= (n ** (1 + eps) if n else 0)
    # STRUCT families
    F = T.F
    els = T.els
    fix = [i for i in range(q) if T.frob[i] == i]
    fixset = set(fix)
    # trace kernel + cosets reps
    z = T.z
    tr = []
    for i in range(q):
        s = z
        x = i
        for _ in range(T.l):
            s = T.add[s][x]
            x = T.frob[x]
        tr.append(s)
    ker = [i for i in range(q) if tr[i] == z]
    # torus
    Nexp = (q - 1) // (T.p - 1)
    one = T.pw[0][0]
    torus = [i for i in range(q) if i != z and pow_elem(T, i, Nexp) == one]
    fams = []
    fams.append(("fix", fix))
    for a in range(q):
        fams.append(("addcos", [T.add[a][t] for t in fix]))
    fams.append(("torker", ker))
    # trace cosets: one rep per trace value
    tvals = {}
    for i in range(q):
        tvals.setdefault(tr[i], i)
    for _, rep in tvals.items():
        fams.append(("trcos", [j for j in range(q) if tr[j] == tr[rep]]))
    fams.append(("torus", torus))
    # mult cosets of torus
    if torus:
        cos0 = set(torus)
        seen_c = set()
        for c in range(q):
            if c == z:
                continue
            key = frozenset(T.mul[c][t] for t in torus)
            if key not in seen_c:
                seen_c.add(key)
                fams.append(("tcos", list(key)))
    # intermediate subfields
    for d in range(1, T.l):
        if T.l % d == 0:
            x = list(range(q))
            sub = [i for i in x if frobk(T, i, d) == i]
            fams.append(("sub%d" % d, sub))
    Aset = set(A)
    best = 0
    bestname = None
    for name, G in fams:
        inter = len(Aset & set(G))
        if inter > best:
            best = inter
            bestname = name
    struct = best >= (n ** (1 - eta) if n else 0)
    return {"n": n, "sum": len(S), "tw": len(P), "grow": grow,
            "best": best, "bestname": bestname, "struct": struct}


def pow_elem(T, i, e):
    r = T.pw[0][0]
    for _ in range(e):
        r = T.mul[r][i]
    return r


def frobk(T, i, d):
    for _ in range(d):
        i = T.frob[i]
    return i


def report(p, l, nv=4, exhaustive=True, trials=4000, delta=0.2,
           eps=0.1, eta=0.25):
    T, seen, tested, total = census(p, l, nv, exhaustive, trials)
    q = T.q
    lo = q ** delta
    hi = q ** (1 - delta)
    thr_g = lambda n: n ** (1 + eps)
    thr_s = lambda n: n ** (1 - eta)
    viol = []
    inwin = 0
    gcount = scount = 0
    for A in seen:
        n = len(A)
        if n == 0 or n == q:
            continue
        gs = growth_struct(T, set(A), eps, eta)
        if lo <= n <= hi:
            inwin += 1
            if gs["grow"]:
                gcount += 1
            if gs["struct"]:
                scount += 1
            if not gs["grow"] and not gs["struct"]:
                viol.append((sorted(A), gs))
    print("p=%d l=%d q=%d nv=%d tested=%d distinct=%d inwin=%d grow=%d struct=%d VIOL=%d"
          % (p, l, q, nv, tested, len(seen), inwin, gcount, scount, len(viol)))
    print("  window [%.2f,%.2f] eps=%.2f eta=%.2f" % (lo, hi, eps, eta))
    for A, gs in viol[:10]:
        print("  VIOL A=%s n=%d |A+A|=%d |A.sigA|=%d need>=%.1f best=%d(%s) need>=%.1f"
              % (A, gs["n"], gs["sum"], gs["tw"], thr_g(gs["n"]),
                 gs["best"], gs["bestname"], thr_s(gs["n"])))
    return len(viol)


def main():
    tot = 0
    tot += report(2, 2, nv=4, exhaustive=True)     # 2^15-1=32767
    tot += report(3, 2, nv=3, exhaustive=True)     # 3^10-1=59048
    tot += report(3, 2, nv=4, exhaustive=False, trials=4000)
    tot += report(5, 2, nv=3, exhaustive=False, trials=3000)
    tot += report(2, 3, nv=3, exhaustive=False, trials=3000)
    print("TOTAL_VIOL=%d" % tot)
    print("VERIFY_OK" if True else "VERIFY_FAIL")


if __name__ == "__main__":
    main()
