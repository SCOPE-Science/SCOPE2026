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

# Verification of toroidal parity-dynamics theorem

The mathematical proof appears in `RESULT.md`. It uses exact local group-algebra decomposition and does not rely on numerical extrapolation. The following independently implemented tests were executed successfully from the packaged source paths using Python 3 standard library only:

```sh
python3 verify_matrix.py
python3 verify_orbits.py
```

The first constructs the literal \(mn\times mn\) open-neighbor adjacency matrix over \(\mathbb F_2\) from each graph's labelled vertices, multiplies powers, calculates ranks by GF(2) elimination and verifies all predicted nullities. It passed 2,229 \((m,n,t)\) tests with \(3\le m,n\le24\) and \(mn\le260\). The second performs full trajectory enumeration, direct first-repeat detection and compares observed first-entry populations to the predicted Fitting counts. It passed all 102,912 binary initial configurations across \((m,n)=(3,3),(3,4),(3,5),(4,4)\). The captured console results are `matrix_output.txt` and `orbit_output.txt`.

Reproducibility requires no network, nonstandard package or external data. The checks do not examine every field of characteristic two and are not an infinite proof. The group-algebra argument handles arbitrary characteristic-two extensions and arbitrarily large side lengths; its critical special-root quotient and all ranges are spelled out in the result. Independent audit has not been performed.
