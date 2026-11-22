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

# Mathematical verification

The complete proof is in `RESULT.md`. The attached `CHECK.py` was executed with Python and SymPy; output:

```
face identities (dimensions 3..6): 112
derivative/limit identities: 5
certified negative upper bounds: -505/256 -61/256
PASS; the all-n theorem is proved in RESULT.md
```

The first family checks exact symbolic differentiations of the stated formula on every nonempty proper coordinate face for dimensions 3 through 6. The second checks one- and two-coordinate derivative identities and the divergence to negative infinity. The final checks use the exact inequality \(\log 2>1/2\) to certify that the full density has a negative boundary limit for both representative sign cases at a rational point. Continuous extension from a face into the interior converts these boundary limits into a copula obstruction.

The parameter-wide and dimension-wide quantifiers are established analytically by the two complementary face limits in `RESULT.md`, not by finite checks. No independent audit, formal verification, or external certification has been performed. The proof's claim is restricted to the exact variable-exponent product ansatz.
