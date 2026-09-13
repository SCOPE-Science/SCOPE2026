"""Tactical-matrix / polarity compatibility level (exact, exhaustive over involutions).
T must be 10x10 with entries in {0,5}, row/col sums 45 => T = 5(J-P), P a
permutation matrix. Symmetric T <=> P symmetric <=> P an involution.
Polarity condition T_ij = T_{pi^-1(j), pi(i)}: with pi=id every symmetric T works.
Also: symmetric incidence => absolute-point count a = trace(N) in {0,10,...,100}
(from eigenvalues 45^1, 5/ -5 pattern); orthogonal needs a>0, a==20 feasible.
Conclusion: tactical level imposes NO obstruction; many (T, pi, p) triples exist.
"""
import itertools

def involutions(n):
    # yield all involutive permutation matrices as tuples p with p[p[i]]==i
    res = []
    def rec(i, p):
        if i == n:
            res.append(tuple(p)); return
        if p[i] is not None:
            rec(i+1, p); return
        # fix i
        p[i] = i; rec(i+1, p); p[i] = None
        # pair i with j>i
        for j in range(i+1, n):
            if p[j] is None:
                p[i]=j; p[j]=i; rec(i+1, p); p[i]=None; p[j]=None
    rec(0, [None]*n)
    return res

INVS = involutions(10)
print("involutions(10) =", len(INVS))
# row/col sum check for T=5(J-P): every row of J-P sums to 10-1=9 -> 45. Always.
assert all(sum(1 for j in range(10) if j != p[i]) == 9 for p in INVS for i in range(10))
# deranged involutions (fixed-point-free) count: round(10!/e)/... just count
der = [p for p in INVS if all(p[i] != i for i in range(10))]
print("deranged involutions(10) =", len(der))  # expect 949
# canonical choice: p = (0 1)(2 3)(4 5)(6 7)(8 9), pi = id
p = [1,0,3,2,5,4,7,6,9,8]
T = [[0 if j == p[i] else 5 for j in range(10)] for i in range(10)]
assert all(sum(r) == 45 for r in T) and all(sum(T[i][j] for i in range(10)) == 45 for j in range(10))
assert all(T[i][j] == T[j][i] for i in range(10) for j in range(10))
# polarity compatibility with pi=id: T_ij == T_{j,i} (symmetric) holds
print("canonical T row sums ok, symmetric ok")
# absolute-point arithmetic: a = 45 + 5*(nplus-nminus), nplus+nminus=99 -> a in {0,10,...,100}
vals = sorted({45 + 5*d for d in range(-99, 100) if (99+d) % 2 == 0 and 0 <= 45+5*d <= 100})
print("admissible absolute-point counts:", vals)
assert 20 in vals
print("TACTICAL LEVEL: FEASIBLE (no obstruction).")
