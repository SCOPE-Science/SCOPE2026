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

# Verification and boundaries

The complete exact recurrence and twelve-column seed table in `RESULT.md` establish the statement for every positive column length; the finite programs are independent checks of their implementation and of the stated coefficients, not an attempted proof by sampling. Run `python3 verify_chase.py` and compile/run `verify_gauss.cpp` using `g++ -std=c++17 -O2 -Wall -Wextra verify_gauss.cpp -o verify_gauss && ./verify_gauss`. The captured files `chase_output.txt` and `gauss_output.txt` are the actual successful outputs.

The Python code enumerates every allowed three-bit initial column and tests the terminal boundary through length 300, including verifying all eight 12-periodic sequences. The C++ code constructs the complete binary closed-neighborhood matrix for each 3-by-n grid, applies full pivot elimination, enumerates all binary free-variable solutions, replays all vertex parities, and compares the exact cardinality histogram through length 80. The two checks use distinct algorithms. The proof separately shows that there are exactly eight possible first columns and explains why its periodic table covers all lengths.

The previously established minimum odd-domination numbers of three-row grids are not novelty claims. The complete weight distribution is not independently certified and may have been recorded in inaccessible or unindexed literature. An unrelated inaccessible source cannot establish an originality guarantee.
