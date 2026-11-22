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

# Reproducible verification

Use Python 3 to run `python3 verify_parity_independent.py`; its exact recorded stdout is `python_output.txt`. It directly generates all frontiers and membership trace families at heights two through four, checks every ancestor antichain against the criterion, and asserts equality; all checks print zero discrepancies and terminate with `PY_PASS`. The height-four independent trace census is 73,901 even-class shattered supports and 73,902 odd-class shattered supports.

Use `g++ -O2 -std=c++17 verify_parity_cpp.cpp -o verify_parity_cpp` followed by `./verify_parity_cpp`; recorded stdout is `cpp_output.txt`. This second independently written program enumerates every trace at heights two and three, matches the criterion and parity-family counts, and checks recurrence degrees and top coefficients through height five. It terminates with `CPP_PASS`.

These checks are bounded exhaustive computational checks on the stated finite input heights only. They are not a substitute for the general proof, and no formal proof assistant or independent external audit was used.
