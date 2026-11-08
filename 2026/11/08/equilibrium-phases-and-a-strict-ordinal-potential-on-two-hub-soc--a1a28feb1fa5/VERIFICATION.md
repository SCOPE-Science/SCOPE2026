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

# Reproducibility checks

Run `python verify_biclique_sdncg.py` from the directory containing this file. Requires only Python 3 standard library, without network access or randomness.

The code enumerates all labeled host-edge patterns for \(k=3,4,5,6,7\), computes all-pairs shortest-path distances by BFS from scratch, and independently decides stability through each endpoint's utility differences under feasible additions and deletions. It compares that result with the theorem criterion, tests closed-form labeled counts, and checks whether the sign of each legal move's potential difference agrees with that move being improving. All utility comparisons use exact rational parameters at positive half-integer probe values, including every even-integer resonance point within the probed range. States with no spanning connection are excluded from the stability set, rather than assigned finite distances.

Observed successful standalone run:

```text
k=3: 64 states, 14 parameter probes, all checks passed
k=4: 256 states, 16 parameter probes, all checks passed
k=5: 1024 states, 18 parameter probes, all checks passed
k=6: 4096 states, 20 parameter probes, all checks passed
k=7: 16384 states, 22 parameter probes, all checks passed
PASS: 465792 direct payoff/profile tests, 90 exact count comparisons, 8951 confirmed equilibrium instances, 116928 improving-move/potential comparisons
```

## Logical checks and limitations

The proof derives the full set of possible host moves by connectivity, then an exact algebraic utility calculation, then an iff equilibrium classification; the count and potential steps use those same verified move thresholds. Only this algebraic reasoning establishes the theorem for all \(k\ge3\) and all real \(\alpha>0\); the finite computations cannot prove an unrestricted assertion. The potential bound counts distinct triples, not distinct labeled graph states. Equality cases are nonimproving by definition. The terminal bound is not claimed tight and no equilibrium claim is made outside two-hub hosts. No external audit or third-party certification has been performed.
