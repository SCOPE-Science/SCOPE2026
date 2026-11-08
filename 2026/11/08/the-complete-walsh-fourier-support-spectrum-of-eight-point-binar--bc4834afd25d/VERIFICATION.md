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

# Verification details

The attached `CHECK.py` executes an exhaustive deterministic integer certificate for the one finite table used in the proof. It runs in Python 3.10+ with no packages beyond the standard library. Command: `python CHECK.py`.

The canonical form \(\{0,e_1,\ldots,e_r\}\cup B\) includes every eight-point set up to affine transformation; the number of candidates is exactly \(\binom{2^r-r-1}{7-r}\). The script checks all \(549\) candidates, independently computes direct Walsh sums and weight-four-zero counts, checks the complete multiplicity table and sharp-case period count, and enumerates all \(12870\) eight-point subsets in four dimensions as a separate check. It prints `CHECK_OK normalized_representatives=549 support_types=12 dimension_four_subsets=12870` when successful.

The proof establishes the extension to arbitrary ambient dimension analytically by dual-space fiber cardinalities. No experiment substitutes for that argument. The check does not test weighted functions, other characteristics, or different set sizes. External priority and mathematical audit remain unverified independently.
