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

For stationary full-rank OU, X_{t+Delta}=E_Delta X_t+Z_Delta with independent positive-definite Gaussian innovation. In Gaussian polar coordinates X=ru, substitution r=t/w converts exceedance Ω>w into ||P_{u perpendicular}(A tu/w+Z)||>Delta t. Gaussian tail domination for w>2||A||/Delta proves via dominated convergence a positive w^-d constant p_X(0)/(d Delta^d) int_S E||P_u Z||^d; rotational sphere integration gives J_d E||Z||^d. Tail integration establishes EΩ^q<infty iff q<d, and critical log. In isotropic case Ω=c_Delta chi_{d-1}/chi_d; exact d2,d3 tails and rotational d3 second moment follow from chi/Gaussian direction moments. Independent gamma evaluations verified J2=pi,J3=3pi²/4 and isotropic constants 1/2 and 1.

## originality

PASS

The previously published Brownian gyrator paper proves two-dimensional signed sampled-angular-velocity density |w|^-3 and divergent variance, a proper boundary special case. It does not establish general d, the anisotropic positive w^-d prefactor, the moment iff threshold, nor a circulating 3D finite-variance example. The extension has a geometric polar-coordinate proof, with generic chi-ratio identities acknowledged.

## value

PASS

Determines the exact dimension where sampled velocity-ratio variance becomes finite, despite circulation, and supplies a nontrivial anisotropic Gaussian tail prefactor and exact 3D rotating counterpoint. This materially distinguishes an experimentally relevant unbounded chord-based estimator from bounded principal angles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
