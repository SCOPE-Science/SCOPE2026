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

# Reproduction

Use `python3 verify.py` (Python standard library only). Expected output: `PASS: 254 exact identities / full-state comparisons`.

The checker first establishes integer-coefficient polynomial identities for every one of the ten lumped backward equations, both absorbing values, the three fixation-probability differences, and the sign tests for the crossover polynomial. It then independently reconstructs and solves the unlumped \(30\)-transient-state chain using exact fractions for eight rational values of \(r\), comparing all thirty transient configurations at each fitness to the lumped expressions. The latter \(240\) checks test the implementation but cannot replace the symbolic identities establishing the theorem for all positive real fitness values.

The model excludes directed/weighted networks, mutation, other initial seed budgets, and fitness \(r=0\). An independent external scientific audit has not been performed.
