---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The invariant quadratic form with matrix entries 1 on the diagonal and −cos(theta) off diagonal conjugates J_c to a rotation with area Jacobian sin(theta). Its dual norm sends the strip to tangent distance r=h cos(theta/2). Opposite normals turn the angular gap sum into polygon area 2r² sum_i tan(delta_i/2); the pullback gives h² cot(theta/2) times that sum. The determinant of the first two strip functionals has absolute value c, giving A_2=4h²/c. At rational rotation number p/v the unoriented normals stabilize at v equal gaps; at irrational rotation number their density gives disk area. More precisely, for strict strips the transformed infinite survivor set is the closed disk minus the countable set of tangent contact points, not literally an open or closed disk. Also the strict-strip departure time agrees with the closed-middle-branch switch almost surely, not on all boundary orbits; neither qualification changes the area or probability results. The tangent Taylor expansion gives the v^(−2) spike, and only finitely many rationals of bounded denominator in (0,1) gives the asserted continuity classification. The lower bound for the excess comes from convexity at equal gaps. Bounded partial quotients give a convergent grid with maximal angle gap O(1/m); the excess is bounded above by a constant times sum_i delta_i³ <= pi(max_i delta_i)². For the conditional law, subtract the never-depart mass from the normalized finite survival probability and divide by the eventual-departure probability. The denominator is positive for irrational angles since A_infinity/A_2=(pi/4)sin(theta)<1; the formula properly excludes zero denominators, e.g. period two. The m^(−2) tail yields a convergent first-moment sum and a harmonic lower bound for the second moment. Independently clipping ±ell J_c^j z<=1 with rational arithmetic and using shoelace area gave 8, 5, 22/5, 13/3, 142/33, 47/11 at c=1/2 for m=2–7, matching separately evaluated gap areas within 2e−12. For replay, start in the exact parallelogram defined by the first two constraints and clip by the subsequent two half-planes per visit. The frozen verification/neutral_strip_check.py was inspected, not executed. No finite clipping check certifies the infinite-time results.

## originality

FAIL

A distinct indexed result demonstrably covers the exact finite and infinite survivor areas, the rational spikes, and the bounded-type quadratic excess, and also proves the converse Diophantine classification. The conditional moment consequence is an immediate tail sum from that result. The distinct catalogue path is dated later than the assigned path; equivalent coverage and historical priority are different, and no historical priority conclusion is made.

## value

FAIL

Exact survival and critical first-switching moments are worthwhile quantities for this center slice. The submission does not add a distinct exact fact: both the area and tail are covered for the identical initial law, with a stronger rate classification, and the explicit moment threshold follows by the standard tail-sum formula. Changing the inequalities on null lines does not recover scientific value as a separate area or probability claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
