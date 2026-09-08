"""Exact finite lattice-embedding decision procedure (stdlib only).

Decides: given integer symmetric positive-definite r x r matrix P (= -G for a
negative-definite Goeritz Gram matrix G), and target rank N, does there exist an
integer r x N matrix M with M @ M.T == P (isometric embedding of the lattice
defined by P into the standard diagonal lattice I_N)?

Method: finite enumeration of integer vectors of prescribed norm + row-by-row
backtracking with exact integer inner-product checks. Complete: every embedding
is enumerated (up to the requested cap); sound: everything returned is checked.
"""
import itertools, sys

def mat_mul_T(M):
    r = len(M); N = len(M[0]) if r else 0
    return [[sum(M[i][k]*M[j][k] for k in range(N)) for j in range(r)] for i in range(r)]

def bareiss_det(A):
    n = len(A)
    if n == 0: return 1
    M = [row[:] for row in A]
    prev = 1
    for k in range(n-1):
        if M[k][k] == 0:
            piv = next((i for i in range(k+1, n) if M[i][k] != 0), None)
            if piv is None: return 0
            M[k], M[piv] = M[piv], M[k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                M[i][j] = (M[i][j]*M[k][k] - M[i][k]*M[k][j]) // prev
            M[i][k] = 0
        prev = M[k][k]
    return M[n-1][n-1]

def is_symmetric(P):
    r = len(P)
    return all(P[i][j] == P[j][i] for i in range(r) for j in range(r))

def leading_minor(P, k):
    return bareiss_det([row[:k] for row in P[:k]])

def is_positive_definite(P):
    if not is_symmetric(P): return False
    return all(leading_minor(P, k) > 0 for k in range(1, len(P)+1))

def enum_vectors(norm, N):
    """Yield all integer vectors in Z^N with sum of squares == norm, exactly."""
    assert norm >= 0 and N >= 1
    if norm == 0:
        yield [0]*N; return
    bound = int(norm**0.5) + 1
    # product enumeration is fine for the small demo norms used here
    rng = range(-bound, bound+1)
    for v in itertools.product(rng, repeat=N):
        if sum(x*x for x in v) == norm:
            yield list(v)

def find_embeddings(P, N, cap=1000000, max_solutions=None):
    """Return (solutions, exhaustive_flag). solutions = list of r x N matrices M
    with M M^T == P. Search is exhaustive (flag True) unless capped."""
    r = len(P)
    assert is_positive_definite(P), "P must be symmetric positive-definite"
    assert N >= 1
    # necessary rank bound shortcut (still exhaustive: empty list)
    if r > N:
        return [], True
    cand = [list(enum_vectors(P[i][i], N)) for i in range(r)]
    sols = []
    count_examined = [0]
    cur = []
    def rec(i):
        if max_solutions is not None and len(sols) >= max_solutions:
            return True  # stop signal
        if i == r:
            sols.append([row[:] for row in cur])
            return False
        for v in cand[i]:
            if len(sols) + 0 > cap: return True
            ok = True
            for j in range(i):
                if sum(v[k]*cur[j][k] for k in range(N)) != P[i][j]:
                    ok = False; break
            if not ok: continue
            cur.append(v)
            stop = rec(i+1)
            cur.pop()
            if stop: return True
        return False
    capped = rec(0)
    return sols, (not capped)

def check_solution(P, M):
    return mat_mul_T(M) == P

def run_self_tests():
    out = []
    def log(s): out.append(s); print(s)
    # T1: [2] into I_1: x^2=2 has no integer solution
    s, ex = find_embeddings([[2]], 1)
    assert s == [] and ex, "T1"
    log("T1 PASS: P=[[2]] N=1 -> 0 embeddings (exhaustive)")
    # T2: [2] into I_2: (+-1,+-1), exactly 4
    s, ex = find_embeddings([[2]], 2)
    assert len(s) == 4 and ex and all(check_solution([[2]], m) for m in s), "T2"
    log("T2 PASS: P=[[2]] N=2 -> 4 embeddings (exhaustive)")
    # T3a: A2 into I_2: none (det 3 not a square)
    A2 = [[2,1],[1,2]]
    s, ex = find_embeddings(A2, 2)
    assert s == [] and ex, "T3a"
    assert bareiss_det(A2) == 3
    log("T3a PASS: A2 into I_2 -> 0 embeddings (exhaustive); det=3 nonsquare")
    # T3b: A2 into I_3: exists, e.g. (1,1,0),(1,0,1)
    s, ex = find_embeddings(A2, 3)
    assert len(s) > 0 and ex and all(check_solution(A2, m) for m in s), "T3b"
    log(f"T3b PASS: A2 into I_3 -> {len(s)} embeddings (exhaustive), all verified M M^T==P")
    # T4: rank bound 3x3 identity into I_2
    s, ex = find_embeddings([[1,0,0],[0,1,0],[0,0,1]], 2)
    assert s == [] and ex, "T4"
    log("T4 PASS: I_3 into I_2 -> 0 embeddings by rank bound (exhaustive)")
    # T5: soundness recheck on a larger demo: [[3,1],[1,3]] into I_3
    Q = [[3,1],[1,3]]
    assert is_positive_definite(Q) and bareiss_det(Q) == 8
    s, ex = find_embeddings(Q, 3)
    assert ex and all(check_solution(Q, m) for m in s)
    log(f"T5 PASS: P=[[3,1],[1,3]] N=3 -> {len(s)} embeddings (exhaustive), all verified")
    log("ALL SELF-TESTS PASSED")
    return "\n".join(out)

if __name__ == "__main__":
    run_self_tests()
