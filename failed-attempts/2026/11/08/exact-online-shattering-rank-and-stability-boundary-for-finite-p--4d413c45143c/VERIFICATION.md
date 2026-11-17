---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

PASS: For b>=2 full leaf cylinders on [b]^h, a positive leaf query gives exactly h+1 nested ancestors, online rank floor(log2(h+1)); the negative branch contains the full sibling subtree. The induction proves the matching rank except (b,h)=(2,1), with h=0 and empty-hypothesis distinctions explicit. Laminarity bounds VCdim by two; the ultraproduct stability equivalence is Łoś transfer of bounded finite thicket rank and applies only to the incidence formula. Independent minimax checks at (b,h)=(2,1),(2,2),(2,3),(3,1),(3,2) confirmed both with- and without-empty ranks. Mathematical validity survives despite prior priority failure.

## originality

FAIL

Decisive earlier 2026-10-26 full-b-ary tree cone theorem establishes the identical all-b,h numerical online and VC profile for node-query descendant cones. Although the newly submitted class queries leaves only, the earlier proof witnesses can be converted to leaf queries by taking leaf extensions of its separating sibling nodes, with ancestor-chain responses unchanged and sibling recursion preserved. Thus the leaf-only rank is a routine restriction/transfer of the earlier sharp theorem; ultraproduct stability is the standard Los bounded-rank corollary. The syntactic ball/leaf presentation does not provide a surviving substantial new classification.

## value

FAIL

The natural metric-ball learner is mathematically motivated, but the claimed exact b,h profile was already derived for the same full regular tree cone structure in the 2026-10-26 theorem. Converting the explicit lower-bound separating queries to leaves and applying Los are routine consequences; no distinct unknown exact invariant or substantive boundary remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
