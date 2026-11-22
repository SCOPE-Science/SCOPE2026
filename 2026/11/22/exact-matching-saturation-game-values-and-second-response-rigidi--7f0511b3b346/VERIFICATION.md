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

The exact minimax recurrences, ordinary smallest/maximal matching counts, every possible opening and every possible second response were checked using two independent implementations.

Run `python3 verify_recursive.py > recursive.json` and `g++ -std=c++17 -O2 verify_bottomup.cpp -o verify_bottomup && ./verify_bottomup > bottomup.json`. After parsing JSON, the output objects must agree and equal the accompanying `checks.json` data. Python uses constructive graph formulas and memoized recursive minimax; C++ uses explicit independent edge lists and evaluates every possible unmatched-vertex mask bottom-up, including all 1,048,576 masks for the dodecahedron. The comparison was performed successfully on the final artifact source files. No simulations or statistical approximations are used.

The proof applies only to the five specified graph skeletons. The 2012 original paper already implies the octahedral example. Historical priority beyond the inspected mathematical literature is not certified; independent mathematical review is unperformed.
