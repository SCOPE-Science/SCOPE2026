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

With Python and NumPy installed, run `python verify.py`. The verifier reconstructs the analytical formula, checks exactly two erased zeros, reproduces trigonometric moments, counts negative weights, compares total negative mass and Euclidean noise amplification, and independently solves selected Vandermonde systems. It also checks the uniform random-erasure variance average for 98 odd grid sizes. The source code is included with the result and can be modified to test further sizes.

The finite numerical checks are implementation checks, not certificates for all odd grid sizes. The universal statements follow from the Fourier-spectrum restriction, explicit cosine solution, sign comparison, sum-of-cosines identities and the cosecant-square averaging identity demonstrated in `RESULT.md`. Approximate floating-point tolerances do not certify exact algebraic equality. Historical priority remains provisional and no independent audit has been conducted.
