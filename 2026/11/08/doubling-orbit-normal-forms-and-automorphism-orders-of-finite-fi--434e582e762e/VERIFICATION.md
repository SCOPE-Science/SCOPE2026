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

## Mathematical and computational verification
The proof is a symbolic classification argument, not an inference from finite testing. The nonstandard steps are the oriented weighted-cycle normal form, the fact that changing the starting vertex squares the invariant modulo the \(2^\ell-1\)-th-power subgroup, and the full stabilizer calculation. All are derived explicitly in `RESULT.md`. The exact checker operates on cyclic exponents of nonzero finite-field elements, which is valid over every finite field; no additive field operations enter its equations.

Run `python CHECK.py` in a directory containing the extracted source. Compare its complete stdout against `CHECK_OUTPUT.txt`. In seven small examples, the checker enumerates all invertible monomial structures and the complete monomial basis-change group; for ten field sizes it checks the Burnside expression through length ten. The saved run output concludes `VERIFY_OK`.

Limits: these small finite enumerations do not prove the general theorem. In particular, a finite run is neither a certificate of absolute novelty nor a proof for all dimensions. There has been no independent audit.
