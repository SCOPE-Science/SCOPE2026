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
# Reproducible finite verification

Compile `checker.cpp` with a C++17 compiler, for example `g++ -std=c++17 -O2 -Wall -Wextra -pedantic checker.cpp -o checker`. Run `./checker --tables` in a directory where the output CSV files may be written. It will regenerate `profiles.csv` and `orbits.csv` and check the semantic definition against a separate rectangular-fibre algorithm for every one of the \(65{,}535\) nonempty teams and \(24\) atoms, a total of \(1{,}572{,}840\) pairwise checks.

The checker asserts the exact \(1{,}342\)-profile count, the \(125\)-orbit count, the minimum-world distribution through the sharp bound \(10\), and orbit sizes and representatives. Successful execution prints `TEAM_CI4_EXHAUSTIVE_OK`. The table files are complete rather than samples. The encoded team is a \(16\)-bit indicator of assignments, the profile a \(24\)-bit indicator of atomic truth, and variable orders are fixed in `checker.cpp` and `RESULT.md`.

This verification is exact for the finite Boolean assignment space and does not constitute an independently performed mathematical or historical-priority audit; the independent-audit channel remains unperformed.
