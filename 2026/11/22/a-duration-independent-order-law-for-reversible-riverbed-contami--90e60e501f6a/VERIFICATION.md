---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Conservation gives export as initial mass minus terminal M+B; in the AB protocol the propagator is P_B P_A. For positive rates, the two eigenvalues of each generator are distinct, with difference κ_i>0. The coefficient of Q_i in its exponential is the positive divided difference (exp(t_i λ_+)−exp(t_i λ_-))/(λ_+−λ_-), exactly h_i. Thus the export difference is h_A h_B times 1^T[Q_A,Q_B] applied to the initial vector. Using 1^T Q_i=(−u_i,0) gives the advertised row (α,β), including the order sign. The load interpolation has opposite endpoint signs iff αβ<0; if only one coefficient is zero it ties at the corresponding pure load, and if both are zero it ties everywhere. The example gives (−1,1) with all rates increasing. The short-stage expansion follows from h_i=t_i+O(t_i²). The frozen verification script was inspected, not executed; the universal check is the independent algebra, not the 3,435 reported finite assertions.

## originality

PASS

Qualified best-of-knowledge PASS for the explicit two-stage terminal-export classification, not for matrix-exponential or commutator identities. The classical algebra supplies the proof; the checked literature and published comparisons do not establish the same matched-duration load threshold.

## value

PASS

A source-free reversible-storage model poses a natural two-stage intervention comparison. The exact answer rules out a duration-driven preference reversal yet allows a sharp initial-loading reversal even when all three rates rise. That distinction gives a useful complete benchmark, not a new matrix trick. It is not a field prescription, evidence of parameter calibration, or a rule for arbitrary multistage schedules.

The dated certificate retains the supplied scientific assessment, sources and limitations.
