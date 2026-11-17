---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For dyadic three-sets pairwise differences have valuations a,a,b (a<b); character annihilation gives exact rank thresholds a+c>=k (rank1), else b+c>=k or a+d>=k (rank2). Unique-close-pair count M_(a,b)=2^(3k-a-b-3), and finite geometric sums give displayed polynomial counts. Independent integer evaluation of rank-partition sums exactly reproduced displayed rank-one and rank-two polynomials for k=3..7; not an all-k substitute.

## originality

FAIL

Decisive prior coverage: published 2026-11-08 Valuation-stratified rank census for three-point Fourier sampling on prime-power cycles handles every prime p and k, gives identical min/max-valuation rank test and complete stratum counts A_(t,u), H1,H2,H3. Specializing p=2 gives M_(a,b) and exactly the submitted dyadic rank distribution, asymptotic 6/(2*2^k)=3/2^k. It even explicitly credits earlier dyadic results. Algebraically expanded dyadic polynomials are consequences of that stronger theorem; no novelty remains in the complete claim.

## value

FAIL

The full dyadic result is a direct specialization and summation of already published all-prime-power rank enumeration, so the submitted invariant and asymptotic are known-table recomputation rather than an independent new useful fact. Correctness and finite checks do not rescue scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
