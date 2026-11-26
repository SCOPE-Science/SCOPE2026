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

Reverse the implicit step: the predecessor of w is (a+h|w|²−ihω)w. The radial map is H(s)=s√((a+hs²)²+b²); its derivative has numerator 3u²+4au+a²+b² with u=hs². This is positive for a≥0, and for a<0 its minimum on u≥0 is b²−a²/3. Positivity, radial properness, and the radius-dependent rotation give smooth global inversion. Equality gives a singular Jacobian, and below equality there is a decreasing radial portion, so smooth invertibility fails at both. Positive fixed radii solve (a+u)²+b²=1: for 0<b<1, both roots −a±√(1−b²) are positive exactly for a<−√(1−b²), and they fit the smooth-inverse condition exactly for b>1/2. At b=1 the possible positive root is double with unit radial multiplier; at b>1 there is none. The origin multiplier has modulus (a²+b²)^(−1/2)<1 in the window. The two reciprocal radial derivatives give inner repulsion and outer attraction. The signs +,−,+ of H(s)−s and monotone inversion give the stated basins and exclude recurrence off the fixed radii; rotations on the two circles have the stated angles. The exact example multipliers check as 25/21 and 25/93. The proof is for the exact step of this isochronous normal form; check.py and VERIFICATION.md were inspected, not executed, and cover only supplementary finite checks.

## originality

PASS

The inspected sources cover local implicit-orbit and evolution-fold theory, not the exact global inverse and bistability intersection, its circle stability, or its basin classification for this oscillator. Credit the classical backward-Euler linear amplification and Stuart–Landau model; the distinct claim is the combined global classification, not either antecedent.

## value

PASS

A standard implicit integrator creates a qualitatively false bistability even where there is no ambiguity or branch choice anywhere in its nonlinear solve. The necessary and sufficient step-frequency restriction and exact separating basin boundary distinguish this artifact from ordinary linear instability or implicit-solver failure. This is a useful benchmark for the natural cubic oscillator, not a claim about arbitrary Hopf systems or discretizations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
