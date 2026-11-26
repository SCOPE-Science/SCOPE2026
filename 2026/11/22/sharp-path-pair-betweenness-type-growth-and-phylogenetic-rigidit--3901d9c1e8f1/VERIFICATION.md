---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For a vertex in the minimal marked hull, the signature is the complete multipartite graph whose parts are the marked sets in the deletion components, together with the singleton of the vertex if marked. Distinct nonleaf essential vertices x,y are distinguished by choosing two parts at x other than the part facing y. An interior compressed-edge vertex realizes a split; different compressed edges have different splits because the intervening region contains a mark or has a branch leading to one. Only pendant splits coincide with marked-leaf stars. Every vertex outside the hull contributes the same empty signature. Thus q=m+b+s+epsilon. If l is the number of hull leaves, b≤l−2 by degree sum and s≤m+b−1−l, giving q≤min(n,3m−4), with equality at the second bound forcing all marks to be leaves, trivalency, every internal edge subdivided, and a vertex beyond the hull. All-marked paths, contraction of internal edges of a binary marked-leaf skeleton, internal subdivision, then attachment outside the hull give all orders; for m=2 there is just the marked-path type and possibly the empty type, and for m=1 all traces are empty. Maximal families expose all the edge splits, and these recover the reduced tree (equivalently, their separating counts recover pairwise leaf distances in the reduced unit-edge tree). Inserting the next named leaf in an edge is uniquely reversible, yielding (2m−5)!!. Independent replay in branches/080ee1f0-6235-4b3f-bec2-0d14e7da863a/independent_check.py compared 56,515 labelled-tree/marked-set cases through n=6 and obtained 1,3,15,105 maximal families for m=3–6. These are checks of the proof, not the basis of the universal claim.

## originality

PASS

Pass for the inclusive marked-pair trace formula, sharp host-order bound and characterization of when the family realizes every reduced edge split, not for classical split reconstruction or binary-tree enumeration in isolation. Inspected related results use a different relation, different parameters, or only reconstruct from assumed split data. No exact covering statement or immediate implication for the supported claim was found in the sources assessed.

## value

PASS

The local formula measures exactly how much the host tree can be distinguished by the naturally specified path queries. It handles internal marks and explains separately which subdivisions contribute information and why arbitrary extra exterior vertices do not. The sharp all-order bound and conversion of saturation into the recovery of a named-leaf tree are useful beyond a finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
