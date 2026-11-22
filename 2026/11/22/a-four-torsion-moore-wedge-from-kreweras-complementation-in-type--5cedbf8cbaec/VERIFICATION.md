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

# Computational verification and limits

The classification is proved by the exact 2-dimensional CW presentation and its homotopy-preserving generator/two-cell cancellations. Two standalone source programs are provided and should be executed from a common directory:

```
python3 verify.py
python3 verify_integral_chains.py
```

The first requires only Python 3; the second additionally requires SymPy for integer Smith normal forms. Both were executed successfully on the embedded source as prepared, using exact integer arithmetic. Their actual success lines were `B4_KREWERAS_WEDGE_CERTIFICATE_OK` and `B4_KREWERAS_INTEGRAL_SMITH_OK`.

The first checker recomputes the entire 384-element Coxeter group and verifies the reflection-length identity using independent breadth-first search. It then constructs all 70 absolute-interval elements, the 68/288/256 original nonempty simplices, the complete barycentric subdivision, the eightfold group orbit counts of 77/264/192, the maximal-tree presentation, and 187 cancellable one-cell/two-cell pairs. The final five attaching degrees on the surviving generator are exactly `0,0,4,4,4`. It computes the ordered elimination-trace SHA-256 `25a49e9a4473dec46f0fb702aeefd74e8592fe12c16db58f84909ceec47c0f33`.

The independent chain checker builds signed matrices with dimensions 77-by-264 and 264-by-192, verifies their composition is the zero matrix, and computes Smith diagonal multiplicities `d1: 1^(76)` and `d2: 1^(187),4^(1)` using exact integer algorithms. In particular, it independently obtains the integral homology asserted in the result.

**Limitations:** The computations are exhaustive only for the finite, explicitly presented rank-four case. A Smith-form calculation alone does not prove a homotopy type; this is why the CW cancellation computation is also supplied. Neither computation proves novelty relative to every possible unpublished or unavailable source. Independent external review has not been performed.
