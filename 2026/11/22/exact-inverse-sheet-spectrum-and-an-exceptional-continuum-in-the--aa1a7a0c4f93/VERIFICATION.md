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

At a prescribed target the cubic ψ(w)=w−w³/6 increases onto [0,5/6), so the permitted third-coordinate lifts are exactly W+k with 0≤k<5A/6−W; the strict upper inequality gives the stated ceiling, even at a seam. For each w, writing mv=δ+j exhausts the second coordinate with j=0,…,m−1. If mv>0 the allowed positive first-coordinate lift lies in (0,δ+j]; it has j integer translates of U−w plus one iff 0<{U−w}≤δ. This checks both half-open boundaries. For mv=0 the first coordinate forces w=U, and the remaining equations give exactly Γ_m, with every u allowed; at most one w-sheet contributes such an interval. For example at m=1 the target (1/2,1/2,0) has exactly the solution (0,1/2,0), (0,1/2,0) as a target has no preimage, (0,0,5/6) excludes the third-coordinate endpoint, and (0,0,0) has the whole v=w=0 interval. On fixed smooth lifts, subtracting the differential terms through U and V gives determinant −m²vA(1−w²/2); this is not a differentiability assertion at modular seams. For m≥2 at least one sheet exists and its baseline count is positive away from Γ_m. For m=1 the given unreachable target also follows from the cubic range. For m=64, 64≤A<66 gives 53≤s≤55 and per-sheet counts between 2016 and 2080, so the two numerical bounds are valid; the record expressly does not claim sharp extrema. The proof is exact, not based on the finite floating-point reconstructions in the supplied script, which was inspected but not executed.

## originality

PASS

The published Zhao–Ma equation itself is prior. The inspected same-map neighbor counts face fixed points rather than full-cube real fibers. No inspected comparable statement covers the exact integer-gain sheet counts, the continuum image, or the onto distinction. The decision is limited to the accessible evidence, not a priority guarantee for modular dynamics in general.

## value

PASS

Real one-step identifiability is a natural invariant of this published noninvertible map. A complete target-dependent count, a positive-dimensional fiber locus and the onto distinction are materially more informative than the forward formula or a sampled bifurcation portrait. The integer slice removes a genuine modular endpoint complication and includes the reference parameter. No finite-precision, cryptographic or long-run conclusion is needed for the value of the classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
