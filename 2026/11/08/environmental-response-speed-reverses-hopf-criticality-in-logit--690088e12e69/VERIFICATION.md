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

# Verification procedure and limits

Run `python verify.py` with Python 3.11 or newer and no external dependencies. The script checks exact-rational simplifications of the two sign factors, positivity on representative admissible sets, and high-precision evaluations of the interior Hopf witness. It then independently evaluates the unreduced third-derivative formula and compares its value with the closed reduced cubic coefficient for the environmental speeds 100 and 400, confirming opposite nonzero signs.

The algebraic derivation and sign proof for all admissible parameters are in RESULT.md; a finite checker cannot replace them. The standard local Hopf theorem is used under the displayed nondegeneracy hypotheses. A vanishing cubic coefficient at the intervening speed does not establish a Bautin bifurcation. Full-text access to a closely related 2026 publication was unavailable, so publication-priority comparisons remain qualified. No independent external audit has been conducted.
