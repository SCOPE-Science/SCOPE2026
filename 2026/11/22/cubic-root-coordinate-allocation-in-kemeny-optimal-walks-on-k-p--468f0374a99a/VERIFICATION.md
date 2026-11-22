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

# Computational and analytical verification

The complete source `rook_kemeny_check.py` accompanies this result. It requires only the Python standard library and computes exact rational inverse traces on the full \(pq\)-vertex system independently from the claimed tensor spectrum, followed by scalar root, exact benchmark, optimizer, and asymptotic checks. Its verified output reports **990 assertions** passing. These calculations are finite sanity checks; the all-size claim follows from strict convexity, the exact eigenvalue decomposition and derivative sign proof in `RESULT.md`.

The optimized stochastic kernel has positive weights on both edge classes and zero diagonal holding. The analytic proof covers every integer \(p,q\ge2\), including the square case \(p=q\), whereas the large-\(q\) formula assumes \(p\) fixed. The fastest-mixing gap is established for a specific globally SLEM-optimal kernel on \(K_2\square K_q\); it makes no uniqueness assertion about other SLEM minimizers. No external or independent audit is represented.
