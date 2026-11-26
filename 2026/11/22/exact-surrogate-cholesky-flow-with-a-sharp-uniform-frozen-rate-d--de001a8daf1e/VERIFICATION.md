---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Set p=ℓ². Then (1/p)'=2−2α/p gives the stated positive reciprocal formula, including α=0. More directly, h=g/ℓ satisfies h'=1−αh and h(0)=0, proving the exact coefficient and uniqueness on the full stated domain. The reciprocal formula gives 0≤(p(T)−α)T≤1/2, also at α=0. Φ is decreasing and (log Φ)'' is the variance under exponential tilting, so the ratio Φ(αT+1/2)/Φ(αT) is smallest at αT=0. Taking s=1, α=T⁻² as T→∞ gives p(T)T→1/2, proving sharpness at positive pivots. Squaring the exact ratio gives the rank-one fraction, attained in the limit with the given nonzero-residual PSD examples. For α>0, αg²≤(1−exp(−αT))/(1+exp(−αT))<1; comparison with the ordinary Schur complement preserves PSD. For α=0, the off-diagonal residual vanishes by PSD. The verification text's reference to ‘indefinite-stage recursion’ is a wording error; neither proof nor Finding covers indefinite matrices.

## originality

PASS

The closest primary paper gives exactly the surrogate ODE, initialization and the terminal-frozen expression, presenting the latter as a solution. The proposed exact formula differs from that expression when the rate varies. The primary treatment of Schur complements concerns the frozen coefficient, not the larger exactly integrated one. The strongest matching Resultary item is the assigned item itself; two inspected distinct Cholesky entries address different objectives. The supported distinct content is the correction, sharp uniform deficit and PSD compatibility of the corrected update, not the ODE model or Schur-complement technique.

## value

PASS

The paper's terminal freezing can lose over a fifth of a nonzero off-diagonal coefficient and nearly 38.1% of its squared update in the sharp limit. Quantifying that discrepancy and proving the same pivot-free PSD recursion can use the corrected coefficient answers a specific algorithmic question that solving the scalar ODE alone does not. The comparison is useful without a downstream reconstruction-error theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
