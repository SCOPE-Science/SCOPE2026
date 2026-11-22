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

Run the accompanying `verify.py` using Python 3.10+ and SymPy. It directly checks the symbolic derivative sign factorization, the factorization of the equal-route versus concentrated-plan difference, the analytic threshold root, and the exact \(s=1/2\) threshold equality \(32/81\). It performs reproducible sampled checks across viability parameters and budgets on both sides of the transition, random feasible within-route divisions, and the shorter one-link backup comparator. The symbolic checks are identities over the specified variables; the finite numerical checks are *not* evidence that every continuously feasible allocation has been searched. The global optimizer conclusion and strict tie classification rely on the derivative sign argument and exact algebra in `RESULT.md`.

No empirical detection or dispersal process was validated. The report is limited to the stated stochastic network model, and no independent audit has been conducted.
