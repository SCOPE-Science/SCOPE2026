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

# Reproducibility

Use Python with SymPy 1.14.0 and NumPy 2.3.5, then run

```bash
python verify_symplectic_jitter.py
```

The accompanying execution record reports `PASS 75 exact/symbolic/numeric checks`. Exact symbolic checks cover \(M(h)^\top G_hM(h)=G_h\), \(\det M(h)=1\), the transfer determinant identity \(\det(I-\mathsf T)=-2\varepsilon^2(h-\varepsilon)^2(h+\varepsilon)^2\), the perturbation numerator, and the stated rational cubic. Independent enumeration compares all two-choice step histories through seven updates for three deterministic initial vectors and two rational parameter choices; sampled spectral and weak-noise coefficients are tested numerically. The proof in `RESULT.md` establishes the universal cone spectral argument and the infinite-horizon bounds without reliance on finite enumeration. The actual source code and its output are embedded beside these documents.

No independent scientific audit or external proof certification has been performed. The assertions concern algebraic identities and finite test cases, not a mechanized proof of the full theorem.
