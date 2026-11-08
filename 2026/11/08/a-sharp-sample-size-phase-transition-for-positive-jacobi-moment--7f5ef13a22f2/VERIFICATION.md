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

The accompanying standalone `verify.py` uses only Python 3 standard-library functions. Run `python verify.py`; a successful execution reports 2,222 exact-rational comparisons and numerical consistency cases/checks. The rational tests enumerate three-node interpolation witnesses and compare them against the moment-curve sign/product criterion for sampled finite node sets. The numerical tests check the exact probability integral against separately integrated nonnegative failure-event integrals and test the sharp prefactors at representative fixed Jacobi parameters, including the transition.

The analytical proof in `RESULT.md` is necessary for the claims for all positive sample sizes and fixed target parameters and for the infinite-sample equivalents. No finite experiment establishes those universal assertions. The tested Python paths and extracted package code are identical in this release. Independent validation has not been performed.
