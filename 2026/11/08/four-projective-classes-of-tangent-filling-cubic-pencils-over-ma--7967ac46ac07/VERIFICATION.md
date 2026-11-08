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

Run using Python 3 and SymPy in the same directory:

```
python3 enumerate_tf_pencils.py
python3 verify_tf_smooth.py
python3 check_nets.py
python3 base_reduced.py
```

The first is an exhaustive integer-base-three vector and finite projective-group census. Expected scientific totals are 29,524 normalized equations, 3,744 tangent-filling equations, 22,464 tangent-filling pencils, four projective orbits of size 5,616, and member-point profiles occurring 11,232 / 5,616 / 5,616 times. The second independently certifies geometric smoothness on all three charts and full projective orbit coverage. The third enumerates all candidate third generators of a tangent-filling net and obtains zero. The fourth certifies unit Jacobian-minor ideals on each affine chart for each representative pair, implying nine reduced geometric base points in every class. The reproducible orbit table is `tf_pencil_orbits.csv`.

**Limits:** Algebraic closure smoothness uses the Jacobian criterion and exact Gröbner bases, not enumeration of points over a bounded collection of extension fields. The code tests all finite rational members, not every member over the algebraic closure. External or independent mathematical audit has not been performed.
