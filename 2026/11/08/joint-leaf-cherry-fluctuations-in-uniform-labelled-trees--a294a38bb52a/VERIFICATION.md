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

Use Python 3 with no third-party packages:

```bash
python3 verify.py
```

Expected output starts with `VERIFY_OK 282379 exact and asymptotic-sign checks`. The checker independently decodes all Prüfer words for every labelled tree at orders five through eight and evaluates all five moments as exact rational numbers. It also compares the exact covariance sign for orders five through five hundred with the positive-sign proof, and checks the limiting covariance matrix and its correlation numerically. These computational checks are finite; infinite-order conclusions rely on the bijections, analytic inequalities, asymptotic expansions and the published local-pattern central limit criterion detailed in `RESULT.md`.

The binary-tree phylogenetic model is not used. The cherry statistic requires a center of **degree three**, not merely a vertex adjacent to two leaves. The unperformed independent audit is not represented as passed or certified.
