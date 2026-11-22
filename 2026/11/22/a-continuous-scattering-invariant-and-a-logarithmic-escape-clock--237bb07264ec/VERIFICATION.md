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

# Reproducibility and analytical verification

Run `python verify.py` with Python 3, SymPy, and SciPy installed. The checker evaluates the exact transformed identities
\[
\dot\varepsilon=x^2(4-q^2p),\qquad
\frac{d}{dt}\log(xe^{q^2/8})=\varepsilon(1-p),
\]
compares the rational trapping inequalities at every relevant boundary, and integrates the sample initial state \((x_0,p_0,q_0)=(1/50,1,4)\) to finite test times using an adaptive high-accuracy ODE solver. The observed tests return `SCATTER_VERIFY_OK`.

The mathematical proof does **not** depend on finite numerical tests. Completeness on the stated open cone follows from the inward vector-field signs and the explicit reciprocal bound. The nonstandard limit proof is the \(L^2\)-convolution argument and its consequent absolute integrability. The asymptotic integration uses \(\int^Q e^{s^2/8}ds\sim4e^{Q^2/8}/Q\); this is a standard one-dimensional integration-by-parts or l'Hôpital calculation. The nonconstant-invariant assertion follows from the explicit small-positive-initial-coordinate estimate, not a plot.

Tests do not address points outside the cone, uniformity at its boundary, or priority against inaccessible research texts. The verification status here records self-review only; no independent audit has been performed.
