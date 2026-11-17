---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Every occurrence of a target word v in P^k corresponds bijectively to increasing period indices with compulsory strict increase at each weak descent v_i>=v_{i+1}; stars and bars gives binom(k+L-d(v)-1,L). For a palindromic halfword of length m, e equal adjacent pairs yield d=m-1+e for odd 2m-1 and d=m+e for even 2m, with q binom(m-1,e)(q-1)^(m-1-e) halfwords. Substitution yields both exact coefficient sums and the rational bivariate generating function by geometric summation. The longest 2k-1 has only e=0 halfwords and each exactly one embedding. Independent small q,k brute-force checked 42 length cells; arbitrary k follows from the bijection rather than finite checks.

## originality

FAIL

Decisive combined prior implication: The published November 2 exact embedding-multiplicity spectrum for cyclic permutation powers already proves binom(k+L-d(v)-1,L) for ALL target words; the published November 8 complete scattered-palindrome spectrum already enumerates palindromic halfwords by q binom(m-1,e)(q-1)^(m-1-e), including equal-transition counts. Restricting the first theorem to the halfwords classified in the second and applying the direct palindrome descent identities yields every submitted E_{q,k}(L), maximal-length count, and rational generating function by ordinary summation. The latter predecessor shares a November 8 date; exact intra-day chronology not established. No original standalone conclusion survives the earlier November 2 general formula plus the independently available halfword combinatorics.

## value

FAIL

Correct and reproducible but essentially a mechanical aggregation of a known all-pattern occurrence formula over the already-enumerated palindrome transition classes. No further structural obstruction, classification, or independent invariant beyond those known inputs; the new rational function is routine algebra from them. Natural occurrence weighting alone does not rescue a theorem whose full result is directly implied by established exact formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
