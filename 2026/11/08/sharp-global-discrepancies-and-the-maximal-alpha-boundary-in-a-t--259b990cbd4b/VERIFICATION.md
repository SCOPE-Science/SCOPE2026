---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For the face fan of Wu's coordinate box slice Q in the zero-sum lattice, the globally defined toric discrepancy is its gauge h(d)=max(max_i d_i/B,-min_i d_i/A). A nonzero integer zero-sum point has a positive integer coordinate at least 1, so h>=1/B, and primitive (1,-1,0,..) attains equality since A>=B. Hence global mld=1/B (centers anywhere, not pointwise local mld). The lattice interior criterion yields canonical iff B=1. When B=1, the same witness is a nonvertex boundary point except at n=2,A=1; there the only integral hexagon points are origin and six vertices, giving terminal iff (2,1,1). A=B+1 is coprime and valid for all n>=2, yielding alpha->1/2 and mld->0. Read actual RESULTS and discrepancy_verify.py; independently enumerated representative n,A,B lattice sections using rational gauge, not a proof of all n.

## originality

PASS

Best-of-knowledge matching theorem search found no logically dominating already published result after comparing actual statements; relevant uninspected primary literature and older methods are recorded as residual risks.

## value

PASS

A natural recently constructed K-polystable toric Fano realization family has a surprising exact global singularity invariant, an all-dimensional canonical/terminal phase classification, and an explicit sharp alpha-versus-mld failure of uniform control near the maximal endpoint. Although toric gauge and lattice criteria are standard, their combined evaluated family consequence addresses a motivated invariant and supplies more than simply renaming a standard condition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
