---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In row convention the shared scalar slope is r=uv, and the reversal changes the deterministic first-mass offset by Delta. The repaired derivation correctly transposes the published split: its final A time is vartheta*h. The two endpoint pi_B coefficients are (1-v) and u(1-v); interpolation with q=(1-exp(-s*vartheta*h))/(1-u) gives the exact coefficient t(1-r)/(s+t). Independent centered innovations give scalar variance q(1-q)Delta^2 times the geometric sum; the Euclidean squared vector error is twice this, with the stated h^3 coefficient. As an exact check, for pi_A=1, pi_B=0, s=1, t=2, h=log 2, q=4/9 and the one-step vector risk is 5/72. For the 3-state pair both split traces agree by cyclicity; after removing the common absorbing contribution, the exact trace uses cosh(sqrt(5)h/2), strictly below cosh(h)cosh(h/2) by Jensen applied at 1/4 and 9/4. Zero-block embedding works in larger dimensions. The frozen verification and script were inspected, not executed; the script's second-state stationary weights in its Delta check change only a sign, which is squared. The analytic review, not the finite grid, supports the verdict.

## originality

PASS

The repaired finding centers the exact finite-n vector risk of calibrated full-length order randomization and the explicit all-positive-h three-state affine obstruction. The binary calibration is explicitly derived and credited as known coverage. No inspected statement gives the finite-step risk for this random experiment; in particular, the known fair-order scaling does not furnish this finite-h moment. The trace obstruction is a concrete witness, not a new trace inequality.

## value

PASS

For a mean-exact random update the remaining question is how much randomness affects the computed probabilities. The finite-n rate/horizon-dependent coefficient answers that directly, beyond an order-of-accuracy statement. The explicit all-h obstruction shows that even allowing signed affine mixing does not produce a universal extension outside the binary setting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
