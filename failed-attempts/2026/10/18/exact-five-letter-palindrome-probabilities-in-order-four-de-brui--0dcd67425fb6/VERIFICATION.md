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

The cycle sample space is exactly labeled cyclic Euler tours of the triple-vertex graph; a contraction of two distinct edges is a bijection even if the replacement is a tagged loop. The degree-factor quotient is 1/(q-1), and the balanced contracted graph has all degrees positive even at q=2, so a zero tree cofactor correctly signifies no tour. The row Laplacian update is (e_s-e_v)(e_v-e_t)^T, including coincident vertices. Since P^3=J, the zero-sum inverse is (I+P+P^2-3J)/q; restricting to a root cofactor only adds a constant to the solution. I checked the three suffix/prefix bilinear forms in equations (2)–(5), including the coincident s=t when a=c, and their sum over the four multiplicities gives q^2-2-2/q. The constant word repeats its four-letter factor and is impossible. An independent binary enumeration via local successor permutations gave eight cycles with zero and eight with two palindromes, with each of 00100, 01010, 10101, 11011 present in four cycles and all others absent.

## originality

FAIL

Rødland's 2006 exact word-count theorem already covers this uniform sample space and returns the exact probability for any prescribed five-letter factor, not merely a bound or an algorithm for sampling. Appendix B already gives the contraction-specific determinant update with a generalized inverse. Here the specialization needs just the two-edge rank-one determinant and the finite geometric sum for a three-symbol shift. The four rational expressions and their linearity-of-expectation sum are not printed in the inspected prior source, but they are a direct evaluated corollary of it. The record does not identify a separate contribution beyond that evaluation.

## value

FAIL

The rotation-class law is natural, and the small formulas make a useful illustration, but the only claimed advance is this narrow invariant. After the prior exact motif law and its inverse-determinant update, the table is obtained by a single two-edge contraction and checking at most two shifts; the mean adds only the four equality-pattern multiplicities. The record supplies no distinct unknown invariant or additional structural result beyond that direct evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
