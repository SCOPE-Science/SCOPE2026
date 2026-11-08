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

The bundled `verify_cartier.py` expands powers of the defining quartic symbolically over the appropriate prime fields, verifies every entry of the Cartier matrix, and establishes both normalized Hasse determinant identities. Execution yielded:

```
PICARD_CARTIER_COEFFICIENTS_PASS 11
PICARD_CARTIER_COEFFICIENTS_PASS 13
PICARD_PRYM_HASSE_DIVISORS_PASS
```

The separately implemented `verify_zeta.py` counts points over extensions of degrees one through three and recovers the first three zeta coefficients. It does not use the coefficient-extraction routine of the first program. Execution yielded:

```
PICARD_PRIME_FIELD_ZETA_PASS 11 {0: 10, 2: 90}
PICARD_PRIME_FIELD_ZETA_PASS 13 {3: 132, 1: 12}
```

The proof over algebraic closures uses direct Cartier coefficient identities and the prime-to-characteristic isogeny with the elliptic quotient; the finite computations alone would not establish the geometric assertions. No external independent audit has been performed, and the 1991 general Picard-Jacobian primary text was not available in full.
