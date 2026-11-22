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

# Verification and reproducibility

The conditional-tail theorem is proved analytically using exact Clayton marginal probabilities, negligible probabilities of opposite-tail pairs, ratio asymptotics, and path independence of positive edge odds on the binary hypercube. Each assumption is explicit in `RESULT.md`.

Run `python verify.py` in the extracted directory. The script uses only Python's standard library and exact rational arithmetic. It tests six positive parameter sets, 360 square-face equations, parameter recovery, exact finite-threshold conditional probabilities in one nonuniform example, and a locally feasible but globally incompatible table.

The finite-threshold checks are diagnostic only; they do not establish infinite-domain claims. No independent mathematical audit has been conducted. The historical-priority comparison is based on the named inspected sources and may not be exhaustive.
