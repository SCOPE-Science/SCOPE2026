---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

A lax witness gives partial functions x→y and u→v that extend to total Boolean functions. Conversely, inclusion in the union of their two equality sets gives a valid lax witness, with overlaps permitted. The complements consist of exactly one row for each (x,u), determined uniquely by the two functions, so all sixteen size-12 envelopes are distinct, incomparable, and exhaust the maximal satisfying teams. Failure is hitting all sixteen complement rectangles. I independently maintained the antichain of minimal hitting sets while adding each edge: retain current members hitting the new edge, extend each missing member by every element of the edge, then delete supersets. This step is exact because every new transversal contains a previous minimal one. It returned 132 members with histogram 4:12, 5:16, 6:96, 8:8. Inclusion-exclusion over rectangle avoidance independently yielded 33,159 violating teams, hence 32,377 satisfying. All 32 symmetry actions were used; the fixed-point sum was 288, and the independently chosen minimum orbit masks and sizes matched every frozen table row. The eight-set witness is one of these irredundant blockers and therefore precludes any smaller uniform bound.

## originality

PASS

The surviving contribution is the exact labeled Boolean census and the finer obstruction spectrum and orbits for the specified team symmetry, not 2-SAT representability or the sharp eight-row cutoff on its own. In particular, the upper cutoff and attainability already follow from older theorems on minimally unsatisfiable 2-CNF through the four function-bit clause reduction. Those theorems do not supply the violating or satisfying census or the exact restricted subgroup profile without additional finite classification and counting.

## value

PASS

The full Boolean cube is the canonical smallest propositional universe of the disjoint two-atom formula singled out in the coherence literature. Its minimal failures give precisely the forbidden basis, not only an instance test or a witness at the maximal size. The exact size distribution and natural equivalence classes provide a benchmark for comparing disjoint-attribute splits and their finite-size thresholds; the labeled satisfying count also measures the extent of overlap of the maximal teams. This value does not depend on crediting the already implied eight-row bound as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
