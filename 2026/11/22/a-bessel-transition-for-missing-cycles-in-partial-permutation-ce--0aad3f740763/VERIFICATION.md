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

The exact combinatorial formula was independently checked by enumerating every partial injection on the underlying labeled point set, computing both partial-map compositions and comparing rank frequencies. Ten parameter pairs were tested, including \((m,\ell)=(3,2)\) and \((2,3)\), each with six points. The checker is `checker.py` and its exact captured output is `checker_output.txt`.

For the critical law, the checker also evaluated total-variation distances against the normalized infinite Bessel series at \((m,\ell)=(40,40),(160,160),(40,20),(160,80)\), with maximum reported distance below 0.008. Finite tests are only a cross-check: the mathematical statements for all positive dimensions and for infinite sequences follow from the domain-orbit bijection, dominated convergence and the weight-ratio concentration argument in `RESULT.md`.

Historical-priority risk remains: the 2020 finite-centralizer study and 1997 monograph were not reviewed in full. Independent mathematical audit has not been performed.
