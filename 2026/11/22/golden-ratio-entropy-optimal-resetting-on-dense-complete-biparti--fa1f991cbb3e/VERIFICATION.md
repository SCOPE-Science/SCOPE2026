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

The accompanying `verify.py` requires only Python 3's standard library. Run `python3 verify.py` beside RESULT.md. Its direct rational Gaussian elimination constructs the entire observed transition matrix and solves the invariant distribution for all \(1\le a,b\le4\) at six reset probabilities; it independently computes transition entropy and checks the full formula, both root sides, and the KL identity. Additional large-size checks evaluate several proportions and compare the predicted strict optimum with local finite-size numerical searches. The observed execution prints `CHECKS_OK 2622`.

This finite numerical replay supports the identities and their normalization, but it is not used as an exhaustive verification of any all-size or continuum-limit statement. The analytic proof establishes every quantified result. Independent scientific validation, publication priority certification and any external attestation have not been performed.
