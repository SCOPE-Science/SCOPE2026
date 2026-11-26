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

Pairing opposite half-lines cancels the linear tilt term; integration gives 4+2(6!)β². The first-order factor at zero is 2(1−|x|), so zero is a strict cusp maximum at every finite tilt. Sign reflection reduces to b=|β|>0. With z=b|x|³ and s=+1 on the right, −1 on the left, the outward derivative has the sign of 6b^(1/3)z^(2/3)(z−s)−(z²−2sz+2). This excludes right-hand critical points for z≤1. On the remaining domains the positive level function H_s=(z²−2sz+2)/(6z^(2/3)(z−s)) diverges at both ends. Its logarithmic derivative is (z³−8z+4s)/(3z(z−s)(z²−2sz+2)); the cubic is negative at the lower endpoint and has only one increasing crossing afterward. Exact endpoint signs in the stated brackets are (−3/8,97/125) and (−1,991/1000). At a minimum level the outward derivative is negative off its isolated zero, so no new local maximum exists there; above the minimum there is exactly one outward + to − transition on that side. At z_L, H_R−H_L=(4−2z_L²)/(6z_L^(2/3)(z_L²−1))<0, establishing b_R<b_L. The independently evaluated thresholds agree with the displays. β=0 and positive location-scale transformations behave as stated. Dividing by β² gives pointwise convergence to x⁶e^(−|x|)/1440, a normalized density whose only maxima are ±6; Scheffé gives total variation. These arguments cover all parameters, rather than inferring them from plots or the frozen symbolic checker.

## originality

PASS

The supported distinction is the sharp two-threshold strict-local-mode classification, including both equality cases. The distribution, the upper bound of three, parameter reflection, and the limiting bimodal law are not awarded originality. The inspected original statements and indexed comparisons do not supply the sharp boundaries or a theorem that already resolves them.

## value

PASS

The number of local peaks is a natural model-design parameter for this density, and the exact classifier lets a user distinguish true shapes even at onsets and when the cusp is too small to see in a plot. The disjoint strict onsets and permanent finite-tilt cusp provide information absent from an upper bound or a list of approximate stationary points. No claim is made about global-height orderings, statistical detectability, or the exponentiated family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
