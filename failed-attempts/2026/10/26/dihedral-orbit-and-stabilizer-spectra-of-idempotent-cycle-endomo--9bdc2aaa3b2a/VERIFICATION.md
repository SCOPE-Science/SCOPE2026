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

An idempotent fixes its image pointwise, and adjacency and connectedness force a proper image to be a cyclic arc with at least two vertices. On its complementary path the map is precisely a length L=n-k+1 walk between the opposite endpoints of the image path. Parity excludes odd n, length excludes k>n/2+1, and a geodesic with two-edge backtracks realizes every allowed rank. Counting the n choices of arc gives nW. The arc stabilizer has order two by transitivity on the n arcs; the reflection i↦k-1-i on the standard arc acts by reversing and complementing the walk. Its fixed walks are uniquely determined by the first half, with the indicated central vertex for even L or central directed edge for odd L. The two middle-vertex possibilities in the latter formula suffice because their complements differ by one. Singleton and paired walk orbits lift to size n and 2n respectively; the full-image idempotent is the fixed identity. The independent enumeration from adjacent signed steps and direct conjugation by all x↦±x+a agreed with the complete formulas for 3<=n<=14, including 3,176 idempotents total; the proof, not the replay, addresses all n.

## originality

FAIL

The distinct indexed finding 2026/11/22/SCOPE-unit-conjugacy-orbit-sizes-of-idempotent-cycle-graph-endomorphis--4f6d49d71533 demonstrably contains essentially the entire audited classification, not merely similar ranks or raw counts: its W and F equivalents and the resulting orbit and stabilizer profiles are identical for all n>=4, and it adds asymptotics. The n=3 endpoint adds only the identity for the complete graph K_3, where strict maps are necessarily permutations. There is no substantive distinct remainder to pass. This is a finding of equivalent existing catalogue coverage at review, not a determination that the listed November record predates the October frozen source, nor an inference about authorship or derivation from catalogue dates.

## value

PASS

As a mathematical classification the rank-refined orbit/stabilizer invariant is natural: labeled counts, monoid equivalence classes, and unlabeled retractions modulo cycle symmetry answer different questions. The explicit reflection criterion and counts resolve which retractions have symmetry and how many genuinely different patterns remain. This credits the value of the classification itself, not an additional contribution beyond the matched catalogue theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
