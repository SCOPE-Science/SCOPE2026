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

Run `python3 check_derangement_shattering.py` with Python 3.9 or newer, using only the standard library. The script enumerates derangements as perfect matchings of the off-diagonal board and independently computes all traces on each test support. It also implements a row-by-row rook polynomial dynamic program and checks an independent inclusion-exclusion formula for all integers \(2\le n\le9\).

The checker exhaustively evaluates all support subsets of sizes \(0\) through \(n\) for \(2\le n\le5\), and support sizes \(0\) through five for \(n=6\); it tests deterministic-seed samples for \(n=6,7,8\). It checks both the all-traces matching-complex identity for support size at most \(n-2\) and the complete shattered-support classification on the tested supports.

Its final stdout line is `ALL_DERANGEMENT_SHATTERING_CHECKS_PASS 197657 support_tests 9_rook_polynomials exhaustive_n_le_5_and_n6_le_5 sampled_n6_to_n8`.

# Mathematical limits

The finite computations do not establish the theorem for arbitrary \(n\); the proof in `RESULT.md` supplies the universal edge-disjoint perfect-matching factor argument and the exact boundary obstruction. The sampling limit follows analytically from the support counting identity and is not empirically validated by this finite checker. No independent audit has been performed.
