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

# Reproduction of spectral and optimization checks

With Python 3, NumPy and SymPy available, execute:

```sh
python verify_gear.py
```

The checker constructs each gear Laplacian independently from its \(3n\) undirected edges, compares the sum of reciprocal positive eigenvalues with the Fourier-block trace, checks the exact endpoint derivative values at \(n=3,4,5,6\), and validates the scalar derivative against centered finite differences. It also numerically locates the unique \(n=3\) interior critical point, verifies the closed-form hyperbolic expression for selected sizes, and checks convergence toward the predicted large-graph constants. On the supplied source it passes 528 finite assertions.

The theorem's unrestricted uniqueness is established by the strict convexity proof in RESULT.md, not by sampling perturbations. The exact all-size endpoint classification depends on the Jensen–Cauchy inequality for \(n\ge7\), exact evaluations for \(n=4,5,6\), and the exact quartic at \(n=3\). The infinite asymptotic claims depend on the derived cyclic resolvent identity and a standard Riemann-sum limit, not on finite numerical ratios. The tests do not provide formal external certification; an independent audit has not occurred.
