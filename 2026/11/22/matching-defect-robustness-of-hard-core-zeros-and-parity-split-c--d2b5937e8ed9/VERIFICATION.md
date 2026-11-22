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

# Finite reproducibility checks

From this directory, run `python verify_hardcore_crown.py` with Python 3, SymPy and mpmath installed. It enumerates actual independent sets on small labeled partial-matching-deleted bicliques, computes exact real-root counts on a larger range, samples complex right-half-plane nonvanishing, and checks convergence of rescaled root locations. Replay on the supplied source printed `CROWN_HARD_CORE_CHECKS_PASSED 156`. This is supplemental finite and numerical evidence; it does not establish the infinite theorem without the proof in RESULT.md. The claimed full complex half-plane and asymptotic statements are derived analytically. Independent scientific audit has not been performed.
