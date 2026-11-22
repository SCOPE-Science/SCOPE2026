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

# Reproducibility checks

Run `python3 check.py` with an ordinary Python 3 standard library. The checker evaluates the exact expectation in rational arithmetic for 245 pairs of sample size and dimension, verifies the planar product-density integral against the exact sum for eight sample sizes, and verifies two boundary identities (255 assertions). It prints quadrature values and two-term approximations for four larger sample sizes. Independent source inspection established the 2010-03-11 public online posting of the cited random-box model paper.

The proof itself is analytical; these finite calculations do not establish the all-size or asymptotic statements. No external expert or independent mathematical audit is claimed. The independent-audit status in the front matter is not a judgment of correctness.
