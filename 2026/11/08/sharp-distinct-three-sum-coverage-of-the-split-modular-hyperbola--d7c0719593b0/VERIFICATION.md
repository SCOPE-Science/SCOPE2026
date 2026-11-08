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

# Reproducibility and scope

Run `python3 verify_hyperbola.py` using Python 3 (standard library only). The independent enumerator covers all unordered triples of three distinct nonzero elements and contributes six to the corresponding ordered target fiber. It separately computes the four character-formula branches. Prime fields and the quadratic extensions of orders \(25,49,121\) use fully explicit polynomial-basis arithmetic. All 42,620 target fibers matched.

The checks include prime orders \(5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67\) and extension orders \(25,49,121\). They also verify that only the predicted possible origin is missing at field orders at least 23. The exact finite table of missing targets for the six smaller fields comes from complete enumeration, not extrapolation.

The infinite statement is derived mathematically: for generic targets a squarefree quartic has a two-point-at-infinity genus-one model, giving \(|a_{s,t}|\le2\sqrt q\); the remaining algebraic cases are evaluated without curve bounds. Computational checks cannot certify all field sizes or historical originality.
