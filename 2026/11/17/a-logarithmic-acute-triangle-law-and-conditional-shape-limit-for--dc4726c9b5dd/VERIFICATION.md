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
# Verification details

Analytical checks: the normalized arclength projection law is \(q_\varepsilon=w_\varepsilon/I_\varepsilon\), with \(w_\varepsilon\ge1\); the exact nonnegative mixture with the uniform projection law is valid. For sorted projected coordinates, the acuteness middle-angle dot product is \(-st+\varepsilon^2H_\sigma\). Since \(|H_\sigma|\le4\), acuteness forces \(st<4\varepsilon^2\) independently of signs. All but the opposite-middle-sign configuration are negligible by \(|\sqrt{1-u^2}-\sqrt{1-v^2}|\le\sqrt{2|u-v|}\). Hyperbola area integration gives \(2c\varepsilon^2\log(1/\varepsilon)\) when \(st<c\varepsilon^2\), yielding the exact stated factor \(2\). On fixed compact pieces, endpoint vertex dot products are positive except for gaps \(O(\varepsilon^2)\); no finite sample is used to justify this infinity-limit step. The joint logarithmic coordinate Jacobian supplies the conditional limit.

Executable checker: `python check_ellipse.py` (with `numpy>=1.24`, optionally `OPENBLAS_NUM_THREADS=1`). Seeds 1, 2, and 3; exactly 2,400,000 independent triangles per configuration, using two distinct sampling techniques: coordinate-uniform plus independent branch signs, and rejection-proposed eccentric angle with exact ellipse-speed acceptance for Euclidean arclength. Checker evaluates three direct dot products and compares the leading ratio, conditional middle-coordinate second moment, logarithmic-gap mean, and correct sign-pattern frequency. Observed:

```
uniform_x: eps=0.018, n=2400000, acute=5931, p=0.00247125, ratio=0.94929, EX^2=0.19972, Elambda=0.99878, central=0.95734
perimeter: eps=0.018, n=2400000, acute=5927, p=0.0024695833, ratio=0.94865, EX^2=0.19625, Elambda=0.99711, central=0.96035
perimeter: eps=0.027, n=2400000, acute=11860, p=0.0049416667, ratio=0.93838, EX^2=0.20149, Elambda=1.01107, central=0.95346
THIN_ELLIPSE_ACUTE_LOG_LAW_CHECKS_OK
```

These are random finite-parameter checks, not interval certification, not a convergence proof, and not independent mathematical validation.
