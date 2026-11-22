---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Strict positivity and scalar logistic bounds give global solutions; reverse induction using z_i=1/x_i and r_i(t)=d+b-bx_(i+1)(t)->d establishes global convergence to 1. Linearized J_n=-dI-bS_n and nilpotent exponential yield R_(n,j)^2=e^(-2dt)F_j(bt), F_j(v)=sum_(r<j) v^(2r)/(r!)^2, and terminal j=n dominates. q_n(v)=log F_n(v)/(2v) vanishes at zero/infinity, attains gamma_n, giving exact single-coordinate iff b/d>kappa_n, tangency equality and initial contraction. Symmetric Jacobian spectrum yields full-norm reactivity exactly b/d>rho_n=sec(pi/(n+1)); strict gap via compact time windows. Bessel I0 upper bounds, Stirling lower sums at v=n-sqrt(n), localization v_n/n->1, prove n(kappa_n-1)/log n->1/4; two-species stationary equation gives 2.48526751266.

## originality

PASS

Full-operator transient reactivity of the same open Jordan chain is already published; the terminal one-coordinate all-time threshold is a different constrained operator-column quantity and not mathematically implied by the path log-norm bound or finite-horizon all-vector peaks. Historical 2001 ecology article inaccessible in full, so priority remains qualified.

## value

PASS

Separates globally attracting dynamics, instantaneous all-vector reactivity, and delayed amplification of a physically restricted positive one-species perturbation, with quantitatively different n^(-2) and (log n)/n thresholds. This motivates the exact column invariant rather than a small benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
