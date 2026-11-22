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

The analytic proof in `RESULT.md` establishes the generator admissibility criterion, the complete attainable two-statistic region, and rigidity. The supplementary `check.py` uses SymPy exact symbolic operations and prints a PASS indication after all assertions succeed; it was executed successfully in the package environment.

**Confirmed exact checks:** the weight integral \(\int_0^a4t(a^2-t^2)dt=a^4\), the two sides of the deficit-kernel identity, the lower generator's mass \(a^2\) and rank value \(a^4\), the upper generator's mass \(1-b\) and rank value \(1-b^3\), the uniform-generator deficit for \(p=a^2\), and three rational probability settings with convex mixtures and nonnegative off-diagonal densities. All comparisons in the checker use exact SymPy expressions or rational inequalities rather than numerical floating-point tolerance.

**Proof checks beyond code:** the measure with off-diagonal density \(h(\max(u,v))\) and diagonal density \(f(t)dt\) has uniform marginals because \(u h(u)+\int_u^1h(v)dv+f(u)=1\). Conversely the off-diagonal mixed derivative of the copula must be nonnegative. The lower-deficit identity is obtained analytically by Fubini. Boundary equality uniqueness and full interval attainment follow by sign and convexity arguments; they are not established by finite sampling.

**Unproved and unverified limits:** no assertion about arbitrary copulas outside the stated max-quotient family; no independent mathematical audit; and incomplete access to the 2015 diagonal-expansion full text leaves a residual historical-priority risk.
