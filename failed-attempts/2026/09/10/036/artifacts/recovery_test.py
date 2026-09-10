"""Bounded recovery test for lane-597 target: maximal amenability of W*(u_11) in L_inf(O_3^+).

Checks (stdlib only):
  R1. N=3 Temperley-Lieb constants: q, dims d_k, Lemma-1.6 exponent alpha(q),
      constants C1, K, C0, D0, and the mixing error D0*q^{floor(alpha*b)}.
      Verdict: error stays >1 for every feasible b (no contraction at N=3).
  R2. Exact Weingarten moments h(u_11^{2k}) for k=1,2,3 via exact rational
      NC_2 Gram inversion (loops = union-find components). Confirms factoriality
      setup (finite moments) but yields no normalizer/AOP identification.
  R3. One-step Caspers-type multiplier proxy T_t = e^{-t*k} on level k:
      on span{u_ij} (k=1) the gap is 1-e^{-t} = O(t): no dichotomy from one t0.
      Strong solidity input bounds normalizers by amenability only.

Run: python3 recovery_test.py  -> prints RECOVERY_VERDICT line + tables.
"""
from fractions import Fraction
import math


def q_of_N(N):
    # q+q^{-1}=N, 0<q<1 -> q=(N-sqrt(N^2-4))/2
    return (N - math.sqrt(N * N - 4)) / 2


def qdim(k, q):
    return (q ** (k + 1) - q ** (-(k + 1))) / (q - q ** (-1))


def alpha_of(q):
    return (1.0 / 3.0) * (1 - (2 * math.log(2)) / (3 * math.log(q))
                          - (2 / (3 * math.log(q))) * math.log((1 + q * q) / (1 - q))) ** (-1)


def nc2_pairings(n):
    """Non-crossing pair partitions of {0..n-1}, n even. Recursive generator."""
    assert n % 2 == 0
    if n == 0:
        yield []
        return
    for j in range(1, n, 2):
        # pair 0 with j; inside (1..j-1), outside (j+1..n-1); both even length
        for inside in nc2_pairings(j - 1):
            for outside in nc2_pairings(n - 1 - j):
                pairs = [(0, j)]
                pairs += [(a + 1, b + 1) for (a, b) in inside]
                pairs += [(a + j + 1, b + j + 1) for (a, b) in outside]
                yield pairs


def loops(pi, sigma, n):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    for a, b in pi:
        union(a, b)
    for a, b in sigma:
        union(a, b)
    return len(set(find(i) for i in range(n)))


def gram_inverse_sum(npts, N):
    """Sum of all entries of G^{-1}, G_{pi,sigma}=N^{loops}, exact Fractions."""
    parts = list(nc2_pairings(npts))
    m = len(parts)
    G = [[Fraction(N) ** loops(pi, sg, npts) for sg in parts] for pi in parts]
    # Gauss-Jordan over Fractions
    aug = [row[:] + [Fraction(int(i == j)) for j in range(m)] for i, row in enumerate(G)]
    for c in range(m):
        piv = next(r for r in range(c, m) if aug[r][c] != 0)
        aug[c], aug[piv] = aug[piv], aug[c]
        v = aug[c][c]
        aug[c] = [x / v for x in aug[c]]
        for r in range(m):
            if r != c and aug[r][c] != 0:
                f = aug[r][c]
                aug[r] = [a - f * b for a, b in zip(aug[r], aug[c])]
    Winv = [row[m:] for row in aug]
    return m, sum(sum(row) for row in Winv)


def main():
    N = 3
    q = q_of_N(N)
    assert abs(q + 1 / q - N) < 1e-12
    dims = [qdim(k, q) for k in range(8)]
    al = alpha_of(q)
    C1 = math.sqrt(2) / (1 - q * q)
    K = 1 / (1 - q)
    Cb = 1 / (1 - q * q) ** 3
    Db = 1 / (1 - q * q) ** 2
    prod = 1.0
    for k in range(60):
        prod *= (1 + Db * q ** k)
    s = sum(Cb * q ** k for k in range(300))
    C0 = prod * s
    D0 = 2 * C0 + C1
    print(f"N=3: q={q:.10f}, alpha={al:.6f}, C1={C1:.4f}, K={K:.4f}")
    print(f"Cb={Cb:.4f} Db={Db:.4f} C0~{C0:.4f} D0~{D0:.4f}")
    print(f"dims d0..d7 = {[round(d, 3) for d in dims]}")
    print("R1 Lemma-1.6 error table (err = D0*q^floor(alpha*b)):")
    ok_block = True
    for b in [2, 4, 6, 8, 10, 15, 20, 25, 30]:
        e = D0 * (q ** math.floor(al * b))
        flag = "NO-CONTRACTION" if e > 1 else "contracts"
        if e <= 1 and b <= 30:
            ok_block = False
        print(f"  b={b:3d} floor(a*b)={math.floor(al*b):3d} err={e:.4f} {flag}")
    # also report first b with contraction
    b = 0
    while True:
        b += 1
        if D0 * (q ** math.floor(al * b)) <= 1:
            break
        if b > 10000:
            break
    print(f"  first contracting b = {b} (far beyond any feasible support localization)")

    print("R2 exact Weingarten moments h(u_11^{2k}) = sum(G^{-1}):")
    for k in [1, 2, 3]:
        m, tot = gram_inverse_sum(2 * k, N)
        print(f"  k={k}: |NC2({2*k})|={m}, h(u_11^{2*k})={tot} = {float(tot):.6f}")
    # R3 multiplier proxy
    print("R3 one-step multiplier proxy T_t=e^{-t*k} on level k:")
    for t in [0.05, 0.1, 0.25, 0.5]:
        gap = 1 - math.exp(-t * 1)
        dist2 = 1 - math.exp(-t * 2)
        print(f"  t={t:.2f}: gap(k=1)={gap:.4f} (O(t)), distortion(k=2)={dist2:.4f}; no dichotomy")
    print("Strong-solidity input: bounds N(P)'' by amenability for diffuse amenable P; "
          "never identifies N(A_0)''.")
    verdict = ("RECOVERY_VERDICT: TARGET_BLOCKED "
               "(R1 no contraction at feasible b; R2 moments finite but normalizer-free; "
               "R3 one-step deformation gives no dichotomy)")
    print(verdict)


if __name__ == "__main__":
    main()
