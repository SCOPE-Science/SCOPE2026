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

# Reproducibility and limits

The accompanying `verification/verify_bruteforce.py` enumerates initial activated sets exhaustively for \(5\le n\le18\), operates the explicit synchronous three-neighbor rule to termination, and checks both minimum seed size and the entire optimal-seed time histogram against the theorem. Its standard output is in `verification/verify_bruteforce.out`.

The independent `verification/verify_gap_certificate.py` enumerates cyclic positive-gap strings subject to the derived necessary no-adjacent-unit-gap condition for \(5\le n\le32\), checks induced acyclicity with disjoint-set unions, and reconstructs the optimal-seed count and completion-time histogram from induced path lengths; its output is in `verification/verify_gap_certificate.out`.

Both scripts are pure Python standard-library programs and can be executed with `python3 verification/verify_bruteforce.py` and `python3 verification/verify_gap_certificate.py`. Recorded output lines terminate in PASS. The small-case computations do not certify the entire infinite family; the proof in RESULT.md establishes the general formulas.

Independent scholarly audit has not been performed.
