"""Replay verifier for lane-340 girth>=5 ceilings at n=54,55,56 (stdlib only).
Checks:
  (A) Unconditional KST ceilings: U_KST = 210/216/222 via integer inequality
      2m(2m-n) <= n^2(n-1) (holds at U, fails at U+1).
  (B) Anchored induction ceilings from external anchor a(53)=181:
      a(n) <= floor(n*a(n-1)/(n-2)) -> 187/194/201 (exact integer division
      checks, quotient*div <= num < (quotient+1)*div).
  (C) Witness graphs in graphs.json: vertex counts, edge counts, C3/C4-freeness.
Usage: python3 output/artifacts/verify.py
"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
ANCHOR = 181
KST_U = {54: 210, 55: 216, 56: 222}
ANCH_U = {54: 187, 55: 194, 56: 201}

def kst_ok(n, m):
    return 2 * m * (2 * m - n) <= n * n * (n - 1)

def check_kst():
    for n, U in KST_U.items():
        assert kst_ok(n, U), f"KST holds check failed n={n} U={U}"
        assert not kst_ok(n, U + 1), f"KST tightness check failed n={n} U+1={U+1}"
        print(f"KST n={n}: {2*U*(2*U-n)} <= {n*n*(n-1)} < {2*(U+1)*(2*(U+1)-n)}  U={U} OK")

def check_anchored():
    a = {53: ANCHOR}
    for n in (54, 55, 56):
        num = n * a[n - 1]
        div = n - 2
        q = ANCH_U[n]
        assert num // div == q, f"induction quotient mismatch n={n}"
        assert q * div <= num < (q + 1) * div, f"induction division check failed n={n}"
        a[n] = q
        print(f"anchored n={n}: floor({num}/{div})={q} "
              f"({q}*{div}={q*div} <= {num} < {(q+1)*div}={ (q+1)*div}) OK")

def audit(n, adj):
    assert len(adj) == n, f"vertex count {len(adj)} != {n}"
    A = [set(x) for x in adj]
    for i in range(n):
        assert i not in A[i], f"loop at {i}"
        for j in A[i]:
            assert 0 <= j < n and i in A[j], f"asymmetry {i}-{j}"
    e = sum(map(len, A)) // 2
    for i in range(n):
        for j in A[i]:
            if j > i and A[i] & A[j]:
                raise AssertionError(f"triangle via edge {i}-{j}")
    for i in range(n):
        for j in range(i + 1, n):
            if len(A[i] & A[j]) > 1:
                raise AssertionError(f"C4 via pair {i}-{j}")
    return e

def check_witnesses():
    graphs = json.load(open(os.path.join(BASE, "graphs.json")))
    for n in (54, 55, 56):
        e = audit(n, graphs[str(n)])
        print(f"witness n={n}: edges={e}, C3-free OK, C4-free OK")

if __name__ == "__main__":
    check_kst()
    check_anchored()
    check_witnesses()
    print("VERIFY_OK")
