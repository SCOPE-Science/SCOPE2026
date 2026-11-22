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
# Verification scope

The proof in RESULT.md is the complete all-length argument. Its critical implications are an at-most-twelve one-heavy count, the monochromatic-incidence inequality \(22-T\le12\), forced deletion labels when \(T=10\), and the full mixed-pair incidence test. These arguments hold for every integer \(n\ge4\); direct checking of finitely many parameters is corroboration only.

Run these two standard-library programs from the package root:

```
python checks/brute.py
python checks/structural.py
```

`checks/brute.py` independently enumerates all size-eleven subsets of the entire ternary simplex at lengths four and five. It obtains twelve and twenty-four valid codebooks after testing 1,365 and 352,716 subsets. `checks/structural.py` directly evaluates every eleven-message candidate consistent with the proven monochromatic-incidence inequality, including all one-heavy-only and one-two-heavy configurations, for each integer length from 4 to 40. It checks the six outputs, the exact total \(12n-36\), and the two families' cardinalities. Stored stdout from the actual successful runs is in checks/brute.out and checks/structural.out.

No formal proof-assistant certificate or independent external mathematical review has been performed. A code execution timeout would not constitute a mathematical impossibility proof. This package contains all verification scripts and recorded outputs it references.
