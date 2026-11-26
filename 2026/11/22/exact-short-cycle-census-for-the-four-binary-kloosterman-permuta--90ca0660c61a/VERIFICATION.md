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

The identity row has 2^(n−1) fixed points and no primitive two-cycles. For admissible nonzero u, trace is invariant under each Frobenius power and the two inverse-power terms therefore sum to trace zero: both t and F_u(t) are nonzero on the trace-one fiber. Hollmann–Xiang Theorem 4.1 gives bijectivity. Independently composed the rational functions and factored their reduced numerators over GF(2) with SymPy, checking fixed-factor membership, irreducibility and the next-to-leading coefficient. The second-iterate factors and multiplicities match the frozen list exactly. Excluding the fixed roots, the multisets of minimal degrees of irreducible factors are {2}, {2,4}, {5,5,10,10}, for u=3,6,10 respectively; fixed factors are {1}, {1} and {1,2}. Each such degree-d irreducible has simple roots with minimal-field trace one. Its roots occur in E_n iff d divides n and have absolute trace one there iff n/d is odd, by the tower formula (multiplicities in the rational numerator do not count). This gives the fixed counts and, after halving primitive-period-two point counts, exactly the table. The degree-five and degree-ten conditions are disjoint, so the uniform ten-cycle bound and its equality regime follow. The inference is for every admissible n, not extrapolated from an enumeration.

## originality

PASS

The four admissible permutation patterns and their sufficiency are already known. The distinct result is the all-degree fixed-point and primitive two-cycle table on the trace-one fibers, under the original admissibility restrictions. The strongest inspected sources classify valid index patterns rather than compute individual orbit lengths, and the closely related short-cycle tables concern different maps and domains.

## value

PASS

Short primitive orbits are a natural invariant of these independently characterized permutation patterns across all extensions. The exact congruence conditions, uniform ten-cycle bound with sharp equality, and reason for the degree-five and degree-ten resonances give orbit information absent from mere bijectivity. The value is in the complete all-degree period-one/two profile, not in the elementary identity or fixed-point case alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
