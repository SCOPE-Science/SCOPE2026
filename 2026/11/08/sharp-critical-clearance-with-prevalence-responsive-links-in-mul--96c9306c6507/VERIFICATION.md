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

The all-time result is established by the analytic steps in `RESULT.md`. The check script `verify.py` independently computes the two-community Perron data with exact symbolic fractions and verifies the explicit formula \(\kappa=(4+3c)/8\). It then integrates the full six-dimensional prevalence/link-density ODE with high accuracy for initial conditions \((y_1,y_2)=(0.75,0.1)\) and \((z_{11},z_{12},z_{21},z_{22})=(0.2,0.35,0.75,0.1)\), stopping at physical time \(10^5\).

For \(c=2\) and linear breaking sensitivity the observed products at that finite time are approximately \(t y_1=t y_2=0.400003\) and \(t(1-z_{12})=t(1-z_{21})=0.800007\), versus the proved limits \(2/5\) and \(4/5\). With the same parameters but quadratic breaking response the products are approximately \(0.999815\) for both prevalence coordinates, versus the proved limiting coefficient \(1\), and the cross-link deficit products approach zero. The script must print `EXACT_COEFFICIENTS_OK` and `VERIFY_OK` if its checks succeed. It requires Python 3, NumPy, SciPy and SymPy.

These finite-time integrations are not exhaustive certificates of infinite-time dynamics or all initial conditions. The proof's global Lyapunov argument, Perron-mode separation and convolution limits supply the infinite-time justification. The general hypotheses do not provide a uniform quantitative convergence speed.
