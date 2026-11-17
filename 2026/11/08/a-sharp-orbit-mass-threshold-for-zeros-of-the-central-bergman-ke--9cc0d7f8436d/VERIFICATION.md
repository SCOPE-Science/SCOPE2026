---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The complete RESULT.md proof reduces the finite-rank RKHS update to K_t(z,0)=1-qt/(1+tL) h_q((rho z)^q), L=q(1+(q-1)rho^(2q))/(1-rho^(2q))^2. The scalar quadratic has exactly one root y_- in (0,1) and y_+>1; y_- crosses r=rho^q once. The q inverse images are distinct and simple for t>T; equality roots lie on |z|=1. My independent SymPy simplification verified g(r)/(q-g(r)L)=T_q(rho) identically, including critical normalization. As t increases without bound y_-->r^2 and the roots approach rho times qth roots of unity; asymptotic limits follow from exact formula. No claim concerns K_t(z,z).

## originality

PASS

Older finite-atomic reproducing-kernel perturbation results supply the low-rank identity, not the q-fold central zero crossing or exact orbit-mass threshold; Perälä radial-weight constructions give zeros in noncentral fibers, while any radial-weight central fiber is constant. Searches did not find an earlier theorem implying the exact cyclic threshold. Best-of-knowledge only; no exhaustive priority certification.

## value

PASS

A motivated Lu Qi-Keng/atomic RKHS phenomenon: a symmetric polygon of point masses creates arbitrarily many central zeros, with an exact, monotone boundary and two nontrivial asymptotic regimes. This is not just a restatement of the general Woodbury formula; cyclic character and root-location analysis yield a concrete reusable family-specific threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
