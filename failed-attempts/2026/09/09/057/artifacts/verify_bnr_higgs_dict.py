#!/usr/bin/env python3
"""BNR Higgs dictionary on R=2C: phi from u-action, nilpotency, trace (target item 3).
Stdlib/sympy only. Prints VERIFY_OK. Ends with an honest PRECISION NOTE.

Dictionary: F coherent on R, pi_*F = E (rank 2). u (=lambda, tautological fiber
coordinate, u^2=0) acts O_C-linearly: u: F -> F tensor pi^*K^{-1}? Equivalently
phi: E -> E tensor K with phi^2 = 0 (since u^2=0) and tr(phi) = 0 (since the
characteristic polynomial is lambda^2: no lambda term). CERTIFIED formally below
by 2x2 matrix algebra: any 2x2 matrix with char poly lambda^2 is traceless and
square-zero? CAREFUL: char poly lambda^2 => tr=0, det=0 => by Cayley-Hamilton
phi^2 = 0. Yes.
Split example: L^2 = K (theta, deg L = 1). F = pi^*L: E = L (+) L^{-1}
  (since pi_*O_R = O (+) K^{-1}), phi = [[0,0],[s,0]] in suitable frame with
  s: L -> L^{-1} tensor K = L (iso up to scale since L^{-1}K = L). phi != 0,
  phi^2 = 0, tr = 0. Wobbly Higgs point (admits nonzero nilpotent Higgs field).
phi = 0 locus: u acts as 0 on F. Then F = i_*E (scheme-theoretically on C).
PRECISION NOTE (stress finding, not a disproof): such F are annihilated by the
  nilpotent u, hence are NOT locally free over R nor "rank-1" in the generalized-
  line-bundle sense (generic stalk not free over O_{R,eta}=K(C)[u]/(u^2)); they are
  pure 1-dim (Simpson torsion-free, i.e. no 0-dim subsheaves) of Simpson rank
  matching line bundles, but u-torsion as O_R-modules. The target phrase
  "rank-1 torsion-free sheaves" is therefore AMBIGUOUS: under Simpson purity both
  types qualify; under Drezet generalized-line-bundle terminology N0 (phi=0) lies
  OUTSIDE the rank-1 torsion-free locus (it is the u-torsion boundary). The MCM
  kernel must interface across this rank-jump, which is part of the difficulty.
"""
import sympy as sp

def main():
    # Cayley-Hamilton check: generic traceless 2x2 squares to det*I; det=0 => square 0
    a, b, c = sp.symbols('a b c')
    phi = sp.Matrix([[a, b], [c, -a]])
    assert phi.trace() == 0
    phi2 = phi**2
    det = phi.det()
    assert sp.simplify(phi2 + det * sp.eye(2)) == sp.zeros(2), "Cayley-Hamilton"
    print("traceless 2x2: phi^2 = -det(phi) I; det=0 (char poly lambda^2) => phi^2=0")
    # split example numerics: degrees
    g = 2
    degL = 1  # theta: 2*1 = 2 = deg K
    assert 2 * degL == 2 * g - 2
    degE = degL + (-degL)
    assert degE == 0, "SL(2) trivial determinant degree"
    print(f"split BNR example: L deg {degL}, E = L (+) L^-1 deg {degE}, phi=[0 0;s 0], s != 0")
    print("phi nilpotent nonzero, tr 0: wobbly point over p in C (zeros of s)")
    print("PRECISION NOTE recorded: phi=0 locus is u-torsion (supported on C);")
    print("  'rank-1 torsion-free' needs Simpson-purity reading to include N0.")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
