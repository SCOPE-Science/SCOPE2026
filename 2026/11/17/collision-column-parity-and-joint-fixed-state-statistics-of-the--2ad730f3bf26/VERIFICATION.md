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

# Verification record

Run `sh run_checks.sh` from the root of the package. The script compiles two standard C++17 programs, runs the independent Python 3 polynomial evaluator, compares their recorded outputs, and additionally checks complete bivariate histogram equality for widths two and three.

- `checks/verify_direct.cpp`: enumerates all \(16^{2n}\) microscopic configurations for \(n=2,3\), performs the actual streaming and collision operations, and prints the particle-count and collision-column histograms.
- `checks/verify_formula.py`: constructs the bivariate polynomial independently by integer polynomial convolution; checks the exact total formula, parity and complement symmetry for \(2\le n\le10\).
- `checks/verify_transfer.cpp`: constructs the local update constraint graph on 65,536 column-pair states and enumerates closed length-three and length-four walks, including the full weighted width-four histogram, without using the collision-column classification.
- `checks/*.out`: literal output recorded from successful executions of these three programs. Executables are intentionally not embedded; source files are complete.

Checked counts: the direct and formula implementations agree coefficient-for-coefficient at widths two and three; the independently built transfer graph gives 566 and 2,060 at widths three and four; its complete width-four weighted histogram equals the polynomial output; all formula checks through width ten passed. The infinite-circumference theorem and Gaussian limit follow from the explicit proof and analytic generating function, not from bounded enumeration.

The original 1973 and 1976 publisher full texts were not accessible; source-priority comparison is qualified accordingly. No independent external mathematical verification has been performed.
