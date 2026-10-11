from fractions import Fraction
from itertools import combinations_with_replacement, product

def monomials_of_weight(weights, target):
    if target < 0:
        return []
    out = []
    def rec(i, rem, exps):
        if i == len(weights)-1:
            w = weights[i]
            if rem % w == 0:
                out.append(tuple(exps + [rem//w]))
            return
        w = weights[i]
        for e in range(rem//w + 1):
            rec(i+1, rem-e*w, exps+[e])
    rec(0, target, [])
    return out

def rank_rational(rows):
    if not rows:
        return 0
    A = [[Fraction(x) for x in row] for row in rows]
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        piv = next((i for i in range(r,m) if A[i][c]), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        q = A[r][c]
        A[r] = [x/q for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                q = A[i][c]
                A[i] = [A[i][j]-q*A[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r

def kernel_dim(weights, t):
    cod = monomials_of_weight(weights, t)
    cod_index = {m:i for i,m in enumerate(cod)}
    domain = []
    for i,a in enumerate(weights):
        for m in monomials_of_weight(weights, t-a):
            domain.append((i,m))
    if not domain:
        return 0
    M = [[0 for _ in domain] for __ in cod]
    for j,(i,m) in enumerate(domain):
        mm = list(m)
        mm[i] += 1
        mm = tuple(mm)
        M[cod_index[mm]][j] = weights[i]
    return len(domain) - rank_rational(M)

checked = 0
for weights in combinations_with_replacement(range(1,7), 4):
    threshold = weights[0] + weights[1]
    for t in range(threshold):
        assert kernel_dim(weights, t) == 0, (weights,t,kernel_dim(weights,t))
    assert kernel_dim(weights, threshold) >= 1, (weights,threshold)
    checked += 1

w = (2,3,5,7)
dims = [kernel_dim(w,t) for t in range(6)]
assert dims[:5] == [0,0,0,0,0]
assert dims[5] >= 1

d = 210
exponents = tuple(d//a for a in w)
assert exponents == (105,70,42,30)
assert all(a*e == d for a,e in zip(w,exponents))
assert d > sum(w)
assert w[0]+w[1] == 5 < d

print(f"weight_quadruples_checked={checked}")
print("all_kernels_below_pair_sum=zero")
print("all_kernels_at_pair_sum=nonzero")
print("example_weights=2,3,5,7")
print("example_kernel_dims_t0_to_t5="+",".join(map(str,dims)))
print("example_threshold=5")
print("example_degree=210")
print("example_fermat_exponents=105,70,42,30")
print("VERIFY_OK")
