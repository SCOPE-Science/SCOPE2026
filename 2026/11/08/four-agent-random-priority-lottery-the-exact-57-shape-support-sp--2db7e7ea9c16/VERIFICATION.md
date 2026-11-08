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

# Verification of the finite census

Reconstruct both exact exhaustive calculations in the same directory as the embedded source and data files:

```text
python3 verify_rsd4_support.py
g++ -O3 -std=c++17 rsd4.cpp -o rsd4
./rsd4
```

Both commands produce a `VERIFY_OK` line on success. Python independently enumerates 17,550 anonymous four-ranking multisets, canonicalizes 762 object-label classes, weights all 331,776 original labeled profiles and checks the complete `SPECTRA.csv` and `SUPPORT_HISTOGRAM.csv` files. C++ separately visits every labeled four-profile tuple and all 24 priority orders, checking the 57 shapes and each support-size frequency. Source files and both exact output tables are standalone, not references to another record or prior execution.

The verified claim is finite: it establishes counts only for four agents and four objects with strict rankings and uniform priority. The certificate uses exact arithmetic and exhaustive loops, not random trials, numerical extrapolation, optimization solver timeouts or an infinite proof. Independently authored source code paths are a scientific cross-check, **not** an external independent audit.
