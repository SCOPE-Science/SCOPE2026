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

# Reproducibility and proof boundaries

Run `python checker.py` using Python 3.10 or newer; it has no nonstandard dependencies. The script enumerates \(n!\) Mallows permutations for each tested market, independently constructs joint first/second selection probabilities and exact exceptional-top probabilities, and compares to the displayed formulas using rational arithmetic. This cross-check does **not** compute a top-cycle majority graph or certify the infinite statement by enumeration. The rigorous infinite proof uses the independent suffix bound, geometric-series limits and Stirling's formula, and invokes the external deterministic top-cycle classification for \(n\ge5\). The uniform limit is treated independently.

Scientific limitations: common center, independent agents, fixed \(0<q<1\) (plus separate \(q=1\) case), strict preferences. The independent audit channel is unperformed.
