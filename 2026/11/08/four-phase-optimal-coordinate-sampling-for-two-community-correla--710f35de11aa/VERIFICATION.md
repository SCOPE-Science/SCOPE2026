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

# Reproducibility

Run `python3 artifacts/verify.py` from the extracted package root with a Python 3 standard library installation. It constructs every full rational block matrix in a finite parameter grid, checks the displayed optimal probability via an exact positive-semidefinite test, and tests non-improvement inequalities for block-uniform and asymmetric sampled competitors. It also checks four phase witnesses and the sharp uniform-sampling comparison in dimensions corresponding to \(2\le q\le24\). The included `artifacts/checks.txt` is the captured output of this exact program.

The program checks finite examples and is not an exhaustive check of all real correlation parameters, probabilities, or dimensions. The infinite statement is justified by the symbolic eigenspace and concavity proof in `RESULT.md`. No independent mathematical audit has been performed.
