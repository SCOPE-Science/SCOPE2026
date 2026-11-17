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

# Reproducibility and limits

Run `python check.py` with Python 3 and SymPy. This standalone file is included in the same package.

Expected output from actual execution:

```text
SYMBOLIC_N3_AND_N4_PATH_VARIATION_IDENTITIES_PASSED
EXACT_RATIONAL_DIMENSIONS_PARAMETERS_AND_STEP_WITNESSES_PASSED 105
ALL_WHITTAKER_PATH_VARIATION_CHECKS_PASSED
```

The checker reconstructs the smoothing and gradient matrices, proves the \(n=3,4\) rational-function identities symbolically in the positive parameter, and verifies exactly the first- and second-order regimes for \(2\le n\le12\) and five positive rational smoothing strengths (105 admissible parameter/order/dimension cases). It verifies a monotone jump with endpoint span greater than one in the second-order case at every tested \(n\ge4\). The proof for all real smoothing strengths and unrestricted sample sizes is the unrestricted algebraic argument in `RESULT.md` using the affine fixed space; finite checks do not prove it. Full text of de Jong–Sakarya (2016) was inaccessible in the available source channels, leaving a stated historical-priority risk.
