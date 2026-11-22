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

# Verification

Run `python verify.py` with SymPy installed. The script constructs the original unit graph Laplacian and grounds two leaders without changing the diagonal degree contributions, then verifies all four exact orbit cost formulas by symbolic differentiation of the stated characteristic factors. It checks every leader pair for core sizes 3–6, representatives for 7 and 8, and agreement of grounded characteristic polynomials with the four determinant factorizations for the exhaustive range. A successful replay reports `PASS: 8 symbolic derivative/comparison identities; 162 exact grounded-matrix comparisons; all tested optimizer regimes.`

The positivity transformations, distinct leader-pair orbits, and all-parameter reasoning are written out in RESULT.md. Exhaustive finite checks are not an infinite proof. The source inspection supports only best-knowledge originality, not publication-priority or independent verification.
