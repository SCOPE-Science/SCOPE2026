---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

PASS: For any nonzero 3-by-3 directed arc-multiplicity matrix, its word realization is equivalent to weak connectivity of the positive-arc support and Euler divergence zero or e_i-e_j. Parameterizing three signed off-diagonal pair differences by one integer circulation gives balanced B=(1+z^3)/((1-z)^3(1-z^2)^3(1-z^3)) and six open-trail classes H=(z+z^2)/((1-z)^3(1-z^2)^3(1-z^3)). Exactly subtract zero, isolated positive loops, balanced disconnected 2+1 components and unbalanced disconnected endpoint+loop components. This yields the stated rational function with (1-z)^7(1+z)^2(1+z+z^2) denominator, first coefficients 9,24,65,156,342,683,1272,2226, and leading 7m^6/8640. Nonzero numerator at primitive 2 and 3 roots establishes *least* quasipolynomial period six. Fresh direct enumeration of every ternary word for 1<=m<=8 matched the first eight counts; this is a finite check, not the all-length proof.

## originality

FAIL

FAIL: A published November 2 full theorem on exactly the same labeled ternary linear ordered bigram-multiplicity observation contains the word-for-word rational numerator and denominator, identical coefficients, asymptotic and zero-error codebook interpretation. Its Euler-trail proof checks the same disconnected-support exclusions. Another November 8 full theorem gives the identical exact generating function. The added least-period-six label is immediate from the earlier rational generating function poles and is not an independently valuable new theorem.

## value

FAIL

FAIL: Exact all-length profiles are a natural reconstruction invariant, but the entire result and code capacity have already been determined by the earlier full rational enumerator; deriving the least period from the same denominator is an elementary consequence. Reproducing the prior coefficient table or adding brute-force checks does not establish a new needed invariant or structural classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
