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

# Reproducibility and limitations

Run `python3 check_matrices.py` and `python3 check_exhaustive.py` with Python 3 and no external packages. `matrix_output.txt` and `exhaustive_output.txt` are their successful captured outputs.

The first program computes the full \(2(2k+1)\)-dimensional temporal transition matrix over \(\mathbb F_3\), compares actual fixed-space dimensions with the formula at all positive times up through the exact order for \(2\le k\le10\), and tests that no proper divisor of the asserted order gives the identity. The second program directly updates paired rows using the edges of each graph, follows all orbits for two triangles, and checks exact primitive temporal populations against the formula without using matrix powers.

The proofs for arbitrary \(k\) and extension fields are in RESULT.md; finite tests do not themselves establish unrestricted results. No external independent audit or certification was performed.
