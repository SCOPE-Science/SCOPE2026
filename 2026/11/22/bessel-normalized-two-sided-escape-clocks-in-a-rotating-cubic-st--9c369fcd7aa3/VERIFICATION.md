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

# Verification of exact rotating-cubic escape laws

## Analytic critical checks

1. Substituting the Cartesian system into polar coordinates gives exactly \(\dot r=\lambda r+(\sigma+\kappa\cos2\theta)r^3\) and \(\dot\theta=\omega r^2\), with no angular singularity away from the origin.
2. Differentiation of \(R/F_\sigma\) with respect to lifted angle gives the constant positive source \(2\lambda/(\omega F_\sigma)\), and the relation \(dW/dt=2\lambda W\) gives the physical-time inversion without an asymptotic clock substitution.
3. The uniformly periodic Laplace average is \(I_0(\kappa/\omega)\) in both the negative-parameter cycle limit and positive-parameter blow-up-time limit. The two factors are the same because changing the direction of phase translation does not change the circular average.
4. The phase blow-up function is everywhere positive and solves \(P'=\{2\sigma/\omega+2\kappa\cos(2\theta)/\omega\}P-1/\omega\). This precludes a constant \(P\) when \(\kappa\ne0\).

## Independent numerical consistency checks

Run `python3 check.py` with Python 3, NumPy, SciPy and SymPy installed. The checker differentiates the reduction symbolically, compares direct ODE integration against the exact physical-time angular relation for three regimes, evaluates the positive-side escape-clock asymptotic for a decreasing parameter sequence, confirms the negative-side cycle scaling, and tests the phase-profile ODE and nonconstancy. Output `all checks passed` indicates these finite numerical consistency checks, not a machine proof of an infinite-domain theorem.

## Limits

The proof is analytic. Quadrature convergence, finite test arrays and symbolic simplifications do not establish originality or independent verification. No formal proof assistant, independent human review or publication-priority certificate is asserted.
