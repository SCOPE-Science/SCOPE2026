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

# Reproducing the proof checks

Run `python verify_four_runs.py` using Python 3 with only its standard library. The certificate program implements independent factor-covering algorithms and compares the resulting two-position attractors with the exact proposed formulas.

Expected output:

```
FOUR_RUN_ATTRACTOR_VERIFY_OK phase_cases 1296 nondegenerate_exact_pair_cases 625 observed_pairs 1563 independent_direct_instances 181
```

The primary algorithm enumerates every distinct factor and unions all its covering occurrence intervals, then tests all position pairs for each word \(0^a1^b0^c1^d\) with \(1\le a,b,c,d\le6\). It compares the full size-two existence phase (all 1,296 inputs) and the exact complete pair set (625 inputs with all run lengths at least two). An independently implemented direct factor/occurrence scan compares all pairs for the 81 smallest quadruples, verifies canonical three-marker witnesses, and checks a fixed-seed sample of 100 larger input quadruples with run lengths up to 23. The algorithms do not access any external files or services.

The infinite correctness claim rests on the occurrence classification and case analysis in `RESULT.md`; these computational checks alone cannot establish results for arbitrary run lengths. A third-party audit and a definitive publication-priority review have not been performed.
