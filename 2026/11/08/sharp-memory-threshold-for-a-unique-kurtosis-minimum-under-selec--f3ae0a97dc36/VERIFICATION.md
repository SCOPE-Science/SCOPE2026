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

The embedded `verify.py` (with `requirements.txt`) recomputes the polynomial generator equations for every degree-two and degree-four monomial; exact symbolic equalities for stationary moments; all eight coefficients of the resetting derivative; the Descartes sign change and disjoint rational positive-root brackets; every positive coefficient in the bath derivative; endpoint limits; both asymptotic implicit-root coefficients; and forty direct exact-rational stationary-system solves. Run `python -m pip install -r requirements.txt` and then `python verify.py` from the same extracted directory.

On the actual package source, the executed program reported:

```text
PASS: exact stationary 2nd/4th moments and normalized excess kurtosis
PASS: all eight resetting-derivative coefficient identities
PASS: Descartes root signs, strict root order and uniqueness certificate
PASS: exact all-positive coefficient certificate for -d(kurtosis)/dg
PASS: limiting kurtosis, simple small-memory optimizer root and -5/6 correction
PASS: 40 independent exact-rational fixed-parameter linear systems
ALL CHECKS PASS
```

The mathematical sign arguments cover all real positive parameters; the finite exact-rational systems are cross-checks rather than exhaustive certification. The model requires \(g,r>0\), and no stationary law is asserted at \(r=0\). The primary paper supplies the selective resetting setup and precursor moments; their publication priority is expressly acknowledged. Independent scientific validation has not been performed.
