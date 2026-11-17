---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

PASS: The three conditional-event cases are correct: fixing a later position j>i leaves the prefix relative ranks exchangeable (record chance 1/i); fixing earlier j<i makes position i the largest of the other i-1 prefix positions (chance 1/(i-1) since the j-valued point cannot be maximal); fixing j=i forces the first i-1 images exactly in {1,...,i-1}, probability reciprocal binomial. Multiply by P(I_j)=1/n and subtract 1/(ni). Summation cancels the negative diagonal 1/i, and independent record indicators give variance H_n-H_n^(2), while Var(F)=1. The endpoint reciprocal-binomial sum gives the claimed asymptotics, all n>=2. Independently enumerated permutations n<=7 and checked every covariance rationally; the conditional proof covers all n.

## originality

FAIL

FAIL: An October 12 published Resultary theorem, Fixed points and records have a triangular covariance kernel, states the IDENTICAL three-case matrix, row sums, diagonal signs, total covariance and correlation asymptotic for uniform S_n. Its full RESULT.md was directly inspected and formulas (1)-(10) compared in detail. Relabeling index j as i and transposing Cov arguments changes no science. This is exact prior coverage, not insufficient literature search.

## value

FAIL

FAIL as a new finding: natural joint permutation statistics are mathematically motivated, but every claimed exact positional and aggregate invariant has already been proven verbatim in a prior complete theorem. Re-derivation and stronger finite checker do not create a new mathematical invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
