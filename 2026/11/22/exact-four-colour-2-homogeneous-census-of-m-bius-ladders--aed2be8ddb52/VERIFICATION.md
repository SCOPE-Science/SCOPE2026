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

# Reproducibility

Run `python3 verify.py` with the Python standard library. The script generates the transfer matrix from its intrinsic local neighbourhood definitions and verifies its two 42-by-42 integer characteristic polynomials by exact Faddeev–LeVerrier recurrence; this is an all-coefficient finite certificate. It verifies Newton sums at widths 3–35, directly enumerates graph assignments for widths 3, 4, 5, constructs parity-complete twisted witness paths, and computes the full reachability closure of the 18-state 3-palette automaton (establishing the all-length lower bound).

Expected final marker: `VERIFY_OK`. Verified run outputs include `EXACT_CHARACTERISTIC_POLYNOMIALS 42+42 PASS`, `GENERATING_FUNCTION_COUNTS m=3..35 PASS`, `DIRECT_GRAPH_ENUMERATION 3 216 PASS`, `DIRECT_GRAPH_ENUMERATION 4 48 PASS`, `DIRECT_GRAPH_ENUMERATION 5 600 PASS`, `THREE_COLOR_REACHABILITY_OBSTRUCTION ALL_LENGTHS PASS` and `VERIFY_OK`. Finite enumerations do not establish all-order identities by themselves; the matrices and all-coefficient identities, with the transfer argument, are the unrestricted proof. No independent mathematical audit has been performed.
