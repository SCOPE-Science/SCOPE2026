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

Run the two self-contained standard-library Python programs with `python3 tests/verify_dynamics.py` and `python3 tests/verify_maxcut.py`.

The first reconstructs every connected labelled simple graph on two through five vertices and enumerates all chip states in the necessary \(0\) through \(2d(v)-1\) ranges. It compares primitive-two mass histograms from direct two-step simulation to independently constructed cut polynomials, also confirming contiguous support and extremal coefficients. In the recorded run it checked 771 connected graphs and 1,769,796 configurations, finding 102,942 immediate primitive-two states.

The second uses a separate graph and update implementation, computes maximum cuts exhaustively for 139 test graphs of orders two through eleven, and constructs a state at every mass inside each maximizing-cut interval; every constructed state is checked by actual two-step updates. Endpoint configurations from distinct oriented maximizing cuts are checked to be distinct. It checked 2,212 oriented maximum-cut witnesses. See `tests/dynamics_output.txt` and `tests/maxcut_output.txt` for the exact output.

These tests are finite and do not prove generality or NP-completeness. The written proof supplies both infinite-domain and complexity arguments. Only the self-review was conducted; no independent audit is represented.
