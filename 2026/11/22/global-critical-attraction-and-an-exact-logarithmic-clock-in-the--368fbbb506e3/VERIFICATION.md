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

# Reproducibility and verification

The derivation begins with the exact derivatives of \(V=-mx^2+y^2+z^2\) for \(m<0\) and \(V=y^2+z^2\) for \(m=0\), then uses the scalar center-manifold invariance equations at the eigenvalue-zero boundary. The quintic Taylor coefficient produces an integrable remainder after subtracting the linear and logarithmic terms from \(1/y^2\). Exponentially close stable fibers inherit the expansion; trajectories in the 2D strong-stable manifold are excluded from reciprocal-square inversion because their decay is exponential.

Run `python checker.py` with SymPy installed. The script verifies the two Lyapunov identities, center Taylor jets through order five, reduced field coefficients, logarithmic constant, and rational parameter substitutions. The script was executed on the exact packaged path before delivery and returned `PASS`. Independent numerical ODE integration for \(n=1/2,1,2,3\) up to time \(20000\) confirmed stabilization of the predicted renormalized clock. Computation does not certify the infinite-time theorem; the analytic arguments in RESULT.md do.

Independent mathematical audit has not been performed. The complete foundational 2005 T-system texts were not accessed, which remains an originality risk.
