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

On a mixed word some zero borders a one, so precisely the two constant words map to all zero, and no word maps to all one. For a checkerboard the two-step local filter is a radius-two de Bruijn edge label; overlapping states on a closed walk identify exactly one cyclic indexed input, with repeated sites forced consistently even at n=2. The seven recurrent states give the four stated classes: each allowed pair of source and destination classes determines the individual destination, making every closed class-walk lift uniquely. All directed simple cycles in K contain the loop vertex: one length-one loop, two 2-cycles, two 3-cycles and one 4-cycle, giving det(I−zK)=1−z−2z²−2z³−z⁴. Its logarithmic derivative gives the numerator z+4z²+6z³+4z⁴, the recurrence and initial terms. Primitivity (irreducibility and a loop) gives one leading eigenvalue, so tr(K^m)~ρ^m. Independent replay: /workspace/branches/c73fdfd5-57cd-47d7-9e0c-e1ef6a594cbd/independent_check.py, recoded window/row/class tests, permutation determinant, traces through m=20, recurrence through m=30, direct indexed exhaustive tests to n=12 (both phases 1,5,13,29,66,155). Finite checks corroborate but do not prove the growth statement.

## originality

PASS

Best-of-knowledge pass for the evaluated two-step checkerboard fiber law on growing indexed even rings, not for general preimage or de Bruijn machinery.

## value

PASS

The checkerboard is the natural nonconstant spatial period-two target (and oscillates under the rule). The law answers how often exactly two updates select a given indexed phase from uniform input at increasing size; stating a generic de Bruijn method does not give that probability or the unexpectedly small quartic. No broader maximum-fiber or all-target claim is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
