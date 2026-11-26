---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The four index branches in RESULT.md lines 18–57 cover the odd indices and indices congruent to 2 mod 4. Their scaled Newton series have an odd linear coefficient and coefficients divisible by 2·j! in Z₂ at every j≥2. The falling-factorial difference is divisible by t−u, so higher terms cannot cancel the linear term at its first nonzero bit. The series converge and give bijections on each finite 2-adic quotient. For indices divisible by four (including zero), Q₄ₘ=2Q₂ₘ²−1≡1 mod 16 since Q₂ₘ is odd. Multiplication by two gives the three stated disjoint balls for V, and for k≥6 their reductions have 2^(k−4), 2^(k−4), and 2^(k−6) lifts. An independent bounded recurrence-state enumeration to first return verified the exact image sets for k=6,…,15, and recurrence differences reproduced all eight listed Newton coefficients. The proportion 9/64 is of attained classes, not a sampling frequency over indices.

## originality

FAIL

A distinct indexed Resultary finding explicitly gives the same image and residue count for the same initial values and recurrence. Renaming the even sequence from V to Q is not a change of object. This is demonstrated exact coverage, not a judgment about which record first discovered the result or how the records are related.

## value

FAIL

The support of a canonical recurrence is a worthwhile invariant: the three-ball statement would settle every dyadic congruence-solvability question for it, stronger than a density alone. But as submitted there is no additional distinct support, frequency result, or other independently useful exact fact beyond the already indexed complete classification. The bounded enumeration corroborates that classification, not a separate contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
