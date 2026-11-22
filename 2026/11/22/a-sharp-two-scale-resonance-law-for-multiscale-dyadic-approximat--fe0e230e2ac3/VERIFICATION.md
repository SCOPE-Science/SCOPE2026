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

The proof in `RESULT.md` establishes the complete infinite-dimensional statement. In particular, no finite grid can certify the global or infinite-depth theorem. The standalone `check_multiscale.py` program runs under Python 3 without third-party libraries and uses `fractions.Fraction` throughout the exact-rational tests. Run:

```
python3 check_multiscale.py
```

The program checks exact maximization over every quadratic cell for six even residual depths, verifies the paired square-deficit formula on rational parameters, and checks several signed multiple-jump residuals via the exact dyadic Gram inner products. Its final success line is `All finite exact checks passed; infinite scope requires the proof in RESULT.md.`

The unbounded-scale assertion uses the uniform geometric tail bound \(\sum_{j\ge J}2^{-j}/4\), not extrapolation from these tests. Equality for general \(BV\) data uses the strict determinant \(s(1-t)(t-s)>0\), which is a symbolic algebraic identity. The first two scales already determine the two allowable jump sites. These are logical checks in the written proof and cannot be replaced by a numerical log. No independent review or external mathematical validation has been performed.
