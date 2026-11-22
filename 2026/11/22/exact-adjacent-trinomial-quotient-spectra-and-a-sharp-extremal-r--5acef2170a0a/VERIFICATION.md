---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Checks performed
The standalone `checker.py` was run against the actual integer trinomial coefficient quotients for \(p=2,3,5\) through \(r=3\), \(p=7\) through \(r=2\), and \(p=11\) at \(r=1\). It returned `CHECK_OK; exact accepted tuples: 31515`. The separate algebraic checks matched the displacement identity and the extrema for 25 odd primes through 101 (1134 single-quotient comparisons). The case \(p=2\) is included in checks but outside the odd-prime theorem.

## Proof-critical points
The quotient is formed from nonzero integer coefficient residues, not by an invalid modular division by \(a\) or \(b+1\) when those are divisible by \(p\). Equal valuations select a unique decisive base-\(p\) digit. The exact factor \(S_r\) includes all possible decisive positions. Sharp uniqueness of the upper extreme uses the equality condition for the permutation footrule; sharp uniqueness of the lower extreme uses the multiplication map, not an arbitrary permutation.

## Limits
Finite exhaustive enumerations are not infinite certifications. This check reports no independent audit, and does not establish global historical priority. The proof in `RESULT.md` supplies all quantified claims.
