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

Execute `python3 verify.py` with SymPy installed. The script verifies all eight facet-normal classes using exact symbolic arithmetic, reconstructs the central-hexagon section, independently checks its area and norm-edge lengths, calculates the self-perimeter and self-volume exactly, and verifies the claimed strict factor \(8/9\) for the first 100 odd dimensions. The written argument in RESULT.md is a proof in all odd dimensions. This finite checker is not an infinite-dimensional certificate.

The source preprint's Definition 4.1 and Theorem 4.2, alongside its Conjecture 2, are sufficient for direct source comparison. Historical priority remains provisional; no independent external mathematical audit has been performed.
