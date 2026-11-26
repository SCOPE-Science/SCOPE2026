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

With counting measure, Parseval reduces the objective to the square of the interpolation operator norm, not to Dirichlet energy. Affine interpolation gives the stated Gram entries. Each edge block has a linear symmetric eigenvalue and a strictly convex antisymmetric eigenvalue. In a nontrivial average with a transposed pair of unequal gaps, equality in the top eigenvalue would force the optimizing vector to be constant on both changed edges, hence constant on the triangle. Unequal endpoint row sums then rule this out. A unit transfer strictly decreases the bound whenever the gap difference is at least two. Reflections give both 2-by-2 radicals, and counting the exceptional gap (or cosets for equal gaps) gives the stated counts. At N=4 the off-diagonal in the reduced block is zero, not positive as suggested by one sentence in the proof; the explicit diagonal entries 3/2 and 1 still give the asserted root, and the remaining eigenvalue is 1. For the asymptotic, the constant-unit-vector block has diagonal N/3, coupling into its orthogonal complement of squared norm 1/18 for either nonzero residue, and a spectral separation q/2+O(1) from that complement. Schur reduction gives the excess 1/(9q)+O(q^-2).

## originality

PASS

The finite-cycle squared interpolation norm, strict placement characterization, exact values and integer-grid penalty are distinct from the inspected Riesz, projection, path-completion and continuous-trace objectives. This is a best-of-knowledge judgment about the joint claim, not priority for Parseval analysis or linear interpolation.

## value

PASS

It answers a natural placement problem for the worst possible energy amplification of harmonic interpolation. The strict equality characterization and leading integrality cost distinguish it from the immediate continuous-average lower bound. The matrix strictness argument explains why every unbalanced placement loses; the result is not a finite simulation or a claim about unrelated recovery criteria.

The dated certificate retains the supplied scientific assessment, sources and limitations.
