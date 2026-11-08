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

# Verification evidence

From the extracted package directory, invoke `python verify.py` with Python 3 and no third-party dependencies. The included checker executed successfully and printed:

`VERIFY_OK: 1968 exact rational identities/coefficient checks; 6 numerical-limit sanity checks`

The rational checks reconstruct the logarithmic population derivative, the exact transformed vector field, cubic/quartic coefficients and parameter identities. The six finite-time ODE integrations compare the derived amplitudes at and above threshold for concrete positive parameters, but cannot certify the infinite-time claims. Those follow analytically from the product monotonicity, logistic comparison, exact quotient dynamics and asymptotic integration in RESULT.md. Only strictly positive initial conditions are covered; no finite collection of simulations supports a global uniqueness or priority claim.
