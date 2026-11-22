---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The even-moment Gram inverse generates the explicit five-degree-denominator quartic coefficient h_{m,k} and reproduces degrees 0–4. Discrete differences commute with convolution; an input step has delta difference so the exact unanchored variation operator norm equals G_m=sum|h_{m,k}|, not merely an upper bound. Independently recomputed all integer gains m=2..1999 with exact rational arithmetic: unique maximum at m=6, G_6=3763/2431. For m>=2000 the paper gives a uniform coefficient difference <34/m relative to K(u)=(225-1050u²+945u⁴)/128 and BV Riemann-sum discrepancy <9/m; hence G_m<G_infinity+78/m. Rational root brackets and polynomial integration prove G_infinity<301/200, and 301/200+78/2000<3763/2431. This analytical tail, not finite enumeration or a floating-point limit, closes the infinite quantifier. The degree-five center intercept equals quartic by odd/even orthogonality.

## originality

PASS

The 1964 Savitzky–Golay full reprint teaches convolution weights, 5-to-25 point tables and noise smoothing; it does not state a quartic all-radii sharp total-variation gain. The full published quadratic/cubic positivity theorem shows a seven-point optimum for different polynomial degree; its one-sign-change kernel and 29/21 gain do not imply the quartic double-negative-lobe maximum 3763/2431. Schmid–Rath–Diebold (2022) discusses ringing/stopband and boundary artifacts, not this stated optimization. The 1983 Marchand–Marmet article is highly relevant to overshoots, but authorized full-text retrieval returned no verified PDF; risk recorded, not declared wholly noncovering.

## value

PASS

Unweighted quartic center smoothing is a standard numerical operator, and its sharp adjacent-variation gain directly measures deterministic amplification/overshoot under a one-jump worst case. The complete all-window comparison gives a nonmonotonic robustness boundary at 13 points distinct from the continuum plateau and from degree-two behavior. This window-design result is an exact mathematically motivated stability invariant, not merely coefficient tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
