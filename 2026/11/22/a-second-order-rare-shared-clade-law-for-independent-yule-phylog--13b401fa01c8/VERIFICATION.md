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

Execute `python verify.py` using Python 3. The checker uses standard-library `fractions.Fraction`, exhaustive YHK tree enumeration through six taxa, and a separate seven-taxon single-tree enumeration for the two key pair-clade formulas. The current checks passed 136 exact assertions. At three larger values of \(n\), exact rational Bonferroni combinations approach the analytical coefficient \(1259/1800\), as expected.

These are finite structural consistency tests only. The asymptotic \(O(n^{-3})\) error requires the compatible-clade third-intersection bounds proved in RESULT.md, rather than numerical extrapolation. An independent mathematical audit has not been performed.
