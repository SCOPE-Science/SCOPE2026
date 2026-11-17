---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: The resident logistic post-x-pulse state X0 has integral b∫X=R_x and transverse multiplier exp(-R_x) in (0,1). The invader linear multiplier m_y exp(dT-e R_x/b) is independent of phi. At equality, its within-cycle profile is E(t) before the y-pulse and m_yE(t) after it. Two exact per-period logarithmic balances on the smooth one-dimensional center manifold eliminate its unknown resident variation and give y_{n+1}=y_n-(f-ec/b)I_phi y_n^2+O(y_n^3), hence n y_n tends to the asserted reciprocal for sufficiently close positive data. I_phi is positive and has derivative (1-m_y)E(phi). The bf>ce strict inequality and local scope are essential. Inspected real verify.py numerical ODE checks; they alone do not prove all-parameter dynamics.

## originality

FAIL

FAIL: A prior October 26 published Resultary theorem handles precisely this constant-rate staggered two-species impulsive competition model as a special case of a much wider time-dependent/pulse-schedule setting, proving global instead of local critical 1/t extinction and its explicit phase envelope. Upon swapping prior x and y roles, its kappa=b_prior-(c_prior/f_prior)e_prior is f_new-(e_new c_new/b_new), and its k-cycle amplitude P(0)/(kappa∫P) is exactly [(f-ec/b)I_phi]^-1. The new derivative of the split I_phi is elementary and gives no independent surviving novelty.

## value

FAIL

FAIL: A correct local special case of a stronger existing global extinction/amplitude theorem and the elementary derivative of its already-defined periodic profile does not add a significant original invariant or boundary insight. The general global theorem resolves the same science with weaker hypotheses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
