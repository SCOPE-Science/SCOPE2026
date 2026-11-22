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
# Verification

The exact Python program `verification/verify.py` reconstructs the graphs, augmented face sets, every matching relation, complete Hasse-DAG acyclicity, and exact integer Morse differentials for both ascending and descending toggle orders. Integer reductions use only unimodular unit pivots and verify a zero remaining matrix. The ascending computations also derive direct independent mod-two simplicial homology; mod-two checks are corroborating and not a substitute for integral attaching maps.

Run from the extracted project root:
```
python3 verification/verify.py
```
The expected complete standard output is in `verification/expected.txt`. The final line is `ALL EXACT CHECKS PASS`. The existing Dürer \(n=6\) output is a control; the new classifications concern only \(n=7,8,9\).

There is no independent external audit. Mathematical proof uses discrete-Morse CW equivalence and classification of cellular \((d+1)\)-attaching maps into wedges of \(d\)-spheres by integer degree for \(d\ge3\). No higher-parameter extrapolation is verified.
