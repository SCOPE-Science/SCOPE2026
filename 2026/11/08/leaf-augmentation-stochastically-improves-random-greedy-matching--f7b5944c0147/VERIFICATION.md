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

Run `python verify.py` with the Python standard library from the extracted package. The expected marker is `VERIFY_OK 541040 exact and seeded checks`. The checker computes exact rational finite laws by recursion and independently enumerates every edge-priority permutation for selected small path-coronas, checks supports and first-order stochastic tail inequalities, runs exhaustive small-core single-leaf-insertion comparisons, tests 4500 deterministic-seed random cores, and verifies the generating-equation coefficients exactly.

The infinite stochastic-order theorem is established by the one-discrepancy priority coupling, not by the finite tests. The exact expansion of the mean and the supergeometric remainder rely on a solved entire first-order ODE and a Cauchy coefficient bound, not a numerical fit. The standard checker intentionally does not purport to certify an infinite family or an independent mathematical audit. The full text of one possible older mixtures comparison was unavailable; historical novelty remains qualified.
