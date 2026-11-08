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

# Reproducibility and scope

Run `python3 verify.py` in this directory. This checks the defining best-response inequalities directly for all pin locations, fixed actions and free profiles when both community sizes range from one to five, separately for weak and active-strict equilibrium. It compares the enumerated minimum costs and the exact numbers of successful minimal interventions with the theorem. This is a finite computational falsification test; the infinite family of claims follows from the independent majority/minority proof in `RESULT.md`.

The fixed agents do not have two feasible actions, so active strictness means strictness among the unfixed agents only. The stochastic probability concerns an independently fair pinned-action choice at a *fixed, uniformly random, minimum-size set* and is not a statement about equilibrium selection or iterative dynamics. No independent scientific audit has occurred.
