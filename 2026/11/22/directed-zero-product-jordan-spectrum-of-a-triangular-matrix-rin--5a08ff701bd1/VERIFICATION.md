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

Run `python checker.py` with Python 3.10 or later and SymPy 1.12 or later. The self-contained checker enumerates field-valued triangular matrices over the prime fields of orders 2, 3 and 5 and the extension field of order 4, forms zero-product directed adjacency with no loops, then independently checks the predicted characteristic polynomials, complex/rational ranks and zero-Jordan chain counts. The observed stdout is in `verification_output.txt`. The universal theorem is proved by the symbolic invariant-subspace argument in `RESULT.md`; finite computations cannot establish it for all prime powers.

The proof is over the complex numbers. In particular the numbers \(q\) and \(q-1\) are nonzero scalars in the decomposition, not elements reduced modulo the field characteristic. The 2013 structural source could not be fully examined and remains a publication-priority risk.
