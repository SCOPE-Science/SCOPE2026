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

Set b=1/lambda in [1,5/3]. Five contributing quadratic spline samples yield Im(Z)/sin(theta)=Delta_1+2Delta_2 cos(theta), bounded below by D_b=Delta_1-2Delta_2. The piecewise quadratic spline second derivatives give D_b concave on x in [0,1/2], with D_b(0)=0 and D_b(1/2)=(-21b²+54b-29)/(8b²)>0, hence positive away from x=0. On x=0, the cosine polynomial P_b(t) is nondecreasing and P_b(-1)>0; on nu=0, Z>0; the nu=1/2 boundary R_b(x) is strictly decreasing to its symmetry zero at x=1/2. Under b>5/3 published aliasing gives positive-length half-frequency zero interval. Independently checked 931 exact rational configurations for b from 1 to 5/3 and b in 7/4,15/8,2; those tests are supplementary to analytic continuum inequalities.

## originality

PASS

PASS: Prior Hasannasab–Lemvig gives the below-threshold half-frequency zero interval and higher-scale results, while published November2 quadratic spline symmetry-fiber theorem addresses only x=1/2 and frequency variation. Neither result as read supplies the global exclusion of off-midpoint spatial/frequency zeros for every b<=5/3. The submitted concavity and boundary proof closes this genuinely two-dimensional subunit classification.

## value

PASS

PASS: A sharp, exhaustive two-variable zero classification for the natural compactly supported quadratic B-spline fills a coherent gap between known symmetry-fiber and superunit results. The exact threshold 3/5 is a usable boundary for Zak/Gabor analysis, without claiming an arbitrary frame-set classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
