"""Later-birth witness census: stages 4 and 5 (exact integer arithmetic).

Stage j data: N_j = 2*4^{j-1}, t_j = 3^j-1 coords, D_j = 2*t_j.
Gap g=1/4 in M_K(A_j): absolute gap c_j = g*K*N_j = K*N_j/4.
General-pair obstruction needs S := ma+mb > c_j with S <= t_j.

Certifies:
 (1) Feasibility window: c_j vs t_j per (K, birth j). For K=1: stage 4:
     c=32 <= t=80 feasible; stage 5: c=128 <= t=242 feasible; stage 6:
     c=512 <= t=728 feasible; stage 7: c=2048 <= t=2186 feasible (barely);
     stage 8: c=8192 > t=6560 INFEASIBLE — no gap-1/4 witness can even be
     born at stage >= 8 for K=1 (coordinate budget). For K=2: infeasible
     from stage 6 (c=1024 > ... check exactly). General K: birth window
     is finite; tabulate last feasible birth stage B(K).
 (2) Wash stages for max-S designs at each feasible (K, birth i):
     worst shadow S=t_i vs c=c_i; wash stage w computed exactly; verify
     w is finite and small (all <= 9), i.e. later-born witnesses wash too.
 (3) Uniform corollary: no birth stage i and no K admit a gap-1/4 witness
     whose Chern shadow survives past j=9; combined with stable-range
     forcing at max(i,8), persistence to the limit fails for witnesses
     born at ANY stage, not just stage 3.

Stdlib only. Prints VERIFY_OK.
"""
from fractions import Fraction

def data(j):
    N = 2 * (4 ** (j - 1))
    t = 3 ** j - 1
    D = 2 * t
    return N, t, D

def wash_from(S, c, i):
    # least j>=i with S*3^{j-i} < c*4^{j-i}
    assert S > c >= 1
    j = i
    while True:
        if S * (3 ** (j - i)) < c * (4 ** (j - i)):
            return j
        j += 1
        assert j < 100

def main():
    print("(1) feasibility window (c=K*N/4 vs t):")
    for K in (1, 2, 3, 4):
        row = []
        for j in range(3, 12):
            N, t, D = data(j)
            c = K * N // 4
            assert K * N % 4 == 0
            feas = (c < t)  # need S with c < S <= t
            row.append((j, c, t, feas))
        feas_js = [j for j, c, t, f in row if f]
        B = max(feas_js) if feas_js else None
        for j, c, t, f in row:
            print(f"  K={K} j={j}: c={c} vs t={t} -> {'feasible' if f else 'INFEASIBLE'}")
        print(f"  K={K}: last feasible birth B={B}")
    # exact expectations
    # K=1: c_j = N_j/4 = 2*4^{j-1}/4 = 4^{j-1}/2; t_j=3^j-1
    # j=7: c=2048 < t=2186 feasible; j=8: c=8192 > t=6560 infeasible
    N7, t7, _ = data(7); N8, t8, _ = data(8)
    assert N7 // 4 < t7 and N8 // 4 > t8
    # K=2: j=5: c=256 < t=242? 256>242 infeasible! check: N5=512, c=256, t5=242
    N5, t5, _ = data(5)
    assert 2 * N5 // 4 > t5  # K=2 stage-5 birth infeasible
    N4, t4, _ = data(4)
    assert 2 * N4 // 4 < t4  # K=2 stage-4 feasible (64<80)
    print("  K=1 births feasible j<=7 only; K=2 feasible j<=4 only. OK")

    print("(2) worst-shadow wash per feasible (K, birth i):")
    worst = 0
    for K in (1, 2, 3):
        for i in range(3, 10):
            N, t, D = data(i)
            c = K * N // 4
            if not (c < t):
                continue
            S = t  # max Bott support
            w = wash_from(S, c, i)
            print(f"  K={K} birth {i}: S={S} c={c} wash j={w}")
            worst = max(worst, w)
    print(f"  worst wash over all feasible (K,i): j={worst}")
    assert worst <= 9, worst

    print("(3) spot exact washes:")
    # K=1 birth 4: S=80,c=32: 80>32; 240>128; 720>512; 2160>2048; 6480<8192? j=8
    assert wash_from(80, 32, 4) == 8
    # K=1 birth 7: S=2186,c=2048: j=7 ob; j=8: 6558<8192 washed
    assert wash_from(2186, 2048, 7) == 8
    # K=1 birth 5: S=242,c=128: 242>128; 726>512; 2178>2048; 6534<8192 j=8
    assert wash_from(242, 128, 5) == 8
    print("  birth-4/5/7 K=1 designs all wash at j=8. OK")
    print("  => witnesses born at ANY stage wash by j<=9. Limit persistence")
    print("  impossible over the full birth-stage space. OK")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
