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

# Reproducibility and mathematical verification

Run `python3 artifacts/checker.py` from the folder containing `RESULT.md`. Python's standard library suffices. The expected successful line is:

```
CENTERED_CROSS_FOURTH_PASS gaussian_convolutions= 576 quintic_alphabet_exact_cases= 25 ternary_dimensions= 29
```

The checker reconstructs the fourth moment by **independent Fourier convolution** for 576 exactly represented Gaussian-integer coefficient samples, including nontrivial center and arm phases. It compares those results with the claimed phase-sum formula. It also lists every ordered pair of fifth-root exponents and compares all 25 resulting fourth moments by exact integer arithmetic in \(\mathbb Q(\sqrt5)\). Finally, integer-count enumeration corroborates the ternary residue formula for all dimensions two through thirty.

The proof in `RESULT.md` supplies all-dimensional independent-coordinate moment identities and equality cases. The algebraic-integer obstruction is exact and applies to **all** finite root-of-unity phase alphabets, not merely those tested. The numerical and finite enumerations are supplemental checks, not extrapolations, exhaustive proofs of unbounded claims, or external certification. Independent mathematical audit has not been performed.
