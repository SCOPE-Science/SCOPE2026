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

# Verification of the elementary collapse

Run `python3 verify.py` from the extracted directory. The script requires Python 3.8 or newer and uses only its standard library. It constructs all two-subsets of the source ground set, calculates Kneser adjacency by disjointness, and checks the induced maximum-degree-one rule for every vertex subset at source orders five, six and seven. It checks the 24 added local faces and partitions their transported copies by unique external ground label.

The exact output is:

```text
n=5: intact_faces=261, fault_faces=285, extra_faces=24, free_face_pairs=12: PASS
n=6: intact_faces=747, fault_faces=795, extra_faces=48, free_face_pairs=24: PASS
n=7: intact_faces=1751, fault_faces=1823, extra_faces=72, free_face_pairs=36: PASS
UNIVERSAL_5_LABEL_COLLAPSE_CORE_PASS
```

Each of the twelve explicitly prescribed local pairs is checked against *every* remaining strict coface after previous pairs are removed, verifying actual elementary collapses. The arbitrary-order theorem is deduced from the independently proved five-source-label support reduction; three finite enumerations by themselves would not prove it. The published intact-complex sphere-wedge classification is cited as background and not re-certified here. Independent external audit has not been performed.
