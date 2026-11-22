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

# Verification of the two-hub avalanche law

Run `python3 verify.py` in this directory with Python 3 standard library only. It performs an independently implemented legal toppling stabilization, uses Dhar's sink-burning test, and tests that against the analytic recurrence criterion for every stable configuration on all labelled graphs in the family with `2 <= n <= 10`. For each recurrent configuration it independently adds a grain at the representative hub and leaf, stabilizes and accumulates exact integer total-toppling histograms, requiring identity with the two claimed polynomial coefficient lists.

The script also checks integer polynomial coefficient sums, both means and extreme-event counts for `2 <= n <= 512`, separately from the finite-state enumeration. The actual run exited successfully with:

`SANDPILE_TWO_HUB_CHECKS_PASSED finite_n=2..10 formulas_n=2..512`

The infinite-family result is established by the burning-count and wave-classification proof in RESULT.md, not by extrapolation from these finite checks. No independent audit of this research claim or of prior-art completeness has been performed. Historical originality is assessed only against the specific listed accessible source texts and published record searches.
