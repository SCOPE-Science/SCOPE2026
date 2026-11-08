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

## Reproducibility
Use Python 3 with SymPy installed. In the directory containing this document, run `python CHECK.py`. The exact symbolic assertions verify the residual-difference factorization, symmetric-sum identities, Vieta reduction, discriminant, converse identity, and the repeated-coordinate critical values. Supplementary tests evaluate 24 numerically specified cycle equations at four parameters, in both orientations. The current packaged checker passed all assertions.

## Limits of verification
Exact symbolic identity checks complement but do not replace the quantified proof in `RESULT.md`. Numerical instances do not certify any infinite family. Real root existence and exhaustiveness follow from the cubic's discriminant and four strict sign comparisons, not a finite numerical scan. Historical mathematical work is cited for context; independent audit has not been performed.
