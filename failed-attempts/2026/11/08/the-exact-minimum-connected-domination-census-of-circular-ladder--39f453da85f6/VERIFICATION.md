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

RESULT.md:27–38 gives a valid exhaustive argument. Connectivity makes occupied columns a cyclic interval when a column is empty; domination forbids three consecutive empties. One empty requires a double (otherwise all chosen vertices lie in one row), and two empties force the two distinct boundary columns to be double for n >= 4. Equality in |S| = n + d - z therefore forces d = z. The one-double case has two compatible row assignments for each empty/double position pair; the two-double case has two assignments if there is an interior singleton and only one for n = 4. A consecutive pair of doubles creates a square only in that latter case. With an occupied path and no consecutive doubles there is one horizontal selected edge at each occupied boundary, so the connected subgraph is a tree. The triangular prism has exactly the three dominating rung edges. An independently written subset enumeration (increasing cardinality, separate coverage and induced flood fill, counting doubles and induced edges) matched every profile and type at n = 3 through 10, including (3 edges), (24 trees, 6 cycles), and (50 trees, 2 cycles) at n = 3, 4, 5. Replay: /workspace/branches/6e151c80-74ef-4b91-a8a2-65276da55577/independent_prism_enum.py and finite_replay_3_10.txt in that directory. The frozen verifier and its recorded output were inspected, not used as the independent replay. The uniform conclusion rests on the equality-case proof, not finite tests.

## originality

FAIL

Material prior coverage of the principal uniform census is established: the distinct Nov. 2 Resultary record explicitly describes all labeled optimizers in three families and gives 2n²+2 for the same C_n × K_2 problem at n >= 6. A complete explicit minimum-set family already encodes the two statistics by evaluating the selected columns and induced edges; packaging it as a generating polynomial does not create a distinct uniform optimizer classification. The available summary does not establish that the older record prints those refined formulas or includes n = 3, 4, 5. This failure is for the submitted combined finding's material overlap, not a finding that every displayed refinement or small case was published verbatim, and not a consequence of an unavailable full text.

## value

FAIL

The exact optimizer family is a worthwhile invariant, but substantially covered on the uniform range. Counting double columns and detecting the induced cycle of an explicitly specified family are local readings of that family. The remaining n = 3, 4, 5 computations close small boundaries (including the square at n = 4), but no separate use or substantive unresolved gap is established for these cases as a standalone finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
