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

Exact rational verification: execute `python3 check.py` in the same directory. The program reconstructs affine maps from the one-sided endpoint-value table rather than reading a stored transition matrix. It checks all \(2044\) orientation words with \(3\le n\le11\) and coincident last two signs, the stationary density and projected transition probabilities, \(16352\) exact covariance identities, and five numerical large-alphabet entropy cases. A successful run prints `VERIFY_OK` with counts.

Logical scope: finite checks are supporting tests only. The all-size theorem depends on the branch image combinatorics, exact invariant-density calculation, finite Markov-chain theory, and uniform Taylor expansion in `RESULT.md`. Proofs of primitive mixing and the entropy comparison apply to all admitted words. No independent mathematical audit or external verification was performed.
