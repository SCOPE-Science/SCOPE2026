---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The included `verify_consensus.py` was run with CPython using only the standard library. All assertions passed: 14,940 exact labeled-state survival checks for every mixed binary state, \(4\le n\le9\), three near-complete group sizes and five event steps; 1,575 separately programmed hypergeometric count-chain checks for \(4\le n\le13\), together with exact expected hitting times obtained by rational Gaussian elimination; and a three-step counterexample check at \((n,k,x)=(6,3,1)\).

The labeled checker enumerates each selected subset and each potential speaker and does not use the asserted occupancy transition matrices. The count checker instead uses a separate hypergeometric kernel. Both operate with rational arithmetic and are reproducible without external data. The general theorem rests on the algebraic argument in RESULT.md; finite enumeration alone would not establish it for unbounded \(n\). The source literature comparison remains subject to unindexed priority risk, and an independent audit has not been performed.
