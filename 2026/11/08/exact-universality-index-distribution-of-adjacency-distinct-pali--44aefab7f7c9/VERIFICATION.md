---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For each q>=2, an adjacency-distinct palindrome has unique form v c reverse(v) with c distinct from v final symbol. The palindrome midpoint lemma (Barker et al. Proposition 15, previously known) gives index 2a or 2a+1 according as the final incomplete arch plus c completes the full alphabet. The generating functions B_{q,s} count levels of the discovered-letter automaton with s-1 old-letter choices and q-s new-letter choices; arch weight alpha_q z^q/D_q with alpha_q=(q-1)(q-1)!. The centered correction multiplies exactly the q-1-letter residual by (u-1); checking initial vs subsequent arch weights yields F_q=q[1+(q-1)sum_s B_{q,s}+(u-1)B_{q,q-1}]/(1-u^2 alpha_q z^q/D_q). Exact minimal lengths follow by making every full arch a permutation and the terminal deficient remainder distinct-letter. q=2, empty halves, h=0, zero index and q-1 symbol residual all addressed. Finite brute coefficient checks independently match.

## originality

PASS

The midpoint lemma and greedy arch factorization are known. Comparing actual statements shows no inspected primary or published related record determines the full labelled all-q exact-index distribution for palindromes ALSO required to be adjacency-distinct and its counts of shortest witnesses. Earlier counts of adjacency-distinct unrestricted words and all palindromes separately do not mechanically yield the intersection without the final-symbol restriction and residual-alphabet refinement. PASS is best-of-knowledge, not an exhaustive priority certification.

## value

PASS

The simultaneous palindrome and forbidden-equal-neighbor constraints define a natural nonregular restricted language, and the precise distribution of subsequence universality and sharp shortest witnesses are natural invariants. The all-alphabet formula and extremal multiplicities answer a complete enumeration problem not implied by the known midpoint lemma alone; this is more than parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
