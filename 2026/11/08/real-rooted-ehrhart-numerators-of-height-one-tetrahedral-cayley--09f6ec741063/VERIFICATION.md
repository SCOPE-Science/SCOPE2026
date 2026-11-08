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

# Reproducibility

Run `python3 verify.py` in the same directory as `certificate.json` (Python 3, standard library only). The verifier constructs the three exact numerator polynomials with integer polynomial arithmetic, reproduces the cubic-discriminant identity, checks all 90 strictly positive coefficients and equality to the embedded certificate, verifies its symmetry and the nonzero linear boundary terms, and separately compares 845 exact lattice counts against the formula.

The finite checks do not certify the theorem for infinitely many parameters; the reconstructed symbolic polynomial identity, positivity of each coefficient, and elementary discriminant criterion do. Degenerate degrees are handled explicitly. No floating-point root calculations or unavailable external dependencies enter the proof.

# Scope and limits

The theorem covers positive integral layer scales at height one in dimension four. It does not classify smooth six-facet polytopes of other bundle types, other heights, or higher dimensions. Literature priority is provisional; independent mathematical validation has not been performed.
