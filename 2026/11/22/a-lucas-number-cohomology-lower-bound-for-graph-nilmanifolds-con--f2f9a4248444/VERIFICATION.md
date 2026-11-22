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

# Exact arithmetic verification

Run `python3 verify.py` in the directory containing this file. No third-party libraries, external data or network access are required.

The program exhaustively enumerates the multiplicative monoid of the four signed two-by-two matrices and confirms its cardinality is twenty-five. It checks all twenty-five coordinates of the integral annihilator identity \(T(T^4-3T^3-4T^2+8T+8I)q=0\). The formal recurrence and four initial values justify the asserted closed form for every positive integer, rather than merely the tested range. An independent exterior-monomial enumeration checks the matrix-to-Euler interpretation for cycle lengths three through six. `verify_output.txt` records its output.

These computations validate the finite algebraic certificate. The proof additionally uses the explicitly described preserved grading, the standard cohomological Euler bound, and induced-subgraph support splitting. The package does not establish equality of the total Betti number with the stated lower bound and has not undergone independent mathematical auditing.
