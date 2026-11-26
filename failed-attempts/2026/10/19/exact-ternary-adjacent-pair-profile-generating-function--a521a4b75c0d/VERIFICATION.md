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

The stated all-length series and leading coefficient are correct. A nonzero matrix is realized exactly when the active support is weakly connected and the degree imbalance is zero or one ordered source/sink pair. Around the oriented triangle the differences are (h,h,h) in the balanced sector, giving (1+z³)/(1−z³) with three independent opposite-arc pair factors and three loop factors. For an ordered endpoint pair, adjoining one sink-to-source arc gives a balanced matrix with that arc count positive; subtracting the forbidden-arc sector and dividing by z gives (z+z²)/[(1−z)³(1−z²)³(1−z³)]. The disconnected balanced supports are multiple loop-only vertices, or a positive two-vertex arc pair plus a positive third loop; a disconnected open sector must have the ordered pair in one component and a positive third loop. These give exactly the stated subtractions. Loop-only one-vertex matrices and the length-one zero matrix are retained. The linear count has leading pole coefficient 7/12 at order seven, hence leading coefficient 7/8640; each code fiber contributes at most one word. The proof's quasipolynomial remark should be read as eventual: the rational function has polynomial part −2, so the quasipolynomial extrapolated to n=1 takes value 3, not the actual value 1. This does not alter the Finding's all-length generating function, asymptotic or code-size assertion.

## originality

FAIL

Distinct corpus records demonstrably give exactly the same principal finding. In frozen record 4, B(w)=C(w) entry by entry, with the same linear, directed, labeled, multiplicity-preserving convention and the same length-one value; the reduced numerator and denominator are identical. Independent catalogue comparisons add a full identical series and an equivalent series shifted only by excluding the empty matrix. The decomposed proof and displayed presentation differ, but not the counted class, exact series, leading constant or fiber capacity. A distinct mathematical result is not established against the corpus. This is not a finding that any of the other entries is earlier or that any was copied. Earlier literature accounts for balanced components and the leading constant, not for the full claim in the passages inspected.

## value

PASS

As a mathematical result, the all-length enumeration is a meaningful exact benchmark for linear ternary profile counting: it quantifies finite endpoint and connectivity effects at every length and gives the noiseless observation capacity. This is value of the theorem, not a separate contribution by this record in the face of exact duplicate coverage. The asymptotic alone or choosing arbitrary representatives would not be independent value beyond the count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
