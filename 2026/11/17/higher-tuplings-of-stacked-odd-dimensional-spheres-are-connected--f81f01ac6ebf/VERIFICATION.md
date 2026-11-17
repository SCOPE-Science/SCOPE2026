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

# Reproduction
Run `python3 check_higher_tuple_stacked.py` with standard-library Python 3. The source enumerates the graph of the tupling directly from the stored top facets, without implementing the proof's incidence-graph counting formula as its graph constructor. It verifies direct counts and BFS connectedness against the theorem for the stated finite collection. `CHECK_OUTPUT.txt` records the resulting integer values and success marker.

The computations are finite checks, not a proof of the universal quantifiers. The universal argument is the Johnson-connectivity replacement proof in `RESULT.md`. There is no external or independent audit.
