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

# Reproduction and mathematical limits

The standalone `check.py` requires Python 3 with `sympy` and `mpmath`. Run `python check.py`. It verifies the exact two-step matrix identities symbolically, checks the zero-gain periodic coordinates and characteristic polynomial for three sinks at \(2h=1.01\), and solves for the continued period-two sinks at \(\mu=10^{-6}\), \(\gamma=2\), verifying their multipliers. It also evaluates representative exact-count inequalities at several coupling values.

The proof of the infinite-parameter theorem is in `RESULT.md`: (i) exhaust the two sine-root classes, (ii) calculate the complete return spectrum, (iii) count strict sinks and derive the coupling asymptotic, and (iv) apply the implicit-function theorem to any finite selection. Finite diagnostic checks do **not** verify infinitely many parameters, do not certify numerical global basins, and are not an independent mathematical audit. The stable multiplicity at strictly positive input is an existence lower bound for small input, not a complete census. Nonhyperbolic threshold cycles are deliberately excluded from the sink count.
