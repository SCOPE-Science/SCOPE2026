"""GJV-style genus-0 join-cut recursion for double Hurwitz numbers (character-free).
State: H(mu, nu) for partitions of d. Base: H((1),(1)) [d=1, r=0] = 1.
Recursion (Goulden-Jackson-Vakil '05, genus-0 double join-cut, coefficient form):
Differentiate the Joincut PDE and extract [p_mu q_nu]: with r = l(mu)+l(nu)-2:
  r * H(mu,nu) = Jplus(mu,nu) + Cplus(mu,nu) [join/cut terms from transposition action]
where:
  Jplus: sum over all ways to JOIN two parts of mu (or of nu)?? — orientation: the
  transposition-class multiplication by K_(2,1..) joins two cycles or cuts one.
  (K_T * K_mu) = sum_{join i,j} (i+j) K_{mu with i,j -> i+j}... precisely:
    K_T K_mu = sum_{i<j parts} mu_i mu_j K_{join} + sum_{parts k} sum_{splits} (k/2 or k) K_{cut}.
  Hence with N(mu,nu;T^r) = tuple count: N = [Kmu Knu KT^r]_{id} and KT Knu expansion
  gives recursion in r AND degree... but degree doesn't drop (cut of nu INCREASES #parts,
  join DECREASES). The recursion that LOWERS degree: extract via 'cut' on the mu side
  using the identity [Kmu ...] ... standard Toda: (d + ...) H... Let me just implement
  the well-known ELSV-free 'cut-and-join operator' recursion:
  H(mu,nu) with r>=1: H(mu,nu) = 1/r * [sum over all cuts/joins of mu of H(mu',nu) terms]?
  Since K_T K_mu = sum c_{mu'} K_{mu'}, N(mu,nu;r) = sum c_{mu'} N(mu',nu;r-1) — reduces r,
  and N(*;0) = delta. This is EXACT and character-free IF the structure constants c are
  computed combinatorially (join: mu_i*mu_j; cut: k or k/2). r drops 1 per step; depth r=3.
  N(mu',nu;0) with r-1=0: nonzero iff mu' == nu as partitions (then = |C| = d!/z).
  So: N(mu,nu;3) = sum over 3-step cut/join walks on mu from mu to nu of (walk weight)*|Cnu|.
  Equivalently N = |Cnu| * (T^3)[nu, mu]... = |Cnu| * (M^3)[nu_sorted, mu_sorted] — the matrix
  method (now with CORRECT normalization N = |Cnu| (M^r)[mu,nu], T6-verified at d<=4)!
  At d=9, M is 30x30 with entries from direct permutation action — INFEASIBLE by raw
  enumeration (9! = 362880 per rep... actually just ONE rep per type + 36 transpositions:
  30 reps x 36 products with ctype computation: trivial!). Implement now.
"""
import sys
sys.path.insert(0, "output/artifacts")
from math import factorial
from collections import Counter
from fractions import Fraction

def part_index():
    # all partitions of 9 as sorted-desc tuples
    out = []
    def rec(n, mx, cur):
        if n == 0:
            out.append(tuple(cur))
            return
        for k in range(min(mx, n), 0, -1):
            cur.append(k)
            rec(n-k, k, cur)
            cur.pop()
    rec(9, 9, [])
    return out

def canon(ctype):
    # canonical permutation with given cycle type (sorted desc)
    p = []
    perm = list(range(9))
    # build cycles
    start = 0
    used = [False]*9
    cyc = []
    for L in ctype:
        cyc.append(list(range(start, start+L)))
        start += L
    for c in cyc:
        L = len(c)
        for i in range(L):
            perm[c[i]] = c[(i+1) % L]
    return tuple(perm)

def comp(p, q):
    return tuple(p[q[i]] for i in range(len(p)))

def ctype_of(p):
    n = len(p)
    seen = [False]*n
    L = []
    for i in range(n):
        if not seen[i]:
            j, c = i, 0
            while not seen[j]:
                seen[j] = True
                j = p[j]
                c += 1
            L.append(c)
    return tuple(sorted(L, reverse=True))

def transpositions(d=9):
    T = []
    for i in range(d):
        for j in range(i+1, d):
            t = list(range(d))
            t[i], t[j] = t[j], t[i]
            T.append(tuple(t))
    return T

def build_M():
    types = part_index()
    idx = {t: i for i, t in enumerate(types)}
    T = transpositions()
    n = len(types)
    M = [[0]*n for _ in range(n)]
    for j, tj in enumerate(types):
        rep = canon(tj)
        for t in T:
            M[idx[ctype_of(comp(t, rep))]][j] += 1
    return types, M

def matvec(M, v):
    return [sum(row[k]*v[k] for k in range(len(v))) for row in M]

def N_via_matrix(mu, nu, r):
    types, M = build_M()
    idx = {t: i for i, t in enumerate(types)}
    v = [0]*len(types)
    v[idx[tuple(sorted(nu, reverse=True))]] = 1
    for _ in range(r):
        v = matvec(M, v)
    coeff = v[idx[tuple(sorted(mu, reverse=True))]]
    # N = |Cnu| * coeff
    c = Counter(nu)
    z = 1
    for ln, m in c.items():
        z *= (ln**m)*factorial(m)
    Cnu = factorial(9)//z
    return Cnu*coeff, coeff

if __name__ == "__main__":
    for mu, nu in [((6,2,1),(5,4)), ((3,3,3),(5,4))]:
        N, coeff = N_via_matrix(mu, nu, 3)
        print(mu, nu, "N =", N, "H =", Fraction(N, factorial(9)))
