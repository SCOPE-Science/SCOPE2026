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

The reproducibility files `verify_joint.py` and `check_graph.py` are standalone Python 3 programs and use no third-party libraries. Running them produced, respectively, `JOINT_PGF_VERIFY_OK 28` and `GRAPH_CYCLE_VERIFY_OK 90`, `COLLISION_VERIFY_OK 19329`, `DEPENDENCE_VERIFY_OK 6`.

The first program compares rational coefficients of the theorem's factorial generating polynomial to direct alphabet-word enumeration. The second independently checks the colored overlap graph's cycle ranks, all pairwise duplication-position equality conditions, and strict positive mixed factorial-moment discrepancies for longer words. Finite tests do not certify universal statements; universal validity depends on the proof in `RESULT.md`.

The full two-variable generating function is proved only in the specified short-length range. The independent-threshold equivalence extends to every permitted source length. No independent scientific audit or experimental biological validation has been performed.
