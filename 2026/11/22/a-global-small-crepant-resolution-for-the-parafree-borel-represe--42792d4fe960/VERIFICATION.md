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

For the triangular matrix M(w,h), its r-th power has upper-right entry sigma_r(w)h; multiplication then gives the stated three coefficients. The base torus has coordinates (lambda mu,nu) with inverse (q^3 nu^(-n),q^(-2)nu^n,nu). Roots of sigma_r are the 2r-th roots other than ±1, all simple. For the 2 choices of lambda with lambda^2=-1 and 4 choices of mu with mu^3=±1, the constraint nu^n=-mu^3 has one excluded sign (n odd) and n-1 admissible roots. At each such point, f1,f2 have independent differentials and generate the maximal ideal in the algebraic local ring; f3=s alpha+t beta with regular alpha,beta after Zariski shrinking. Thus the blow-up center is reduced, and its transformed coefficient row surjects onto O(-D), giving the rank-two kernel and its smooth total space. The induced map is a closed immersion into the projective base change Z_m×_{T_m}X_m followed by projection. In coordinates (s,t,u,v,w) with equation su+tv=0, the two charts divide out a single exceptional factor and impose u+zv=0 or zu+v=0. When (u,v)≠(0,0), the exceptional direction [-v:u] gives the regular inverse near s=t=0; when u=v=s=t=0 the direction is free and w is unconstrained. Thus exactly a P^1×A^1 per center is exceptional, of codimension two. Its transverse normal factors are the tautological direction for (s,t) and the kernel line of (u,v)↦su+tv over P^1, both O(-1). The irreducible hypersurface is normal by R1 and S2, and smallness gives discrepancy zero for its Cartier canonical divisor. Independently K_Z and det K both equal O(D), as in the record. For homology replace disjoint small real 4-balls in the torus by disk bundles over the exceptional spheres, gluing along S^3; Mayer–Vietoris adds one free H_2 per center, with the H_3/H_4 terms unchanged because each filling has vanishing H_3 and H_4. The vector bundle retracts to Z_m. Each exceptional divisor adds a Picard generator independent by restriction degree -1 on its own sphere and 0 on the others; the torus has Pic=0, and pullback to a vector bundle over the regular base preserves Pic. Fiber stratification gives [X_m]=L^2([T_m]-N)+NL^3 and [resolution]=L^2([T_m]+NL), N=16m, yielding the claimed difference, Euler characteristic and Hodge–Deligne realization. CHECK.py was read, not run; its finite polynomial checks do not establish the universal count or geometric assertions.

## originality

PASS

Qualified family-level originality: the coefficient presentation, point count, singular lines and transverse conifolds are known. The projective simultaneous model realizes a particular common choice of local rulings using the coefficient ideal over the torus. The blow-up and bundle identities are standard; the assessed contribution is the concrete global construction and the resulting invariants of this smooth model, not a new general small-resolution mechanism.

## value

PASS

The exact source distinguishes the affine variety and its punctured regular locus but does not supply a smooth relative-projective model. Constructing a single global small crepant resolution of all the conifold lines addresses that concrete gap and retains a usable rank-two bundle description; the homology, Picard and motivic formulas characterize this model and distinguish the families. Routine invariant formulas are useful here because the smooth model is first identified, not because the formulas themselves are new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
