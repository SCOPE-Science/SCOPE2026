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

The all-order proof establishes a bitstring bijection and exact move correspondence for both closures. The following computations are independent finite cross-checks, not an infinite proof:

1. `python3 verify_binary_model.py` regenerates perfect matchings, compares every state of the binary model and its entire local-move neighborhood against direct enumeration for each \(5\le n\le14\) in the prism and Möbius cases, and checks the two exceptional frozen states precisely when predicted.
2. `g++ -std=c++17 -O2 verify_direct.cpp -o checker && ./checker` uses separate C++17 edge-mask enumeration, square-mask toggling and exhaustive breadth-first search to check component orders, edge counts, radii and diameters for each \(5\le n\le13\).

Both completed successfully when run from the packaged scientific sources. The resulting finite confirmations do not establish originality or independence. In disconnected cases the reported radius and diameter concern the nontrivial moving component only. Scientific priority is qualified by the directly relevant 2013 cyclic-fibonacene analogue and an incompletely accessible 2020 matching-count paper.
