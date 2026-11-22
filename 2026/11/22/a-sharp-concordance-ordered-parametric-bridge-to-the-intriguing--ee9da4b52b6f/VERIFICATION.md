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

# Verification of the parameter-bridge theorem

The decisive analytic checks are the exact identities for \(\partial_y C_\gamma\), the two density summands, \(L_s'(t)=(s-t)/t^2\le0\), and the global positive mixed-density lower bound. The corner limits establish the necessity of both parameter bounds, including strict negative density on an interior open neighborhood. The parameter derivative is strictly positive because \(u^a(-\log u)/(1-u)\) increases for \(a\ge1\).

`check_int1.py` is a standalone supporting checker. With Python 3, mpmath and sympy installed, run `python check_int1.py`. The fixed-seed 60-digit run passed 3614 support checks, including exact symbolic identities for the auxiliary functions, high-precision double derivatives, density-bound inequalities, strict parameter comparisons and explicit negative-density witnesses. The checks are finite numerical/symbolic diagnostics; they do not establish the all-point theorem independently of the proof.

The construction is assessed only as a bivariate copula with uniform margins. Higher-dimensional copulas, estimation procedures and full historical priority are not verified. Independent mathematical audit: not performed.
