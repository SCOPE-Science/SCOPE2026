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

The translated vertex orbits follow from Bayer et al., Thm. 2.3(b); the strictly increasing positive labels ensure no coincident ranks. For fixed ranks, opposite rearrangement minimizes the dot product. If their sum exceeds n, each endpoint's smallest positive label is on a shared coordinate in an opposite arrangement. Delete the smaller of the two minima: its partner is at least the larger minimum, so the squared distance strictly increases by u(2v-u). This excludes sums above n+1 from the second shell. For sums below n, one can add a new minimum in a vacant coordinate; for a fixed disjoint rank sum, strict discrete concavity of F gives balanced ranks and, at sum n, the next-best imbalance. At the diametral ranks, any defective pair has overlap cost at least 2t_m^2 in even dimension or 2t_mt_{m+1} in odd dimension, more than the missing-slot deficit t_m^2. For sum n+1 the minimum positive product requires just one overlap and both minima at that coordinate. Counting placements of the distinct labels gives n! at each winning rank/overlap pattern, with factor 1/2 exactly when one can exchange equal-rank endpoints. These arguments prove the second distinct level and all ties. Independent exact orbit-compressed enumeration (/workspace/replay/parking.py) reproduced both levels and each second-shell geometry/count in 132 label lists at n=4,5,6, including (D,D2,count)=(112692,102692,240) on the three-mechanism tie. Computations corroborate the all-parameter argument; the result is not for b_1=1, graph distances, or the continuous polytope.

## originality

PASS

The classical second-shell result is a real structural antecedent. Its degenerate orbit set and fixed label gaps do not supply the arbitrary positive-label competition, all realizers, or tie census here. Other inspected close results give vertex orbits, a first diameter, or a probabilistic regime, rather than this second Euclidean level.

## value

PASS

The next distinct Euclidean chord length and its all-pair census refine the diameter of a standard polytope. The formula replaces enormous vertex-pair enumeration by a linear-size list; variable gaps change which geometry wins and can force ties. This is not just the diameter calculation or a reinterpretation of a combinatorial graph invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
