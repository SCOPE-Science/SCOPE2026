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

# Verification record

Run `python3 verify.py` in the directory containing this file and the included `verify.py` with Python 3 standard library only. The exact-rational script enumerates the 15 pairings of six indices and verifies a nonzero general point, a simple branch vanishing, symmetry consistency under 120 permutations, a repeated-root nondivisibility witness, two transverse vanishing branches with Jacobian minor 9/8, and an explicit six-I2 Weierstrass discriminant-square identity.

Expected terminal lines include:

```
MATCHINGS 15
GENERIC_NONZERO 4259997759969637171200
EVEN_ZERO_BRANCHES 1
DOUBLE_BRANCHES 2 TRANSVERSE_MINOR 9/8
SIX_I2_DISCRIMINANT_SQUARE_OK
CERTIFICATE_OK
```

The certificate contains exact checks for named examples and algebraic identities. It does not enumerate every binary sextic or independently certify irreducibility, the universal surface classification, or mathematical priority; those claims are supported by the written geometric proof and explicitly cited published results. There has been no independent mathematical audit.
