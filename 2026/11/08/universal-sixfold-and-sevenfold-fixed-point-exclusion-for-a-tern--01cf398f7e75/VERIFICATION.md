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

# Reproduction and limits

Run `python3 verify.py` with Python 3.9 or later, from the directory holding this file and the script. The script computes complete cyclic support-mask transition relations independently from binary-difference lifts and from ternary column enumeration. It checks the printed tables for multipliers \(6\) and \(7\), checks acyclicity off the zero mask, and directly enumerates all finite states for lags \(2\) through \(9\). It also verifies that \(T_2\) fixes all its nine states after eight updates.

Expected terminal markers include `MASK_GRAPH_OK`, `DIRECT_STATES_OK`, `SHARP_ENDPOINT_OK`, and `VERIFY_OK`. Computations are exact integers in \(\mathbb F_3\), with no randomized components and no dependencies beyond the Python standard library. The graph proof is finite because the row count is fixed at \(6\) or \(7\), independently of the arbitrarily large lag. The direct-state checks for lag at most \(9\) alone would not establish the theorem for every lag. The results are the subject of a self-review only, not an independent mathematical audit.
