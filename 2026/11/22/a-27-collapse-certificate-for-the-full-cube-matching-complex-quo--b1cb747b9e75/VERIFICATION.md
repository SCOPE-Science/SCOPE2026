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

## Reproducible checks
Run `python3 verify.py` in the directory containing `collapse_certificate.json`, with Python 3 and no nonstandard packages. It rebuilds the graph, all matchings, their strict flags, all 48 symmetry edge maps, and the 55 complete-flag orbit cells. It independently derives the attaching-face orbit multilist and checks all 27 free-face pairs, requiring unique actual incidence, maximal coface and closure of the surviving cells. The output for the verified certificate is:

`CUBE_MATCHING_FULL_QUOTIENT_COLLAPSES_OK group=48 matchings=107 flags=1385 cells=55 pairs=27 last_vertex=8`

`collapse_certificate.json` has 27 index pairs. The canonical cell ordering is reconstructed by the verifier; the certificate is a list of proposed pairs, *not* a trusted list of correct incidences. Each pair is checked from the graph-based incidence data.

The proof is an exact finite computation for the cube graph. It gives no higher-dimensional-cube classification, and no independent mathematical audit has been performed.
