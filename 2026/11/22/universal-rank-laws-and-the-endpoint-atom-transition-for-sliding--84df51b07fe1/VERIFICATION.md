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

All formulas are evaluated under independent continuous inputs with no sample ties. Execute `python3 verify_rank_plateaus.py` with standard-library Python 3. It independently enumerates every ranking of the union of overlapping windows for widths 2–4, verifies the unconditional equal-rank and entry-conditioned plateau tails, and checks the exact factorial formulas for wider windows. The included program completed with 1,678 exact assertions.

The checker gives finite evidence only. All-rank correctness and all limiting probabilities rest on the beta-integral, entry-stationarity and rational asymptotic arguments in RESULT.md. No independent mathematical audit has been performed.
