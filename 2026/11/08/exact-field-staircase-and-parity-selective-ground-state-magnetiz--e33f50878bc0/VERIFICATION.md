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

# Reproducibility of the finite checks

From the directory containing this file and the accompanying Python program, run:

```bash
python3 verify_triangular_ising.py
```

The script requires only Python 3's standard library. A completed replay returned normally and printed:

```text
PASS: exhaustive spin-configuration strata for n=3..6; 33864 configurations checked
PASS: all finite-difference identities, convexity, critical fields, and zero-field magnetizations for n=3..100
PASS: 2622 independently constructed almost-regular graphs for n=3..25, all edge counts
```

The first check enumerates every \(\pm1\) spin assignment for each graph \(T_n\) with \(3\le n\le6\). The second compares integer-valued sector formulas with independently listed successive differences and exact zero-field minima for \(3\le n\le100\). The third constructs a balanced-degree witness at every edge count for \(3\le n\le25\). There are no external datasets, floating-point tolerances, remote services or cached scientific dependencies.

These finite tests are corroborative only. The universal proof, including every physical field value and every \(n\ge3\), is the separate edge-switching and discrete-slope argument in RESULT.md. No finite search establishes the absence of equivalent historical results or constitutes an independent audit.
