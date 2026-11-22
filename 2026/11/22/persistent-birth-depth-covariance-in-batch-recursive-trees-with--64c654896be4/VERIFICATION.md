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

# Reproduction and scope

Run \(\texttt{python CHECK.py}\) with Python 3 and no third-party packages. This computes complete rational finite laws, checks the mean/variance identities and every cross-batch covariance of the enumerated experiments, and asserts the finite-sum identity for twenty batch sizes through two hundred steps. It also checks certified rational bounds used to prove the global integer optimum. Recorded execution yielded 4,332 passing assertions. The exact recurrence, telescoping, integral-test and monotonicity arguments in RESULT.md establish the infinite statements; the code by itself does not.

Independent mathematical review has not been performed. The motivating paper's path-length covariance constant is prior work and is not claimed as newly established by this package.
