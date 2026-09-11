"""Finite-stage replay for lane-851 target attempt (recovery test).

Checks the only rigorously closed step: permutation-unitary combinatorics of one
M27 cyclic-factor-permutation block. Does NOT prove any Cu^G limit claim.
Run: python3 finite_stage.py -> prints FINITE_STAGE_OK on pass.
"""
import cmath

def main():
    n = 27
    fixed_basis = 3  # i=j=k
    assert (n - fixed_basis) % 3 == 0
    orbits = (n - fixed_basis) // 3
    assert orbits == 8
    m1 = fixed_basis + orbits
    mw = orbits
    mw2 = orbits
    assert (m1, mw, mw2) == (11, 8, 8), (m1, mw, mw2)
    assert m1 + mw + mw2 == n
    w = cmath.exp(2j * cmath.pi / 3)
    tr = m1 + mw * w + mw2 * w * w
    assert abs(tr - 3) < 1e-9, tr
    dim = n * n  # dim M27 = 729
    dim_fix = (dim + abs(tr) ** 2 + abs(tr) ** 2) / 3  # tr u = tr u^2 = 3
    assert abs(dim_fix - 249) < 1e-9, dim_fix
    assert dim * 3 == 2187  # dim of finite-stage crossed product M27 rtimes Z/3
    print(f"block: eig mults (1,w,w2) = ({m1},{mw},{mw2}), tr = {tr:.6f}")
    print(f"block: dim M27^sigma = {dim_fix:.0f}, dim crossed = {dim*3}")
    print("FINITE_STAGE_OK")

if __name__ == "__main__":
    main()
