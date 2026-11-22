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

# Verification and reproducibility

The runnable package includes `check_supports.cpp`, `check_formula.py`, `check_constructions.py`, and `run_checks.sh`, plus `verification_output.txt` containing the observed output. From the directory containing these files, run `sh run_checks.sh` with a C++17 compiler and Python 3 (standard library only). The runner compiles the program in the current directory, executes the programs, and prints the coefficients independently computed from all three approaches.

The C++ program constructs actual Kneser graphs from all triples, computes distances by breadth-first search for each vertex, verifies that every pair of distinct intersecting triples is at distance two and every disjoint pair at distance one, enumerates every potential optimum defender subset through order twelve, and checks the actual Roman and totality rules. The Python formula enumerator compares the factorial census through order eighteen and separately classifies the order-ten one-overlap count. The direct construction tests verify explicit minimum assignments for each admissible case through order twenty. The output in `verification_output.txt` was recorded from successful execution; no preexisting or unrelated artifact is required.

Limits: These calculations are finite. They do not independently certify the all-order theorem, which rests on the forced-one lower bound and exact equality cases in RESULT.md. There has been no independent external audit.
