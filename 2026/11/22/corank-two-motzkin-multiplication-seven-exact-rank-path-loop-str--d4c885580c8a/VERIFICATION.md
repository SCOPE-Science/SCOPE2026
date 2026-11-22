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

`motzkin_product_checker.py` uses only Python 3 standard-library modules. Execute `python motzkin_product_checker.py` from the directory containing the extracted files. The output must match `checker_output.txt` for all four tested sizes, with 625, 6,561, 38,416 and 160,000 ordered products, respectively. The checker independently glues diagrams and classifies the resulting connected components rather than invoking the closed formula to generate observations.

This checks finitely many instances and does not certify all natural-number dimensions. The general conclusion rests on the exhaustive intersection-and-hook case analysis in `RESULT.md`. In particular, the unusual two-hook shared-vertex rank-rescue case and the convention that an isolated middle vertex counts as a floating path were included in the direct graph enumeration. No external independent audit has been performed.
