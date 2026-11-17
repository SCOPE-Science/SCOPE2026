---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For the literal printed 5x25 generator over F_3, independently parsed all 25 columns, computed 243 codewords and the complete coefficient table, and enumerated each r-plane in F_3^5 exactly once via its unique reduced-echelon basis. Totals for r=1..5 were 121,1210,1210,121,1 and exact support minima were (14,19,22,24,25); every support-profile coefficient agrees with the result. The 25 projective-normalized columns were distinct/nonzero. Exhaustive triple and quadruple relation checking gave 15 dependent triples and 486 four-supports, hence 30 and 972 low-weight dual words. Positions 1,7,9,10 were the only positions absent from dependent triples and all occur in dependent quadruples. Exact normalization gives the four locality-three exceptions and other 21 locality-two coordinates. The finite census is exhaustive by canonical RREF, not statistical sampling; rank 5 and Gram determinant 1 also follow from modular elimination.

## originality

PASS

The generator and its [25,5,14] parameters come from An–Hong–Kim–Lim, but the inspected original Proposition 4.1 does not furnish the all-dimension support histogram, projective line/plane incidences, or exact coordinate repair-locality pattern. Published support-profile records for other binary/ternary matrices do not imply this literal generator’s spectrum. This is best-of-knowledge originality of its finite structural fingerprint, not authorship of the code or novelty proof by unsuccessful search.

## value

PASS

A specified recently constructed LCD code is a natural object whose full generalized-weight hierarchy controls erasure/privacy/wiretap-II support thresholds beyond its minimum distance. The genuinely nonuniform locality distribution identifies which four actual transmitted symbols require three helpers rather than two; complete exact finite code fingerprints can be independently useful and are not arbitrary numerical slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
