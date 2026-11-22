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

# Reproduction and limits

Run `python3 verify.py` from the folder containing this file with a Python 3 standard-library interpreter. No network, extra package, or nondeterministic sampling is needed. The command reports 3,343 exact-rational conditional distribution and Dirichlet cut-pattern assertions, 1,458 exact mixed-factorial moment assertions, and 544 exact cut-variance assertions, totaling 5,345. These tests were run on the packaged verifier. Boundary cases include \(C_n=n\), the no-cut case, and radii above one half. For the asymptotic law, the proof's analytical inputs are the exact conditional ratio, the concentration of the number of cuts, and Poisson factorial-moment determinacy; the verifier does not claim to certify every sample size or an infinite limit.

Self-review: passed. Independent audit: not yet performed.
