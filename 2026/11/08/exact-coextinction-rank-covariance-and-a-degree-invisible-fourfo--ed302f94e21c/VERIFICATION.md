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

# Reproducible finite checks

The standalone artifact `verify.py` uses Python 3 and only the standard library. Run `python3 verify.py` from the directory containing this file and the verifier. It enumerates all \(n!\) primary extinction orders for all feasible degree, overlap and size combinations at \(1\le n\le7\), and performs exact rational comparisons to the proposed closed formula. It also exhaustively enumerates all 24 primary removal orders for the two four-primary bipartite examples, computes their exact distributions, and verifies their exact mean and variance.

Expected output: `PASS 707 exact rational checks; two bipartite networks E[R]=2/3; Var 1/1800 versus 1/450`.

The exact computations check finite instances, not every network size. Universal correctness relies on the self-contained probabilistic proof in `RESULT.md`; literature originality is provisional pending external examination. Independent audit has not been performed.
