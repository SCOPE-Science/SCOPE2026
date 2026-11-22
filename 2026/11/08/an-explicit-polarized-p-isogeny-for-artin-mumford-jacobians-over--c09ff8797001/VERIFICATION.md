---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

Reconstructed from the frozen RESULT.md. For odd p, G=Fp² translations, fixed field Fp(w), w=x^p−x; two axes provide the only inertia over 0,∞. Each of p points over each pole contributes different 2(p−1), giving g(C)=(p−1)^2. For t≠0, H_t=< (1,t) > meets both inertia axes trivially, so π_t is an étale p-cover and D_t:z^p−z=w^{−1}−tw has genus p−1. Every distinct H_t,H_s generates G; the (normalization of the) fiber-product correspondence over P1_w makes π_{t*}π_s^*=0, while π_{t*}π_t^*=[p]. These identities prove ΨΦ=[p]_B; dimension equality and finite kernel make Φ an isogeny and surjectivity gives ΦΨ=[p]_{J(C)}. Norm/pullback Rosati adjunction yields Φ*λ_C=pλ_B; principal polarizations and deg[p]=p^{2g} give deg Φ=p^g and an isotropic maximal subgroup scheme B[p] of length p^g (no separability assumption). Scaling x by u,y by u^{-1} sends t→t/u²; Fp point counts of Dt give 2p+2 in the square class and 2 in the nonsquare class, so the two representative Jacobians have distinct traces and are not Fp-isogenous. The p−1 factors give stated zeta numerator identity. Independent direct Fp and Fp² arithmetic checks for p=3,5,7,11 all agreed; finite checks were not promoted to a proof of universal or scheme facts.

## originality

PASS

Best-of-knowledge PASS for the exact integral sum-of-pullbacks isogeny of the classical Artin–Mumford curve, its two-sided [p] identities, p-primary polarization and degree, and arithmetic square-class trace distinction. The underlying curve, quotient genera, Kani–Rosen unpolarized product decomposition, and the general polarized norm/pullback method are prior art and are not asserted novel. The nearest earlier polarized Artin–Schreier construction has a genuinely different cover, genus, quotient count and base field. A highly relevant 1991 Kloosterman/p-torsion paper was not obtainable in full, which is explicitly retained as a priority risk.

## value

PASS

The Artin–Mumford curve is a central natural ordinary high-automorphism example, and its full p-primary polarized Jacobian factorization is a natural integral structural invariant beyond abstract rational group-idempotent decomposition. The exact degree p^{(p−1)^2}, isotropic kernel length, and two arithmetically nonisogenous square-class quotient factors hold for every odd p. Although the norm/dual calculation is known in analogous families, the interaction of nontrivial inertia axes, only the p−1 non-axis quotient lines, and arithmetic square-class Frobenius splitting makes this a motivated exact result for a natural object, not an arbitrary numerical slice or a claim of a new general principle. No kernel scheme classification, optimality or simple-factor theorem is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
