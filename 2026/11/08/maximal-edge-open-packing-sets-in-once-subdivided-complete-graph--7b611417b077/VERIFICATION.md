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

For n>=3, incidences i--s_ij encode directed arcs i->j. Two distinct chosen arcs conflict iff nonreciprocal and they form a length-two directed walk with three distinct old vertices, because this creates a three-edge path whose outer edges are selected. A reciprocal pair i<->j excludes any further incidence at i or j, so such pairs are vertex-disjoint. Remaining arcs must run from sources to targets with no vertex both a head and tail. Inclusion-maximality forces every old vertex to be used, every source-target arc present, and excludes the single 1x1 block since its reverse remains feasible; without block, reciprocal pairs must be perfect or near-perfect. The disjoint structural census yields n!/(2^c c!a!u!) for c reciprocal pairs and complete a-by-u block, plus perfect/near-perfect pairings. Size 2c+au=n-1+(a-1)(u-1) and maximum floor(n²/4); odd n implies even sizes. Raw 3-edge-path bridge tests and exhaustive subset enumeration independently reproduce n=3:9z², n=4:8z³+9z⁴, n=5:85z⁴+20z⁶. Finite test not universal proof.

## originality

PASS

Earlier October26 exact S(G) theorem already gives a matching-plus-oriented-cut decomposition of ALL edge-open packings and their all-size generating polynomial, and determines maximum size and maximizing cuts for S(K_n); these are credited, not original. It does not state saturation/maximality rules, perfect/near-perfect reciprocal-pair or complete-block facet classification, nor the polynomial counting ALL inclusion-maximal sets. Primary edge-open-packing graph literature addresses complexity and trees, not this exact facet spectrum in material read. Best-of-knowledge O with risk that facet derivation from all-sets decomposition is implicit.

## value

PASS

The exact facet structure of a natural graph packing complex is independently useful beyond the all-packing enumerator: it classifies irredundant maximal configurations and full size spectrum, including parity restrictions and exact lower bound n-1. The new maximality saturation argument is necessary, not a mere substitution of known all-set polynomial coefficients. The value bar allows self-contained exact structural finite-family classifications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
