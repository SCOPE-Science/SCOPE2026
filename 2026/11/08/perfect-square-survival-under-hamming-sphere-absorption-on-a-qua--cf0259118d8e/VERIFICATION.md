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

The algebraic dark-subspace proof in `RESULT.md` establishes every dimension and every positive rate choice. Numerical checks are finite consistency tests and cannot replace this proof.

Run `python verify_fourier.py` and `python verify_dynamics.py` with NumPy and SciPy installed. The first program uses all Walsh eigenspaces and directly computes the nullspaces of their restrictions to the entire detector shell (35 cases through dimension eight). It separately tests the exact second-shell integer-root condition through dimension 499. The second program uses an independently constructed full graph adjacency matrix, 15 nonuniform-rate choices on dimensions two through six, explicit matrix exponentials at two times, and comparison to the predicted survival limit. The checks executed successfully on the packaged scripts.

The long-time numerical output is not certified error-bounded and is not used as an infinite-time proof. It tests only finite dimensions and finitely many unequal loss assignments. The all-dimension and arbitrary-rate assertions instead follow from the contraction semigroup, permutation-invariance, Walsh decomposition and exact degree-two Krawtchouk polynomial identities.
