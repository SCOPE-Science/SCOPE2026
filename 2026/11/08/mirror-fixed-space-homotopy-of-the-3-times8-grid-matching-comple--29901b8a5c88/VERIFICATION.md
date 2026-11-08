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

The exact standard-library verifier `verify_mirror8.py` reconstructs all 37 graph edges, the admissible involution edge-orbits, the complete face-posets, the greedy acyclic matchings, and the signed Morse boundary. It topologically sorts all 10,996 and 4,828 oriented incidences, respectively, to exclude gradient cycles; finite sampled faces alone would not suffice. For column reflection at width eight the critical 3- and 4-cell counts are 2 and 6; two signed degree vectors have a 2-by-2 determinant of 1. The row model has no reduced critical faces. A separate computation of direct simplicial boundary ranks over the two-element field yields one nonzero reduced Betti rank, 4 in degree 4. Run `python3 verify_mirror8.py`; its exact recorded output is `verify_output.txt`. This is a complete computation for these explicit finite complexes, not a claim about general widths. The homotopy implication is separately justified in RESULT.md. No independent external audit or validation has occurred.
