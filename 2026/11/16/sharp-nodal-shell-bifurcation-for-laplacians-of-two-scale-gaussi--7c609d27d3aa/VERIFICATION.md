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

## Reproducibility

Run `python3 verify.py` from the directory holding the embedded result. The script uses only the Python 3 standard library. Its numerical and algebraic checks cover seven dimensions, mixed weights inside/outside the predicted three-shell window, strict turning-point ordering, direct Laplacian zero substitution, the exact logarithmic derivative, and the \(3/2\)-power cusp asymptotic.

A complete run of this exact supplied script returned:

```
PASS: 308 numerical/algebraic checks (including all seven dimension samples).
```

All nontrivial equalities used for the infinite family have separate derivations in `RESULT.md`: the Gaussian Laplacian formula, nonzero comparison factor, strictly positive derivative denominator, the threshold quadratic, endpoint root multiplicities, and the uniform shrinking-interval estimate. Floating-point tests cannot establish the general theorem, completeness of an infinite root classification, or publication priority. No independent mathematical audit has been performed.
