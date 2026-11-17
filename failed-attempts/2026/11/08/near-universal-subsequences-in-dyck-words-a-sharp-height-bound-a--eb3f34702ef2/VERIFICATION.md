---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The actual RESULT.md uses the binary arch/maximum disjoint unlike-neighbor matching correspondence. Any matching of k adjacent unlike pairs leaves n-k unmatched openings and closings; at a prefix at most one matched edge crosses, hence H<=n-k+1. The explicit 0^h1^h(01)^(n-h) attains the bound. Unique perfect matching gives D[n,n]=1; height<=2 and its 0B1...B(n-1)1 factorization gives D[n,n-1]=2^(n-1)-1. The three-state arch-state matrices A,B and recursive Dyck-height transfer M_j=(I-x A M_(j-1) B)^(-1), j<=3, give [t^2]G3=z^3(1-z)/(1-2z)^3 and the all-n third coefficient (n-2)(n+1)2^(n-5). Independently enumerated all Catalan words through n=9 and checked actual matching index, height, and counts; this diagnostic is finite, formal transfer supplies the infinite proof.

## originality

FAIL

Exact third-layer series and formula and every preceding height/near-universality statement are covered by earlier complete, explicitly read results: the November 2 rational arch-deficit theorem gives G_2(z)=z^3(1-z)/(1-2z)^3, the identical coefficient, and a stronger rational transfer formula for every fixed defect; the October 25 height-three Dyck universality-index law contains the identical bivariate rational F3. An earlier October 26 theorem covers the sharp height tradeoff and top layers. The peak enumerator is classical and explicitly disclaimed as novel in the submission.

## value

FAIL

Although the all-length third-layer census is naturally motivated, its exact sequence, height argument and finite-transfer method are already published in the stronger prior fixed-defect classification. The residual peak refinement is classical and the two upper layers are also covered; no distinct correct original valuable theorem survives unchanged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
