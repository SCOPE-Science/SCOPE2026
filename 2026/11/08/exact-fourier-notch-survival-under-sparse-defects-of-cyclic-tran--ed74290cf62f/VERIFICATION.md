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

# Reproduction and boundaries

The theorem is proved for every odd prime \(p\), every \(k>b\ge1\), and every allowed sparse relocation. Reproduce the finite consistency checks with `python CHECK.py` using the Python standard library. The direct exact coefficient-fiber tests and independent numerical Fourier-sum comparisons, including multi-defect examples and a sharp \(r=p\) failure example, produced `CHECK_OK checks=33317`.

The checker is deterministic but tests finitely many cases. Universal validity rests on the cyclotomic minimal-polynomial argument and the two exact counting steps in `RESULT.md`. The correctness of source priority and the general theorem has not received independent validation. No numerical tolerance is used to establish the proof, and no empirical test is represented as an infinite certificate.
