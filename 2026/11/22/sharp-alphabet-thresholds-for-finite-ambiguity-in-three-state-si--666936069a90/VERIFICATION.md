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

The proof uses a complete classification of letter patterns that force unbounded ambiguity by pumping and two explicit 48-element semigroup closure certificates. `matrices_X.csv` and `matrices_Y.csv` are sorted complete lists of reachable integer path-count matrices encoded as six coordinates.

Run `python3 verify.py` next to both matrix files. It checks the 23 legal letter generators in each case, exactly 48 reachable matrices in each closure, all generator products, the maximal \((1,3)\) entry four, every ordered binary transition pair, the unary bound and three witnesses. It reports `VERIFY_OK`.

Separately run `g++ -O2 -std=c++17 verify.cpp -o verify_cpp && ./verify_cpp`. It uses independent full three-by-three matrix arithmetic and prints the same checks and `VERIFY_OK`. Both programs were run successfully using these exact package contents.

These finite checks prove the infinite-word upper bound because all word products lie in the certified closed matrix set; ordinary bounded-length enumeration alone would not. The model review is not an independent audit. This verification does not cover automata with skip edges or more than three states, nor does it exclude undiscovered equivalent literature.
