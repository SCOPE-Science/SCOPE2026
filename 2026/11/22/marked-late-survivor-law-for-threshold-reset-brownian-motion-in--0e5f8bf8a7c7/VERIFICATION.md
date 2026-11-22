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

# Verification and limits

The mathematical statements are proved in `RESULT.md` by heat-kernel boundary-current asymptotics, a marked renewal identity, a two-region convolution-tail estimate, normalized tightness and an independent future-cycle decomposition. No finite computation certifies the continuum theorem.

Run `python check.py` using Python 3 standard-library facilities only. The program performs 171 algebraic and deterministic marked-renewal tests. Its synthetic integer-Pareto example is a deliberately different discrete regenerative process whose exactly equal large-time marked tails offer a diagnostic check of the general renewal mechanism; it is not claimed to simulate the Brownian wedge or establish continuous-time convergence. The half-plane and quadrant prefactor checks independently compare the wedge heat-kernel amplitude with reflection and product formulas.

The pre-anchor literature provides the threshold-renewal setup and the free-wedge heat-kernel/currents. The new proof independently reconstructs the total target-survival tail from the geometric random sum before obtaining the conditioned four-variable path law. The November 2026 direct wedge threshold-reset study supplies an independently checked matching tail and unconditional reset-count comparison. Limiting count moments are computed from the limiting law; moment convergence before taking the limit is not established.
