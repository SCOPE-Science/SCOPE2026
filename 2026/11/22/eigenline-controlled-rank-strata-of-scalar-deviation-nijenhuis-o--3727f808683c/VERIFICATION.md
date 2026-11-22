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

# Reproducible mathematical checks

Run `python VERIFY.py` from a directory containing the extracted file. Only the Python 3 standard library is required. The script independently enumerates all matrices in the tested scalar-rank-one-deviation stratum and checks the original left Leibniz Nijenhuis identity on all ordered basis pairs, without using the derived classification as the primary acceptance test. It then compares exact enumeration with the two-equation normal form, rank polynomial, and shifted-Jordan-index-three formula.

The included cases have \(d\in\{2,3,4\}\) and \(k=\mathbb F_2\) or \(\mathbb F_3\), with invertible actions having no rational eigenvectors, some rational eigenvectors, or entirely scalar action. The final success marker is `LEIBNIZ_GENERAL_RANK_ONE_SCALAR_DEVIATION_VERIFIED`.

These are finite consistency checks. The all-dimensional, all-characteristic theorem follows from the algebraic argument in `RESULT.md`; no finite experiment is claimed as its proof. Neither publication priority nor independent certification is established by the checker.
