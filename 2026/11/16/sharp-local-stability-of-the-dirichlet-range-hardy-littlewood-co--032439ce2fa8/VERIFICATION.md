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

PASS: The source primary Hardy–Stein and weighted Hilbert identities give N_{s,t}(1+h)^t=1+(t²/4)||h||_{s,2}²+O_t(||h||∞ ||h||²_{s,2}) for |h|≤1/2. Taylor of power 2/t yields quadratic form (p/2)(||h||²_{alpha,2}-(beta/alpha)||h||²_{beta,2}) with uniform O((||h||∞+||h||²_alpha)||h||²_alpha) remainder. Monomial orthogonality gives λ_k, ratio c_alpha(k+1)/c_beta(k+1) relative = (alpha+k)/(beta+k)<1, λ_1=0 and λ_2=p/2*(beta-alpha)/(beta+1)>0, increasing to p/2. h=t z² makes sharp local ratio. The common automorphic isometry and real implicit-function theorem kill first derivative under local modulation; scope is local only and requires both norm smallness hypotheses. Independent rational test alpha=2/5,beta=4/3,p=3/2 produced gap 3/10, λ1=0, λ3=213/500 and strict increasing modes; finite test not all-parameter proof.

## originality

PASS

PASS best of knowledge: Brevig–Kulikov–Seip–Zlotnikov 2025 primary establishes base sharp contraction, equality, isometric group and coefficient Hilbert identity but the inspected full HTML did not give a sharp transverse quadratic remainder or diagonal Hessian spectrum; the global qualitative inequality alone cannot imply a positive quantified local complement gap. Llinares 2024 and Kulikov 2021 address contractive inclusions/coefficients in different settings. Older stability work under different terminology remains residual risk.

## value

PASS

PASS: Removing conformal equality symmetry and finding its exact first positive Hessian eigenvalue is a natural local stability question for a sharp functional inequality, identifies the correct transversal direction and sharp perturbative coercivity scale. It does not overstate global stability; the spectral decomposition has meaningful structural content beyond the base inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
