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
# Reproducibility and bounded verification

Run `python check_transport.py` in this directory (requires NumPy and SciPy). The independent full-adjacency matrix exponential checks match the four-eigenspace closed formula for 143 graph-size/time pairs; further checks evaluate the two strict-concavity constants, twelve integer-frequency finite-size optima, and noninteger-frequency two-phase witnesses, for 168 assertions total. Expected terminal line: `ALL_NEW_TRANSPORT_CHECKS_PASSED 168`.

This is a supplementary finite test. The all-size statements rely on the explicit mathematical proof in RESULT.md: graph diagonalization, eigenphase obstruction, localization via the exact squared norm identity, irrational two-torus density, and the uniform resonant rescaling. Finite numerical optimizations are not treated as proofs of infinite limits.

The research is self-reviewed, not independently audited. One directly relevant dissertation on quantum windmills was available by abstract and metadata only; its full manuscript could not be inspected. Historical-priority risks and scientific scope are discussed in REVIEW.md.
