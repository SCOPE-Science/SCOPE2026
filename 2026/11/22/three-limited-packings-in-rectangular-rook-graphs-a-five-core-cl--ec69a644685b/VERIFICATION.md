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

The classification and generating polynomial are proved mathematically in `RESULT.md`. The computations below are finite consistency checks, not a substitute for the unrestricted argument.

The standard-library Python program `verify_formula.py` computes exact coefficients from the seven summands and, separately, tests every vertex subset by explicit closed-neighborhood masks on boards up to four rows and five columns. Run `python3 verify_formula.py`; the exact expected text is `formula_output.txt`.

The standalone C++ program `verify_direct.cpp` enumerates all vertex subsets and tests every closed rook neighborhood using independent bitmask code. Compile using `g++ -O3 -std=c++17 verify_direct.cpp -o verify_direct` and run `./verify_direct`. The actual expected text is `direct_output.txt`, including the three-by-six, three-by-seven and four-by-six cases.

The further Python program `verify_shapes.py` independently identifies the bipartite components of all valid edge sets on five small boards. Run `python3 verify_shapes.py` and compare against `shapes_output.txt`. It reports no invalid component or mixed-center configurations.

For any other sizes, `verify_formula.py` exposes the integer-arithmetic `calc(m,n)` function. The proof is quantified over all \(m,n\ge3\), while the bounded tests have no such force. No expert or independent audit has been performed.
