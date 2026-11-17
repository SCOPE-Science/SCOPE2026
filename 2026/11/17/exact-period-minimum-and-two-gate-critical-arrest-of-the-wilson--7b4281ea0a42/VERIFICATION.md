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

The exact identities checked algebraically in the proof are the invariant-circle equation \(\dot R=-2x(x^3-bx)R\), the angle equation \(\dot\theta=-[1+xy(x^2-b)]\), the quarter-turn identity, and the positive strict-convexity integrand. The sharp period coefficient is derived from the two nondegenerate quadratic zeros and the identity \(2u-1=2[u(1-u)]^{3/2}\). The transverse multiplier is computed from the exact normal cofactor, not a numerically fitted exponent.

The included `checker.py` uses Python's standard library and composite midpoint quadrature to check numerical consistency. It locates \(u\), compares the exact center period and the symmetry \(T(0.2)=T(0.8)\), and evaluates both endpoint period and log-multiplier scalings at three decreasing positive displacements. On execution it finishes with `WILSON_CIRCLE_DIAGNOSTICS_OK` and reports convergence toward the proved constants. This numerical procedure is neither an interval certificate nor an exhaustive mathematical proof. Its numerical values are illustrative only.

The 2019 and 2020 related primary articles could not be inspected in full via available lawful access. Their abstracts and bibliographic records were checked; scientific priority should receive external human review. No independent audit was performed.
