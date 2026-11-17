---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

In finite m+1 dimensional cooperative ODE with increasing concave C³ contamination h_i(0)=0 and q_i=h_i′(0)>0, the arrowhead Metzler Jacobian has Perron bound sign of R-1 where R=d/γ+Σ b_iq_i/(γδ_i). Concavity and scalar equilibrium relation yield unique positive endemic equilibrium iff R>1 and order-comparison global attraction. Linear dominance yields R<1 exponential clearance; positive linear left null vector and LaSalle gives R=1 global convergence. Strict convexity of Σa_i/δ_i gives unique KKT water-filling δ_i=max(d_i,sqrt(a_i/(λ c_i))) and unique finite B* if d<γ and baseline R>1. At R=1 the Perron/stable projection and quadratic nonlinear remainder yield V′=-(Λ/C²)V²+o(V²), with C=1+Σb_iq_i/δ_i², Λ=γ+Σ(b_i/δ_i)(q_i²/δ_i-h_i″(0)/2)>0; positivity excludes a purely exponentially stable orbit, so t x(t)→C/Λ, t y_i→(q_i/δ_i)C/Λ for every nonzero initial state. Independently verified two-class exact critical budget sqrt(2)-1/2, threshold index=1 and exact symbolic C/Λ expression; finite numerical runs not proof of t→∞.

## originality

PASS

Known Metzler epidemic thresholds, KKT inverse-rate allocation and generic critical center manifold t^-1 decay individually are credited. The target is a joint sharp optimization and nonlinear curvature-dependent critical prefactor for finite heterogeneous aerosol classes with arbitrary concave contamination curves. Nguyen–Porter analyzes original hypergraph closure and numerical heterogeneous-size/removal cases; the full Resultary 2026-11-08 heterogeneous *networked* critical extinction theorem assumes fixed uniform δ/σ and arctan, lacking class-wise optimal budget and general h_i″ dependence, and cannot be directly specialized to the submitted full class. No broader prior theorem found that entails the whole final claim without additional analysis. Best-of-knowledge O PASS with theory-coverage risk.

## value

PASS

A concrete ventilation budget threshold separates global persistence, critical algebraic clearance and exponential eradication. Sharp class allocations together with explicit t^-1 coefficients have natural use in comparing deterministic finite-class aerosol controls; the critical prefactor depends on response curvature and is not just an algebraic restatement of the linear invasion index.

The dated certificate retains the supplied scientific assessment, sources and limitations.
