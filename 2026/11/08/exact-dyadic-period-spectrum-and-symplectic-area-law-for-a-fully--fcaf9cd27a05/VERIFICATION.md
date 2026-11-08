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

Run `python CHECK.py` using Python 3 and the standard library only. The program checks all sixteen initial polygon-edge pairings and twenty-five dyadic-depth combinations: 400 two-step transition rules plus 400 primitive-period computations, all in exact rational arithmetic. It additionally checks sixteen exact determinant weights and twenty-five finite cumulative survival identities. It should print a `PASS` line. The separate line–segment intersection implementation does not assume the five-case symbolic transition rule when constructing actual orbits.

The mathematical proof is in `RESULT.md`, including the exhaustive affine cases, the invariant depth cycle, the half-return antipodal/reflection identity, and the exact measure convolution. Separately from the standalone checker, the full open-cell affine formulas were derived by exact rational polygon clipping and tested on 400 entire dyadic rectangles before acceptance. These checks are supporting evidence only: finite sampling cannot establish claims over all real points. The invariant phase measure excludes a null set of vertex-collision trajectories; no positive-measure conclusions are asserted on that set.

Independent mathematical audit has not been performed.
