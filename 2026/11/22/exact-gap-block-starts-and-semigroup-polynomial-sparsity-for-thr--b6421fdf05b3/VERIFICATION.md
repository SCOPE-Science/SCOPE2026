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

# Verification record

The accompanying `verify_gap_starts.py` computes membership in the full integer interval through the predicted Frobenius number by a coin-reachability dynamic program independent of the Apéry-set proof. For each integer \(2\le n\le80\) it checks the complete list of negative membership transitions, equal to gap-block starts, and confirms genus, Frobenius number and semigroup-polynomial nonzero coefficient count. Its output is `VERIFY_OK cases=79 checked_positions=20988799 n_range=2..80`.

The proof establishes the assertion for all \(n\ge2\); finite computation does not certify an infinite theorem. No external independent audit has been performed. A potentially relevant general Hilbert-series source could only be inspected at abstract level; the priority comparison is not exhaustive.
