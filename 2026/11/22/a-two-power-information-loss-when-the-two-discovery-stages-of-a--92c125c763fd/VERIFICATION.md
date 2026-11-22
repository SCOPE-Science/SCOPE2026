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

# Reproducibility and limits

`python3 check_coupon.py` runs with the Python standard library and should report `PASS: 6029 exact-rational identities (finite diagnostics only)`. It checks rational coefficient identities for the geometric convolution and rational quadratic denominator, first two moments, inversion, score coefficients, Fisher information, and exact neighboring-bin differences. The code needs no data files, random seeds, or external packages.

The proof of the all-parameter distributional assertions is in `RESULT.md`; specifically, exact score information is obtained by negative-binomial factorial-moment identities and asymptotic testing limits follow from uniformly summable likelihood derivatives and the triangular-array central limit theorem. Finite coefficient and moment checks are diagnostics, not independent certification or exhaustive enumeration. The limiting likelihood constants were additionally checked numerically outside the standalone artifact for \(h=2\), without treating that computation as a proof.

The model presumes independent repeated experiments. No independent mathematical audit has been performed.
