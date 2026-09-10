"""Cell scan: primitive 3x3 (0,1) matrices up to permutation similarity.

Computes for each class representative A:
  - SNF of I - A^t  -> K0(O_A) = coker, K1(O_A) = ker (rank)
  - unit class [1_A] = class of (1,1,1) in coker
  - det(I - A^t), tr(A^k) k=1,2,3 (periodic data)
Groups by (SNF diag, K1 rank) to exhibit Elliott collisions.
Pure python + sympy only. Writes invariant_table.json + prints summary.
"""
import itertools
import json

import sympy as sp


def mat_mul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def mat_pow(A, k):
    n = len(A)
    P = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for _ in range(k):
        P = mat_mul(P, A)
    return P


def is_primitive(A):
    # Wielandt bound (n-1)^2+1 = 5 for n=3
    for m in range(1, 6):
        if all(v > 0 for row in mat_pow(A, m) for v in row):
            return True
    return False


PERMS = list(itertools.permutations([0, 1, 2]))


def canon(A):
    best = None
    for p in PERMS:
        t = tuple(A[p[i]][p[j]] for i in range(3) for j in range(3))
        if best is None or t < best:
            best = t
    return best


def snf_of(M):
    from sympy.matrices.normalforms import smith_normal_form
    D = smith_normal_form(sp.Matrix(M))
    return tuple(int(D[i, i]) for i in range(3))


def main():
    mats = []
    for bits in itertools.product([0, 1], repeat=9):
        A = [list(bits[i * 3:(i + 1) * 3]) for i in range(3)]
        if is_primitive(A):
            mats.append(A)
    print("primitive ordered count:", len(mats))
    classes = {}
    for A in mats:
        classes.setdefault(canon(A), A)
    print("classes up to perm similarity:", len(classes))
    rows = []
    for c in sorted(classes):
        A = classes[c]
        At = [[A[j][i] for j in range(3)] for i in range(3)]
        ImAt = [[(1 if i == j else 0) - At[i][j] for j in range(3)] for i in range(3)]
        d = snf_of(ImAt)
        det = int(sp.Matrix(ImAt).det())
        rank = sum(1 for x in d if x != 0)
        k1 = 3 - rank
        tr = [sum(mat_pow(A, k)[i][i] for i in range(3)) for k in (1, 2, 3)]
        rows.append({"A": A, "snf": list(d), "det": det, "k1rank": k1, "tr": tr})
    with open("output/artifacts/invariant_table.json", "w") as f:
        json.dump(rows, f, indent=1)
    from collections import defaultdict
    grp = defaultdict(list)
    for r in rows:
        grp[(tuple(r["snf"]), r["k1rank"])].append(r)
    ncoll = sum(1 for v in grp.values() if len(v) > 1)
    print("distinct (SNF,K1) keys:", len(grp), "| keys with collisions:", ncoll)
    for k in sorted(grp):
        v = grp[k]
        if len(v) > 1:
            print("KEY snf=", k[0], "k1rank=", k[1], "size=", len(v))
            for r in v:
                print("   A=", r["A"], "det=", r["det"], "tr=", r["tr"])


if __name__ == "__main__":
    main()
