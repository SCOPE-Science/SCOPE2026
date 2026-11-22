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

The accompanying `verify_affine.py` constructs the affine incidence graphs at orders two, three and four without external dependencies. It computes shortest-path distances by breadth-first search, derives every all-geodesics interval from the distance identity, enumerates every vertex set of each of the two relevant cardinalities, and compares the output with the theorem. In the order-four case it uses the explicit field \(\mathbb F_2[t]/(t^2+t+1)\).

The independent `verify_affine_cpp.cpp` constructs the prime-order graphs by a differently ordered incidence enumeration, uses Floyd–Warshall shortest paths and verifies every relevant vertex subset in orders two and three. It checks the number of selected line-vertices in each geodetic near-minimum set.

Reproduce with Python 3 using `python verify_affine.py`, then with a C++17 compiler using `g++ -std=c++17 -O2 verify_affine_cpp.cpp -o verify_cpp && ./verify_cpp`. The exact observed output is in `verify_output.txt`. These finite computations are consistency tests; the theorem for every existing affine plane follows from the incidence-axiom argument in `RESULT.md` and does not depend on finite testing. The q-plus-one gap is proven only for \(q\ge3\); order two is exceptional. No independent external audit has been performed.
