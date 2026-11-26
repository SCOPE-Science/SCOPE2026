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

Salazar arXiv:2611.10059v1, PDF p. 11, Theorem 4.9, has the stated hypotheses and strict inequalities. For k≤2 they imply c≤3 and the four strict thresholds 58,155,387,925. Adding every prime divisor ≥5 of n preserves both zero and k, so these thresholds apply with c=ω of the enriched colliding support. The survivors are precisely the h with gcd(h(2n−h),6n)=1. Each remaining noncolliding prime removes exactly two residue classes and no prime ≥2n can remove a survivor; hence the finite set-union cover test is equivalent in both directions, including zero and one prime. An independent argument and exact replay also certify the spectrum without importing the cutoff: pad to two noncolliding primes, and take one admissible progression mod 6 of length L≥floor(n/6). CRT inclusion–exclusion on this progression gives a survivor count at least Lδ−(9·2^c−1), where δ is the product of 1−1/p over colliding primes and 1−2/p over the other two. Order the c+2 primes with p_i≥2i+3: the density is minimized by assigning the two larger exclusions to the two smallest primes, so δ≥D_c=(3/7) product_{i=3}^{c+2} (2i+2)/(2i+3). A zero has n<F_c=6((9·2^c−1)/D_c+1). For c=4, n≥5·7·9·11>F_4=184425/64; each extra colliding prime increases the product lower bound by at least 13, while F_c grows by a factor less than 6, ruling out all c≥4. For c≤3 the four cutoffs are 118,1095/4,4899/8,214173/160. Independent replay: python3 /workspace/audit_evidence/prime_cover.py /workspace/source/2026/11/22/*1694014ba029/small_support_certificate.csv. It scanned 13,192,162,21 candidates by c, verified all 207 certificate rows (minimum and validity of the stated minimizing pair), and found only 26,28,34,40,46. Their (base size, max one-prime coverage) pairs are (2,1) for the first four and (3,2) for the last. Direct gcd tests verify the five displayed squarefree products and exactly two noncolliding factors each. This proves J(0)=J(1)=0 and J(2)=46 in the n≥13 domain. The frozen verifier was read, not executed. The inspected source for the imported theorem is a public preprint; journal status was not asserted by this review.

## originality

PASS

The exact noncolliding-budget-two classification and the first nonzero sharp endpoint extend the inspected statements. The necessary global inequalities and the CRT counting framework are prior, not part of the supported distinct claim. Neither gives the exact endpoint and exceptional set without resolving the finite cover problem, and the inspected prior tables do not do so.

## value

PASS

J(k) was an existing sharp extremal invariant with noncolliding support as the parameter. The theorem resolves its first budget at which a zero is possible, proves that one noncolliding prime can never suffice in the specified domain, and records all exceptions at budget two, not merely the largest or an isolated witness. An exact finite reduction and census are useful here because neither broad positivity criteria nor upper bounds can answer these sharp first-case questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
