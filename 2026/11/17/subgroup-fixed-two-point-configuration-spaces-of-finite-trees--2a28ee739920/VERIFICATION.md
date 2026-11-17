---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The program `verify_tree_fixed.py` enumerates the six nonisomorphic trees on six vertices, their graph automorphisms and 194 generated subgroup actions. It subdivides each edge once to sample its endpoints and midpoint. For each subgroup it enumerates all invariant unordered distinct sample-vertex pairs and computes the action on their two points. It independently constructs fixed subsets of sample vertices for each occurring index-two kernel and verifies that every nontrivial pair is obtained from exactly one exchanged orbit of complementary subtrees, and that the remaining pairs are precisely unordered pairs of globally fixed sample points. The observed output is included verbatim in `verify_tree_fixed_output.txt`.

The finite calculation examines 2,014 invariant sampled pairs (213 with nontrivial swap). It does not verify arbitrary points in an edge or the full homotopy classification; the proof uses convexity, unique arc midpoints, and the cited ordinary two-particle tree theorem. The program is not a proof of the infinite statement, and no external audit has been performed.
