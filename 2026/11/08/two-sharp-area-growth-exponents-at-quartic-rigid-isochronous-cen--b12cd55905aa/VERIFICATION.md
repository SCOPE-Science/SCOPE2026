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

# Verifiable steps and limits

The proof begins from the exact original-time identity \(r(t)^{-3}=r_0^{-3}+P(\theta_0)-P(\theta_0+t)\). Check differentiation of \(r^{-3}\) and \(\dot\theta=1\) directly for the written vector field. Check the threshold \(K>M\) to distinguish globally periodic from forward finite-time escaping trajectories. Verify that the integration variable \(r\,dr\,d\theta\) is ordinary planar area.

For the maximal-contact step, expand a general homogeneous cubic on the unit circle into first and third trigonometric harmonics, which satisfy \(A^{(4)}+10A''+9A=0\). Uniqueness for this equation excludes a zero of multiplicity four or greater unless the cubic is zero. Analytic maxima of its primitive can therefore only have contact order two or four.

For a contact of order \(k\), rescale angle by \(R^{-3/k}\) in the exact disk-area integral; the limiting integrand has tail power \(2k/3>1\) and integral \((2k/(2k-3))c^{-1/k}\). At critical \(K=M\), use \(\theta(t)=\theta_0+t\) to read the exact rate of radial divergence in **original time**.

The standalone command `python3 verify_quartic_rigid.py` checks exact factorization at 63 rational cosine values, two Taylor coefficients and numerical disk-area ratios at radius 1000. The observed output was:

```
QUARTIC_RIGID_EXACT_POTENTIAL_FACTOR_OK cases=63
QUARTIC_RIGID_AREA_PHASE_CHECK_OK R=1000 exponents=1/2,5/4
normalized=3.223071439,1.719523221 limits=3.265986324,1.719311891
```

The quadratic-contact numerical ratio approaches its limit more slowly because of an additive lower-order contribution. These finite checks do not prove the general theorem. No independent validation has been performed. Source overlap risk is documented in the review and audit material.
