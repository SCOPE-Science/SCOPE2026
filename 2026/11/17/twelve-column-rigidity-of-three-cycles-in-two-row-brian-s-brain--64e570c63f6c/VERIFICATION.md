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

## Reproduced checks
The three supplied programs test the same three-step return formula using different constructions:

- `verify_transfer.py`: exact finite transfer graph from phase-incidence constraints; cyclic component decomposition and traces through circumference 24.
- `verify_history.py`: independent original-state time-history transitions and independent SCC algorithm, showing the same 12, 12, 1 cycle decomposition.
- `verify_direct.cpp`: exhaustive original dynamics through circumference six and an explicit primitive-three witness at circumference twelve.

Expected and reproduced stdout are stored in `transfer_output.txt`, `history_output.txt`, and `direct_output.txt`, respectively. Python 3 and a C++17 compiler suffice; `networkx` is used by the first script (see `requirements.txt`). The exact all-circumference proof relies on enumerating the finite local constraint graph and proving its entire cyclic core, not on checking many circumferences.

## Boundary conditions and limitations
The eight Moore offsets are counted with multiplicity, including coincidences on the two-row torus. All finite transfer states and edges are generated from explicit local rules; no external files are needed. Original-state exhaustive enumeration ends at circumference six; the displayed length-twelve witness is a check of existence, not an exhaustive enumeration at that length. No other temporal periods are addressed.
