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
# Reproducibility and limits

From the same directory run `python3 verify.py`. The output must match `check_output.txt` exactly. The program builds the open-neighborhood simplicial complexes from the punctured graphs, calculates the connectivity and mod-two ranks of the triangle-to-edge matrix, and computes the Euler characteristic directly from all faces. The symbolic two-dimensional collapse proved in `RESULT.md` supplies the final second Betti number. Both parity sides are tested at each vertex-pair distance in every dimension from three through seven (50 cases, 111,952 total faces). The exceptional seven-triangle local filling is also explicitly tested in dimensions four through seven. The program uses only the Python standard library.

These checks are independent of any earlier packaged computational output. They do not establish the all-dimensional theorem, torsion freeness or the homotopy type without the accompanying integral proof. No independent mathematical audit has been performed.
