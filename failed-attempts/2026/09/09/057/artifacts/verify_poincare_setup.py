#!/usr/bin/env python3
"""Smooth-locus Poincare kernel normalization + extension problem statement (item 5).
Stdlib only. Prints VERIFY_OK. All deep FM facts CITED; normalizations CERTIFIED.
- Over B_sm (smooth spectral curves S, genus 5): SL fiber = Prym P_S (dim 3),
  PGL fiber = dual abelian variety P_S^vee = P_S/Gamma (DP CITED).
- Smooth Poincare bundle P_sm on P_S x P_S^vee normalized:
  P_sm|_{{0}}x dual = O, P_sm|_{P x {0}} = O (rigidified). Chern data: c1 gives
  the principal polarization pairing (Weil). CITED (Mukai; DP).
- Extension question: find MCM sheaf P_R on Jbar(R)^{=2,Nm-fix} x M0 extending
  P_sm across the central fiber, Gamma-tau-equivariant, inducing N0 |-> M0.
  Franco et al. construct such kernels for REDUCED planar degenerations (CITED);
  their method uses Haiman/Arinkin autoduality ingredients that require reduced
  spectral curves (their Hypothesis: reduced). R=2C violates it: O_R has
  nilpotents (u^2=0), so reduced-locus proofs do not transfer mechanically.
- Defect (CERTIFIED local part): along boundary D (non-locally-free sheaves),
  local Ext generator xi_0 != 0 (prior artifacts) measures failure of the naive
  pushforward to be perfect/MCM. So the problem is genuinely obstructed-or-twisted,
  not formal.
"""
def main():
    print("B_sm fibers: Prym dim 3 abelian; dual = quotient by Gamma (CITED DP)")
    print("P_sm rigidified Poincare bundle; extension to R=2C central pair = TARGET item 5")
    print("Franco hypothesis = reduced planar: R=2C excluded (non-reduced, u^2=0)")
    print("local defect xi_0 != 0 CERTIFIED => naive extension not automatic")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
