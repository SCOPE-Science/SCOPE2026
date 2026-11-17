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
# Verification notes

The bundled `verify.py` was executed using Python 3 and SymPy. Its exact-arithmetic output was:

```text
VERIFY_OK symbolic_dulac=1 sharp_maximum=1 general_repeller=2 rational_witness=7
rational_witness trace=19/30000 determinant=2233/1875000 d=923/3750
```

The script checks the general Dulac expression, the identity \((x+b)^2-4bx=(x-b)^2\), the Jacobian of the parameterized positive equilibrium, and strict sign conditions for the rational example. The proof of the universal no-cycle assertion relies on the Bendixson–Dulac theorem; the converse existence relies on a bounded trapping region, boundary hyperbolicity and the planar Poincaré–Bendixson classification. Finite or symbolic computations alone do not verify infinitely many trajectories. No independent mathematical audit has been performed.
