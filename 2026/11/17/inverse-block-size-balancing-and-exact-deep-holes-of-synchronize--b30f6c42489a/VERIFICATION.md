---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For each binary cube vertex x, reflect coordinates to the origin; the synchronized parity code splits into exactly two convex coset types, with block sum lower bounds lambda or 1-lambda. Blockwise Cauchy–Schwarz gives norm^2 >=lambda^2 W_T+(1-lambda)^2(S-W_T) and minimizing lambda yields W_T(S-W_T)/S. Uniform mixtures of single-coordinate flips in the designated odd blocks attain equality; strict convexity gives unique projection. Squared distance to a convex set is convex, hence max over cube occurs at a vertex; the variance identity plus distinct nonzero signed residual vectors at every two distinct noncode vertices strictly excludes other maximizers. Reciprocal subset balance gives farthest patterns and counts, including equal blocks and one dominating reciprocal weight. Independently enumerated all codewords and verified normal-cone projection inequalities by exact Fraction for block sizes (1,1,1), (1,2,3), (2,2,2), (2,2,3), (1,1,2,2); this finite check supports, not proves, the general formula.

## originality

PASS

Best-of-knowledge PASS for the distinct simultaneous-block-parity codeword polytope, with a complete Euclidean projection and deep-hole classification not implied by inspected single-check work.

## value

PASS

The synchronized parity code is a natural multi-check linear-code family whose Euclidean codeword-polytope approximation to a hypercube is distinct from Hamming covering radius. The exact projection, all deepest corner configurations, reciprocal block balancing and sharp synchronization-vs-independent-block comparison provide a usable nontrivial geometric decoding invariant for arbitrary positive block lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
