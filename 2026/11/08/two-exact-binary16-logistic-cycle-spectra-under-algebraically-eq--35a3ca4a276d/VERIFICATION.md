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

The exact standalone checker `verify_logistic_binary16.py` requires Python 3 only. It evaluates all 15,361 IEEE binary16 inputs for each map by integer arithmetic and nearest-even binary search. It exhaustively labels successor graphs, cycle states, basins and transient distances; it compares reported exact values and counts differing successor edges. `CENSUS.json` gives complete cycle words and SHA-256 hashes of the little-endian 16-bit successor arrays.

A separately implemented binary16 numerical conversion check using NumPy agreed on all 30,722 successor edges. Such agreement is supplementary and not needed for the exact-integer enumeration. The verification is exhaustive on the finite domain only and does not apply to continuous logistic dynamics or all arithmetic evaluation conventions.
