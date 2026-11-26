---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The repaired finding is saved at /workspace/repairs/5/RESULT.md. In the frozen result the geometric transversality assertion did not follow from continuity of g; in fact for q*=1/2, b=R(1/2), the allowed g(q)=q(1+cuberoot(q−1/2)) makes both branch tangents vertical (parameterize q=1/2+s³). The contrast itself has a negative derivative at q* by its difference quotient, even without differentiating g. The repair keeps the simple sign-changing contrast zero and claims distinct tangent lines only when g is differentiable there. All other conclusions survive: the exact contrast A g f_h(R−b) has g f_h>0 inside; since x coth x increases strictly for x>0, R strictly decreases between b_foot and b_peak. This gives the sharp open interval and rules out interior equality at the endpoints. The cancellation ratio is the weighted average of R with positive weight g f_h, strictly between the endpoints; the signed area is affine in b with negative slope and the two signed lobe integrals cancel nontrivially. For g(q)=q integration gives J, and |U′|≤Ak+Bh<a≤U yields the asserted strict rise and fall of C about t=1. Independent benchmark replay python3 /workspace/branches/review_checks.py gives b_g=0.8540017411631949 and q*=0.4403936786577953; supplied script was read, not executed. The proof is continuum, the calculation a benchmark only.

## originality

PASS

Figure-eight loops, their mixed orientations, and scalar-area limitations are not new. The distinct finding supported here is the necessary-and-sufficient strength interval independent of rating, the unique interior weighted cancellation ratio, and the synchronized single-peak example for exactly the triangular two-exponential model. Read statements on comparable supply models and exact cancellation do not imply this combination. Historical priority is provisional.

## value

PASS

The exact open interval decides when a two-source response produces a second lobe with no need to specify the rating. The existence of a unique cancellation ratio inside that interval and a synchronized-single-peak example show specifically why both net area and peak timing can miss a two-lobe response. Those are useful limitations of summary measures in a transparent ideal model, not claims of field calibration or source identifiability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
