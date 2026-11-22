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

# Verification notes

The exact proof uses the Sherman–Morrison inverse of every positive-definite selected principal block, the trace of its Schur complement, a strict order-statistic mass inequality, and an elementary symmetric polynomial identity. All assumptions are explicitly stated in `RESULT.md`; no asymptotic or probabilistic approximation is needed for those identities.

`verify.py` is a standalone standard-library rational-arithmetic checker. Executing `python verify.py` yields: `PASS: 90 orientations and 2586 rational equalities; all claimed interior subset sizes through n=8.` It compares direct Gaussian-elimination Schur complements against the derived formula for all interior subsets of dimensions four through eight, tests the exact best-subset objective and its equality cases, and independently checks the determinantal eigenvalue formula. This is finite test coverage only, not a formal certificate of all dimensions or real parameters.

The literature comparison establishes the limited statement and remaining historical-priority risk in `REVIEW.md`; the new claim is not a proof for arbitrary spectral configurations. Independent audit and external validation have not been performed.
