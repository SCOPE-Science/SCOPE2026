"""Exhaustive stage-3 gap-1/4 projection-witness census (exact integer arithmetic).

Setup: stage 3 has N3=32, t3=26 coords, D3=52. A witness in M_K(A3) with
normalized gap g=1/4 has absolute rank gap c = g*K*N3 = 8K.
Write a = E_m + th^t (m Bott lines on distinct coords + t trivial lines),
b = th^{m+t+c} (trivial target; non-identity required: m+t+c < K*N3).
Complement of E_m inside b: R = t + c. Chern obstruction iff m > R.
Coordinate budget: m <= t3 = 26. Rank budget: m+t+c <= K*N3 - 1 (strict:
target non-identity).

Certifies:
 (1) K >= 4 admits NO stage-3 obstructed witness: R >= c = 8K >= 32 > 26 >= m.
 (2) Full enumeration for K=1,2,3 of all (m,t) with m<=26, m+t+8K<K*N3... wait
     K*N3 with strict < : m+t+8K <= K*32-1, m>R=t+8K: list count, max m/R,
     and per-design Chern-shadow wash stage w = least j>=3 with
     m*3^{j-3} < R*4^{j-3} (i.e. (m/R)*(3/4)^{j-3}<1).
 (3) Uniform conclusion: EVERY stage-3 gap-1/4 projection witness with genuine
     Chern obstruction washes by j <= 7 (max over census); hence none persists
     to the limit. Combined with the stable-range J(1/4)=8 (independent route),
     step-4 persistence fails exhaustively, not just for sample witnesses.
 (4) Design optimality: pure (t=0) maximizes m/R; global max m/R over census
     identified with its wash stage.

Stdlib only. Prints VERIFY_OK.
"""
from fractions import Fraction
import math

N3, T3 = 32, 26

def wash_stage(m, R):
    # least j>=3 with m*3^{j-3} < R*4^{j-3}; assumes m>R>=1
    assert m > R >= 1
    j = 3
    while True:
        if m * (3 ** (j - 3)) < R * (4 ** (j - 3)):
            return j
        j += 1
        assert j < 100

def main():
    print("(1) K>=4 impossibility:")
    for K in (4, 5, 8, 100):
        c = 8 * K
        # R >= c > 26 >= m always
        assert c > T3, K
        print(f"  K={K}: c=8K={c} > 26 >= m, so m>R impossible. No witness. OK")

    print("(2) exhaustive census K=1,2,3:")
    total = 0
    maxratio = Fraction(0)
    maxdesign = None
    maxwash = 0
    washlist = []
    for K in (1, 2, 3):
        c = 8 * K
        cap = K * N3 - 1  # strict non-identity: m+t+c <= cap
        nK = 0
        for m in range(0, T3 + 1):
            for t in range(0, cap + 1):
                if m + t + c > cap:
                    break
                R = t + c
                if m > R:
                    nK += 1
                    total += 1
                    r = Fraction(m, R)
                    w = wash_stage(m, R)
                    washlist.append(w)
                    if r > maxratio:
                        maxratio = r
                        maxdesign = (K, m, t, R)
                    if w > maxwash:
                        maxwash = w
        print(f"  K={K}: c={c}, cap={cap}, obstructed (m,t) count={nK}")
    print(f"  total obstructed designs: {total}")
    print(f"  max m/R = {maxratio} ~ {float(maxratio):.4f} at {maxdesign}")
    print(f"  max Chern-shadow wash stage = {maxwash}")
    assert total > 0
    assert maxwash <= 7, maxwash
    # exact max: K=1 pure m=23,t=0,R=8 gives 23/8=2.875; check it is the max
    assert maxratio == Fraction(23, 8), maxratio
    assert maxdesign == (1, 23, 0, 8), maxdesign
    assert wash_stage(23, 8) == 7
    print("  max design (K=1,m=23,t=0,R=8), wash j=7 OK")

    print("(3) uniform wash bound:")
    assert max(washlist) <= 7
    # every design washed strictly before stable-range J(1/4)=8 (or at 7<8)
    print(f"  all {total} designs wash at j<=7 < J(1/4)=8. Uniform persistence")
    print("  failure exhaustive over ALL stage-3 gap-1/4 projection witnesses. OK")

    print("(4) spot table (pure optimal per K):")
    for K, m in [(1, 23), (2, 26), (3, 26)]:
        c = 8 * K
        R = c  # t=0
        assert m > R
        w = wash_stage(m, R)
        print(f"  K={K}: m={m}, R={R}, m/R={Fraction(m,R)}, wash j={w}")
    # K=2 pure: 26/16, wash 5; K=3 pure m=26,R=24: 26/24, wash 4
    assert wash_stage(26, 16) == 5
    assert wash_stage(26, 24) == 4

    # coordinate-budget persistence for the max design (fits through wash):
    m = 23
    for j in range(3, 9):
        assert m * (3 ** (j - 3)) <= 3 ** j - 1, j
    print("  max-design coordinate budgets fit through j=8 OK")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
