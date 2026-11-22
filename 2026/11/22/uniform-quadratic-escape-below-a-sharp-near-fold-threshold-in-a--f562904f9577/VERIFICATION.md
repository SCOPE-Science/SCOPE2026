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
The analytical proof uses an exact one-step coboundary and a coercive two-step drift at the critical boundary. Both are identities or consequences valid for **all** real initial states. The symbolic checker uses SymPy and verifies the potential identity, the necessary two-cycle midpoint, the exact gap to its fold, and three rational parameter sets. Run `python3 verify_escape.py` after installing `sympy`.

The checker does not certify the existence of a global positive minimum by sampling. Existence is proven by coercivity, continuity, and the absence of transitions between the two zero-drift points. The absence of invariant probabilities follows by dominated convergence. No result is asserted about parameters outside the stated closed escape chamber or the narrow intermediate region.
