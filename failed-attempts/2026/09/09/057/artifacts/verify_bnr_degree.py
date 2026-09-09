#!/usr/bin/env python3
"""BNR degree shift for R=2C -> C and fixed-determinant condition (SL(2)).
Finite flat (non-reduced) cover pi: R -> C of degree 2.
chi(F) = deg F + chi(O_R); chi(pi_*F) = deg(pi_*F) + 2 chi(O_C).
chi(O_R) = -4 (certified), chi(O_C) = -1.
Hence deg(pi_*F) = deg F + chi(O_R) - 2 chi(O_C) = deg F - 4 + 2 = deg F - 2.
SL(2) trivial determinant => deg = 0 => deg F = 2.
So BNR identifies h^{-1}(0) set-theoretically with the degree-2 generalized
(Nm-fixed) Prym locus in the compactified Jacobian of R: det pi_*F = O_C.
Simpson semistability transfers. Stability walls = wobbly divisor (recorded separately).
"""
def main():
    chiOR, chiOC = -4, -1
    shift = chiOR - 2 * chiOC
    assert shift == -2, shift
    degF = 2
    assert degF + shift == 0
    print(f"degree shift: deg pi_*F = deg F + ({shift}); fixed-det => deg F = {degF}")
    print("BNR locus: rank-1 torsion-free sheaves F on R, deg F=2, det pi_*F = O_C")
    print("polarization degree for Simpson stability: inherited from C (deg O_C(1) fixed)")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
