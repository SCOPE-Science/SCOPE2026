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

# Verification of fixed-order Rule 184 one-sweep image

The mathematical proof uses the exact in-place sequential site equations, a complete necessary-and-sufficient output-language characterization and a fully explicit inverse. The four-state cyclic transfer graph then gives an exact formal rational generating function. The infinite family is established by those arguments rather than a finite test.

Run `g++ -O2 -std=c++17 checks/sweep184.cpp -o /tmp/sweep184 && /tmp/sweep184`, `python3 checks/transfer.py`, and `python3 checks/symbolic.py` from the directory containing these documents. The corresponding captured outputs are `checks/sweep184.out`, `checks/transfer.out` and `checks/symbolic.out`, respectively. Each program is self-contained aside from a C++17 compiler and Python 3 with SymPy for the symbolic stage. `checks/REPRODUCE.md` gives the specific commands and scope.

The C++ program independently evaluates every input and prospective output on all labelled rings from circumference three through eighteen, testing the three boundary/pattern conditions and replaying the constructed predecessor. The transfer program independently forms the graph, compares its exact trace/boundary formula for lengths three through thirty-four and checks the recurrence. The symbolic program checks the determinant and rational generating function exactly.

Limits: these calculations are finite corroborations; the general theorem requires the proof in `RESULT.md`. They do not establish arbitrary update-order results, long-time convergence, or independent mathematical certification. The cited historical literature is not exhaustively searchable.
