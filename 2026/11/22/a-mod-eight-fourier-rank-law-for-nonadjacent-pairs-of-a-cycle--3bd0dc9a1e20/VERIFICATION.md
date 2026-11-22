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

# Computation and mathematical scope

Running `python3 verify.py` from a directory containing the file performs a direct integer transform of the explicit two-element independent-set indicator. It compares every Fourier coefficient with the proved closed form for \(4\le n\le15\), 65,520 coefficients in total, checks rank/nullity and tests the modular classification through \(n=399\). The observed output is:

```text
verified 65520 full integer Walsh coefficients, n=4..15; rank/zeros 4..399
[(4, 8, 8), (5, 32, 0), (6, 64, 0), (7, 128, 0), (8, 216, 40), (9, 512, 0), (10, 1024, 0), (11, 1476, 572), (12, 3616, 480), (13, 8192, 0), (14, 16384, 0), (15, 32768, 0)]
```

The script uses no packages beyond the Python standard library. Verification code enumerates finite cases only; the all-length conclusions use the algebraic and cyclic-composition proof in RESULT.md. The displayed status does not imply an external or independent review.
