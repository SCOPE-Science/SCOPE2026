---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

The standard-library program `verify_cartier_c12.py` (Python 3.9 or later) checks formal characteristic-two identities in the quotient ring defined by \(y^2+y=t^3\) and \(v^2+v=y^3+c_0^2 y\). It also computes the semilinear Cartier ranks over \(\mathbb F_4\) for all four \(c_0\) and for the specialization corresponding to each \(\lambda\in\mathbb F_4\). It explicitly checks inverse Frobenius and counts successive images of the six-dimensional space, rather than treating the map as linear. Finally, it checks the gap set of the semigroup \(\langle4,6,9\rangle\).

Execute `python3 verify_cartier_c12.py` in the directory containing this file and the script. The observed output is:

```text
FORMAL_CHAR2_POLYNOMIAL_IDENTITIES_OK
GF4_CARTIER_POWER_RANKS_OK 6,4,3,2,1,0 (all four c0 and all four lambda)
WEIERSTRASS_SEMIGROUP_GAPS_OK 1,2,3,5,7,11
CERTIFICATE_OK
```

These finite-field checks do not establish the infinite-field theorem. The general claim uses an exact six-element holomorphic differential basis and the Cartier action computed algebraically for unrestricted parameters.
