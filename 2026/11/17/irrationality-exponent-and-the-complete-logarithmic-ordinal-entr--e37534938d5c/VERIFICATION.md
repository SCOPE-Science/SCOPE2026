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

# Verification and limits

The proof's fundamental identities are the exact representation of order-\(n\) ordinal probabilities by \(n\) circular gap lengths, the estimates \(H_n\ge\log(q/3)\) for \(n\ge q\) and \(H_n\le\log q+h(2n/Q)+(2n/Q)\log n\) for \(n\le Q/4\), and the continued-fraction identity expressing the irrationality exponent through consecutive denominators. The real-variable entropy argument establishes both extreme limits; insertion of one new rotation phase point changes Shannon entropy by no more than \(\log2\), giving the entire accumulation interval.

Running `python verify.py` from this directory with Python 3 and `mpmath` at 90-digit precision returned the terminal marker `VERIFY_OK: ordinal cells 20 custom fraction denominator 24005, finite entropy bounds and normalized ratios`. The script checked a near-rational slope and golden-mean slope, with entropy bounds on selected finite orders and exhaustive ordinal-signature checks for orders 2 through 11. This diagnostic is noncertifying: finite tests do not check all irrational slopes or establish any infinite limit. Those conclusions depend on the analytic argument in `RESULT.md`.

No independent mathematical audit has been performed. Novelty relative to any unindexed or inaccessible historical results remains unverified beyond the documented comparisons.
