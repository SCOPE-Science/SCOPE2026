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

If two deleted matched pairs were wholly omitted, their same-side vertices would have identical signatures. Hence at least n−1 pair indices are represented, and equality in size forces a one-hole transversal with omitted index h. If exactly one A vertex a_i is selected, its signature equals that of a_i b_h; if exactly two A vertices a_i,a_j are selected, it equals that of a_i b_j. Symmetrically any nonempty side must have size at least three. For a balanced transversal, covered indices of the oriented edge a_i b_j are decoded by its 0 or 2 entries (the shore determines the orientation), with a missing exceptional coordinate indicating h. This distinguishes all edges. Selected vertices have a zero and at least two twos on their own side, while an edge with that zero has at most one two on that side. Unselected vertices with a selected mate have a unique three, and the two omitted vertices have twos on opposite landmark sides, at least three twos each, unlike an edge. The same decoding for a one-sided transversal works when its sole side has at least three, since even an edge through h has a non-one entry; the omitted vertices are then all-ones and all-twos. Such a one-sided transversal cannot dominate its omitted vertex on the selected side. Balanced ones dominate, with a split possible iff n>=7. For n=3..6 a full side gives a size-n witness by the signature rules, including one distinct three per vertex on the opposite side. The stable count is n times the number of orientations of n−1 indices excluding assignments with 0, 1 or 2 on either side, giving n(2^(n−1)−n²+n−2).

## originality

FAIL

A distinct published Resultary record, 8416a7acedbc, gives exactly the same optimum values and stable minimizing families for doubly resolving sets of the same crown graphs. This is verified coverage by implication, not just a numerical match or same-day priority assertion: every mixed resolving dominating set in a crown graph is doubly resolving, and all of that record's stable optimal doubly resolving bases are mixed resolving and dominating. For n=3..6 the full-shore witness supplies the upper bound matching the same record's lower bound. The related edge-only crown bases result supplies the edge separation directly, leaving only elementary vertex-edge signature checks to transfer the stable family.

## value

FAIL

The crown family and phase transition would be useful in isolation, but the frozen transition, stable optimum sets and count are mechanically recovered from the indexed doubly resolving result with the adjacent-pair reduction and the already classified edge-basis family. No independent new exact invariant or transition-case enumeration remains in the frozen claim. This does not dispute its mathematical correctness or the usefulness of studying the relation between the predicates more generally.

The dated certificate retains the supplied scientific assessment, sources and limitations.
