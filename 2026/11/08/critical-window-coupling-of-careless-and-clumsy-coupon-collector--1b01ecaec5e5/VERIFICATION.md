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

# Reproducibility

Run `python checker.py` beside the standalone Python file. Python's `fractions.Fraction` is used for exact arithmetic; no random seed or external package is required. The checker executed successfully with 1,813 exact-rational checks.

The tests compare complete per-step loss-set distributions, exact finite-state clumsy and careless transitions, inclusion in the auxiliary coupling, and the analytic one-label and point-disagreement inequalities for small finite state spaces. They do not simulate or certify the infinite limit. The main proof is analytic and depends on the cited critical clumsy limit theorem; the latter is not independently certified here.

For a direct audit of the bound, use the notation and explicit finite expression (4) in RESULT.md. Equation (6) adds the pre-window classical unseen-label term and gives the first-completion distribution error.
