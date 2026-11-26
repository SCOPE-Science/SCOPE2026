---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For distinct singleton partial injections any nonempty composite of both orders gives different maps; commuting therefore requires that neither ordered composite is nonempty. Aggregate source and target supports of a face are disjoint, not necessarily singleton or pairwise different within each support. An independent all-n proof uses simplex weights lambda_ij: their row and column marginals p,q have disjoint supports, and x=p-q has coordinate sum zero and ℓ1 norm 2. Conversely x returns the weights lambda_ij=x_i^+ x_j^- because each sign part sums to 1. For a starting simplex point, interpolation to the weights returned by its marginals stays within the simplex of all arcs between its original two supports, and fixes the section pointwise. This is equivariant under label permutations and transposition of indices. On the resulting sphere in the sum-zero hyperplane the determinant of a coordinate permutation is its sign, and the determinant of inversion is (-1)^(n-1). This proves the integral orientation-lattice claim, including reduced H0 at n=2. The frozen mod-two and integral trace computations are finite checks, not the integral theorem.

## originality

FAIL

The claimed increment, the joint integral orientation character, is a direct consequence of the prior Hom(K2,Kn) support model, with the natural endpoint and label actions. The statement need not appear verbatim there. Passing from this rank-one commuting complex to that model is the immediate equivariant closure of an arc set to its source × target rectangle. This is positive prior-coverage evidence, not a failure based on the inaccessible Jonsson chapter.

## value

FAIL

The actions on the rank-one complex are natural, but the attainable invariant is just the determinant of the standard representation and its antipodal map after a routine face closure. The record gives no independent mathematical need for restating that already implied orientation lattice in this rank-one slice, or a distinct implication for commuting complexes. This is not a judgment against the underlying sphere theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
