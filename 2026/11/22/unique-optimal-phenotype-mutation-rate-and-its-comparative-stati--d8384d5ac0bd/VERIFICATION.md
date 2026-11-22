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

# Verification and limits

Execute `python check_threshold.py` with SymPy and SciPy available. The script creates the exact binary Laplace kernel from the source coalescent, reconstructs the published threshold expression, and proves its symbolic identity with the partial fractions and first/second derivatives used in RESULT.md. It verifies the algebraic coefficient inequality and the exact calibration root to printed precision. The numerical grid exercises positive mutation/recognition parameters and verifies uniqueness by bracketing, while the actual all-parameter uniqueness and strict comparative-statics conclusions rest on the inequalities proved in RESULT.md, not that grid.

The result's domain is the large-population weak-selection regime with exactly two periodic recognition phenotypes. No finite-population, stronger-selection, multi-coordinate or larger-cycle classification is claimed. The relative originality assessment is literature-bounded and is not an independent scientific audit.
