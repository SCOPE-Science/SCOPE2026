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

The exact graph theorem, planar-dual interpretation, sixteen-state transition rules and matrix determinant reduction are in `RESULT.md`.

Run `python3 verify/check_wheel.py` to compare direct edge-subset enumeration with the independent transfer and recurrence calculations; run `g++ -std=c++17 -O2 verify/check_wheel.cpp -o check_wheel_cpp && ./check_wheel_cpp` for a separately implemented union-find enumeration; run `python3 verify/check_symbolic.py` (with SymPy installed) to verify the full symbolic polynomial determinant. The output from these commands was saved as `verify/outputs.txt`.

Finite exhaustive checks cover all \(2^{2m}\) subsets for each wheel with \(3\le m\le9\) (Python through eight, C++ through nine), not just random samples. Symbolic identity verification checks all coefficients in both indeterminates and, together with the combinatorial automaton argument, supports the unrestricted-order formula. Finite tests alone do not establish an infinite theorem. No outside independent mathematical audit has been performed.
