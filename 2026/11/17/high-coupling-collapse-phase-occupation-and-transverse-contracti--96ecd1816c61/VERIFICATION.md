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

# Verification and reproducibility

The claim concerns a specified quartic polynomial and the resulting positive planar chemical vector field. The stand-alone companion `verify.py` requires only Python's standard library and terminates with `FOUR_OVAL_HIGH_COUPLING_CHECK_OK` after successful tests. It uses exact fractions to verify the cofactor equation at nontrivial rational points, checks the quartic-root relation at several points, independently approximates exact branchwise original-time periods, lobe area and the cofactor action, and checks their sharp large-coupling constants using a square-root-singularity-removing midpoint quadrature. The proof of the limits, uniform error terms, and the phase-law convergence is analytical in RESULT.md. The finite tests do not certify infinite parameter ranges or identify all possible published equivalents.

The limit analysis must keep the actual time factor \(xy\), the fixed positive coupling \(\varepsilon\), and the shift \((x,y)=(2+u,2+v)\). Periods are least times around the four regular ovals. The common transverse multiplier uses one full circuit and the cofactor of the invariant polynomial. No independent mathematical audit or independent validation is claimed.
