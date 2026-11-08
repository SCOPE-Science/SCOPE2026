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

# Reproducibility and limits

Run `python3 check.py` in the directory containing this file and `check.py`. The standalone script requires only Python 3. It integrates the stated hierarchical equations and, independently, the cumulative predecessor exposures used in the exact projective ratio identities. The deterministic pseudorandom finite-time checks cover lengths 2–9 and yield 540 ratio assertions. The longer runs cover lengths 2–6 and yield 20 assertions on the selected support and exponential rates. The observed output was `PASS: 540 finite-time ratio/integral identities; 20 long-time selection/rate assertions`.

These are discrete numerical tests of representative finite systems, not exhaustive checks of continuous initial conditions. The full mathematical theorem is supported by the proof in `RESULT.md`. Error estimates and all-initial-condition quantifiers follow from analytical comparison and induction, not extrapolation from simulations. No external independent audit has been performed.
