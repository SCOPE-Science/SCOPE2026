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

# Reproduction and limits

For the physical-time ecological flow, the decisive exact identities are
\[
h(z_*)=h'(z_*)=0,\qquad h''(z_*)=-\alpha^2(d+1),\qquad
\lambda(z_*)=-\mu,\qquad -\lambda'(z_*)/\kappa=2q/(1-q).
\]
The appendix script `verify.py` evaluates all four symbolically using SymPy, checks the strong-stable eigenvector identity, then performs a fixed-step fourth-order Runge–Kutta numerical diagnostic in \((\log u,z)\) for the exact example \(\alpha=d=1\), \(q=1/10\), \(u(0)=10^{-4}\), \(z(0)=0.95\). Run it with `python verify.py` in a Python 3 environment with SymPy available.

Actual run: `VERIFY_OK`. The diagnostic reported ratio products \(t(z-z_*)\) approximately \(1.06084845660\) at \(t=500\) and \(1.08504803780\) at \(t=1000\), converging toward the analytically proved \(10/9\). The normalized prey amplitudes \(e^{(4/5)t}t^{2/9}u(t)\) were approximately \(0.000209549635665\) and \(0.000210890674029\) at the same times. This finite computation checks arithmetic consistency, not the existence of the limiting amplitude or the theorem for all parameters and initial states.

The infinite-time statements follow instead from the invariant positive wedge, a quadratic angular upper/lower comparison, the integrable forcing term \(u/w^2\), an \(O(\log t/t^2)\) remainder, and the exact coupling coefficient in the log-prey equation. No external code or numerical certificate is required for the proof. The exceptional strong-stable curve is obtained by a local invariant-manifold theorem, not a numerical fit.
