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

The universal type reduction was checked by `python scripts/check_type_cycles.py`, independently enumerating every simple directed cycle for each of 504 colour-support patterns on the at-most-eight-vertex quotient. The output is archived as `verification/type_cycles.txt`.

Direct simulation used `python scripts/check_dynamics.py` and checked CCA and GHM orbit-averaged excitation rates for every one of 13,716 labelled initial configurations across ten pairs of shore sizes. For each, it compared the observed rate classes and their exact populations with the stated formulas; the output is `verification/dynamics.txt`.

Both programs use Python 3's standard library. The finite experiment on small graphs alone does not prove the infinite-parameter theorem. The exhaustive 504-case quotient computation does apply to every parameter by the proved colour-type reduction; the published finite-graph cycle-integral theorem supplies the bridge from cycle means to dynamical rates.

Full historical priority has not been independently established. Scientific independent audit: not performed.
