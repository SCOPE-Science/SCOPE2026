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

# Reproduction and limitations

From a directory containing `verify_icosahedral_lerw.py`, run:

```sh
python3 verify_icosahedral_lerw.py
```

The script is Python 3 standard-library only. It builds the graph explicitly, checks its 12-vertex 30-edge degree sequence and distance shells, evaluates its spanning-tree cofactor exactly, exhaustively enumerates all simple paths for all 66 unordered endpoint pairs, and verifies the three entire integer path-length distributions, rational means and geodesic probabilities. Exact rational Green-function checks are performed on selected paths independently of the fraction-free determinant implementation.

Successful output ends with `PASS: all 66 vertex pairs, exact distributions, matrix-tree normalization, and Green-function spot checks`.

The finite search is exhaustive because every simple path on a twelve-vertex graph has at most eleven edges and the recursion visits every unused neighbor at each step. The mathematical equivalence between path minors and tree counts is proved in `RESULT.md`. The reproducibility check is not a general theorem for larger graphs and not an independent scientific audit.
