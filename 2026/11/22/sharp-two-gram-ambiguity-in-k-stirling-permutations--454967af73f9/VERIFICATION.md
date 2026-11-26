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

For the stated linear directed counts and fixed k copies, the largest label is contiguous; its observed neighbors uniquely determine the deletion update. Fixed row and column deficits recover the endpoints, so every reduced realization admits exactly one compatible endpoint insertion or exactly the reduced count of the specified internal pair. Insertion and deletion are inverse, also when the neighbors coincide. The realizability procedure inverts every accepted chain, and rejects a negative count, invalid largest-label pattern, or mismatched boundary. If an oriented pair ab with a!=b occurred twice, some smaller letter would lie between copies of a larger letter. A self-pair count is k minus the number of its homogeneous runs. Accordingly every branching factor is <=k-1. In the nontrivial k>=3 equality case, all stages split a fully contiguous block; induction forces the immediately previous largest label to be the only such block and hence fixes the entire maximizing profile. For k=2 all factors equal one. A first split of any block when k>=3 already gives k-1 choices; conversely all-block words give singleton fibers, with n! orders. This covers n=1 as the empty product. The cardinality product, Gamma identity and fixed-k asymptotic give the stated probability. As a cross-check the branching product for any attainable profile reduces to the product over labels of (k-1)!/m_aa!, since a loop branch consumes exactly one loop of its host and only those branches change old loop counts. Independent small multiset-word enumeration rejecting forbidden interlacings directly (not by generating via the supplied insertion routine) verifies that product and the extremal counts, replay: python3 /workspace/review_checks/stirling.py. Finite cases are supplemental; the universal assertions follow from deletion and induction.

## originality

PASS

Best current evidence supports the higher-multiplicity restricted-fiber calculation, unique extremal spectrum and singleton law. Largest-label insertion, ordinary two-Abelian factor counting, the total source count and k=2 rigidity are established ingredients or exact overlaps and are not treated as novel.

## value

PASS

The complete labeled directed observation defines a natural lossless/ambiguous reconstruction problem on an established nested language. An all-profile exact decoder and fiber product, a unique worst spectrum achieving exponential ambiguity, and an attained classification and probability of exact recovery supply a reusable inverse result rather than isolated collisions or routine recounting of the language.

The dated certificate retains the supplied scientific assessment, sources and limitations.
