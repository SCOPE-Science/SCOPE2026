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

The planar first-moment Steiner formula and coarea give qG'=(L+2πt)(H(t)−G(t)). Resolving the numerator of G' along H−G and S−H yields two positive coefficients whose ratio increases strictly from zero to infinity; the exact criterion is that the two nonzero vectors oppose. This handles permanent coincidence, equality of just two centers, and reversal at the unique positive root. For a scalene triangle strict concavity of sine gives noncollinearity via the three angle/side pairs; for an isosceles triangle the perimeter apex weight lies between the other two, as follows from the signs of the strictly concave comparison function across π/3. For a trapezoid, independent chord, side-midpoint and turning-angle expressions put H=G strictly above S at h0: arcsin(z)/z<π/3 for 0<z<1/2. Continuity and the sign of 2s−√(d²+h²) give the stated one-sided interval and strict axial maximum. The derivative of H_y−G_y at h0 is −d h0²/(36s³); the ratio in the stationary equation is 2πt/L+O(t²). These give exactly the stated positive slope. The rational enclosures for the witness certify the needed strict signs. Independent replay: python3 /workspace/branches/frozen_exact_checks.py 4; it verified the differentiated identity and height derivative and returned 10.82830409446180928 for the witness radius.

## originality

PASS

Credit existing coverage of the centroid polynomial, the triangle obstruction and the exact static height; the general stationary criterion is an elementary implication of the polynomial, not a separate original theorem. The distinct contribution is the positive-radius onset for every unequal base ratio, the resulting sharp quadrilateral threshold, and the explicit onset law; the strongest inspected statements do not establish the decisive height-dependent comparison with the Steiner centroid or these consequences.

## value

PASS

This identifies the first polygonal complexity permitting an isolated equality of two intrinsic centroids, and explains how it arises. The witness is stable over a nonempty height interval for every unequal base ratio; the slope quantifies how the positive optimum emerges at the static transition. This is stronger than computing an isolated example or repeating the known static height.

The dated certificate retains the supplied scientific assessment, sources and limitations.
