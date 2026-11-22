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

# Reproducibility and verification limits

Run `python3 verify_composition.py` using Python 3 and no third-party packages. The script performs exact rational-coordinate reconstruction from the high coefficients of \(H(t)^2+bH(t)\), tests the parity-fixed stratum, and checks clean tangent intersections for normalized compositions in degrees \(m=3,5,7,9,11\), including the power map. It also checks by explicit monomial enumeration the first five Hilbert coefficients in four normal-form dimensions. The completed execution reported `ALL EXACT CHECKS PASS`.

The general assertions rest on the written polynomial graph and parity argument, which works for arbitrary odd \(m\), and on the fiber-product depth and conductor calculations. Exact tests at finitely many values do not certify the universal quantifier. There is no claim about nonreduced ambient resultant structures, arbitrary projective closures, or the full reducibility locus for composite odd indices. Independent audit has not been performed.
