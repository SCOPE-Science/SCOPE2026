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

With both sides of size at least three, two same-side vertices lose at most two common neighbors, so equality or a shared neighbor defines the side relation in three variables. Cross-side nonadjacency then defines exactly the deleted matching. Scoped rebinding inside the unary and binary tests genuinely allows k simultaneous witnesses with only k names for k>=3. The two separately scoped one-side tests detect the smaller clipped unmatched count, not just the larger. Conversely, after removing the moved pebble at most k−1 matching indices or unmatched vertices on a side can be in use; maintaining a partial injection on matching indices as well as on unmatched vertices preserves all atomic relations in either direction. At width two the three possible pair types can always be matched, and width one is immediate. The disjoint profile counts sum to the stated cubic, and the clipped parameters attain the componentwise least admissible sizes. Minimum-order uniqueness is in the k>=3 classification, not at widths one and two. The strictness witnesses work, including the transition from two to three. Inspected the frozen refinement and structure programs and their recorded outputs (not rerun): they cover 50 graphs at widths 2 and 3, a 13-graph width-4 sample and finite structural/profile ranges; the proof, not these checks, gives unrestricted depth and graph order.

## originality

PASS

The t=0 branch overlaps a distinct same-date indexed result by setting the number of homogeneous biclique components to one; no priority is inferred and no originality credit rests on that branch. The supported distinction is the sharp positive-deletion classification, including simultaneous truncation of the match class and both unmatched populations, and the resulting complete spectrum. The closest inspected general framework and object-specific papers do not cover that classification.

## value

PASS

This is a complete sharp variable-width classification on a natural near-complete family, not a finite census or a single width test. The positive-deletion result gives exact indistinguishability witnesses, minimal models, and an explicit count of theories despite unbounded quantifier depth. Reconstructing the latent sides and mates with reusable variables and proving sharp sufficiency contribute beyond the already available complete-biclique subcase.

The dated certificate retains the supplied scientific assessment, sources and limitations.
