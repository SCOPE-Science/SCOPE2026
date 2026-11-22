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

The algebraic proof in RESULT.md covers every integer \(n\ge2\). To replay the separate checks, place `check_spectrum.py` and `check_counts.py` beside this document and run each with Python 3 (standard library only).

- `check_spectrum.py` independently directly enumerates every possible mask for \(2\le n\le8\), compares the sum over distinct ordered endpoints against the closed multiplier, and checks nullity and sharp spectral extremes.
- `check_counts.py` independently enumerates feasible row-negative and overlap types for \(2\le n\le30\), compares exact zero classification against the claimed residue law, and checks all extremal sign constructions.

Both programs were executed successfully from the packaged contents. The finite checks are not a replacement for the all-width proof. Sources and their implications are discussed in RESULT.md and REVIEW.md.
