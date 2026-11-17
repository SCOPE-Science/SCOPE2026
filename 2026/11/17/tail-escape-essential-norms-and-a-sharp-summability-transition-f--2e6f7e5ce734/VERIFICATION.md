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

# Verification

The proof is based on the explicit weighted difference isometry, exact finite row norms, two finite-rank truncations, and disjoint-support weakly null vectors in the nonseparable \(\ell_\infty\) coordinate space. The full compact-operator lower bound therefore does not rely on the false premise that bounded pointwise-null sequences in \(\ell_\infty\) are always weakly null.

The standalone `check_big_tree_multipliers.py` has been executed from this package directory. It compares 90 exact-rational finite tree/symbol profiles with unrestricted sign maximization (510 edge-row profiles), verifies every computed finite-section identity, checks the harmonic critical-symbol equality at 250 levels for the boundary powers, and obtains explicit diminishing tails for the summable square-weight example.

Expected final output is `BIG_WEIGHTED_TREE_MULTIPLIER_CHECKS_PASS`. Finite tests do not establish the infinite compactness theorem; that assertion is proved in `RESULT.md`. No independent audit or third-party mathematical certification was performed.
