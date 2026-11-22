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

## Reproduction

From this package run `python check.py` using Python 3 with SymPy installed. The checker constructs transition matrices by enumerating all 35 three-particle seven-site configurations, independently reduces them to five rotation classes, and verifies the symbolic stationary law, first and second tilted-generator cumulants, positivity-relevant polynomial formula, equilibrium noise and high-drive ratio. Two exact rational rate values are additionally checked with the unreduced 35-state system. The script terminates with a PASS message when every assertion succeeds.

## Mathematical certification and limits

The five-dimensional generator and tilted-derivative matrices, plus the finite-state eigenvalue perturbation identities, prove the result for every positive real forward rate. The numerical-specialization tests alone do not establish the parameter-uniform theorem; this role belongs to the symbolic polynomial identities. There are no external datasets, stochastic Monte Carlo logs or other-run certificates. No result for higher particle counts, other ring lengths or full count-distribution limits is established. This is a self-review, not an independent external audit.
