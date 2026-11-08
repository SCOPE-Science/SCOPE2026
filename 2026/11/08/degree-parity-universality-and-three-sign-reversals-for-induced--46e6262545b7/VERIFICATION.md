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

The proof conditions on one \(k\)-vertex induced-motif event; the exact conditional parity-sign sum is \(q^{n-k}(k-2o(H))\), while all exterior vertices retain mean parity sign \(q^{n-1}\). Expanding the conditional expectation of total odd-degree count yields the exact covariance. No infinite inference is drawn from the finite exhaustive checker.

Reproduce using `python3 verify_covariance.py` from the same directory. The script reports 420 rational exact equalities across all unlabelled induced graph types of sizes two through four within all ambient graphs of orders two through five, at five rational probabilities. Direct exact rational sign samples for the five-vertex path at order six use edge probabilities \(1/10,2/5,3/5,9/10\) and alternate sign. The exact threshold proof for all even \(n\ge6\) is analytic and contained in RESULT.md.

The independent-audit channel has not been performed. A broader unreviewed thesis and possible general generating-function methods remain historical-priority risks, not errors established by the source review.
