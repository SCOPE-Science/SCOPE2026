---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The Hermite normalization gives a=|b|/sqrt(m!), with phase removable by rotation. For nonzero radius the angular derivative forces the two ray types and the polar mixed derivative vanishes there. On constructive rays the derivative in t=|z|² is a positive factor times a t^((m-2)/2)(m-t)-1; the scalar factor has its sole maximum at m-2 with strictly negative second derivative there. This gives the claimed types, the radial stationary inflection at the fold, and the stated square-root splitting. On destructive rays the simple polynomial zeros are quadratic minima. The only other stationary radius solves a t^((m-2)/2)(t-m)=1, with t>m; this function has positive derivative, and a t^(m/2)=t/(t-m)>1 there gives strictly negative radial curvature, versus positive angular curvature. The origin is a strict nondegenerate maximum for m>=3. Decay at infinity and the explicit strictly rising outer-peak height give the unique global switch. Writing d=m-t_m gives d=m exp(-m/2) exp(d/2) with 0<d<2, and expanding the two threshold factors yields 2 exp(m/2)/(e m). Inspected frozen VERIFICATION.md and husimi_checks.py without executing the upload. The independent `python3 /workspace/reproductions/frozen_checks.py 1` corroborates the equal heights and curvature and the large-order ratio using a Lambert-W evaluation; universality rests on the calculus.

## originality

FAIL

A distinct Resultary record explicitly reports a complete all-order Morse portrait and the same two transitions, including exact threshold formulas, for e^(-|w|²)|w^n-c|² with n>=3 and c>0. With n=m, w=e^(i pi/m) z and c=1/a the frozen intensity is exactly a² times that landscape. This proves coverage of the main claimed finding, not just similarity of notation or thresholds. Both records bear the same date; the comparison does not assign precedence or authorship. The polygon full text was not recovered, so explicit publication of the ratio asymptotic is not asserted; the ratio is a short asymptotic extraction from the equivalent thresholds and does not supply a surviving substantive repaired finding on its own.

## value

PASS

The complete classification for a natural two-mode family has mathematical value: it distinguishes the creation of new local peaks from a change in global localization and quantifies the extent of coexistence. This is a judgment on the substance of the classification, not credit for a second publication of the same portrait or for a standalone repair based only on the ratio.

The dated certificate retains the supplied scientific assessment, sources and limitations.
