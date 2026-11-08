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

The mathematical argument is analytic and covers every admissible real \((d,c)\) and positive weight triple. The included `cimmino_verify.py` is an independently executable, standard-library-only numerical diagnostic. Invocation: `python3 cimmino_verify.py`. It checks 320 random valid Gram parameters, 24,000 arbitrarily weighted comparisons, five exact transition points and a rational example; the reported count is 24,005. These finite experiments do not establish universality or independence, and numerical minimization is not used as a theorem.

The positive-definiteness determinant, the orthogonal swap symmetry, the algebraic two-mode eigenvalues, monotonicity of the smaller eigenvalue, the active-mode crossing and the two rate branches are explicitly proved in `RESULT.md`. The original source date is taken from the first arXiv posting (2026-05-23), not a journal or revision date. Full older optimal-scaling literature remains a historical-priority limitation.
