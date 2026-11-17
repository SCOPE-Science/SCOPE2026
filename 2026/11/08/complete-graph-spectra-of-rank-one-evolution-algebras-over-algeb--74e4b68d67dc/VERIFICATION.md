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

For dim A²=1 write xy=B(x,y)v, where B is symmetric and radical=Ann(A). Any natural basis diagonalizes B, giving d active source coordinates T; all active squares are nonzero multiples of v so their directed out-neighborhood equals the same nonempty support S. The projection w of v to A/Ann(A) is zero exactly when A³=0; if w≠0, B(v,v)=0 gives isotropic case requiring ≥2 active coordinates, and B(v,v)≠0 requires ≥1. Over algebraically closed char≠2, nondegenerate quadratic form has orthonormal basis, and orthogonal-group transitivity on equal-norm nonzero vectors (including isotropic) realizes any allowed active support. Radical shears independently assign arbitrary radical support when w≠0; if w=0, radical basis changes realize every nonempty S in radical. Permutation gives all T; direct subsets counts give labeled C(n,d) times 2^r(2^d-d-1), 2^r(2^d-1), or 2^r-1, and isomorphism classes depend solely on the two support sizes. This also proves finite-family simultaneous realization within a fixed algebra. Finite SymPy construction illustrates d<=3,r<=2 but is not the arbitrary-dimensional proof.

## originality

PASS

The quadratic-form normal model and Witt orthogonal transitivity are known, but the inspected earlier literature and Resultary entries do not state the complete support-graph spectrum of all ordered natural bases of one fixed rank-one-square algebra, nor its exhaustive labeled/unlabeled counts and simultaneous-realization criterion over algebraically closed char≠2. Earlier binary finite-field spectra involve different orbit geometry.

## value

PASS

A natural graph invariant of evolution algebras depends on the choice of natural basis. The theorem classifies all graph presentations for every algebra with one-dimensional square, including its radical, computes exact labeled and unlabeled spectra, and answers a motivated restricted simultaneous-realization problem. The Witt and radical-shear realization removes an actual structural ambiguity beyond mere form classification. It is a meaningful complete infinite-family structural fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
