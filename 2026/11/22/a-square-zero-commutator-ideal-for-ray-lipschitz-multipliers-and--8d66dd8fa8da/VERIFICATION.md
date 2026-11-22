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

# Verification

Analytic check: map \(f\mapsto(f(0),(\Delta f_n))\) is an isometry onto \(\mathbb C\oplus_1\ell_\infty\) or \(\mathbb C\oplus_1c_0\). Binomial expansion gives the stated derivative rows. For fixed \(m\), the coefficient remainder from \((1-q^{-1})^{m+1}U_qH\) has tail row norm \(O_m(1/n)\); hence it is compact. The Hardy model has essential norm one by finite-row upper approximants and a compact-adjoint lower bound. Dirichlet/Abel cancellation gives \(\| (I-P_N)HU_qH\|=O_q(\log N/N)\). Thus the square is compact and the exact Calkin class is proved. Separately, every bounded-multiplier/parent-shift word has multiplier-times-shift normal form; two commutator factors force a product of two \(O(1/n)\) symbols, hence a compact multiplier. Norm closure proves the ideal is square-zero.

Computational check: execute `python verify.py` with Python 3. The observed output is `RAY_CALKIN_COMMUTATOR_CHECK_OK 17484`. The finite tests check matrix identities over `fractions.Fraction` inputs and numerical Abel-bound spot checks; no finite computation verifies an infinite claim.

Limits: no independent audit performed; references and bibliographic residual risks are in REVIEW.md and AUDIT.json.
