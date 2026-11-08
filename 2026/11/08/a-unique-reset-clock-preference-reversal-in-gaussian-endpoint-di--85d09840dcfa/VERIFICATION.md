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

Run `python3 verify.py` with the Python standard library. The checker implements the exact finite-width Gaussian endpoint reward, its displayed second derivative, the nonnegative comparison kernel, and exponential quadrature. It performs finite-difference derivative comparisons, sampled curvature sign checks, sampled strict ordering-kernel comparisons, bisection for five width parameters, and high-/low-frequency protocol-order spot checks. The recorded execution reports 2695 deterministic checks passed.

No finite test proves a unique crossing for every parameter. That conclusion follows from the exact cubic curvature sign, strict kernel-ratio ordering, two signed-integral endpoint asymptotics, and continuity in RESULT.md. The numerical crossover for \(q=1/2\) has roundoff/quadrature precision only; the defining equation is the exact integral equality. No formal proof assistant or third-party independent audit is claimed.
