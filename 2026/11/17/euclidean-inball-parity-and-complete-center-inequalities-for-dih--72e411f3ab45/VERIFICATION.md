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

PASS. For n>=3 in the standard orbit embedding, the 2n centered dihedral vertices are positive and negative cyclic translates of one centered sawtooth; differences of adjacent translates equal n e_i-1. The polar is linearly identified with cube-section y in [-1,1]^n with sum y_i=0, inverse u_i=(y_{i+1}-y_i)/n. Every cube-section vertex is balanced ±1 if n even, or one 0 with balanced ±1 if odd, so each primal facet plane is at distance n/sqrt(sum (y_{i+1}-y_i)^2). A sharp cyclic alternating-sign energy bound gives max energy 4n (even) or 4n-6 (odd), attained by precisely 2 or 2n cube-section vertices; hence radius sqrt(n)/2 or n/sqrt(4n-6). Opposite tight facet pairs give linear center equalities, and strict slack on the other finite facets gives all center inequalities. For even n the active signed difference vectors span one dimension, giving an (n-2)-dimensional incenter locus; for odd n a discrete Fourier evaluation of the alternating zero pattern is nonzero on each nontrivial nth root, giving full rank n-1 and a unique origin center. Independently enumerated all zero-sum cube vertices for n=3..11 and checked exact integer energy maxima, counts, and rational ranks; the finite test supports but does not establish the all-order theorem. No affine-metric invariance is claimed. The finite checks are corroborative to the sharp combinatorial and Fourier proof.

## originality

PASS

Best-of-knowledge PASS for precise Euclidean inball radius, contact-facet parity counts and complete center-set dimension/inequalities on standard dihedral permutohedra; prior source gives complete facets but not this metric optimization.

## value

PASS

PASS: The same canonical dihedral orbit polytopes whose facets/triangulations were recently determined have an exact ambient Euclidean inball with sharp even/odd uniqueness transition and an explicit complete high-dimensional set of centers. This is a natural metric question in an intrinsically defined family, not a renamed or tiny numerical improvement; known combinatorial facet counts do not settle the max-energy optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
