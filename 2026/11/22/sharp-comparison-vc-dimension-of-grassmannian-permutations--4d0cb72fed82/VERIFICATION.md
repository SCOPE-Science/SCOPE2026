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

The theorem's all-order upper bound reduces to two complete finite trace enumerations: no three-query support is shattered on four positions, and no four-query support is shattered on six positions. These are checked by independent construction strategies in `verify.py` and `verify.cpp`; the mathematical hereditary reduction is given in `RESULT.md`. The lower bound is proved constructively for every order using ordered blocks of positions. The finite online assertion at six positions is independently checked by `check_tree.cpp` against `tree_n6.txt`. No claim of external or independent mathematical certification is made.

To reproduce from this directory: `python3 verify.py`; compile and run `verify.cpp` with a C++17 compiler; compile `check_tree.cpp` and run it with the path `tree_n6.txt`. Tests cover orders two through eight; they do not constitute an all-order computational proof. No arbitrary-order Littlestone claim is offered.
