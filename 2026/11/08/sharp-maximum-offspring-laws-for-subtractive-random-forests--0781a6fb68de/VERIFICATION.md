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

The claim concerns the full-support iid subtractive forest defined in `RESULT.md`. The mathematical proof (not a finite computation) derives the two sharp marginal tail exponents and transfers them to a dependent maximum via independent disjoint-window lower events, a union bound, Borel–Cantelli and monotone interpolation.

`checker.py` is a self-contained Python 3 standard-library verification program. Run `python checker.py` to reproduce exact finite-state geometric-lag computations through \(n=8\), with exact rational comparisons of vertex offspring histograms, the maximum histogram and the geometric generating-product bound. A completed run gave `PASS 398 exact assertions`.

Finite checks do not prove any infinite-volume limit; the theorem's critical upper bounds require the generating-product estimates, and its lower bounds require the disjoint-window argument. All probability and almost-sure quantifiers are stated in the proof. No outside computational certificate is required for the analytic argument.

The original forest model, a marginal Bernoulli representation and the distribution-free maximum upper bound were published previously; only the sharpened two-class almost-sure extreme limits are asserted here. Historical-priority verification is incomplete, particularly concerning inaccessible older renewal-tree full text. Independent validation has not been performed.
