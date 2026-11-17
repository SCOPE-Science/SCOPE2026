---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

One-grain overwrite can flip only position j>=1 to its previous bit. For each weight-two support {a,b}, singleton descendants are ∅ for {0,1}, {0} for a=0,b>=2, {b} for a>=1,b=a+1, and {a,b} for a>=1,b>=a+2. Disjoint singleton descendants force at most n codewords, and extremality forces {0,1}, then either all adjacent pairs plus {0,r} with r>=3, or replacement of one adjacent {j−1,j} by {1,j} for j>=4. Pairwise weight-three outputs of these codes are separated by consecutive/nonconsecutive support types. For n>=4 exactly (n−3)² codebooks; n2=1,n3=2. Direct independently constructed collision graphs confirmed optima and full extremizer equality n=2..8.

## originality

PASS

PASS best of knowledge. Gabrys–Yaakobi–Dolecek 2013 defines the same one-grain overwrite channel and proves unrestricted coding bounds, while Kashyap–Zémor gives unrestricted upper bounds; neither inspected statement classifies the all-length Hamming-weight-two optimal codebooks. Prior finite unrestricted n=6 codebook census concerns a different feasible universe. Risk: unindexed constant-weight variants.

## value

PASS

The two-one sparse-weight layer is a canonical coding restriction for grain-overwrite media; sharp cardinality and classification of every extremal codebook for all lengths answer a natural exact combinatorial capacity problem. The full (n−3)² indexed multiplicity is structural, not a table or arbitrary small calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
