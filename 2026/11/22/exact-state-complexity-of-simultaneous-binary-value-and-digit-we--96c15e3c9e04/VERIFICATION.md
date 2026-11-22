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
# Reproduction and checks

In a directory containing the included programs, execute:

```sh
python3 check_minimize.py
python3 check_quotient.py
python3 check_density.py
```

The programs use only Python standard-library modules. Their normal output is embedded as `check_minimize.out`, `check_quotient.out`, and `check_density.out` and was reproduced by actual execution. The first enumerates reachable residue states and performs deterministic minimization for \(1294\) accepting residue pairs. The second applies an independently implemented complete quotient signature across \(2610\) residue targets and checks that quotient transitions are well-defined. The third uses integer counts of all binary words of specified lengths and checks distribution convergence. The statements for unbounded moduli and arbitrarily long words are proved in `RESULT.md`, not inferred from test coverage.

Source comparisons were limited to inspected scientific claims and material identified in the accompanying review; priority is not independently certified.
