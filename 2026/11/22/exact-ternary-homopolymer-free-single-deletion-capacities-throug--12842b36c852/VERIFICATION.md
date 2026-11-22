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

# Computational verification

The checks below are finite and reproducible from the companion files. The proof-critical enumeration is implemented directly in `verify_exact.cpp`; no incumbent from a heuristic solver is used as an upper-bound certificate. The compatibility graph is rebuilt from the channel definition. In a recursive call, a proper coloring of the remaining compatibility graph bounds how many more vertices can belong to a clique, and all unpruned alternatives are considered.

On a clean extraction, compile the C++ file with `g++ -O3 -std=c++17 verify_exact.cpp -o verify_exact`, then invoke `./verify_exact 2`, `./verify_exact 3`, `./verify_exact 4`, `./verify_exact 5`, `./verify_exact 6`, and `./verify_exact 7`. Outputs must respectively report maxima \(1,3,4,8,12,22\); the length-seven call reports \(1,526,900\) recursion nodes. `optimal_codebooks.json` gives directly checkable feasible sets for the same maxima.

Run `python3 verify_fractions.py`. This uses only Python's standard library and `fractional_certificate.json` to verify exact rational primal/dual feasibility and equal objectives \(3/2,3,9/2,42/5,27/2,99/4\) for lengths \(2\) through \(7\). The checker independently regenerates all possible words and deletion descendants, including outputs containing adjacent repeated letters.

For a separately formulated integer-model cross-check, run `python3 alternate_milp.py` with a recent NumPy/SciPy installation. It creates output-incidence inequalities independently and requires an optimizer status of proven optimality, not a time-limit status. No solver logs are accepted as proof without the exact mathematical reduction and verified arithmetic.

The base case at length \(1\) has three possible letters and one common empty descendant, giving integer and fractional optimum \(1\). The tests establish no claim for longer lengths. This package has not been independently mathematically audited.
