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

# Verification scope

`verify.py` contains a complete, standard-library-only finite check of the graph, all polyhedral Hom cells, their cover incidences, local links, connectedness, signed integral orientation cycle and affine target symmetry character. Run `python3 verify.py` in the directory containing the file. The program uses two descriptions of Hom vertices: all five-step closed graph walks and all generator permutations. It expands faces only through valid common-neighbor additions and checks that no dimension greater than two occurs. Every two-cell is checked to be a square with four distinct edges and four corners. Vertex links and one-cell incidences are checked independently of genus.

The purely mathematical proof of the generator relation, equivalence of adjacent recoloring with label-swaps, circle links, connectedness, and classification of surfaces is in `RESULT.md`. The finite enumeration confirms the special graph identities, incidence counts and global orientation signs but cannot prove any generalized folded-cube claim. `verification_output.txt` is captured execution output. No independent human audit or separate external validation has been performed.
