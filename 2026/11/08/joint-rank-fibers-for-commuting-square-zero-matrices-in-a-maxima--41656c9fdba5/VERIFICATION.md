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

# Reproducibility and limits

The proof in `RESULT.md` establishes the theorem for all prime powers and all positive block sizes; these tests are finite checks only. `check.cpp` enumerates all prescribed block-centralizer possibilities for \((q,r)=(2,1),(2,2),(3,2),(4,2),(5,2),(2,3)\), evaluating square-zero constraints and matrix ranks via arithmetic in the relevant finite field. `full_enum.cpp` independently scans all \(65,536\) binary matrices in the \(4\times4\) case, testing multiplication, commutativity, squareness, and ranks without using the commutant representation. `formula.py` evaluates the exact product formula with Gaussian coefficients and independently compares the count vectors at those six parameters. The code uses C++17 and Python 3 without extra dependencies.

To reproduce, compile `check.cpp` and `full_enum.cpp` as C++17 and execute; run `python3 formula.py`. Compare their standard outputs respectively with `check_output.txt`, `full_output.txt`, and `formula_output.txt`. The exact outputs in this package were produced by executing these source files. Finite checks do not certify that no prior theorem implies the formula, and independent mathematical validation has not occurred.
