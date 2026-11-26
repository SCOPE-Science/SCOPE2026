---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Writing P(z)=b+cz, the noncentral part of P([Pz,v]) is ω(b,v)b, while [Pz,Pv] is central, so nondegeneracy forces b=0 over any field. The remaining original equations are A²=A, c²=c, fA+cf=f, and ω(Au,Av)=cω(Au,v)=cω(u,Av). With c=0 this is exactly an isotropic image, arbitrary complementary kernel and f pulled back from the image; a Lie endomorphism also preserves the derived line, and fixing it forces A symplectic and thus the full idempotent to be identity. With c=1 the sum im A⊕ker A is orthogonal by the form equations and each summand is then nondegenerate; conversely the orthogonal projection and any f on its kernel work. The image contains z and has rank 2r+1. Symplectic basis changes carry any such complementary pair to a fixed one, and an arbitrary central shear kills f on the kernel. For the finite count, the ordered isotropic frame count has factors q^(2m−i)−q^i, divided by the count of ordered bases of an r-space; the complementary kernels and functionals give the first term. In the second branch the stabilizer of a nondegenerate plane of dimension 2r is Sp_(2r)×Sp_(2m−2r), and the orthogonal kernel contributes q^(2m−2r) functionals. These arguments use alternating forms and apply in characteristic two. On the reduced locus c and rank of the idempotent A are locally constant; image/kernel maps are regular on constant-rank strata by local minor charts. Complements on the isotropic locus form an affine bundle, and functionals form the asserted bundles. The isotropic Grassmannian is smooth and irreducible (symplectic transitivity and local isotropy equations whose differential surjects onto alternating forms on the plane), and the nondegenerate open in the other Grassmannian is smooth and irreducible. Thus these nonempty open-and-closed strata give exactly 2m+2 reduced components, without a scheme claim. Independently generated all 20,834 idempotents on F₂^5 via all complementary image/kernel pairs, not imposing the center or form classification; checked both original averaging identities on all ordered basis pairs. The two branch profiles were (1,240,960,0,0,0) and (0,16,0,80,0,1), agreeing also on 96 nonendomorphisms. Replay: python3 -B /workspace/repro/3.py; /workspace/repro/3.log. This is finite corroboration only.

## originality

PASS

The classification and census of the Lie-retraction branch, the identity endpoint, and the m=1 boundary are not distinct contributions. The supported distinction is the all-field classification and conjugacy, finite-field sizes and additional reduced strata for the nonendomorphism branch m≥2, c=1, r<m. The general averaging criterion and standard symplectic geometry explain the specialization but do not themselves enumerate its possibilities, conjugacy classes or census.

## value

PASS

The Heisenberg algebra is a natural test case for the difference between Lie retracts and averaging projections. The exact extra family gives a characteristic-independent explanation of the high even-rank exclusions, specifies full nonendomorphism orbit representatives and labeled class sizes, and describes the geometry of the new components. These are structural all-parameter refinements rather than isolated enumerations; no novelty credit is needed for the pre-existing retraction term.

The dated certificate retains the supplied scientific assessment, sources and limitations.
