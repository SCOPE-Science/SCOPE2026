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

The proof checks are symbolic: the geometric fixed-set face correspondence, a globally acyclic monomer-toggle matching, its exact critical cells, and the resulting CW attachments.

The standalone `verify.py` independently constructs every prism perfect-matching complex from perfect-matchings of the **original prism**, filters its layer-invariant simplices, and independently constructs its monomer-dimer tile complex. It checks equality for eight cyclic inputs and nine varied graphs, including disconnected graphs. It enumerates all matching incidences and topologically sorts the complete directed Hasse graph, then computes the reduced Lefschetz number from faces. This verifies the actual finite examples, not all finite graphs.

Run `python3 verify.py` from the same folder; output is recorded in `verify_output.txt`. No additional data files, network access, special packages, or external certification channels are required.

Limitations: finite tests are not an infinite proof; arbitrary-graph correctness follows from the symbolic matching argument in `RESULT.md`. The 2026 expanded circular-ladder preprint was accessible in abstract form but not full text; a stronger unindexed result could affect originality. Independent mathematical audit has not been performed.
