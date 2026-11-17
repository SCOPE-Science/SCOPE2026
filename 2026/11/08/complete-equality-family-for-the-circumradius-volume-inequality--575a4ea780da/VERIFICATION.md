---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

A nonzero 3x4 kernel dependency can be made nonnegative by sign flips, orienting the generators with 0 in their tetrahedral hull. Tetrahedral dissection gives zonotope volume as one tetrahedron determinant; the three balanced signed sums w_j have det four times the volume. All balanced half-sums are vertices/candidates of the centered zonotope and have norm <=R. Hadamard forces three w_j perpendicular and of length 2R at equality. Inverting the 3x4 Walsh transform gives p_i=q_i+v and the positivity condition -v in T_R. The other signed sums exhaust the circumradius: 2v, three balanced R terms, and v-q_i, yielding exactly the region constraints, necessary and sufficient even at degeneracies. Independent exact rational witness at R=2,v=(1/10,0,0) has V=16, R^2=4, unequal generator squared lengths 281/100 and 321/100. The open interior of Omega_R shows genuinely nonregular equality. The witness proves existence, while general necessity/sufficiency follows algebraically.

## originality

PASS

Joós–Lángi arXiv:2206.03204, Theorem 3 already proves the sharp inequality and section 3.2 gives small common-shift perturbations; both are explicitly prior, not claimed. Their Section 5 Problem 1 still asks uniqueness of the minimizing rhombic dodecahedron, so it cannot contain this complete necessary-and-sufficient equality parameter region. Lángi arXiv:2102.11621 optimizes mean width for parallelohedra, not fixed circumradius-volume equality. Related Resultary four-generator results bound inscribed tetrahedron occupancy, distinct functional. The exact exhaustive 3-dimensional equality family and boundary classification is the assessed increment; historical equality-characterization priority provisional.

## value

PASS

This fully resolves the equality classification for an extremal sharp inequality and answers the explicitly posed regularity question by constructing nonregular optimizers, with a precise semialgebraic parameter locus including boundary configurations. It is a global geometric structural result, not merely a known inequality or a single perturbation counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
