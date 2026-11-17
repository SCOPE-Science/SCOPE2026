---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

With B=1+alpha xi>xi, R(x)=(x+xi)/(B+x) is strictly increasing. Logistic prey comparison first gives limsup x<=K. Predator comparison at critical delta=eta R(K) gives y->0; lower logistic comparison then x->K. The exact stable-filter ODE for w=(K-x)/y has coefficient -1+o(1) and forcing ->A=K/(B+K), so w->A. Taylor R(x)-R(K)=-R′(K) A y+o(y) gives y′=-beta y^p-Lambda y^2+o(y^2), Lambda=eta K(B-xi)/(B+K)^3. For 0<r=p-1<1, u=y^-r obeys u′=r beta+r Lambda u^(-(1-r)/r)(1+o(1)), yielding finite shift for r<1/2, logarithm at r=1/2, and fractional-power correction for 1/2<r<1; at p=2 t y->1/(beta+Lambda). Our independent high-precision solve_ivp at T=5000 verified (K-x)/y=0.57173,0.57166,0.57158,0.57158 for p=1.4,1.5,1.75,2 vs A=0.57143. Initial finite numerical test was unstable due near-zero y absolute tolerance; rerunning with tighter tolerance resolved it, not a mathematical contradiction.

## originality

PASS

Goyal et al original published 2026-07-21 proposes this exact predator–prey/food/generalized-competition model, studies equilibrium bifurcation and strict invasion inequalities. Available abstract and assigned citations do not establish a global equality-case extinction clock, matching prey displacement, or sharp p=3/2 correction transition. Resultary semantic searches returned similar extinction laws for DIFFERENT ecological equations with distinct forcing, dimensionality or exponents; no theorem implication is established. This is a best-of-knowledge qualified PASS with explicit full-primary access risk.

## value

PASS

The invasion-equality boundary is biologically and mathematically natural; the sharp p=3/2 transition in first correction distinguishes integrable drift, logarithmic resonance and fractional-power drift across a continuum of fractional nonlinear competitions. Global convergence and prey/predator synchronization make the exact rate useful for perturbation and long-horizon ecology, beyond routine local stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
