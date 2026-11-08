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

# Reproducibility and mathematical boundaries

Run `python3 verify_minimax.py` in the directory containing this file. It uses only Python's standard library and requires no data downloads. The attached `verification_output.txt` records a successful run with **3,217 exact rational assertions**, for eight sample sizes, including non-unit-step tests. The checker derives means, squared norms and covariance integrals by direct piecewise-polynomial integration, and compares the worst-case formula on a rational grid. Its test at \(n=1\) is a known consistency limit, not an additional novelty claim.

The actual correctness justification for the universal statement is **not** the grid check: it is the analytic reduction to unit jumps, the explicitly averaged Hilbert-space lower bound, and the equality of the bound with the clipped-ramp objective. Exact arithmetic does not turn a finite grid into exhaustive real-variable verification. All local sample coordinates are unit-interval coordinates; global stratum scale is \(1/n\). Controls are centered before estimating an integral, and all variances use independent stratum samples. General quadrature classes, adaptive fitting, dependent sampling, and unknown-mean control functions have not been tested or proved optimal. Independent audit has not been performed.
