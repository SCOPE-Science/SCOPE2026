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

The accompanying `verify.py` is self-contained apart from Python 3 and SymPy. It constructs the sixteen-state transition matrices from the written exclusion rates and verifies stationarity of the equilibrium vector; both matrices' column sums; the two normalized perturbative Poisson solves; a symbolic rational identity for the quadratic current coefficient; positivity of the polynomial coefficients; the vanishing at homogeneous residence time; and two exact rational parameter specializations. Execution returned:

```
EXACT_IDENTITY_PASS
SIGN_AND_HOMOGENEOUS_LIMIT_PASS
TWO_EXACT_RATIONAL_SPOT_CHECKS_PASS
```

A separate direct stationary solve at reservoir differences \(\delta=\pm1/100\), done with exact rational arithmetic, found an even-current part of opposite sign for residence times \(a=1/2\) and \(a=2\). The symbolic rational-function identity, not these finite specializations, supports all-positive-parameter quantification. The global minimality step uses only reflection symmetry of shorter chains and the exact four-site nonvanishing. Independent audit has not been performed; this script does not certify originality or physical model adequacy beyond stated rate conventions.
