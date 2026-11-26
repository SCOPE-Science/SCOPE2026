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

The basis product collapses to XY=r_X c_Y^T. The margin map has image all pairs with common total s and has a kernel of dimension d=(m−1)(n−1), as is seen by filling one row and one column. Thus X^h=s^(h−2)rc^T, with the factor interpreted as 1 for a square. For nonzero target total, each scalar root of s^h=t(Z) forces the two margins; for rank one the identity rho(Z) gamma(Z)^T=t(Z)Z proves sufficiency. At zero total, nonzero square targets require both margins zero and have exactly q−1 ordered rank-one factorizations; the same targets cannot be higher powers. The zero-square fiber is the union of the two zero-margin cases, while the higher zero fiber is the total-sum hyperplane. Normalizing one factor to have total 1 gives q^(m+n−2) rank-one targets at every prescribed nonzero total; dividing the ordered nonzero zero-sum factor count by q−1 gives the exceptional cone. These arguments cover m=1 or n=1 and all field characteristics, and give both advertised image counts and the input mass. The accompanying direct basis-law code and 29 recorded finite checks were read, not rerun.

## originality

PASS

The inspected sources establish the rank-one sandwich framework and several other exact statistics of the same algebra, but not this complete all-exponent prescribed-target power distribution. The overlap in zero-margin targets with the nearby commutator record is a different map, not a duplicate fiber law.

## value

PASS

The complete fiber function is a useful exact invariant of the natural power map on a standard nonunital algebra. It distinguishes the scalar cyclic-group obstruction from a separate zero-total cone that is hit by squaring but by no higher power. Both the support and actual multiplicities are needed for power-map counts; the result identifies precisely when this extra support exists, including degenerate rectangles and extension fields. It is more than counting nonzero scalar roots or reporting finite experiments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
