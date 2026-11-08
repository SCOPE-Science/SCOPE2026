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

The proofs of the tree-lift bound, the sharpness constructions, and the basin formula are given in `RESULT.md`. `verify_tree_grafts.cpp` performs direct labelled three-color iteration and checks every state's first periodic-entry time, least period, and destination-orbit basin against the claimed formulas on thirteen finite clique-graft systems. The complete machine output is `direct_enumeration.log` and ends `ALL_CASES_OK`. The tested cases include single and multiple attachment roots, a star, internal branching, and both even- and odd-length paths.

`verify_height_lifts.py` separately implements the integer-height comparison and checks it against the direct color rule for 7,000 deterministically seeded random rooted-forest grafts (three to six clique vertices, at least one attached vertex and up to fourteen attached vertices). It checks tree-edge one-Lipschitzness throughout and the forced-wave limit. Its output `height_comparison.log` ends in `INDEPENDENT_HEIGHT_CHECK_OK`.

Reproduce with:

```sh
g++ -O2 -std=c++17 verify_tree_grafts.cpp -o verify_tree_grafts
./verify_tree_grafts
python3 verify_height_lifts.py
```

The two programs test finite instances and are not substitutes for the all-size proof. There is no third-party independent scientific audit, and no formal proof-assistant certificate is asserted.
