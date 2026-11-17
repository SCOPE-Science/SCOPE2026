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

The local proof establishes all-size claims; the scripts below offer finite independent checks and cannot certify novelty or the infinite-parameter conclusion. Run `python3 check_dynamics.py`, `python3 check_transfer.py`, and `python3 check_survivors.py` on the standalone files. All three were executed with normal exit status, and the corresponding outputs are included as text files. The numerical code has no external dependencies.

The dynamics checker enumerated 312593 initial states, verified first-entry times and counted recurrent states. The independent transfer checker verified 112 matrix/count comparisons and direct time-return counts for the stated finite sizes. The survivor checker independently verified the exact wave reconstruction on 218084 initial states and checked explicit worst-case configurations. A self-review inspected the proof assumptions, normalization and source comparisons; no independent audit has been performed.
