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

# Verification

Run `python verify.py` from this directory with SymPy installed. The script checks the trigonometric-to-polynomial identities, the exact quadratic reductions and parameter-boundary junction, the coefficient maximum and Chatterjee-optimal parameters, orthogonality of the Fourier eigenfunctions, and rational interior/exterior cases.

The theorem for all real parameters is established analytically in `RESULT.md` by exact extrema of a two-variable polynomial; grid or randomized testing is not an infinite-domain certificate. The finite symbolic probes are a supplementary check. Self-review passed; independent audit has not been performed, and literature searching does not certify historical priority.
