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
# Verification

The complete mathematical proof is given in `RESULT.md`. `check_radial.py` is a standalone Python 3 script using only the Python standard library. From a directory containing the extracted files, run:

```sh
python check_radial.py
```

It calculates exact coefficients in rational arithmetic independently of an edge-orientation enumeration. The enumeration retains exactly acyclic orientations, calculates each signed-degree vector and bins by `4*norm_squared`. No optimization solver, numerical approximation, or external dataset is used.

Observed successful replay: `UNICYCLIC_RADIAL_PASS graph_cases=2500 vertices_enumerated=1168282 iso_shell_pairs=1 example={4: 2, 8: 16, 12: 14, 16: 16, 20: 6, 28: 2}`.

This is a finite consistency test, not an exhaustive test of all unicyclic graphs; the unrestricted claim relies on the Walsh expansion and the graph-theoretic characterization of even-degree subgraphs. No independent audit, external theorem-prover certification, or historical-priority guarantee is asserted.
