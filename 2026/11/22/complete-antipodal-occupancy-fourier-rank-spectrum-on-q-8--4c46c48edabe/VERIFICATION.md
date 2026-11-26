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

For exact complex support, pair sums give four scalar Walsh coefficients, and pair differences give the two-dimensional irreducible block, repeated twice in the regular representation. The determinant is the sum of the four squared differences; the block vanishes only when all differences vanish. Singleton differences have prescribed sign and magnitude, while doubles exclude just the two choices ±s. Walsh support sizes on 0,1,2,3,4 nonzero coordinates are respectively {0}, {4}, {2,4}, {3,4}, {1,2,3,4}; in particular two Walsh terms cannot make a three-coordinate vector. With no doubles, isotropy excludes a=1, excludes K=2 at a=2, and excludes K=1 at a=4 (a pure Walsh character has nonzero square sum); the remaining possibilities have explicit witnesses. With one double and no singleton isotropy is impossible for a nonzero block. Otherwise the real choices 7 on earlier doubles and an imaginary final difference solve the one quadratic equation without destroying exact support. The zero-block case requires no singleton. These exclusions and constructions give the whole table, not merely lower bounds. The affine group of F2^2 is S4 on its coordinates and preserves Walsh zero count; independent singleton sign changes preserve the determinant. Thus attainment holds on each specified support, with 255 total and 64 row-rank entries. Independently reproduced all 64 canonical entries by number-field rank of direct Hamilton regular matrices; no search was used to prove exclusion.

## originality

PASS

Supported scope is the complete joint scalar/matrix block classification on each fixed Q8 support, not the transform, the general uncertainty inequality, or the isolated spinor rank-two cases. The closest same-day analogue uses S3, which has a different Fourier and support structure. No inspected comparison dominates the combined claim.

## value

PASS

Q8 is a standard minimal nonabelian test of Fourier uncertainty with both scalar and matrix blocks. The classification detects kernel dimensions not recoverable from sparsity alone: two doubled four-point pairs allow rank two and only even ranks, whereas a double and two singletons admit ranks 4 through 8. Resolving the complete profile, not just its minimum or the known isolated spinor cases, provides a concrete benchmark for nonabelian uncertainty and structured convolution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
