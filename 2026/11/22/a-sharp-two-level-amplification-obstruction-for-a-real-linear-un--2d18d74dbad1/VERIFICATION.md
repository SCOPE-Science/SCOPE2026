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

The theorem is proved by the explicit block-row inequality and the exact four-by-four unitary witness in `RESULT.md`. Every step is valid for arbitrary \(k\ge1\), so no finite enumeration or sampled matrix search is used to infer an infinite-level statement.

`CHECK.py` uses exact symbolic matrix algebra to verify \(WW^*=2I_4\), \(Z^2=2Z\), \(Z=Z^*\), and the eigenvalues of \(Z/\sqrt2\). It also checks 27 seeded random matrices at each size \(k\in\{1,2,3,4,6\}\), testing the universal and row-compression inequalities. Run `python CHECK.py`. Observed output: `AMPLIFICATION_CHECK_OK 301`.

The most relevant primary work, arXiv:2611.13822v1, was inspected in its available full HTML text, including the non-Jordan classifications and ordinary norm-one result. Bibliographic novelty remains subject to discovery of older equivalent formulations. Independent audit is not performed.
