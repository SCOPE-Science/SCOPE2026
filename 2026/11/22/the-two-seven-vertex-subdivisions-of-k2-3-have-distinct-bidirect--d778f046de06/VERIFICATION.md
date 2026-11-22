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

## Reproduce the finite certificates

Place `verify.py` and `verify_output.txt` beside this file. Run `python3 verify.py` with Python 3.9 or later; the program has no third-party dependencies. Its output must exactly match `verify_output.txt` (excluding operating-system differences, of which none are expected). It generates, rather than loads, all arcs, faces, matched pairs, full Hasse incidences and integer simplicial boundaries. It does not consult any recorded precomputed certificate when determining the answer.

For the two theta graphs, the code cross-checks a hereditary-enumeration face set against independently generated recursive include/exclude faces. It confirms complete face vectors, acyclicity of the full oriented Hasse graph (not merely absence of cycles in a sampled traversal), all signed boundary-composition identities, and unit-only integral Smith reductions. The explicit Morse pivot sequences are in `RESULT.md` and `verify.py`.

## Limits of the checking

Computational exhaustion covers exactly the two sixteen-arc complexes. The upgrade to the homotopy statement uses the standard discrete-Morse CW theorem, a primitive third-cell attaching degree to the unique two-sphere and the Hurewicz isomorphism for wedges of three-spheres. The code does not constitute independent peer review, and it makes no claim for larger graphs or equivariant topological data.
