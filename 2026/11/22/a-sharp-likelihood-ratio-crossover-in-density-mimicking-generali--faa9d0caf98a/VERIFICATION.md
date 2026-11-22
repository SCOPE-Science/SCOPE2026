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

# Verification and reproducibility

The mathematical certificate is the infinite-index proof in RESULT.md, specifically the exact adjacent-ratio formula, the unique sign transition of the hyperbolic-cosine curvature expression, and the positive-level one-crossing lemma. The solution of the critical rate equation is unique by strict decrease of the logistic average; no numerical optimizer is required for that conclusion.

Run the embedded standalone checker from the extracted package root:

```sh
python3 verification/check.py
```

Observed output from this package:

```text
PASS: exact witness; mode and log-concavity slices; one-turn likelihood ratios; sharp crossover checks
```

The checker uses only the Python standard library and includes exact rational arithmetic for the sign witness:
\[
\left(R_1/R_0\right)^4=(6/5)^5/2>1,\qquad
\left(R_2/R_1\right)^4=(50/51)^5/2<1.
\]
It tests selected rates and shapes, finite probability sums with explicit upper bounds on omitted tails when used to substantiate normalization accuracy, local strict log-concavity at numerically resolvable indices, and sample adjacent likelihood-ratio sign patterns. These finite experiments do not certify statements quantified over all parameters or infinitely many integer indices; those statements rest entirely on the analytic proof. No external independent audit was performed.
