---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproduction

Use Python 3 and SymPy. Run in a writable copy of the record directory; the census writes the orbit table to that directory. Use the portable version of `base_reduced.py` that decodes the generator pairs from the finding rather than relying on another installation.

```sh
python3 enumerate_tf_pencils.py
python3 verify_tf_smooth.py
python3 check_nets.py
python3 base_reduced.py
```

The census exhausts all 29,524 normalized nonzero cubic equations. The expected outputs are 3,744 equations passing the tangent-coverage test, 22,464 pencils, four orbits of size 5,616, and the three member profiles occurring 11,232, 5,616 and 5,616 times. The orbit table is `tf_pencil_orbits.csv`. The smoothness verifier checks the chart ideals of the thirteen distinct codes in the table and verifies orbit coverage. The net verifier checks 3,740 candidate third generators for each representative pencil and finds no extension. The base verifier decodes the four displayed generator pairs independently, tests three chart ideals per pair, and fails if any one ideal is not the unit ideal. This certifies transversality for the displayed pairs; the degree-nine and all-orbit conclusions also use Bézout and the orbit census.

**Scope:** The geometric smoothness and reducedness checks use exact Gröbner bases over \(\mathbb F_3\), not sampling over a finite collection of extension fields. Only the four rational parameter members of each pencil are required to be smooth and tangent-filling.
