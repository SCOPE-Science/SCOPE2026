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

A geometrically fixed point has barycentric weights constant on each vertex orbit. Normalizing by the total orbit weights identifies the fixed set with the independence complex of admissible orbits, with incompatibility precisely a pair at distance >4. On augmented oriented simplicial chains, a setwise invariant face on s vertices in k orbits has permutation sign (−1)^(s−k) and ordinary Euler contribution (−1)^(s−1); the product is (−1)^(k−1). Including the augmentation and negating the reduced alternating trace gives exactly I(−1) as claimed. I reconstructed all eleven orbit graphs and signed sums, using isolated-vertex and leaf reductions and component factorization as well as vertex deletion. The orbit counts and all traces match, including 253 at the identity (2,238 cached states in this implementation). I computed irreducible characters independently of rim-hook enumeration, extracting coefficients of the Vandermonde determinant times the product of power sums in the Frobenius formula. The full class-weighted orthogonality check and all multiplicities (7,4,5,1,4,4,1,4,5,2,2) agree. By barycentric subdivision, an invariant simplex is pointwise fixed and flags have invariant orientations. The Euler characteristic of the true quotient is the average of the geometric fixed-space Euler characteristics by ordinary orbit counting on flags. It is thus 1−7=−6, with reduced value −7; connectedness follows from the cube edges, so higher rational homology is nonzero. Replay: python /workspace/checks/cube.py (output /workspace/checks/cube.txt). The finite result says nothing about a separate graded decomposition or quotient torsion.

## originality

PASS

The fixed-locus and Lefschetz tools are standard; the distinct data are the ten nonidentity coordinate-class values on the full six-cube at scale four, the complete coordinate virtual character, and its trivial multiplicity/quotient Euler consequence. The same-object translation result already covers the identity value. The strongest broader representation theorem advertises ranges excluding (6,4); the closest same-scale coordinate result uses a different vertex set.

## value

PASS

The six-cube at scale four is a natural first intermediate symmetry case beyond the established low and terminal scales. The full class data refine the known dimension and the translation restriction, giving specific test data for wider equivariant approaches. The trivial multiplicity detects nonzero positive-degree rational homology of the coordinate quotient despite the small simultaneous fixed locus. The computation's modest size is not itself the novelty or the motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
