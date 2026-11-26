---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Bilinear expansion gives xy=r(x)c(y)^T. The margin map onto the common-total hyperplane W is surjective by filling the first row and column, and has kernel dimension d. Pair equations for a tuple with nonzero margins on both sides force at least one mixed row, then proportionality of all margin rows to it. Otherwise all first or all second margins are zero. Thus the reduced locus is exactly the rank-at-most-one cone in W^m and the two pure loci, times affine dm-space. For m≥2, either pure side is contained in the cone exactly when its margin space is one-dimensional; a mixed point prevents the reverse containment. The rank-one parametrization gives dimension a+b+m−2 before adding dm. All equations and noncontainment tests are valid also in characteristic two. Counting the two pure loci, subtracting their common zero, then counting q^m−1 tuples on each of the N/(q−1) mixed lines gives the exact bracketed formula. At m=0 it gives 1 and at m=1 it gives q^(ab). The recorded finite checks were inspected, not rerun; the proof does not depend on them.

## originality

FAIL

The exact rectangular-band pair census is a distinct indexed record. Its proof already gives the same common-total quotient and an exhaustive zero-bracket criterion in that quotient, including the entire centralizer of a mixed margin pair. Those exact subspaces determine all higher arities and the reduced geometry without an additional structural result. An indexed biclique theorem independently gives the same classification of bracket-vanishing spans before restricting to the common-total hyperplane. This is demonstrable coverage by direct implication, not a claim about chronology.

## value

FAIL

The component dimensions and counts are convenient to have together, but as proposed incremental mathematics they are routine consequences of the already explicit pure-side/mixed-line classification. The result does not add a geometric obstruction, a new threshold mechanism, or a finer invariant of the overlap or scheme.

The dated certificate retains the supplied scientific assessment, sources and limitations.
