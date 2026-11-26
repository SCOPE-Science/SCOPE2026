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

A local size-64 ring with radical of size 32 has 64 ordered zero-product pairs outside J×J: one unit and one zero. In central lift coordinates the product of two radical elements is B(v,w)+u z'+u' z since Z0²=0. When dim W0=2, the map u↦uc identifies V with W0. The 16 quotient pairs have central-offset ranks 0 for (0,0), 1 for six single-zero and three nonzero diagonals, and 2 for six distinct nonzero pairs. All targets in the rank-two cases are attained; the three diagonal tests give 416+32t. For dim W0=1 the perfect pairing gives rank 1 except at (0,0). The quotient target must vanish modulo W0; if h quotient pairs vanish, the count is 96+32h. The coefficient matrices of reduced multiplication give h via four kernel sizes, not by pointwise polynomial polarization in characteristic two. A direct central-coset enumeration reproduces the three regime histograms and their sole overlap at 480. To guard against representative-transcription errors, a second replay checks all 88 displayed rows represent distinct rings: impose the elementary central subspace relations and 2·1=d0, 2a=a d0, 2b=b d0, with multiplication extended from the basis tables. The relations are compatible since J-products of radical generators are central of exponent two and the doubles of radical generators lie in W0. Associativity reduces to the eight triples of the noncentral basis generators and is checked; any triple including a central radical generator vanishes in both associations. The radical is nilpotent and the quotient is F2. Noncentral radical elements multiply an appropriate central element to nonzero W0; units can use any nonzero element of W0, so the models are centrally essential. The invariant fingerprint minimizes the generator product and 2·1 signatures over basis changes preserving central action and the commutator, and over all central lifts. An isomorphism preserves these sets, since it preserves J, Z0, W0, the unit and their operations. All 88 fingerprints are distinct, enough for exhaustiveness using the published cardinality input even without line-by-line comparison of its tables.

## originality

PASS

The classification of the rings is fully credited. The reviewed statement is the multiplication-fiber comparison across radical regimes, with the explicit rank rules explaining all levels and their unique overlap. Numerical extraction from a ring presentation is possible but is not the structural comparison; there is no affirmative evidence of a published matching annihilation spectrum or rank analysis in the sources available here.

## value

PASS

Ordered annihilation counts capture multiplication relations in a natural complete class, not an arbitrary subset of tables. The structural reduction to central lift ranks shows why many characteristic and square-offset parameters do not affect the statistic, and the cross-regime collision measures exactly where this invariant fails to identify radical type. That comparison is useful beyond a raw table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
