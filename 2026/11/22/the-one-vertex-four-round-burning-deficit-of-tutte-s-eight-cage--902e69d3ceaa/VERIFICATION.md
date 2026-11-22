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

# Reproduction and exact claim boundaries

The sole theorem is for the particular thirty-vertex duad–syntheme Levi graph. A length-four ordered source tuple produces four-round coverage \(B_3(x_1)\cup B_2(x_2)\cup B_1(x_3)\cup B_0(x_4)\), even if it is not itself a legal ignition sequence. The theorem proves that the largest possible coverage is 29, gives a complete equality classification and derives the ordinary burning number five. The results are neither extrapolated beyond this graph nor presented as a count of genuine four-round burning sequences.

Reproduce with `python3 verify_python.py`, and with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_cpp.cpp -o check_cpp && ./check_cpp`. Both are standalone source files and need no network access or external data sets. On replay, Python printed `CHECKER_PYTHON_OK`, verified the thirty-vertex distance profiles, an explicit point–line duality, all 900 two-radius intersections and all 810,000 four-source tuples. C++ printed `CHECKER_CPP_OK` after independent construction and the same complete exhaustive enumeration. The output of both is maximum coverage 29, count 2,160, source counts 72, per ordered antipodal pair nine and the second-source split 720/1,440. Both checked that every maximum-coverage tuple is a legal source sequence. Python verified a legal five-ignition construction.

The lower bound on four-round coverage is analytic: a first radius-three ball leaves eight distance-four vertices; the subsequent radius-two, radius-one and radius-zero balls can cover at most four, two and one of these vertices. The equality count follows from the explicit six-plus-eight case split and a verified part-swapping automorphism. The verification code is a transparent finite cross-check of these mathematical steps, not a proof for other graph families. There has been no independent external scholarly validation or auditing.
