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

The full theorem is proved analytically in RESULT.md. The Fourier frame operator is reduced to five trigonometric moments. Elementary symmetric sums of six and seven roots and the map from the cyclotomic ring to \(\mathbb F_p\) exclude respectively six-point rules at \(p=7\) and seven-point rules at every \(p\ge11\). A closed positive eight-point rule is verified through exact cosine moments. Endpoints \(p=3,5,7\) are handled without extrapolation.

The accompanying `checker.py` uses only the Python standard library and independently computes both parity-obstruction tables. It checks a rational interior instance by exact `fractions.Fraction` arithmetic, then verifies the explicitly constructed rules numerically for every odd prime from eleven to 501, as well as the exceptional subgroup cases. Run `python checker.py` from an extracted copy of the supplied artifacts. Numerical tests are supplementary and do not certify all primes; the proof supplies the infinite quantifiers.

No independent audit has been performed. Absolute historical priority and stability under noisy data have not been established.
