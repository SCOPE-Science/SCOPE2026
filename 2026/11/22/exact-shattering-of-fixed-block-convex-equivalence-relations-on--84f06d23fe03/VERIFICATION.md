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

Cut sets of size c=b−1 encode the partitions bijectively; answer zero is interval intersection. The single-negative, all-negative and all-positive traces force private sites, tau≤c and at least c outside sites, respectively. With private sites, intervals have no containment and their left and right endpoint orders agree; at a triple common point the middle interval is covered by the outer two, a contradiction. Consequently when piercing the intended negatives, a site hitting an unwanted interval can hit only one intended interval and can be moved to its private site. At most c sites suffice before exact padding outside the whole support. For s intervals, private sites are distinct, and an all-negative witness needs at least max(0,s−c) distinct shared sites, disjoint from private sites. Thus s≤2c, s≤m−c and m≥c+s+max(0,s−c)≥2s. Singletons attain the bound for s≤c; otherwise s−c disjoint overlapping pairs and 2c−s singleton gadgets occupy 2s−c sites with one piercer per active gadget. Empty supports and c=0,m are covered. My bounded replay, `/tmp/opencode/frozen-review-repro.py intervals`, computed piercing directly from cut-set traces instead of using greedy piercing and checked 202,013 support/quota pairs for m=0,…,5. Source checker and its recorded output were inspected, not executed; the universal conclusion follows from the argument, not replay.

## originality

PASS

The private-site obstruction and cut encoding are prior. The distinct result is simultaneous sufficiency on one exact-cardinality layer and the attendant sharp all-parameter VC law; none of the inspected formulations supplies that result.

## value

PASS

A fixed number of blocks is a natural constraint in ordered segmentation. The result gives a decision criterion for each support and a nonmonotone sharp VC formula, including the distinct obstructions at small and large cut quotas. It is more informative than the private-site condition for variable block counts. No counting polynomial or online dimension is evaluated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
