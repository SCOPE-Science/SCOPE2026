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

# Verification of the finite \(p\)-closed foliation fiber theorem

The written proof in `RESULT.md` is the source of the infinite, scheme-theoretic conclusion. The standalone `CHECK.py` uses only Python's standard library. It enumerates the nonzero zero-sum residue tuples for selected primes and degrees, verifies their closed count, verifies the length-versus-geometric-point predictions, and checks the characteristic-two formulas in the split ordinary and supersingular elliptic examples.

Command executed on the actual included source file: `python CHECK.py`.

Observed output:

```text
RESIDUE_CENSUS_OK
CHARACTERISTIC_TWO_FIBER_WITNESSES_OK
SCHEME_LENGTH_AND_GEOMETRIC_POINT_PROFILES_OK
CERTIFICATE_OK
```

The checker is not a proof for all primes or divisors. The critical unrestricted steps are the Jacobson restricted-power identity, the surjectivity of multiplication by \(p\) on \(\operatorname{Pic}^0(Y)(k)\), the global residue theorem, and the displayed equality of coefficient ideals. These are supplied with their hypotheses in `RESULT.md`. The geometric structure is asserted for the expressly defined restricted-Lie equation scheme, not an unidentified alternative moduli scheme. No independent mathematical audit has occurred.
