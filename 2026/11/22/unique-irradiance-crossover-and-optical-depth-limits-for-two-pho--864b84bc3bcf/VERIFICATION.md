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

# Verification scope

The accompanying `verify.py` is standalone Python 3 code using the standard library. Invoke `python3 verify.py`. The recorded execution returned `PASS: 7,839 deterministic assertions`; it verified the two **exact rational** opposite-sign witnesses, the analytic-vs-separate-integrals identity on 600 reproducibly sampled parameter triples, signs on each side of each computed crossover, increasing integrated ratios, and convergence trends toward the thin- and thick-layer scalar limits.

The complete real-parameter theorem is supported by the symbolic derivation and quantifier-level arguments in `RESULT.md`, not by finite sampling. In particular, the checker does not formally certify infinitude, originality, physiological accuracy, or independent review. The full text of one historical multispecies-canopy paper was unavailable; historical priority is provisional. The review is a self-review only, with independent audit not performed.
