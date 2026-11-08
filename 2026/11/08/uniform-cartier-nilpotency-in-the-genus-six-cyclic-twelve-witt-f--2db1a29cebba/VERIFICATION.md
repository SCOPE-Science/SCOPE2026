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

# Reproducibility

The standalone Python 3 standard-library program `verify_cartier_c12.py` checks formal characteristic-two identities in the quotient ring defined by \(y^2+y=t^3\) and \(v^2+v=y^3+c^2 y\). It also computes the semilinear Cartier ranks over \(\mathbb F_4\) for all four parameter values and checks the gap set of the semigroup \(\langle4,6,9\rangle\).

Execute `python3 verify_cartier_c12.py` in the directory containing this file and the script. The observed output is:

```text
FORMAL_CHAR2_POLYNOMIAL_IDENTITIES_OK
GF4_CARTIER_POWER_RANKS_OK 6,4,3,2,1,0 (4 parameter values)
WEIERSTRASS_SEMIGROUP_GAPS_OK 1,2,3,5,7,11
CERTIFICATE_OK
```

These finite-field checks do not establish the infinite-field theorem. The general claim uses an exact six-element holomorphic differential basis and the Cartier action computed algebraically for unrestricted parameters. No independent mathematical audit or external verification is claimed.
