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

Run `python3 verify.py` under Python 3 without third-party dependencies. The script performs exact modular calculations, Hensel critical-root lifts, complete residue histograms through modulus \(3^7\), and direct Stirling recurrence / inclusion–exclusion comparisons. The final expected line is:

```
VERIFY_OK levels=1..7 direct_stirling_checks=726 critical_lifts=PASS square_fiber_histograms=PASS
```

The checks were executed on the complete standalone checker included in this package. Exhaustiveness is restricted to the explicitly tested finite moduli; the infinitely many levels are justified by the 3-adic proof. No independent audit has been performed.
