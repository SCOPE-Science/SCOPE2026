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

# Reproducibility and verification

Run `python3 CHECKER.py` (Python 3 standard library). The checker uses a scaled stationary equation to avoid exponential overflow, tests exact stationary interval signs, numerical bisection at 48 extrema, finite-grid global envelope inequalities, weak-angular asymptotic ratios and coherent-Weyl unitary conjugation on three polynomial examples. The delivered checker yielded `PASS 18295 finite diagnostic checks`.

Analytical rather than finite verification: unitarity of Gaussian coherent displacements and the exact norm; the differentiation identity; strict monotonicity of the stationary function on every half-period; the global backward-period comparison; the implicit small-zero expansion at infinitely many critical times; and its uniform weak-angular first-peak limit. A finite numerical grid cannot establish global uniqueness, arbitrarily many alternating extrema, or asymptotic assertions. No independent mathematical validation is claimed.
