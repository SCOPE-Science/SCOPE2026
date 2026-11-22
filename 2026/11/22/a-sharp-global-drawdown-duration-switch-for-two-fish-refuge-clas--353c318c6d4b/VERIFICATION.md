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

# Reproducible verification

The theorem holds for every \(0<w<1\), \(\lambda,\mu>0\) and \(0\le c_f<c_s\), for all decision durations \(T\ge0\). Its proof is the branch-by-branch calculation in RESULT.md, including the positivity and strict convexity inequalities needed to show the candidate maximizers are actually feasible at the critical delay. The join is checked explicitly, and the equality case has exactly two global maximizing times.

Execute `python3 checker.py` with Python 3's standard library from the same extracted directory. The reproducibility run completed successfully: 5,000 seeded parameter draws, 1,505,000 grid evaluations, 5,000 nonsmooth-join checks, 20 critical-delay identities, and an exact rational two-maximum witness. These checks do not assert exhaustive floating-point certification or replace the proof. The mathematical identities for the illustrative witness can also be verified with exact rational arithmetic and elementary exponential identities.

The stochastic model is not calibrated to field data. Only the specified whole-event exposure survival, two deterministic travel times, shared exponential reaction latency and independent mortality are proved. No independent external scientific audit has been performed.
