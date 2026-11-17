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

# Reproducibility and verification

Run `python3 proof/verify_matrix.py` and `python3 proof/verify_direct.py` from the extracted package root, using Python 3 and only the standard library. Corresponding completed program outputs appear at `proof/matrix.out` and `proof/direct.out`.

The matrix program constructs the correct edge-deleted adjacency for every \(3\le n\le18\); it checks \(608\) time-indexed nullities by exact arithmetic modulo three and verifies the first identity power equals the predicted sharp order. The independent direct update implementation iterates all \(3^{2n}\) states for \(n=3,4,5\), exactly \(66{,}339\) labelled states. The period counts match the analytical formulas and sum to the complete state space.

The proof is unrestricted in \(n\) and applies to every \(\mathbb F_{3^f}\). Finite replays are corroboration, not a proof for arbitrarily large graphs, fields, or times. No independent external mathematical audit has been performed.
