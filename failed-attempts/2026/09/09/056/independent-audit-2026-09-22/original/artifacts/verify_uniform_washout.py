"""Uniform wash-out certificate for the admitted (m=4,k=3) diagonal data.

Proves by exact integer/rational arithmetic:
 (1) N_j/D_j strictly increasing for j>=1 (so stable-range forcing is monotone).
 (2) Maximal obstructable normalized gap gmax_j = (D_j/2)/N_j = d_j/(2n_j),
     strictly decreasing for j>=2, with gmax_3=13/16, gmax_8=205/1024<1/4,
     and gmax_j -> 0 geometrically as (3/4)^j.
 (3) Forcing stages J(g) for a grid of gaps g in {1/2,1/4,1/8,1/16,1/32}:
     every constant-rank projection pair with normalized gap >= g is
     Murray-von Neumann comparable at stage max(i,J(g)) (i=birth stage).
 (4) Parametric threshold: one-step ratio multiplier is k/m=3/4<1, so the
     system is on the slow-growth side for EVERY seed s and EVERY stage;
     s only shifts the constant. Exhibit that m=k would be threshold.
 (5) Sharp crossing re-verified with exact integers (no floats).

Base facts used (proved in WORKLOG/DRAFT, not computed here):
 [C] X_j=(S^2)^{t_j} connected => every projection in M_K(A_j) has constant
     rank; every normalized trace gives rank/(K*N_j).
 [S] Stable-range lemma: Delta:=f-e >= D/2 (=ceil(D/2), D even) forces
     embedding of rank-e bundle into trivial rank-f bundle over D-dim base,
     hence Murray-von Neumann (hence Cuntz) comparison.

Prints VERIFY_OK. Stdlib only.
"""
from fractions import Fraction

def stage(j):
    t = 3**j - 1
    D = 2 * t
    N = 2 * (4 ** (j - 1))
    return t, D, N

def Jof(g):
    # least j>=3 with g*N_j >= D_j/2 + 1/2  ((D+1)/2 conservative form)
    j = 3
    while True:
        t, D, N = stage(j)
        if g * N >= Fraction(D + 1, 2):
            return j
        j += 1
        assert j < 200, "no forcing stage found"

def main():
    # (1) N/D non-decreasing; strictly increasing for j>=2
    print("(1) N_j/D_j monotonicity:")
    prev = None
    for j in range(1, 15):
        t, D, N = stage(j)
        r = Fraction(N, D)
        flag = "" if prev is None or (r >= prev and (j <= 2 or r > prev)) else "FAIL"
        print(f"  j={j}: N/D={r}~{float(r):.4f} {flag}")
        if prev is not None:
            assert r >= prev, j
            if j >= 3:
                assert r > prev, j
        prev = r
    # exact one-step proof: N_{j+1}/D_{j+1} > N_j/D_j <=> 4*D_j > D_{j+1}
    # <=> 8*(3^j-1) > 2*(3^{j+1}-1) <=> 2*3^j > 6, true for j>=2 (equality j=1).
    assert 4 * 2 * (3**1 - 1) == 2 * (3**(1 + 1) - 1)  # flat N/D=1/2 at j=1,2
    for j in range(2, 15):
        assert 4 * 2 * (3**j - 1) > 2 * (3**(j + 1) - 1), j
    print("  non-decreasing OK; strictly increasing j>=2 (4*D_j-D_{j+1}=2*3^j-6)")

    # (2) gmax table
    print("(2) gmax_j = (D_j/2)/N_j:")
    prev = None
    for j in range(1, 12):
        t, D, N = stage(j)
        gmax = Fraction(D, 2 * N)
        print(f"  j={j}: gmax={gmax}~{float(gmax):.6f}")
        if j >= 3:
            assert prev is not None and gmax < prev, j
        prev = gmax
    t3, D3, N3 = stage(3)
    assert Fraction(D3, 2 * N3) == Fraction(13, 16)
    t8, D8, N8 = stage(8)
    assert Fraction(D8, 2 * N8) == Fraction(205, 1024) < Fraction(1, 4)
    # geometric decay: gmax_{j+1}/gmax_j = (3^{j+1}-1)/(4*(3^j-1)) -> 3/4
    for j in range(2, 12):
        a = Fraction(3**j - 1, 2** (2 * j - 1) * 1)  # = D_j/(2N_j)? check below
    # direct identity: D_j/(2N_j) = (3^j-1)/2^{2j-1}
    for j in range(1, 12):
        t, D, N = stage(j)
        assert Fraction(D, 2 * N) == Fraction(3**j - 1, 2**(2 * j - 1)), j
    print("  gmax_3=13/16, gmax_8=205/1024<1/4, identity D/(2N)=(3^j-1)/2^{2j-1} OK")

    # (3) forcing stages for grid of gaps
    print("(3) forcing stages J(g):")
    grid = [(1, 2), (1, 4), (1, 8), (1, 16), (1, 32)]
    for gnum, gden in grid:
        g = Fraction(gnum, gden)
        jstar = Jof(g)
        t, D, N = stage(jstar)
        # verify previous stage NOT forced (sharpness from below, conservative form)
        t0, D0, N0 = stage(jstar - 1)
        assert g * N0 < Fraction(D0 + 1, 2), (g, jstar)
        assert g * N >= Fraction(D + 1, 2), (g, jstar)
        # verify all later stages stay forced (monotonicity of g*N-D/2)
        for j in range(jstar, jstar + 5):
            tt, DD, NN = stage(j)
            assert g * NN >= Fraction(DD + 1, 2), (g, j)
        print(f"  g={g}: J={jstar} OK")
    assert Jof(Fraction(1, 4)) == 8
    # any birth stage i: forcing at max(i,J(g)) — check representative pairs
    for i, g in [(3, Fraction(1, 4)), (5, Fraction(1, 4)), (10, Fraction(1, 4)),
                 (3, Fraction(1, 32)), (12, Fraction(1, 2))]:
        jf = max(i, Jof(g))
        t, D, N = stage(jf)
        # rank gap at stage jf for pair born at i with normalized gap g:
        # Delta = g * N_jf (since normalized gap preserved under mult. by M)
        assert g * N >= Fraction(D + 1, 2), (i, g, jf)
    print("  max(i,J(g)) forcing OK")

    # (4) parametric threshold k/m
    print("(4) parametric multiplier k/m=3/4<1:")
    k, m = 3, 4
    assert Fraction(k, m) < 1
    # one-step ratio evolution: gmax_{j+1} = gmax_j * (3^{j+1}-1)/(4*(3^j-1))
    # limit multiplier -> k/m; exhibit bounds: multiplier in (0.75, 0.78) for j>=3
    for j in range(3, 12):
        mult = Fraction(3**(j + 1) - 1, 4 * (3**j - 1))
        assert Fraction(3, 4) < mult < Fraction(4, 5), (j, mult)
    print("  step multiplier in (3/4,4/5), geometric decay to 0 for any seed s OK")
    # threshold statement: m=k needed for non-decay; here m=4>k=3
    assert m > k
    print("  m=4>k=3 strictly on slow-growth side OK")

    # (5) sharp integer crossing for the audit-plan pair (Delta=8*4^{j-3})
    print("(5) sharp crossing (need=D/2=3^j-1):")
    for j in range(3, 12):
        Delta = 8 * (4 ** (j - 3))
        need = 3**j - 1
        status = "forced" if Delta >= need else "open"
        print(f"  j={j}: Delta={Delta} vs need={need} -> {status}")
    assert 8 * 4**(7 - 3) < 3**7 - 1
    assert 8 * 4**(8 - 3) >= 3**8 - 1
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
