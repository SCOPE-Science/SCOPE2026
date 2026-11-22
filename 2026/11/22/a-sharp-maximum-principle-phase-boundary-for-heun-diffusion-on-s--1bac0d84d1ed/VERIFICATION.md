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

# Verification of the sharp Heun positivity threshold

Execute `python VERIFY.py` with Python 3. NumPy is optional for the fractional spectral reconstruction; exact rational tests use the standard library only. Verified local output with NumPy installed:

```
EXACT_RATIONAL_CASES 2162
FRACTIONAL_SPECTRAL_CASES 24
VERIFY_OK
```

The exact-rational section constructs the full matrix directly for every integer multipartition of orders two through eight and internal weights chosen from the listed rational menu; it checks every matrix entry, all row sums, positivity at and before the predicted critical step and a step beyond it, as well as positive diagonals. The independent NumPy section forms the *original* graph Laplacian, raises it spectrally to fractional powers, then compares the derived missing-edge weights and the resulting regularized spectrum. Floating zero modes are thresholded only in this optional section to suppress harmless eigensolver roundoff near zero. Theorem-level universal quantifiers rely on the projector and exact sign arguments in `RESULT.md`, not on finite tests.

The sharp amplification threshold is checked algebraically from the strictly increasing divided-difference function; the particular numerical instance with two equal parts is an illustration, not an exhaustive proof of the general phase law. Independent external validation is not represented.
