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

Run `python3 verify.py` and `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify.cpp -o verify_bin && ./verify_bin` in a directory containing the included programs. Compare the output with `python.out` and `cpp.out`. The programs use only Python's standard library and a C++17 compiler. The Python checker includes a finite-field implementation for order four and directly checks every support through size three at orders two, three, four, and five. It exhaustively checks all minimum dominating sets only for orders two and three, and exactly checks Littlestone dimension by recursive state search at those two orders. The C++17 checker independently reconstructs orders two, three, five and seven, enumerates all supports through size three and checks every minimum dominating set at orders two and three.

The all-order optimal-set classification, no-triple upper bound, exact adaptive dimension, uniform first-order interpretation and topological classification are established by the written proofs and do not rely on finite enumeration. In particular, no computer check of a coordinatized plane verifies the existence or properties of non-Desarguesian planes in general. Publication priority and independent mathematical review remain open.
