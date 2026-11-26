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

The proper survival is indexed by X>=n, and the hazard-difference sign is the sign of the second difference D_n of Phi, independent of q. Coefficients of t^m in D_n have the sign of m beta-1 (the multiplier (2^m-2)/m! is positive for m>=2). At beta>=1/2 there is always a strictly positive term, including at equality. Below 1/2 the ratio of the positive series to the absolute negative polynomial is strictly increasing, by the separated powers, goes to zero at zero and diverges by any one positive monomial of greater degree. This gives the unique positive age threshold. The triangular-kernel integral holds even at n=0, since K(x)Phi'(x)=O(x^(2 beta)) and K(x)Phi''(x)=O(x^(2 beta-1)) near zero. For fixed t, the normalized adjacent tent weights times the common positive curvature factor have a single strict crossing from left to right (their ratio is strictly increasing on the overlap), so integration of the strictly increasing curvature multiplier beta f(t x^beta)+beta-1 is strictly larger for the next age. Here f'(z)-1=e^z(e^z-1-z)/(e^z-1)^2>0. At t_n this proves t_(n+1)<t_n. Centering at n+1 gives the scaled second difference H_c''(1)+O((n+1)^(-2)), after multiplication by (n+1)^2; testing fixed c on both sides of its unique zero proves the threshold asymptotic and eventual increase. The age-zero formula follows by taking positive square roots. A bounded independent rational replay certifies the particular signs (-,-,+) at beta=1/4, t=1; strict threshold order supplies the subsequent signs.

## originality

PASS

The squared-odds model and qualitative hazard plots are prior art, including the exact nested Weibull model in Yousof et al. The supported distinct claim is the unique, strictly ordered staircase of discrete age thresholds, the sharp all-age cutoff and asymptotic constant; the inspected prior results did not give or imply that full classification.

## value

PASS

This replaces qualitative plots for a named discrete lifetime model by a precise cutoff, eliminates invisible late reversals, and quantifies how the reversal ages move as the scale parameter becomes small. The global ordering and endpoint of the staircase, rather than the elementary hazard formula, give its structural value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
