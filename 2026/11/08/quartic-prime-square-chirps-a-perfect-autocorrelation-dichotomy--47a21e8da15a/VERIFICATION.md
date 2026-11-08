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

To repeat the finite arithmetic checks, run `python3 check_quartic.py` in an ordinary Python 3 environment. The program independently computes the exponent histogram of every ambiguity sum for primes \(5,7,11,13\), applies the exact minimal cyclotomic polynomial criterion, and compares each zero/nonzero result with the discriminant/permutation theorem. It also checks the total surviving frequencies and the CAZAC congruence class.

Completed execution printed `QUARTIC_PRIME_SQUARE_EXACT_CYCLOTOMIC_PASS`, with support counts \(317,1219,7361,14353\). No numerical thresholds, symbolic algebra packages, remote resources or precomputed lookup tables are needed.

The infinite family is established by the proof in `RESULT.md`, not by the finite checker. Reproducing the checker does not constitute independent mathematical validation. The historical-priority comparison is bounded and does not exclude every generalized perfect-polyphase construction.
