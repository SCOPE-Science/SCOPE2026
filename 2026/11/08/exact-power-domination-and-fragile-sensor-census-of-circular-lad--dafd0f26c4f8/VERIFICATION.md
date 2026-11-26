---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For opposite-rail offsets 0,1,2 and same-rail offset 1 the initial observations include two consecutive complete rungs. For same-rail offsets 2 or 3, the observed rail vertex at column 1 can force its rung partner if needed, giving complete rungs 0 and 1; then the full rungs propagate. Only realizable offsets are needed at short rim orders. Conversely, distance at least four leaves disjoint closed neighborhoods with no edges between them. The cubic triangle-free graph gives each observed nonsensor exactly two dark neighbors, so the process stops at 4k<2n (each cyclic gap is at least three, with the singleton handled separately). A singleton succeeds on the triangular prism. Choosing the even number of cyclic color changes, adding nonnegative slack to minimum gaps of three or four, and marking and unmarking a starting sensor give the stated labelled binomial coefficients. The two-color gap matrix has eigenvalues x³(1+x)/(1−x) and −x³; the logarithmic derivative gives the rational series and its Lucas corrections at z=1. At fixed retention the positive root ρ is simple and strictly dominant by the triangle inequality with equality requiring the x term to be positive real; the other factors are analytic there and −xD'/D contributes leading coefficient ρ⁻ⁿ. A disjoint horizontal matching bounds failure by an exponentially decaying probability, so q²/ρ<1. At p=c/√n the distance-three graph has 11n edges; disjoint edge tuples give the Poisson factorial moments and tuples with any overlap contribute O(n⁻¹ᐟ²) because a component then requires at least three selected vertices. The same matching and a first-moment bound give the two off-window limits. Weighting failed sets by retention probabilities and dark counts gives reliability and expected coverage. A fresh bit-mask enumeration for orders 3–8 reproduced the distance, stopping-size and coefficient statements there.

## originality

PASS

The prism pair criterion, pair count 11n, scalar maximum and random-sensor framework are prior, and much of the sparse limit is a natural consequence of that pair criterion and bounded degree. The full labelled failure distribution, its rational gap generating function and Lucas correction for these particular admissible sets survive that overlap. The strongest exact competing all-sizes enumerators on the same prisms count different set systems, including a same-day externally supported independence census whose actual definition and short polynomials are demonstrably different.

## value

PASS

The census answers a natural reliability question that the known extreme sizes and minimum pairs do not: the chance of full or partial observation for an arbitrary independent survival probability on this family. The cyclic color/gap formula determines an exact size-refined invariant, unusually simple total counts, and the fixed-retention decay. The sparse window is a useful further interpretation, with the prior close-pair contribution credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
