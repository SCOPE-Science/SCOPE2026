---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For generic off-axis points of prolate spheroid (1,1,r), all boundary normal feet lie in the meridian plane. The meridian stationarity equation has 2 or 4 simple solutions, distinguished by the ellipse evolute astroid (rho/k)^(2/3)+(r|z|/k)^(2/3)<1, k=r²−1. The revolving caustic is entirely inside the spheroid iff t=r²<=2; for t>2 its intersection with boundary has a single admissible latitude q*=t(t−2)/(t²−1). Exact intersection-volume quadrature yields p4=8(t−1)^3/(35t) for t<=2 and the stated positive radical correction above 2. Independent high-precision numerical cross-sectional integrations match the closed formula for r=1.2,sqrt2,1.8,3,9,20. Under unit-ball scaling both astroid coordinate coefficients decrease strictly with t, proving strict p4 growth and invertibility of mean 2+2p4. Expansion shows (t−2)^(5/2) loss (C² not C³), and uniform cap asymptotics yield 1−p4=15r^−4+O(r^−6). A 2D ellipse area-average law does not equal the 3D volume-weighted law. Exceptional symmetry axis/evolute have zero volume.

## originality

PASS

Best-of-knowledge targeted statement comparison against actual published same-object sources. The existing general principles and any known same-size phenomena are explicitly credited; the surviving contribution is the precise additional scoped statement (see four checks and residual risks).

## value

PASS

Natural 3D exact integral-geometric distribution for uniformly sampled interior points of a prolate spheroid, including where the caustic cuts the body, strict aspect-ratio identifiability from expected normal multiplicity, fractional regularity, and sharp elongated limit. The planar counterpart and evolute are classical; computing the different three-dimensional volume weighting is mathematically useful rather than a restatement of planar area averaging.

The dated certificate retains the supplied scientific assessment, sources and limitations.
