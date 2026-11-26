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

For the nonunital algebra defined by the nondegenerate symmetric form, write N(z)=u+az. The vector part of the identity on (v,z) is B(v,u)u=0 for all v, forcing u=0. On V×V the remaining scalar identity is exactly B((T−aI)v,(T−aI)w)=0; products with z then impose nothing, and the block parameters are unique. Over the algebraic closure the incidence space with a maximal isotropic plane U and a map into U is the bundle Hom(V,U) over the maximal orthogonal Grassmannian. Its image is closed by projectivity, all isotropic images extend to a maximal plane, and the generic full-rank image determines U. The dimensions are the Grassmannian dimension m(m−1)/2 in even or m(m+1)/2 in odd dimension, plus nm+n+1. In the even case an isotropic (m−1)-plane has two extensions through its hyperbolic-plane quotient, in opposite families, so the two component images meet exactly in ranks ≤m−1. Over F_q the Witt sign is invariant in each even-dimensional quotient by an isotropic plane; counting one-step extensions by nonzero isotropic vectors and dividing by the number of hyperplanes gives the stated I_r. For a=0, rank r arises from the q^r functionals vanishing on ker S, and rank r+1 from the remaining ones. For a≠0, ker(aI+S) lies in im S; fixing im S⊆W of dimension h, the shifted matrix has a free h×(n−h) block and a bottom diagonal block aI, so its nullity is the nullity of the h×h block. Choose that kernel and an injection of its quotient to obtain E_(h,j), and invert on subspaces W of the fixed r-plane to obtain H_(r,j) using the stated subspace Möbius factors. Every j≤w is realized by S=−aP_J for an isotropic j-plane J, giving the upper rank interval, while the a=0 construction gives the lower. Only the nonsplit even interval leaves rank m+1 missing. A fresh direct enumeration over all isotropic images and surjections in the n=4, q=3 cases matched both complete sample count vectors, including zero at rank three for the nonsplit form.

## originality

PASS

Credit the proven prior Gram-zero geometry and the binary cases. The distinct supported contribution of the frozen theorem is the explicit Nijenhuis classification for the specified higher-dimensional algebra, with the odd-finite-field rank support and full labeled operator rank census. The orthogonal-null-cone component result is not a new theorem in its own right; the original contribution is the operator identification and the rank enumeration, especially the shifted-nullity distribution and nonsplit gap, not the imported geometry.

## value

PASS

This is a natural labeled rank invariant for a two-step commutative algebra whose defining extra structure is its bilinear form. The census distinguishes split and nonsplit forms by the absence of just one operator rank (starting at algebra dimension five); ordinary ranks of bilinear forms do not distinguish these nondegenerate cases. The full distribution resolves exactly how the free scalar shift and annihilator row change operator rank, so it is usable beyond the sample comparison. No independent value is assigned to reobtaining the known cone components as pure geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
