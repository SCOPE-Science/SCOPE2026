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

Run `python3 check.py` in a directory containing only the packaged checker. This program reconstructs physical shelf-list insertion for exact finite cases, computes all cross-prefix moments with rational weights, and independently tests the explicit formulas. The proof in RESULT.md supplies the infinite-size justification via conditional projections, degenerate kernel orthogonality, Doob's maximal inequality and the vector Donsker theorem.

The finite check explores \(m\in\{1,2,3\}\), several rational top probabilities, and up to five arrivals. No finite enumeration is represented as an exhaustive proof of the infinite functional limit. Historical priority of a model-specific trajectory result is not independently validated; the 2026 asymmetric-shuffle article's complete text was not accessible for inspection.
