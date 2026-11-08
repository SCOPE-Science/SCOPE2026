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

# Verification of the finite \(B_5\) diameter certificate

Place `verify.py` and `verify_fast.cpp` in the same directory. Execute:

```bash
python3 verify.py
c++ -std=c++17 -O2 -o verify_fast verify_fast.cpp
./verify_fast
```

The two implementations use different generators and collision data structures; the C++ implementation additionally reduces by reflection. The first exhaustive run reports exactly \(1{,}028{,}790\) normalized candidate tuples through \(d=72\), \(342{,}414\) four-mark survivors, and the two stated final sets. The C++ run confirms a unique reflection-canonical solution, and reproduces the independently published earlier minima \(11,23,41\) at orders \(2,3,4\). Both programs assert their claims and exit with a nonzero status on a discrepancy.

The proof of exhaustiveness is a finite-domain partition into the nested integer ranges written in `RESULT.md`; it is not a heuristic test or inference from a timeout. The property tested is equality of multisets from complete nondecreasing index enumerations, not equality of ordered strings. This establishes the reported fixed finite theorem. No independent audit, formal proof assistant, or independent archival priority certification is asserted.
