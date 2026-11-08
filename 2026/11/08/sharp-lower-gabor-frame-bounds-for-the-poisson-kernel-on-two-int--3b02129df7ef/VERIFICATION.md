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

# Verification notes

`CHECK.py` uses symbolic algebra to confirm the exact Zak-modulus identity and strict-convexity derivatives, numerical real-space sums to cross-check Poisson summation, frequency/position grids to test the lower inequality, and independent global minimizations to confirm attainability. It tests multiple widths and offsets, including half-period and near-integral offsets, and the predicted quadratic onset. Run `python CHECK.py` with `numpy`, `scipy`, and `sympy`.

All universal assertions, particularly the global sharp bound and uniqueness, have analytical proofs in `RESULT.md`. The finite checker does not constitute an exhaustive grid or an independent mathematical audit. No exact upper-frame-bound formula or noisy inverse reconstruction is claimed. The finding is self-reviewed; independent validation has not been performed.
