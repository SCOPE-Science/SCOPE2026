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

# Reproducibility and limitations

The standalone `verify.py` runs with Python 3, SymPy, NumPy, and SciPy and requires no source-document files or network access. Invoke `python3 verify.py` from the directory containing the script. The successful observed output begins:

```
PASS 75 exact symbolic identities/positivity conditions and independent geometric volume comparisons
critical small/large ratio: 0.402394259925177568
critical normalized large coordinate: 0.634264060482970744
critical section volume: 1.31889442272420290
```

The script constructs each rational piece from the independently derived positive-part convolution sum, asserts equality with eight explicit rational branches, differentiates their formulas, checks junction values and first derivatives, verifies the two Bernstein positivity identities exactly, and checks the defining quadratic root and both interval exclusions. It also computes twenty four-dimensional convex-hull volumes from actual five-cube edge-plane intersections at distinct real parameters, and checks agreement with the analytic volume formula.

The convex-hull test uses floating point arithmetic with a conservative absolute error tolerance; only the symbolic algebra and sign certificates are exact. Neither twenty geometric profiles nor seventy-five program assertions constitute exhaustive proof over real parameters. The general theorem is established by the explicit positive-part formula, full-gradient symmetry argument, and exhaustive sign proof in `RESULT.md`.

The work classifies only normals with full support and precisely two absolute-coordinate levels. Independent audit has not been performed.
