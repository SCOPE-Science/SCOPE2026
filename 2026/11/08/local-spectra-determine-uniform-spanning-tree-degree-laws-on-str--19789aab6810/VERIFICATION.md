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

# Verification record

Run `python3 verify.py` with Python 3 and no third-party dependencies. The checker reconstructs the graphs directly from their defining edges, verifies all 16×15 common-neighbor counts for each, computes their local adjacency characteristic polynomials, and uses fraction-free integer determinants of weighted Laplacian cofactors to evaluate the rooted spanning-tree generating functions independently of the spectral proof. Seven distinct integer weights determine each degree-at-most-six polynomial, making the finite-polynomial check exhaustive. It also checks the Petersen graph, the polynomial difference and its first three factorial-moment consequences. Actual output: `VERIFY_OK 551 exact assertions`.

The general strongly regular graph statement is proved symbolically in `RESULT.md`; the finite checker is corroboration, not a substitute for that proof. Historical novelty cannot be certified solely by unsuccessful searches, and one older general degree-distribution paper was not available in full text. No independent mathematical audit has been performed.
