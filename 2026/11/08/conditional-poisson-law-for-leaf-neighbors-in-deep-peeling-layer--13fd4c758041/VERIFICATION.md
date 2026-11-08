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

Run `python3 verify_joint_rank_layer.py`. It requires only the Python 3 standard library, does not access external services, and prints a deterministic report. Directly executed result: 53,374 passing assertions. The checker enumerates all recursive-parent assignments for sizes three through eight, tests actual leaf-neighbor status against leaf-child status with the root exception, and verifies peeling-layer equivalence for sufficiently deep vertices. It numerically integrates the Poisson-thinning recurrence, checks exact known second-layer constants, and simulates a seeded tree with 90,000 vertices to compare empirical joint frequencies. It also tests numeric consistency of the proposed high-layer total-variation upper bound on a finite set of layer indices.

The program does **not** constitute an exhaustive check over all tree sizes or proof of almost-sure convergence, the Poisson limit, or historical originality. Those are argued mathematically in RESULT.md, using bounded differences, Yule fringe convergence, independent marked Poisson processes and an explicit age-tail estimate. Independent assessment of the proof has not been performed.
