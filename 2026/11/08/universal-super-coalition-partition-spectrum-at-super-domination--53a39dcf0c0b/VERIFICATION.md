---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The five-vertex claim and its minimality are established by the explicit feasible-pair lists and the complete connected four-vertex table in `RESULT.md`. Check a proposed pair by testing for a selected neighbour exclusive to each omitted vertex. This test does not require enumerating all five-vertex graphs to establish the obstruction.

The original `verify.py` uses the witness condition and exact unordered set partitions to check a wider range of graphs. Its subcheck `SAME_SET_POLYNOMIAL_DIFFERENT_COALITION_SPECTRA_OK` concerns the two six-vertex examples in `RESULT.md`; it does not check the five-vertex cutoff. To reproduce that six-vertex subcheck together with the rest of the script, run `python3 verify.py` using a standard Python 3 interpreter.
