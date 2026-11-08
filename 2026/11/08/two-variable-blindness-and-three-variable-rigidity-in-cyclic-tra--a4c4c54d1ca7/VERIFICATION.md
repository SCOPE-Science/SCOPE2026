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

# Verification of cyclic transitive-block tournament classification

Execute with Python 3 standard library only:

```
python3 tournament_logic_refinement.py
python3 tournament_formula_check.py
```

The exact stdout is preserved in `tournament_logic_refinement.out` and `tournament_formula_check.out`. The first program computes stabilized counting-free finite-variable tuple types from atomic arc/equality types with *sets* of one-coordinate replacement types; over twenty rotation-orbit representatives of sizes three through eight it finds one width-two sentence type, twenty width-three types, and tests all four hundred ordered graph pairs. The second program independently checks all 364 positive ordered triples of total sizes three through fourteen: 48,321 ordered same-block pair cases, 589,407 ordered distinct-vertex cycle cases, 52,416 local block-size thresholds, and orbit numbers for twelve orders. It also recognizes the class among all labelled tournaments of orders three through six and obtains counts 2, 24, 240 and 2,400 respectively, as predicted.

Both programs were run from their actual embedded contents and their stdout reproduced. They are *finite corroborations*, not independent or exhaustive validation of the all-orders result. The theorem's critical noncomputational steps are the exact directed-triangle block lemma, syntactically three-name recursive unary path tests, indefinite two-pebble strategy, and Burnside/orbit counting. These are proved separately in `RESULT.md`. No third-party paper or unavailable data file is required to replay either program.
