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

The displayed proof reduces the lower bound to necessary realizability of the four traces `0101`, `1010`, `1111`, `0000` and then uses `0110` to isolate the two critical supports. Its affine table supplies all sixteen realizations for every integer \(r\ge2\).

Run `python3 verify_two_windows.py` with a standard Python 3 interpreter. The executed script printed `WITNESS_AFFINE_PASS 15984 r_range_2_1000`, `EXHAUSTIVE_FOUR_SUPPORT_PASS 92099 r_range_2_7 critical_counts [(2, 9, 2), (3, 12, 2), (4, 15, 2), (5, 18, 2), (6, 21, 2), (7, 24, 2)]`, and `INDEPENDENT_RUN_SHAPE_PASS`.

A finite enumeration corroborates the proof but is not an all-parameter proof. The theorem does not determine lower-dimensional counts or online-dimension values. Independent audit has not occurred.
