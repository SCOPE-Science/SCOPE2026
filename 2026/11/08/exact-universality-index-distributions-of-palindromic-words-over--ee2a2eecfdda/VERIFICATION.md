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

For q>=2, the ordinary half-word has unique greedy complete-alphabet arch factorization. Its arch enumerator is A_q=q!z^q/prod_{j=1}^{q-1}(1-jz); residual words are R_q=(1-A_q)/(1-qz), and exactly q-1-symbol residuals are S_q=A_q/z. Barker et al. midpoint lemma gives all even palindrome index exactly 2m and an odd palindrome index 2m or 2m+1 according as the center completes the deficient arch; the exact formal distributions E=R/(1-u^2 A) and O=[qR+(u-1)S]/(1-u^2 A) follow. The index-zero and empty-word cases and binary cancellation were checked. For uniformly random odd-palindrome half and center the completion is exactly renewal of uniform q-coupon collection at time h+1; its rational aperiodic generating function has sole simple unit-circle pole and mean qH_q, proving probability 1/(qH_q)+O_q(eta_q^h), eta_q<1. The mean result holds at fixed q, not uniformly growing q.

## originality

PASS

The known palindrome midpoint lemma and coupon-collector renewal are not new. General arch enumerators and algorithms do not provide the full all-alphabet even/odd palindrome index series or its centered parity probability as an explicit enumerative theorem in inspected texts. An adjacency-distinct specialization (a separate, more constrained class) cannot determine ordinary palindrome counts. Best-of-knowledge PASS with unindexed-equivalence risk.

## value

PASS

Ordinary palindromes are a canonical nonregular symmetry class; the full joint distribution at every length and universality level is a natural precise combinatorial statistic. The exact all-q rational series and exponential odd-index renewal limit give substantive global information beyond the structural midpoint lemma, useful for future sampled-palindrome universality calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
