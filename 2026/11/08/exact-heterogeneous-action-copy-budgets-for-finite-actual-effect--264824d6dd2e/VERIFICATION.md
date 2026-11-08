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

# Reproduction and scope
Execute `python checks/verify_budget.py` in Python 3; no external packages or remote resources are required. The output is `VERIFY_OK slice_cases 1486 frame_cases 463`. The verifier enumerates 1,486 feasible coordinate-grid profiles for budgets at most four and two through four agents, verifies that every fixed-coordinate slice sees every required color, then checks 463 small actual-effectivity action systems, including full two-agent compatible neighborhood-family instances for at most three outcomes and at most three distinct neighborhoods per agent. It also tests asymmetric budget examples and examples violating the necessary inequality.

The general result requires the exact algebraic proof in RESULT.md, not finite extrapolation. The checker does not independently establish novelty, the nonavailability of equivalent earlier publications, or minimum actions for individual frames. No independent audit has been performed.
