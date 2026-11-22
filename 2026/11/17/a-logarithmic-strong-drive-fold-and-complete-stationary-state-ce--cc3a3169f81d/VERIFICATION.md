---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

At each vertex-adjacent ordered branch x=rho_1=u/k, y=rho_2=v/k, k-b-log k=c, the logistic odds identity gives w0=(k^{-1} exp(-c+2u+v))/(1+k^{-1} exp(-c+2u+v)); the other forward rates tend to 1 exponentially. The exact current equations, rescaled by k, converge in C^2 on compact sets to du/dt=A-2u, dv/dt=u-v, A=exp(-c+2u+v). Stationarity requires v=u and c=3u-log(2u), uniquely minimized at u=1/3 with c*=1+log(3/2), giving zero/two positive roots off threshold. At a root, Jacobian trace=4u-3 and determinant=2-6u (independently recalculated symbolically), so low root stable node, high root saddle. Compactness on the closed simplex: any nonvertex limit forces every clockwise rate to 1 and a uniform limiting equilibrium; at a vertex, current balance y-x exponentially small and x>=C/k, while log(2kx)=-c+2kx+ky+o(1) prevents kx escaping, forcing convergence to one of the two reduced roots; no boundary equilibria at positive finite rates. Fold equation H=H_u=0 has H_uu=6, H_c=-2/3, first epsilon coefficient -2/3 at u=1/3, giving c_SN=c*-1/k+O(k^-2) and the two-term inversion for k_SN(b). Uniform state Jacobian real part -3/2+O(ke^-b)<0. The exact rate model and proof were read at frozen RESULT and verify.py; finite numerical fold values do not prove global completeness.

## originality

PASS

The original contribution is the analytic high-drive fold location with nontrivial next term and complete 1-versus-7 stationary-state census of the exact homogeneous continuous-time active-Potts Glauber flow; the primary physics paper has finite-drive numerical folds/Hopf but not the stated strong-drive global theorem.

## value

PASS

The qualitative folds were known numerically but the precise large-b analytic saddle-node scale, next coefficient, exact count and stability types are natural missing dynamical-system facts. An all-state completeness theorem on a compact 2-simplex is scientifically useful even without a broader PDE or finite stochastic lattice implication. This is not merely restating a textbook saddle-node theorem: the logarithmic singular scaling and exclusion of remote equilibria are the content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
