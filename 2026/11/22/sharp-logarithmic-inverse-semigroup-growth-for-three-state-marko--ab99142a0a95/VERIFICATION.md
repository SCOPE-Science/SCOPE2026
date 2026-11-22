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

Run `python3 check.py` with Python 3.10 or later, without third-party packages. The included code verifies with exact rational operations the projection and nilpotent decomposition and spectral coefficients of the sharpness example; it additionally runs a deterministic 41-by-41 rational grid, 12,000 pseudorandom generator samples and finite scaling checks. Observed output: `PASS 13685 supplementary tests; exact projection/nilpotent certificate holds`.

The correctness of the universal bound and the limiting sharp coefficient follows from the analytic characteristic-polynomial and Jordan-decomposition proof in `RESULT.md`. The checker only corroborates the formulas. Novelty comparisons include a fully read 2020 source and a published three-state cycle result, but a relevant 1975 paper remained unavailable; absolute historical priority has not been independently confirmed. Independent mathematical audit has not been performed.
