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

The formula is proved for every integer \(n\ge3\) by exactly classifying hub-fixed and hub-alternating two-cycles. Its essential nonstandard step is the equality \(x_i=x_i(x_{i-2}\vee x_{i+2})\), which reduces the alternating-hub period-two equation to cyclic words with no isolated ones on the step-two rim graph; the hub inequalities then select coefficients.

Reproduction from the same package: execute `python code/wheel_majority_brute.py` and `python code/wheel_run_census.py` in its root. Outputs are `reports/brute_output.txt` and `reports/run_output.txt`. Both scripts use the standard library only. The former directly verifies all \(524{,}272\) labelled initial states for rim sizes \(3\) through \(17\); the latter checks cyclic-word coefficient counts by direct string enumeration for lengths \(2\) through \(13\) and computes all formula values up to rim length \(60\).

Limits: finite checks are not a proof for untested size; the infinite claim uses the explicit local-update and run-count argument. The external period-two theorem is used only to rule out eventual higher-period attractors, not to produce the enumerative formula. Full-text inspection of the original 1980 threshold theorem was inaccessible, and independent mathematical validation has not been performed.
