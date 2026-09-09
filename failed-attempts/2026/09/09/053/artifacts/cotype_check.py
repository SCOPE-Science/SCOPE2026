"""Spot-check of Lemma 1 chain on random instances via exact sign enumeration."""
import itertools, math, random

def E_norm2_sq(A, p):
    # A: list of vectors (m x n); exact E_epsilon ||sum e_i v_i||_p^2
    m = len(A); n = len(A[0])
    tot = 0.0
    for bits in itertools.product([-1,1], repeat=m):
        s = [sum(bits[i]*A[i][j] for i in range(m)) for j in range(n)]
        tot += sum(abs(x)**p for x in s)**(2.0/p)
    return tot / 2**m

random.seed(0)
worst = 1e9
for trial in range(20):
    m, n = 3, 4
    p = random.choice([1.0, 1.25, 1.5, 1.75, 2.0])
    A = [[random.uniform(-2,2) for _ in range(n)] for _ in range(m)]
    lhs = sum(sum(abs(x)**p for x in v)**(2.0/p) for v in A)
    rhs = E_norm2_sq(A, p)
    ratio = rhs / lhs if lhs>1e-9 else float('inf')
    worst = min(worst, ratio)
    print(f"p={p} sum||v||^2={lhs:.4f} E||S||^2={rhs:.4f} ratio={ratio:.4f}")
print("min ratio (must be >= 0.5):", worst)
assert worst >= 0.5 - 1e-9, "cotype lemma violated!"
print("COTYPE_CHECK_OK")
