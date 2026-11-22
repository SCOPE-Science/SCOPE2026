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

## Reproducible checks

Run `python3 verify_exhaustive.py` and `python3 verify_token_model.py` with Python 3 and no third-party dependencies. The first script exhaustively enumerates actual deleted position sets and their residual fibers. The second reconstructs fibers from nonempty block tokens and the number of ways to reinsert a fully deleted `01` block. The recorded outputs are `verify_exhaustive.out` and `verify_token_model.out`.

The direct enumeration passed 447 parameter triples and 7,181 actual embeddings through host size 9. The independent token-model comparison passed 286 parameter triples through host size 11, comparing complete dictionaries of outputs and their multiplicities rather than only totals. Boundary cases with no matching subsequence are included in the direct enumeration. The mathematical proof covers all positive parameters with pattern length at least three; bounded verification is not an exhaustive check of infinitely many cases.
