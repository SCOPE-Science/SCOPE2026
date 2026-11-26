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

Choose a Weierstrass point w as base for the theta divisor C−w in the genus-two Jacobian. Its intersections with the 2-torsion are exactly the six classes o_i=[w_i−w], since 2P∼2w precisely at the ramification points. The tropes come from 2-torsion translates of this theta divisor. Label the two classes of vertices by a copy each of J[2]; incidence is translation by the six o_i. Therefore the Levi graph is the Cayley graph on F₂⊕J[2] with generators (1,o_i). There is no dependency of weight 2 or 4: the o_i are distinct, and an equality between sums of disjoint pairs would identify two different effective degree-two divisors, each a pair of distinct Weierstrass points, outside the unique hyperelliptic pencil. Odd-length relations are impossible by the first coordinate. Thus the six generators in dimension five form one circuit and the graph is exactly the folded six-cube, independently of the parameters (this argument works in odd characteristic as well). I built the graph using the five unit vectors and their sum. Its exact Laplacian characteristic polynomial gives the stated spectrum and connectivity, and the cofactor determinant is 3·2^72. Exact Smith form gives 1(12), 2(4), 4, 16(4), 32(9), 96. The 96 incidences give cycle rank 65.

## originality

FAIL

There is concrete equivalent coverage of the complete invariant in a distinct indexed record: cb0c19041c53 lists exactly 2(4), 4, 16(4), 32(9), 96 in its identity Frobenius row and expressly treats the total group as existing content, not as its new fixed-group classification. The two records have the same publication date; that fact does not establish which appeared first or any dependence, and this review makes neither finding. The defect is exact substantive coverage of the standalone finding, not a suspicion based on table parameters or an unresolved search. Gao et al. additionally cover the odd-primary factor and mod-2 rank, but those partial results alone would not establish the entire Smith form.

## value

FAIL

The full Smith group is a natural and potentially useful invariant of the Kummer configuration. The frozen record, however, adds no mathematical content beyond the exact identity row already contained in the distinct indexed classification, and the other stated data follow from the standard folded-cube or biplane model. As a scientific finding rather than a reproducibility check, it has no distinct surviving result to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
