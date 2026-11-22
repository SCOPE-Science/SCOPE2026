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

The accompanying dependency-free Python 3 program `checker.py` reconstructs a connected eight-vertex shattering example and a connected thirteen-vertex twelve-profile example, checks all explicit edges and four-parameter traces, checks deletion-based constructions for counts one through twelve, and checks a pendant/twin elimination certificate for both witnesses. It exhaustively checks that two row strips and two column strips can cover at most twelve of sixteen profile cells.

Run: `python3 checker.py`

Expected leading output: `VERIFY_OK VC3_witness=8 four_trace_witness=13 four_spectrum=1..12 crosscut_max=12`

The proof's universal rank-width-one bound is an analytic consequence of the existence of a two-versus-two marked leaf split and binary cut-rank at most one. Finite witness verification does not independently certify this graph-decomposition theorem or historical novelty. No independent audit has been performed.
