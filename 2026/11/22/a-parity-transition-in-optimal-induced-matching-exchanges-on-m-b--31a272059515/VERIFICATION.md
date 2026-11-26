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

Independent reconstruction: adjacent start columns always conflict, so the start support bounds the cardinality by floor(n/2), attained by alternating rungs. In a locally untwisted three-column window a gap of two allows R→R, R→H, and opposite-rail H→H, but not H→R; a gap of at least three gives no conflict in that direction. For n=4 test the two directions of the same pair, rather than discarding one. An even optimum uses an alternating support; the all-horizontal phase must alternate, and the single seam reversal closes it exactly for an odd number of selected edges. Distinct even supports or rail phases cannot differ by just one edge. Odd supports have one long gap and an R-prefix/H-suffix; one initial rail bit fixes a nonempty H-suffix, giving n choices per support. Changing the first H to a rung stays feasible, and all-rung supports are joined by the shift of two. For degree, deletion of an interior start merges two gaps of two, allowing only reinsertion at that start. Deletion next to the long gap merges gaps two and three, allowing exactly one genuinely new start on that side; the n=5 case has one surviving start and the same two insertions into its cyclic gap of five. Applying the transition rules gives unchanged-support counts 2,3,2,1 and changed-support counts 4,2,2,3 for h=0, h=1, 2≤h<m, h=m. Summing yields precisely the stated polynomial and edge count. The size, connectivity, and degree arguments respect the seam without defining a global untwisted rail.

## originality

PASS

Bounded evidence supports the whole-edge optimum-exchange dichotomy and exact odd degree classification as distinct from known move rules, matching-complex invariants, and ordinary matching enumeration. Priority for the scalar size and enumeration alone is not established.

## value

PASS

On a canonical twisted cubic family the exact optimum move structure changes from complete immobility to connectivity, with the full one-step branching profile. This is information not contained in an optimal size or configuration count and is useful when comparing whole-edge move rules on ladder graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
