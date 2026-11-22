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

# Verification and reproducibility

**Claim under verification:** exactly one interior figure-eight branch crossing for the strict two-memory amplitude interval, a unique interior signed-area cancellation ratio for any continuous positive rating, and an explicit synchronized-single-peak cancellation example.

Run the self-contained `CHECKER.py` using Python 3.9 or newer. It uses no external packages. In the packaged source replay it checks branch formulas directly against original time-domain values, monotonicity and both endpoint thresholds, each sign regime, interval-root behavior, the closed-form integral against composite Simpson quadrature, and the synchronized-maxima example. Reported result: **PASS 21822 finite diagnostics**, with linear-rating cancellation \(B/A\approx0.854001741163\) and crossing discharge \(q_*\approx0.440393678658\).

The analytic proof rests on the exact branch identity and the strict monotonicity of \(x\coth x\) on positive inputs, not on finite grids. The area identity is an evaluated elementary integral. The derivative bound for synchronized maxima is global on both half-events, except at their common cusp where the left derivative is positive and the right derivative negative. This proves one maximum, not merely an observed numerical peak.

**Limits:** numerical checks cover only selected parameter values and sampled discharges; the proof supplies the continuum and all-rate quantifiers. The model does not assert calibration, mechanistic conservation, noise robustness, or historical publication priority. No external independent audit has occurred.
