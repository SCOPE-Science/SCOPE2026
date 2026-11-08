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
# Verification and reproducibility

The standalone `check_unitary_sixth.py` script requires Python 3 only. The command `python3 check_unitary_sixth.py` was executed on the artifact to verify the exact order-three unitary Weingarten Gram inverse, its contraction into the sixth-moment polynomial, the sharp rank-one and flat-spectrum endpoint values, the dimension-two formula, the universal-deficit algebra and hundreds of rational spectral test vectors.

Recorded output:

```
UNITARY_GRAM_WEINGARTEN_EXACT_CHECKS_PASSED 934
UNITARY_SHARP_RANK_ENDPOINTS_AND_STABILITY_PASSED
```

The exact rational Gram inverses supply independent finite checks of the nonstandard integration coefficients for dimensions three to nine; finite spectra are *not* an exhaustive proof for all dimensions or real coefficients. The universal theorem uses the published order-three Weingarten identity and the explicit strict Schur-concavity proof in `RESULT.md`. The separate \(n=2\) formula uses the two allowed Schur representations. The external independent audit is not yet performed.
