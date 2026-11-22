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

# Reproduction and limitations

Run `python3 verify.py` in the extracted directory. No nonstandard Python packages, external network connection or cached data are required. The program computes all 16,257 states of each of the two defined bfloat16 logistic graphs using scaled integers and nearest-even rounding, then independently recomputes each successor via `fractions.Fraction` and cross-checks cycle basins via a separate indegree-peeling traversal.

The exact assertions include six (three per map) primitive cycles, their basin populations, maximum and total preperiod lengths, the two entire successor-array SHA-256 digests, 275 unequal one-step successors, and the full basin-cross table with 10,423 transitions from the eleven-cycle basin to zero. It additionally checks tie rounding and independent floating-point conversions on representative normal inputs. The two graph digests refer to full state-order successor vectors serialized as two-byte unsigned little-endian values. This is an exhaustive finite algorithm: the proof that all states and successor edges are tested is the explicit sequential integer code range, not a heuristic sample.

Actual reproduced output: `BFLOAT16_EXACT_LOGISTIC_GRAPHS_OK`, `states=16257 edges_changed=275`, independent exact-rational probes 16257. The largest transient distances are 81 and 99, and the sum-of-distance invariants are 623656 and 773744 respectively.

No extension to continuum orbits, uniform real initial distributions, alternate compilation trees, other rounding modes or numerical formats follows. A result of a self-review is recorded, but no independent audit has been performed.
