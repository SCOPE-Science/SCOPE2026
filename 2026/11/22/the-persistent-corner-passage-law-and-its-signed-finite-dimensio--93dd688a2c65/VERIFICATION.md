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

# Verification scope

The companion `checker.py` executes using standard-library Python 3. It constructs exact Hamming-weight transition matrices for the independent-coordinate flip chain, solves exact first-passage equations for the expected time and for two generating-function arguments, and compares the results with the spectral/renewal formula. It tests dimensions 1 through 7 at three rational flip rates, as well as the \(1/d\) asymptotic coefficient and sign at dimensions 100, 200, 400, 800 and 1600 for five fixed positive parameters.

Execution: `python3 checker.py`. The checked execution passed 225 exact-rational and numerical assertions. Computations test the identities but do not prove the infinite limits. The latter rely on the stationary renewal identity, binomial concentration, convergence of nonnegative time correlations and a controlled Taylor expansion in `RESULT.md`. The scope is stationary initial distribution, one corner and fixed \(a>0\); it excludes general holes, nonstationary starts and a marked point-process limit.
