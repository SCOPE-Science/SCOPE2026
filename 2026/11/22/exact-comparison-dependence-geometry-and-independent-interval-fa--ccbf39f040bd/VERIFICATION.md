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

The proof is analytic and applies to all integers \(n\ge2\). The exact-rational program `verify.py` enumerates every priority permutation of sizes two through eight and checks the per-pair probabilities, covariance entries, and nontrivial zero-covariance characterization. It also enumerates all admissible nondegenerate strict-laminar triples at those sizes, checking exact product probabilities. When run, the program reports 935 assertions and 11 triple tests. These finite computations check the stated formulas in bounded cases; they are not an exhaustive proof over unbounded \(n\), which is supplied in `RESULT.md`.

No separate, independent mathematical audit has been conducted. Historical priority may require additional verification against equivalent treap or random search-tree formulations.
