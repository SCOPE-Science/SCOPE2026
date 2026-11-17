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

# Verification of the Hamming codeword-polytope distance

The exact supporting-plane certificate is \((n+3)\langle e_i-y^{(i)},z\rangle=6z_i-2\operatorname{wt}(z)\le0\) for every codeword \(z\). Equality occurs only at zero and weight-three words containing \(i\). All prescribed projection coordinates and the convex combination have rational values. Its squared residual norm is \(4/(n+3)\).

The standard-library `hamming_hull_checker.py` was executed and produced:

```
HAMMING_HULL_EXACT_PASS finite=(n,codewords,noncode_vertices,face_equalities): [(3, 2, 6, 6), (7, 16, 112, 28), (15, 2048, 30720, 120)]  sampled: [(31, 2000), (63, 2000), (127, 2000)]
```

The independently formulated `hamming_numeric_projection.py`, requiring NumPy and SciPy, was executed and produced:

```
HAMMING_NUMERIC_QP_PASS: [(3, 2, 0.6666666666666667, 5.551115123125783e-17), (7, 16, 0.4000000000000015, 4.218847493575595e-15)]
```

The numerical solver directly minimizes squared Euclidean distance over weights on all codewords. It was tested only for lengths three and seven. Exact exhaustive codeword checks were performed only at lengths three, seven and fifteen; the remaining tests were samples. No finite run proves the infinite-family theorem. The proof depends on the elementary code minimum distance, the projection variational inequality and residual variance, each displayed explicitly in `RESULT.md`. An independent mathematical audit has not been performed.
