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

# Verification of dispersion phase diagram

The theorem is verified analytically by the following dependencies, each given explicitly in `RESULT.md`:

1. The conditional negative-binomial factorial moments yield the exact quadratic identity in the mixture-retention weight.
2. A derivative argument for the auxiliary function \(h_r(u)\) proves the non-numerical global sign identity \(\operatorname{sgn}(A-2B^2)=\operatorname{sgn}(1-r)\).
3. Exponential tilting of the size-biased excess count shows \(d(A/B)/d\log q=\operatorname{Var}(Z^*)>0\). Endpoint limits establish a unique additional cutoff.
4. Strict quadratic concavity, endpoint signs, and the vertex location supply all sign regimes and root formulas.

To reproduce the independent exact-rational witness and sampled numerical checks, run `python3 verify.py` from a directory containing that file. The checker intentionally does not claim to prove the global theorem by finite enumeration. Rational identities require no tolerance; finite-tail and boundary illustrations use explicit numerical tolerances. Neither an external certificate nor an independent mathematical audit is asserted.
