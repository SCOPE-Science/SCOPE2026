---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the rational homology character

Running `python3 verify.py` from the directory containing the companion script uses only the Python 3 standard library. It returns `ALL_CHECKS_PASS`; the accompanying `verification_output.txt` records the complete expected output.

The verifier tests all \(85\) cycle types of the symmetric groups on \(5,6,7,8,9\) symbols. For each cycle type it enumerates invariant edge-orbit choices using exact integer support-count dynamic programming, calculates the reduced Lefschetz trace from these choices, and compares with the closed fixed-point character formula. For \(n=5,6\) a separate simplex enumeration with explicit orientation inversions checks the chain-level trace. Class-size-weighted exact character inner products and hook-dimension checks establish self-consistency for the tested cases.

The general proof is the finite-support cancellation and equivariant Euler–Poincaré argument written in `RESULT.md` for arbitrary \(n\); finite tests do not imply the infinite theorem. The nonequivariant concentration used in the argument is the published Nilakantan–Singh homotopy theorem (arXiv:1802.05848). The full existing \(n=6\) representation is acknowledged as prior. Rational quotient acyclicity is not a statement of contractibility or integral quotient torsion.
