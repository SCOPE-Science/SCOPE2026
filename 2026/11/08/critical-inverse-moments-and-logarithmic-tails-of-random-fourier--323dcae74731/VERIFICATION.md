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

The standalone checker is `CHECK.py` (Python 3 with NumPy and SciPy). Running `python CHECK.py` returned:

`CHECK_OK assertions=1015 dimensions=2..10`

It verifies the Lagrange-inverse coefficient formula and deterministic inverse-Frobenius comparison at 16 irregular configurations for each dimension from two through ten. It independently compares the reciprocal-chord Mellin integral with its gamma-function expression at four exponents and verifies the exact two-node formula. This test does not enumerate continuous random configurations or establish an asymptotic probability tail.

The universal proof consists of four fully stated mathematical steps in `RESULT.md`: exact Lagrange inversion and coefficient bounds; conditional independence and an elementary beta integral; convolution of exponential-tail logarithmic chord densities; and a deterministic comparison plus tail-integration identities. The logarithmic exponents and moment cutoff follow from these steps, not from numerical simulation. In particular, the exact surrogate tail constant must not be confused with an exact constant for the full matrix amplification.
