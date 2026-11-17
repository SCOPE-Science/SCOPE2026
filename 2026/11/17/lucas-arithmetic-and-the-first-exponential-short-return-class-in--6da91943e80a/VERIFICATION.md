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

# Exact checks

`verify_graph.py` was executed directly and produced the attached `graph_output.json` with certificate `PASS`. It enumerated every permitted local block for return times 1 through 5, computed every cyclic strongly connected component, and evaluated each complete determinant polynomial with exact-integer trace/Newton recurrences. In particular the 1024-state graph at time 5 has 1042 permitted edges, with one singleton loop and one size-64 cyclic component with 74 internal edges. The cyclic determinant is exactly `(1-z)(1-2z^5)(1+z^5-z^10)^2`.

`verify_direct.cpp` was compiled with `c++ -std=c++17 -O2` and executed. It independently reconstructed the local update with bit operations and exhaustively enumerated all `2^n` configurations for each `n=1,...,20`, comparing return times 1 through 5 against the exact formulas. Output terminates with `ALL_EXHAUSTIVE_CHECKS_PASS n=1..20`.

The finite direct census is a cross-check; the all-length conclusion derives from the finite symbolic graph and determinant identities. No independent external audit has been undertaken, and no claim is made about eventual basins or return times beyond five.
