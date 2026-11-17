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

PASS: For Laplacian L(K_m square K_n), the PBH decomposition into constants, row contrasts, column contrasts and zero-row/column-sum arrays is exact. The top eigenspace kernel supported on unselected bipartite edges is precisely the cycle-space kernel, so the unselected set must be a forest. At m=n the two middle spaces merge and selected-edge components introduce exactly two independent row/column component-size equations. The n>=3 minimum-square forbidden spanning-tree families are double-stars (n²) and a selected isolated edge in complement (n²(n−1)²), giving n^(2n−2)-n²((n−1)²+1). Independently enumerated every minimum-size n=2,3,4 square board placement using graph components and verified counts 4,36,3936. All-size reasoning follows PBH and tree counting, not finite tests.

## originality

FAIL

FAIL: Resultary 2026-10-18 already proves the complete all-selected-set weighted rook-graph forest/component-imbalance iff criterion at ap=bq, whose unit a=b=1 specialization is the identical all-set theorem here. Resultary 2026-11-02 proves the exact unit-weight minimum placements, the SAME two disallowed tree families and the identical square count for every n>=3; n=2 follows from the October criterion. The original is wholly implied by two strictly earlier fully read publications.

## value

FAIL

FAIL: The canonical rook-board actuator budget/count and component test are mathematically useful, but these exact answers are already available from the October weighted theorem plus November 2 all-minimum-set theorem. Restating their unit-weight specialization and n=2 direct boundary gives no motivated independent new mathematical fact. This is coverage, not computational inaccuracy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
