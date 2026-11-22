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

# Reproduction and scope of verification

The accompanying `verify.py` requires Python 3 and only its standard library. Run `python3 verify.py` from the directory containing the extracted files. On the actual reviewed content, it completed 46,820 exact finite assertions. It enumerates all binary creation words through ten vertices and compares direct graph edges and a separate maximum-matching dynamic program with the random-walk formula; it computes exact rational covariances of the two graph invariants through sixteen vertices and independently checks the prior marginal matching distribution through fourteen vertices. It also checks the numerical limiting correlation against the elementary Brownian variance formulas.

The finite checker is a reproducibility aid. It does not independently certify any Brownian weak-convergence theorem or mathematical novelty. The analytic steps required for the infinite statement are the common-walk coupling, functional invariance principle, fourth-moment uniform integrability, Gaussian integration by parts and the classical Brownian arcsine argmax law, all laid out in `RESULT.md`. Historical comparison is best-knowledge and not exhaustive. No external mathematical audit has been performed.
