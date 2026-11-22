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

The standalone `verify.py` uses Python 3.9+ standard library only, performs complete 14-arc-subset enumeration, implements the specified augmented discrete-Morse matching, checks every reversed Hasse-incidence orientation for cycles, and reconstructs the geometric quotient's signed cellular chain groups independently. Its asserted output is:

```
PASS faces 1849 morse_pairs 910 critical_5 29 free_C7 True quotient_orbit_cells 264 quotient_betti_mod2 [1, 0, 0, 0, 0, 5] quotient_betti_mod7 [1, 1, 1, 1, 1, 5]
```

The quotient mod-three Betti vector is also asserted to be `[1, 0, 0, 0, 0, 5]`, and all signed integral boundary compositions are asserted zero. The finite computation alone would not establish a parametrized infinite theorem; no such extension is claimed. The integral torsion and rational module statements are justified by the mathematical covering and Lefschetz arguments in RESULT.md. The available abstract of a relevant 2020 Cayley-graph thesis does not resolve whether its full text already contains an equivalent computation. There has been no independent external audit.
