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

For r=m-k, any nonempty base clique needs at least r selections, since its selected vertices see every omission in the clique. In a block of m cliques, an empty clique a forces the selection of each bridge endpoint pba for b≠a: pab has unequal last two symbols and its only external neighbor is pba. Each forced endpoint spends one unit of the k budget on the bridge, so each other clique has at least r+1 selections. This gives a block bound mr+k−1 in the empty case and mr otherwise. Hence at equality for k≥2 no clique is empty and all have cardinality r. The upper bound uses r residues invariant under negation: the last-pair difference either changes sign across a last-coordinate-pair bridge or is zero at both endpoints of an earlier bridge. Thus selected vertices see exactly k omissions, all within their clique. The one-coordinate case is K_m; m=2 and k=1 are included without requiring strict block excess. In VERIFICATION.md line 19, ‘exactly k−1’ means the excess in the lower bound, not the realized excess for an arbitrary set. Independently generated graphs recursively and exhaustively checked minima on six small graphs and balance of all relevant minima using `python3 /workspace/independent_checks.py`. The proof, not that finite sample, covers all n,m,k.

## originality

FAIL

The distinct Resultary record indexed under October 12 states and proves exactly the same formula on exactly the same graph family and parameter range. Its block lower bound already yields the claimed base-clique balance by the equality case. This is demonstrated coverage, not an inference of authorship or publication priority from path dates.

## value

FAIL

The full conjecture is a worthwhile mathematical question, but the exact solution and the bound driving this proof are already in the matching record. The residue choice is a realization of the same symmetric last-pair construction, and the balance clause just notes equality in the same block bound. The frozen record does not give a new classification, enumeration, or otherwise independently useful remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
