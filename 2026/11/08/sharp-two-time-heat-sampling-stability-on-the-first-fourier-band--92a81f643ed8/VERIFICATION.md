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

Real Fourier cosine/sine normalization yields a 4×3 analysis matrix whose normalized Gram blocks as scalar η and a 2×2 positive matrix with trace T=4+2(1+q²)(1+c), determinant 4(1−q)²(1+c). Thus positive eigenvalues iff −1<c<1. η decreases strictly, μ− increases strictly on [−1,1], giving a single crossing; the crossing quadratic has exactly one positive root cstar∈(1/2,1). Its Taylor expansion gives 1−cstar∼(1−q)²/6; unimodality gives exact two-neighbor finite-grid search. Independent construction of 105 different 4×3 matrices reproduced all three Gram eigenvalues. Finite tests not mistaken for proof across N,t.

## originality

PASS

The explicit q-dependent optimal raw two-time observation spacing and eigenvalue crossing are not implied by the published spectrally demixed frame theorem, and the accessible general graph Paley–Wiener literature does not exhibit this finite-cycle sharp optimizer.

## value

PASS

Sharp stable recovery in a natural three-mode graph signal space, with explicit tradeoff between time separation and spatial sensor placement, provides an exact operational design invariant distinct from frame injectivity or generic placement algorithms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
