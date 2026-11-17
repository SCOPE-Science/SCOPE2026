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

# Verification and boundaries

The complete proof is in `RESULT.md`. The exact iteration, path probability and exit-time calculations were checked against the standalone `checker.py`, which uses rational arithmetic for finite examples and ordinary floating-point calculations for sanity checks. A successful local run reported:

`MOVING_SEED_PARABOLIC_POISSON_OK exact_paths=3 pgf=4 survival=multiple critical_rates=3`

The computer checks have finitely many examples and cannot establish infinite asymptotics. The proof of the sharp total-variation rate uses an explicit common-uniform coupling and a matching one-coordinate lower bound. Weak Poisson point-process convergence is distinct from quantitative total-variation convergence for the total count. All claims require the positive-seed triangular sampling assumptions; no independent audit has been performed.
