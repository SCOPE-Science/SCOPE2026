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

# Reproducibility and mathematical limits

**Analytic evidence.** The exact reduction \(y_{n+3}=ab y_{n+2}y_n^2\) and nonzero normalization \(L_n=\log(\sqrt{ab}|y_n|)\) give a third-order linear recurrence with characteristic polynomial \(\lambda^3-\lambda^2-2\). The positive left eigenvector yields \(\log H\) and the exact nonlinear eigenfunction identity, including the zero faces by continuity. Eigenvalue moduli and the nonreal complex phase prove the sharp strict-regime asymptotics and critical oscillation. Enumerating three logarithmic zeros gives the eight preperiodic points. Recurrence considerations and Poincaré recurrence classify invariant probabilities. These universal steps do not depend on numerical tests.

**Executable diagnostics.** Run `python checker.py` under Python 3 (standard library only). The checker was executed successfully from this package directory: `PASS: 336 exact rational recurrence comparisons, 401 log-eigenfunction tests, 12 threshold/exception tests.` It also reports \(r\approx1.695620769559862\), \(s\approx1.086052035863345\), and positive/negative high-precision critical logarithmic excursion examples.

**Scope.** Exactly \(c=1\), \(a,b>0\), full real state space. The script is finite testing, not a proof of any infinite or all-real assertion. No independent mathematical audit or independent validation has been performed.
