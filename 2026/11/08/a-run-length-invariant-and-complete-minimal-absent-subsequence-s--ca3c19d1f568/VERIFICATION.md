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

# Verification methods and limits

Run `python3 verify.py` using Python 3 and its standard library. The script constructs literal finite host strings, greedily tests each binary candidate's scattered embedding, independently tests every one-letter deletion, and compares the exact resulting MAS sets to the formula's state-graph enumeration for 19 parameter pairs. This checks absence, minimality, distinctness, and the finite-host boundary without relying on the weighted transfer equations.

The script separately compares the graph's length distributions to the rational-function coefficient recurrence for 112 additional parameter pairs. A successful execution yielded 131 passed parameter/spectrum comparisons; the direct exhaustive checks inspected 11,133,114 candidate binary words. The enumerated host parameter ranges and exact recurrence are specified inside the script and RESULT.md.

The weighted-state equations were independently eliminated symbolically and matched the numerator and denominator in RESULT.md. These are finite computational checks. The theorem for arbitrarily large parameters rests on the greedy bridge proof, the exhaustiveness of state transitions and terminal boundaries, and exact algebraic elimination, rather than on experiments. No external independent audit has been performed.
