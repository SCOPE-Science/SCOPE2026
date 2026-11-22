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

# Reproducibility and verification

The accompanying `verify.py` requires Python 3.9 or later and only its standard library. Executing `python verify.py` from this package produces:

```text
PASS: 2516 exact rational witness/range tests
```

The checker uses fractions with exact integer numerators and denominators. It constructs the lower- and upper-endpoint symmetric fractional matching matrices at every graph order from 2 through 160, verifies every vertex degree equals one, checks that all edges have length one or two, and calculates the exact long-edge objective. It also verifies the integrated endpoint formulas for all reduced rational separations in the specified range having denominator at most 120, and checks representative boundary and interior cases.

The finite script does not prove the infinite statement or certify novelty. The analytic proof supplies parity and modulo-four inequalities for every finite graph order, establishes attainability by explicitly repeating finite blocks, and disintegrates the continuum coupling over all real residues. The script tests its finite realizations, rather than extrapolating from sample cases.

Independent audit: not performed. No external correctness certification is claimed.
