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

# Verification

The accompanying `verify_cycle.py` uses exact integer arithmetic for every fairness and blocking condition. Execute `python3 verify_cycle.py` without dependencies beyond the Python standard library. It enumerates all committees on the 4–10 candidate cycles and every smaller deviation for JR committees; constructs the sharp 16-voter example; checks all 924 qualifying parameter pairs for 16–99 voters; and tests random examples of the sharp improver bound. The expected terminal output ends with `PASS`.

This computational evidence is finite. The infinite necessity and sufficiency theorem is proved algebraically in `RESULT.md`, using constant welfare, cyclic run decomposition, and an explicit witness family. The finite checker does not verify novelty or replace independent examination of the proof.

Independent scientific validation has not been performed.
