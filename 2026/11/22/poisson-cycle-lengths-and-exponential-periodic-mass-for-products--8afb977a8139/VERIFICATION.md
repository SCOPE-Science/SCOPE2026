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

Run `python3 verification/check_cycles.py` using Python 3 and its standard library, without dependencies or network access. The checker independently extracts noncommon cycles of every ordered pair of idempotent maps of size at most five and compares exact rational mixed factorial moments with the stated closed formula in every feasible root-size/intersection stratum. Direct enumeration covers 40,207 ordered pairs and reports 40,837 exact assertions. These finite tests address the deterministic cycle correspondence and finite moment identity; the root-rank limit, point-process convergence and exponential law are established analytically in `RESULT.md`.

The normalizations use natural logarithms and the composition convention \(T_n=F_n\circ G_n\). Fixed points common to the two maps are excluded from all counted cycles. The model's conditional probabilities use fixed root sets, not independently sampled roots. No independent audit has been performed.
