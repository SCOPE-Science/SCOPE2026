---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For any finite nonempty labeled open unit-interval family of ply <=2, if left endpoints a_i are sorted, an overlap of indices i<j with j>=i+2 implies simultaneous coverage by interval i+1, violating ply two. The overlap graph is thus disjoint consecutive paths; nonneighbor disjointness forces their sorted order. Two adjacent inversions would invert nonneighbors, so realizable permutations are exactly products of disjoint adjacent swaps. Conversely the point choice p_{pi(t)}=max_{u<=t}a_{pi(u)}+t epsilon realizes every permutation respecting disjoint interval order. For a path, W_1=1, W_m=W_(m-1) m (m-1) contains all matching-swap permutations, while any common word either uses >=2 copies of m or a unique final-ish m with both universal prefix and a required later m-1, forcing length >=2m-1. Projection onto components proves OPT=2n-c and Fibonacci matching counts. Independently enumerated path targets and BFS minima for n=1..5: (1,3,5,7,9); correct n=1 and coincident-pair boundary. The finite BFS alone does not prove the general lemma.

## originality

PASS

Best-of-knowledge PASS: Löffler and Raichel 2026 prove a generic smooth sorting-supersequence upper bound 4 Delta n for unit intervals, which gives <=8n at ply two but not the exact instance-dependent 2n-c minimum or Fibonacci enumeration. Their 2025 convex-hull precursor repeats the generic upper bound. No earlier exact path matching-supersequence profile found in actual Resultary search; this is not proof of absolute historical priority.

## value

PASS

PASS: The minimum-length sequence problem is motivated by uncertain-data sorting, and the exact 2n-c cost and optimal linear-output construction replace a worst-case constant-factor bound with a sharp instance-sensitive theorem. The connected path matching-permutation universal-word lower bound is substantive rather than a name substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
