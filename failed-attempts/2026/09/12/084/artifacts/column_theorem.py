"""Column lower-bound theorem verification + C4^2 exact check (reproducible).
Run: python3 column_theorem.py
Theorem: for G=(Z_N)^2 (any N>=2), S={(1,j):1<=j<=N-1} U {(0,j):1<=j<=b}
with T_b=b(b+1)/2<N is zero-sum-free. Hence Ol(G) >= N+b.
Proof: split T=T1+T0 (x=1 part of size r; x=0 part). x-sum=r in 0..N-1.
 r>=1 -> x-sum in 1..N-1, nonzero mod N. r=0 -> pure column subset with
 integer y-sum in 1..T_b<N, nonzero mod N. QED.
"""
from math import comb

def has_zero_subset(S, mod):
    if not S:
        return False
    reach = set()
    for g in S:
        new = {g}
        for s in list(reach):
            new.add(((s[0] + g[0]) % mod, (s[1] + g[1]) % mod))
        reach |= new
        if (0, 0) in reach:
            return True
    return (0, 0) in reach

def max_b(N):
    b = 0
    while (b + 1) * (b + 2) // 2 < N:
        b += 1
    return b

for N in [4, 9, 25, 49, 121]:
    b = max_b(N)
    S = [(1, j) for j in range(1, N)] + [(0, j) for j in range(1, b + 1)]
    assert (b * (b + 1)) // 2 < N
    print(f"N={N}: b={b} |S|={len(S)} Ol((Z_N)^2)>={len(S)+1} Davenport<={2*N-1}")
    if N <= 9:
        assert not has_zero_subset(S, N), f"column set has zero-sum for N={N}!"
        print("  brute-force verified zero-sum-free")
print("column theorem instances OK")
