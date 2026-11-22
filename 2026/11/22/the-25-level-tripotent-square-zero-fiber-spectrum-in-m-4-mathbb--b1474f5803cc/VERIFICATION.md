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

For an exact replay, run `python3 verify.py class_table.csv` from the artifact directory. The script uses only Python's standard library. It exhaustively enumerates all binary order-four matrices; checks the tripotent and square-zero polynomial relations by actual field multiplication; enumerates every admissible ordered pair; separately recomputes all fibers via 16-bit Walsh inversion; and constructs the complete 34-class primary rational canonical census with class sizes. It asserts pairwise agreement of the direct and Walsh totals and class-weighted agreement with the full histogram. The expected success marker is `TRIPOTENT_SQUAREZERO_FIBERS_OK 34 65536 25`. The script regenerates the supplied class-table CSV. This is exact finite verification; it does not establish an unrestricted dimension theorem or constitute independent validation.
