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

The Yule embedding has uniform parent choice independent of birth times, so conditioning on population size gives the ordinary z^(n-1) series of the parity expectations. The two-type backward equations give A'=A^2+alpha B^2 and B'=(1+alpha)AB, with (A,B)(0)=(0,1). For v=A/B these give v'=alpha(1-v^2)^(1-h) and B=(1-v^2)^(-h), proving the stated local inverse, signs and first coefficients. At odd time, interchanging all bits interchanges the two position states. For the analytic step compressed at RESULT.md line 72, nonnegative Taylor coefficients and Pringsheim rule out a radius smaller than R: the real inverse is analytic all the way up to R. The derivative diverges as v tends to 1 there, giving radius exactly R. Monotone convergence gives the absolute coefficient sum 1 at R; positivity of the z and z^3 coefficients forces strict inequality |v(z)|<1 elsewhere on the circle except at -R. Local analytic ODE continuation then applies at those ordinary boundary points. To justify the dented domains at the two exceptions, write R-z=(1-v)^h times an analytic nonvanishing factor at v=1, take a local analytic h-th root of the factor, and invert the resulting regular map in (R-z)^(1/h); use oddness at -R. The leading contribution is 1/[(1+alpha)(R-z)] and the error has order (R-z)^(-1+1/h). The two pole terms add for the odd powers z^(n-1), and transfer gives the claimed relative O_alpha(n^(-1/h)); dividing the character by two gives TV. The integral gives R>2/(1+alpha)>1 and R=pi/2 at alpha=1/2. The uploaded check.py was inspected, not run; it has 680 counted exact comparisons/assertions and 3 floating diagnostics, despite the frozen summary calling the combined count 683 exact. This does not affect the proof.

## originality

PASS

Credit prior exact odd-time uniformity, even-time positivity, the recurrence/evaluation representation and exponential convergence in the identical model. The distinct supported claim is the exact inverse-beta generating function and sharp fixed-alpha even-time exponential base, prefactor and relative error. The strongest same-model paper, inaccessible to the frozen author in full, was accessed for this review: it proves two-sided exponential bounds rather than that sharp asymptotic. The bounds, prior recurrence, and other regimes were assessed for implication, not just exact wording.

## value

PASS

The even-time character is the exact obstruction to uniformity in this minimal nontrivial finite group. Identifying its sharp mixing scale and normalization resolves what prior two-sided bounds leave undetermined. The inverse-integral series is a usable all-times description of the same probability (also the all-even-cluster probability), not merely another probabilistic encoding or a fitted finite rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
