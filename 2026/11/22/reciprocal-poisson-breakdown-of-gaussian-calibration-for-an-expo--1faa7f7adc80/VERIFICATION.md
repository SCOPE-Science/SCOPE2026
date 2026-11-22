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

Run `python3 verify.py` in the directory containing the standalone script. It requires only the Python standard library and independently recomputes the Stein ratio in exact rational arithmetic, the delta-method mean correction and influence variance for fixed Poisson parameters, the necessary Poisson remainder formulas, and the integer cutoff classification at nominal 5%.

The proof of the weak limit is in `RESULT.md`, Steps 1–5. Numerical checks confirm algebra and cutoff values; they do not establish the limit theorem by enumeration or simulation. The hard claims are for independent Poisson triangular arrays with positive mean, a deterministic positive exponential weight approaching zero, and a specific evaluated Gaussian approximation. On the all-zero sample, the undefined ratio is assigned zero for definiteness; this event is asymptotically negligible.

Self-review status: passed. An independent audit has not been performed, and no external certification is asserted.
